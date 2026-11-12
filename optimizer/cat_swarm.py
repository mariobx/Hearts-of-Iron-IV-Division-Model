"""
optimizer/cat_swarm.py
======================
Cat Swarm Optimization (CSO) for Hearts of Iron IV Division Design.

Reference
---------
Aram M. Ahmed, Tarik A. Rashid, and Soran Ab. M. Saeed (2020),
*"Cat Swarm Optimization Algorithm: A Survey and Performance Evaluation"*,
Computational Intelligence and Neuroscience, Vol. 2020, Article ID 4854895
(PMC7204373), building upon Chu, Tsai, and Pan (2006).

Algorithmic Architecture
------------------------
Cat Swarm Optimization (CSO) models the two distinct behavioral phases of felines:
1. **Seeking Mode (Resting & Alert Local Exploitation)**:
   Cats spend most of their time resting while maintaining high situational
   awareness, slowly adjusting their posture to move toward better local vantage
   points. Controlled by four hyperparameters:
   - ``SMP`` (*Seeking Memory Pool*): Number of candidate copies generated per cat.
   - ``SPC`` (*Self-Position Considering*): Whether the cat's current position is
     included as one of the ``SMP`` candidates in the memory pool.
   - ``CDC`` (*Counts of Dimension to Change*): Fraction of dimensions ``D`` to
     mutate in each candidate copy.
   - ``SRD`` (*Seeking Range of the Selected Dimension*): Maximum perturbation
     magnitude applied to the selected dimensions, augmented with discrete
     HOI4 template neighborhood moves (battalion swaps, column resizing,
     divisional/regimental support swaps).
   Selection from the Seeking Memory Pool follows the official CSO probability
   formula (Eq. 1 of PMC7204373):
       P_i = |FS_i - FS_b| / (FS_max - FS_min),   where FS_b = FS_min (for maximization)

2. **Tracing Mode (Active Chasing Global Exploration)**:
   A fraction ``MR`` (*Mixture Ratio*) of cats are randomly assigned each
   iteration to actively chase the global best leader ``X_best`` using velocity
   dynamics (Eq. 2 & Eq. 3 of PMC7204373):
       v_{k,d}(t+1) = w * v_{k,d}(t) + c_1 * r_1 * (x_{best,d}(t) - x_{k,d}(t))
       x_{k,d}(t+1) = clip(x_{k,d}(t) + v_{k,d}(t+1), 0.0, 1.0)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from optimizer.base import (
    BaseDivisionOptimizer,
    CandidateSolution,
    DivisionGenome,
    GENOME_VECTOR_DIM,
    OptimizationConfig,
    RegimentColumnGene,
    register_optimizer,
)


@dataclass
class CatAgent:
    """
    Represents an individual cat k in the Cat Swarm Optimization population.

    Attributes
    ----------
    cat_id : int
        Unique identifier of the cat in ``0 .. population_size - 1``.
    position : List[float]
        Continuous latent position vector ``X_k in [0, 1]^D``.
    velocity : List[float]
        Continuous velocity vector ``V_k in [-V_max, V_max]^D`` used in Tracing Mode.
    candidate : CandidateSolution
        Decoded ``DivisionGenome``, ``Division`` instance, and ``FitnessMetrics``.
    mode : str
        Current behavioral flag: ``"seeking"`` or ``"tracing"``.
    """

    cat_id: int
    position: List[float]
    velocity: List[float]
    candidate: CandidateSolution
    mode: str = "seeking"

    @property
    def fitness(self) -> float:
        return self.candidate.fitness


@register_optimizer("cso", aliases=["cat_swarm", "catswarm", "cat"])
class CatSwarmOptimizer(BaseDivisionOptimizer):
    """
    Cat Swarm Optimization (CSO) engine for discovering optimal Hearts of Iron IV
    division templates across multiple terrains and eras.
    """

    ALGORITHM_NAME: str = "Cat Swarm Optimization (CSO)"

    def __init__(self, config: OptimizationConfig, **kwargs) -> None:
        super().__init__(config, **kwargs)
        self.cats: List[CatAgent] = []

    def initialize_population(self) -> None:
        """
        Initializes ``config.population_size`` cats with positions in ``[0, 1]^D``,
        small initial velocities in ``[-V_max, V_max]^D``, and evaluated fitness.
        """
        self.cats.clear()
        self.population.clear()
        vmax = float(self.config.get_param("cso_vmax", 0.35))

        archetypes = self.generate_archetype_genomes()
        num_cats = max(4, self.config.population_size)

        for k in range(num_cats):
            if k < len(archetypes):
                genome = archetypes[k].copy()
                genome.repair(self.unit_pool, self.config, self.rng)
                vec = genome.to_vector(self.unit_pool)
            else:
                genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
                vec = genome.to_vector(self.unit_pool)

            vel = [self.rng.uniform(-vmax * 0.5, vmax * 0.5) for _ in range(GENOME_VECTOR_DIM)]
            cand = self.evaluate_genome(
                genome=genome,
                vector=vec,
                iteration=0,
                agent_id=k,
                mode="seeking",
            )
            cat = CatAgent(
                cat_id=k,
                position=list(cand.vector),
                velocity=vel,
                candidate=cand,
                mode="seeking",
            )
            self.cats.append(cat)
            self.population.append(cand)

    def _assign_mixture_ratio_modes(self) -> Dict[str, int]:
        """
        Randomly assigns cats to Tracing Mode vs Seeking Mode according to the
        Mixture Ratio ``MR`` (``config.cso_mr``).
        """
        n_cats = len(self.cats)
        mr = float(self.config.get_param("cso_mr", 0.25))
        n_tracing = max(1, min(n_cats - 1, round(n_cats * mr)))
        indices = list(range(n_cats))
        self.rng.shuffle(indices)
        tracing_set = set(indices[:n_tracing])

        seeking_count = 0
        tracing_count = 0
        for idx, cat in enumerate(self.cats):
            if idx in tracing_set:
                cat.mode = "tracing"
                cat.candidate.mode = "tracing"
                tracing_count += 1
            else:
                cat.mode = "seeking"
                cat.candidate.mode = "seeking"
                seeking_count += 1

        return {"seeking": seeking_count, "tracing": tracing_count}

    def _discrete_neighbor_mutation(self, genome: DivisionGenome) -> DivisionGenome:
        """
        Applies a fine-grained discrete HOI4 template mutation in Seeking Mode
        (e.g., swapping a battalion within a column's group, adding/removing a
        battalion, toggling a regimental support, or mutating a divisional support).
        """
        mut = genome.copy()
        active_groups = self.unit_pool.get_active_groups()
        move_type = self.rng.random()

        non_empty_cols = [c for c in mut.columns if not c.is_empty()]
        if move_type < 0.35 and non_empty_cols:
            # Swap 1 or 2 battalions within a column for another unit in the same brigade group
            col = self.rng.choice(non_empty_cols)
            grp_pool = self.unit_pool.battalions_by_group.get(col.group, [])
            if grp_pool and col.battalions:
                slot_idx = self.rng.randrange(len(col.battalions))
                new_bat = self.rng.choice(grp_pool).name
                col.battalions[slot_idx] = new_bat
                # Occasionally homogenize column
                if self.rng.random() < 0.35:
                    for i in range(len(col.battalions)):
                        if self.rng.random() < 0.5:
                            col.battalions[i] = new_bat

        elif move_type < 0.60:
            # Adjust column battalion count (+1 or -1) or activate/deactivate a column
            col = self.rng.choice(mut.columns)
            if col.is_empty() and active_groups:
                col.group = self.rng.choice(active_groups)
                grp_pool = self.unit_pool.battalions_by_group[col.group]
                b_name = self.rng.choice(grp_pool).name
                col.battalions = [b_name] * self.rng.randint(2, 4)
            elif not col.is_empty():
                if self.rng.random() < 0.55 and len(col.battalions) < 5:
                    col.battalions.append(col.battalions[-1])
                elif len(col.battalions) > 1:
                    col.battalions.pop()
                else:
                    col.group = "none"
                    col.battalions = []
                    col.regimental_support = None

        elif move_type < 0.82 and self.unit_pool.divisional_supports:
            # Mutate a divisional support company slot
            slot_idx = self.rng.randrange(5)
            if self.rng.random() < 0.20:
                mut.divisional_supports[slot_idx] = None
            else:
                mut.divisional_supports[slot_idx] = self.rng.choice(
                    self.unit_pool.divisional_supports
                ).name

        else:
            # Mutate or toggle a Regimental Support slot on a column with >= 3 battalions
            eligible_cols = [c for c in mut.columns if not c.is_empty() and len(c.battalions) >= 3]
            if eligible_cols and self.config.allow_regimental_support:
                col = self.rng.choice(eligible_cols)
                compat_regs = self.unit_pool.regimental_supports_by_group.get(col.group, [])
                if compat_regs:
                    if col.regimental_support is not None and self.rng.random() < 0.25:
                        col.regimental_support = None
                    else:
                        col.regimental_support = self.rng.choice(compat_regs).name

        mut.repair(self.unit_pool, self.config, self.rng)
        return mut

    def _run_seeking_mode(self, cat: CatAgent, iteration: int) -> None:
        """
        Executes Seeking Mode for ``cat`` following PMC7204373:
        1. Create ``SMP`` candidate copies in the Seeking Memory Pool (if ``SPC=True``,
           create ``SMP - 1`` mutated copies and include the current cat as the
           ``SMP``-th copy).
        2. For each mutated copy, randomly choose ``CDC * D`` dimensions and
           perturb each by ``+- SRD`` (combined with discrete HOI4 neighbor moves).
        3. Evaluate fitness ``FS_i`` of all candidates in the pool.
        4. Select the new position using ``P_i = |FS_i - FS_min| / (FS_max - FS_min)``.
        """
        smp = max(2, int(self.config.get_param("cso_smp", 5)))
        srd = float(self.config.get_param("cso_srd", 0.25))
        cdc = float(self.config.get_param("cso_cdc", 0.30))
        spc = bool(self.config.get_param("cso_spc", True))

        num_dims_to_change = max(1, round(cdc * GENOME_VECTOR_DIM))
        num_mutated_copies = (smp - 1) if spc else smp

        pool: List[CandidateSolution] = []
        if spc:
            current_copy = cat.candidate.copy()
            current_copy.mode = "seeking"
            pool.append(current_copy)

        for _ in range(num_mutated_copies):
            if self.rng.random() < 0.55:
                # Continuous CSO Seeking perturbation along CDC selected dimensions by +- SRD
                new_vec = list(cat.position)
                selected_dims = self.rng.sample(range(GENOME_VECTOR_DIM), num_dims_to_change)
                for d in selected_dims:
                    delta = self.rng.uniform(-srd, srd)
                    new_vec[d] = max(0.0, min(1.0, new_vec[d] + delta))
                new_genome = DivisionGenome.from_vector(
                    new_vec, self.unit_pool, self.config, rng=self.rng
                )
                # Optionally pair with a discrete tweak for rich local exploitation
                if self.rng.random() < 0.40:
                    new_genome = self._discrete_neighbor_mutation(new_genome)
                sync_vec = new_genome.to_vector(self.unit_pool)
            else:
                # Direct discrete HOI4 template neighborhood move synchronized back to [0, 1]^D
                new_genome = self._discrete_neighbor_mutation(cat.candidate.genome)
                sync_vec = new_genome.to_vector(self.unit_pool)

            cand = self.evaluate_genome(
                genome=new_genome,
                vector=sync_vec,
                iteration=iteration,
                agent_id=cat.cat_id,
                mode="seeking",
            )
            pool.append(cand)

        # Compute CSO selection probabilities P_i = |FS_i - FS_min| / (FS_max - FS_min)
        fitnesses = [c.fitness for c in pool]
        fs_max = max(fitnesses)
        fs_min = min(fitnesses)

        best_in_pool = max(pool, key=lambda c: c.fitness)

        # If the best candidate in SMP improves over the cat's current fitness, adopt it directly
        # Otherwise use the PMC7204373 roulette selection probability formula
        if best_in_pool.fitness > cat.fitness or abs(fs_max - fs_min) < 1e-9:
            chosen = best_in_pool
        else:
            probs = [abs(c.fitness - fs_min) / (fs_max - fs_min) for c in pool]
            total_prob = sum(probs)
            if total_prob <= 0:
                chosen = best_in_pool
            else:
                r = self.rng.uniform(0.0, total_prob)
                upto = 0.0
                chosen = best_in_pool
                for cand, p in zip(pool, probs):
                    upto += p
                    if upto >= r:
                        chosen = cand
                        break

        cat.candidate = chosen
        cat.position = list(chosen.vector)

    def _run_tracing_mode(self, cat: CatAgent, iteration: int) -> None:
        """
        Executes Tracing Mode for ``cat`` following PMC7204373:
        1. Updates velocity toward global best ``X_best``:
               v_{k,d}(t+1) = w * v_{k,d}(t) + c_1 * r_1 * (x_{best,d}(t) - x_{k,d}(t))
        2. Clamps velocity to ``[-V_max, V_max]``.
        3. Updates position:
               x_{k,d}(t+1) = clip(x_{k,d}(t) + v_{k,d}(t+1), 0.0, 1.0)
        4. Decodes to a valid ``DivisionGenome`` and evaluates fitness.
        """
        if self.best_candidate is None:
            return

        w = float(self.config.get_param("cso_inertia_w", 0.7))
        c1 = float(self.config.get_param("cso_c1", 1.8))
        vmax = float(self.config.get_param("cso_vmax", 0.35))
        x_best = self.best_candidate.vector

        new_pos: List[float] = []
        new_vel: List[float] = []

        for d in range(GENOME_VECTOR_DIM):
            r1 = self.rng.random()
            v_d = w * cat.velocity[d] + c1 * r1 * (x_best[d] - cat.position[d])
            # Add small stochastic impulse if cat has converged onto x_best
            if abs(x_best[d] - cat.position[d]) < 1e-4 and self.rng.random() < 0.20:
                v_d += self.rng.uniform(-0.15, 0.15)
            v_d = max(-vmax, min(vmax, v_d))
            x_d = max(0.0, min(1.0, cat.position[d] + v_d))
            new_vel.append(v_d)
            new_pos.append(x_d)

        new_genome = DivisionGenome.from_vector(
            new_pos, self.unit_pool, self.config, rng=self.rng
        )
        sync_vec = new_genome.to_vector(self.unit_pool)

        cand = self.evaluate_genome(
            genome=new_genome,
            vector=sync_vec,
            iteration=iteration,
            agent_id=cat.cat_id,
            mode="tracing",
        )

        cat.velocity = new_vel
        cat.position = list(cand.vector)
        cat.candidate = cand

    def step(self, iteration: int) -> Dict[str, int]:
        """
        Executes one full iteration of Cat Swarm Optimization:
        1. Assigns cats to Seeking Mode or Tracing Mode via Mixture Ratio ``MR``.
        2. Executes Seeking Mode or Tracing Mode for each cat.
        3. Updates ``self.population`` and returns mode counts.
        """
        mode_counts = self._assign_mixture_ratio_modes()

        for cat in self.cats:
            if cat.mode == "tracing":
                self._run_tracing_mode(cat, iteration)
            else:
                self._run_seeking_mode(cat, iteration)

        self.population = [cat.candidate for cat in self.cats]
        return mode_counts

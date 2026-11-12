"""
optimizer/genetic.py
====================
Evolutionary & Stochastic Optimization Algorithms for HOI4 Division Design.

All optimizers in this module implement the ``BaseDivisionOptimizer`` interface
and register themselves via ``@register_optimizer`` so they can be swapped in
for Cat Swarm Optimization (CSO) with zero changes to the evaluator, logger,
web dashboard, or CLI:

1. ``GeneticOptimizer`` (``"ga"``):
   Elitist Genetic Algorithm with tournament selection, regiment-column-aware
   uniform crossover, and multi-operator discrete HOI4 template mutation.
2. ``DifferentialEvolutionOptimizer`` (``"de"``):
   Storn & Price (1997) Differential Evolution (``DE/current-to-best/1/bin``),
   one of the primary benchmark comparison algorithms evaluated alongside CSO
   in Aram M. Ahmed et al. (2020), PMC7204373.
3. ``SimulatedAnnealingOptimizer`` (``"sa"``):
   Population-based Simulated Annealing with Metropolis-Hastings acceptance
   and geometric temperature cooling.
4. ``RandomSearchOptimizer`` (``"random"``):
   Pure Monte Carlo random search baseline for quantifying metaheuristic
   optimization gains.
"""

from __future__ import annotations

import math
from typing import Dict, List

from optimizer.base import (
    BaseDivisionOptimizer,
    CandidateSolution,
    DivisionGenome,
    GENOME_VECTOR_DIM,
    OptimizationConfig,
    RegimentColumnGene,
    register_optimizer,
)


@register_optimizer("ga", aliases=["genetic", "genetic_algorithm"])
class GeneticOptimizer(BaseDivisionOptimizer):
    """
    Elitist Genetic Algorithm (GA) tailored for HOI4's 5-column regiment and
    divisional/regimental support structure.
    """

    ALGORITHM_NAME: str = "Genetic Algorithm (GA)"

    def initialize_population(self) -> None:
        self.population.clear()
        archetypes = self.generate_archetype_genomes()
        pop_size = max(4, self.config.population_size)

        for idx in range(pop_size):
            if idx < len(archetypes):
                genome = archetypes[idx].copy()
                genome.repair(self.unit_pool, self.config, self.rng)
            else:
                genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
            cand = self.evaluate_genome(
                genome=genome,
                iteration=0,
                agent_id=idx,
                mode="ga_init",
            )
            self.population.append(cand)

    def _tournament_select(self, k: int) -> CandidateSolution:
        contenders = self.rng.sample(self.population, min(k, len(self.population)))
        return max(contenders, key=lambda c: c.fitness)

    def _crossover(self, parent_a: DivisionGenome, parent_b: DivisionGenome) -> DivisionGenome:
        """
        Regiment-column-aware uniform crossover: inherits whole regiment columns
        and divisional support slots from either Parent A or Parent B.
        """
        cols: List[RegimentColumnGene] = []
        for c in range(5):
            src_col = parent_a.columns[c] if self.rng.random() < 0.5 else parent_b.columns[c]
            cols.append(
                RegimentColumnGene(
                    group=src_col.group,
                    battalions=list(src_col.battalions),
                    regimental_support=src_col.regimental_support,
                )
            )
        div_sups = [
            parent_a.divisional_supports[s] if self.rng.random() < 0.5 else parent_b.divisional_supports[s]
            for s in range(5)
        ]
        child = DivisionGenome(columns=cols, divisional_supports=div_sups)
        child.repair(self.unit_pool, self.config, self.rng)
        return child

    def _mutate(self, genome: DivisionGenome, mutation_rate: float) -> DivisionGenome:
        mut = genome.copy()
        active_groups = self.unit_pool.get_active_groups()

        for col in mut.columns:
            if self.rng.random() < mutation_rate:
                if col.is_empty() and active_groups:
                    col.group = self.rng.choice(active_groups)
                    grp_pool = self.unit_pool.battalions_by_group[col.group]
                    col.battalions = [self.rng.choice(grp_pool).name] * self.rng.randint(2, 4)
                elif not col.is_empty():
                    op = self.rng.random()
                    grp_pool = self.unit_pool.battalions_by_group.get(col.group, [])
                    if op < 0.45 and grp_pool and col.battalions:
                        idx = self.rng.randrange(len(col.battalions))
                        col.battalions[idx] = self.rng.choice(grp_pool).name
                    elif op < 0.75:
                        if self.rng.random() < 0.5 and len(col.battalions) < 5 and grp_pool:
                            col.battalions.append(self.rng.choice(grp_pool).name)
                        elif len(col.battalions) > 1:
                            col.battalions.pop()
                    elif self.config.allow_regimental_support and len(col.battalions) >= 3:
                        compat_regs = self.unit_pool.regimental_supports_by_group.get(col.group, [])
                        if compat_regs:
                            col.regimental_support = (
                                None if self.rng.random() < 0.25 else self.rng.choice(compat_regs).name
                            )

        for s in range(5):
            if self.rng.random() < mutation_rate and self.unit_pool.divisional_supports:
                if self.rng.random() < 0.20:
                    mut.divisional_supports[s] = None
                else:
                    mut.divisional_supports[s] = self.rng.choice(
                        self.unit_pool.divisional_supports
                    ).name

        mut.repair(self.unit_pool, self.config, self.rng)
        return mut

    def step(self, iteration: int) -> Dict[str, int]:
        pop_size = len(self.population)
        elite_frac = float(self.config.get_param("ga_elite_fraction", 0.15))
        crossover_rate = float(self.config.get_param("ga_crossover_rate", 0.80))
        mutation_rate = float(self.config.get_param("ga_mutation_rate", 0.18))
        tourn_size = int(self.config.get_param("ga_tournament_size", 3))

        sorted_pop = sorted(self.population, key=lambda c: c.fitness, reverse=True)
        n_elite = max(1, round(pop_size * elite_frac))

        new_pop: List[CandidateSolution] = []
        for idx in range(n_elite):
            elite_copy = sorted_pop[idx].copy()
            elite_copy.mode = "elite"
            new_pop.append(elite_copy)

        crossover_count = 0
        mutation_count = 0

        while len(new_pop) < pop_size:
            agent_id = len(new_pop)
            p1 = self._tournament_select(tourn_size)
            if self.rng.random() < crossover_rate:
                p2 = self._tournament_select(tourn_size)
                child_genome = self._crossover(p1.genome, p2.genome)
                mode = "crossover"
                crossover_count += 1
            else:
                child_genome = p1.genome.copy()
                mode = "mutation"
                mutation_count += 1

            child_genome = self._mutate(child_genome, mutation_rate)
            cand = self.evaluate_genome(
                genome=child_genome,
                iteration=iteration,
                agent_id=agent_id,
                mode=mode,
            )
            new_pop.append(cand)

        self.population = new_pop
        return {
            "seeking": n_elite + mutation_count,
            "tracing": crossover_count,
            "elite": n_elite,
            "crossover": crossover_count,
            "mutation": mutation_count,
        }


@register_optimizer("de", aliases=["differential_evolution", "diffevo"])
class DifferentialEvolutionOptimizer(BaseDivisionOptimizer):
    """
    Differential Evolution (``DE/current-to-best/1/bin``) optimizer operating
    on the continuous latent space ``[0, 1]^45`` with deterministic HOI4 genome
    decoding and greedy survival selection.
    """

    ALGORITHM_NAME: str = "Differential Evolution (DE)"

    def initialize_population(self) -> None:
        self.population.clear()
        archetypes = self.generate_archetype_genomes()
        pop_size = max(4, self.config.population_size)

        for idx in range(pop_size):
            if idx < len(archetypes):
                genome = archetypes[idx].copy()
                genome.repair(self.unit_pool, self.config, self.rng)
                vec = genome.to_vector(self.unit_pool)
            else:
                genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
                vec = genome.to_vector(self.unit_pool)

            cand = self.evaluate_genome(
                genome=genome,
                vector=vec,
                iteration=0,
                agent_id=idx,
                mode="de_target",
            )
            self.population.append(cand)

    def step(self, iteration: int) -> Dict[str, int]:
        pop_size = len(self.population)
        f_weight = float(self.config.get_param("de_mutation_factor", 0.70))
        cr_prob = float(self.config.get_param("de_crossover_prob", 0.85))
        x_best = (
            self.best_candidate.vector
            if self.best_candidate is not None
            else self.population[0].vector
        )

        new_pop: List[CandidateSolution] = []
        improved_count = 0
        retained_count = 0

        for i, target in enumerate(self.population):
            other_indices = [idx for idx in range(pop_size) if idx != i]
            if len(other_indices) >= 3:
                r1, r2, r3 = self.rng.sample(other_indices, 3)
            else:
                r1 = r2 = r3 = other_indices[0] if other_indices else 0

            v1 = self.population[r1].vector
            v2 = self.population[r2].vector
            v3 = self.population[r3].vector
            xi = target.vector

            j_rand = self.rng.randrange(GENOME_VECTOR_DIM)
            trial_vec: List[float] = []
            for d in range(GENOME_VECTOR_DIM):
                if self.rng.random() < cr_prob or d == j_rand:
                    # DE/current-to-best/1/bin donor
                    val = xi[d] + f_weight * (x_best[d] - xi[d]) + f_weight * (v1[d] - v2[d])
                    if self.rng.random() < 0.25:
                        val += 0.5 * f_weight * (v2[d] - v3[d])
                    trial_vec.append(max(0.0, min(1.0, val)))
                else:
                    trial_vec.append(xi[d])

            trial_genome = DivisionGenome.from_vector(
                trial_vec, self.unit_pool, self.config, rng=self.rng
            )
            trial_cand = self.evaluate_genome(
                genome=trial_genome,
                vector=trial_genome.to_vector(self.unit_pool),
                iteration=iteration,
                agent_id=i,
                mode="tracing",
            )

            if trial_cand.fitness >= target.fitness:
                new_pop.append(trial_cand)
                improved_count += 1
            else:
                kept = target.copy()
                kept.mode = "seeking"
                new_pop.append(kept)
                retained_count += 1

        self.population = new_pop
        return {
            "seeking": retained_count,
            "tracing": improved_count,
            "improved": improved_count,
            "retained": retained_count,
        }


@register_optimizer("sa", aliases=["simulated_annealing", "annealing"])
class SimulatedAnnealingOptimizer(BaseDivisionOptimizer):
    """
    Population-based Simulated Annealing (SA) with Metropolis acceptance
    criterion and geometric cooling schedule.
    """

    ALGORITHM_NAME: str = "Simulated Annealing (SA)"

    def __init__(self, config: OptimizationConfig, **kwargs) -> None:
        super().__init__(config, **kwargs)
        self.temperature: float = float(config.get_param("sa_initial_temp", 10.0))

    def initialize_population(self) -> None:
        self.population.clear()
        self.temperature = float(self.config.get_param("sa_initial_temp", 10.0))
        archetypes = self.generate_archetype_genomes()
        pop_size = max(4, self.config.population_size)

        for idx in range(pop_size):
            if idx < len(archetypes):
                genome = archetypes[idx].copy()
                genome.repair(self.unit_pool, self.config, self.rng)
            else:
                genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
            cand = self.evaluate_genome(
                genome=genome,
                iteration=0,
                agent_id=idx,
                mode="seeking",
            )
            self.population.append(cand)

    def step(self, iteration: int) -> Dict[str, int]:
        cooling = float(self.config.get_param("sa_cooling_rate", 0.90))
        step_scale = max(0.08, min(0.45, 0.30 * (self.temperature / max(1.0, self.config.sa_initial_temp))))

        accepted_uphill = 0
        accepted_improving = 0
        rejected = 0
        new_pop: List[CandidateSolution] = []

        for idx, current in enumerate(self.population):
            vec = list(current.vector)
            num_dims = max(2, round(0.25 * GENOME_VECTOR_DIM))
            for d in self.rng.sample(range(GENOME_VECTOR_DIM), num_dims):
                vec[d] = max(0.0, min(1.0, vec[d] + self.rng.uniform(-step_scale, step_scale)))

            neighbor_genome = DivisionGenome.from_vector(
                vec, self.unit_pool, self.config, rng=self.rng
            )
            neighbor = self.evaluate_genome(
                genome=neighbor_genome,
                vector=neighbor_genome.to_vector(self.unit_pool),
                iteration=iteration,
                agent_id=idx,
                mode="seeking",
            )

            delta = neighbor.fitness - current.fitness
            if delta >= 0:
                neighbor.mode = "seeking"
                new_pop.append(neighbor)
                accepted_improving += 1
            else:
                prob = math.exp(delta / max(1e-4, self.temperature))
                if self.rng.random() < prob:
                    neighbor.mode = "tracing"
                    new_pop.append(neighbor)
                    accepted_uphill += 1
                else:
                    kept = current.copy()
                    kept.mode = "seeking"
                    new_pop.append(kept)
                    rejected += 1

        self.temperature = max(0.05, self.temperature * cooling)
        self.population = new_pop
        return {
            "seeking": accepted_improving + rejected,
            "tracing": accepted_uphill,
            "improving": accepted_improving,
            "uphill": accepted_uphill,
            "rejected": rejected,
        }


@register_optimizer("random", aliases=["rand", "random_search", "monte_carlo"])
class RandomSearchOptimizer(BaseDivisionOptimizer):
    """
    Pure Monte Carlo Random Search baseline that samples valid HOI4 division
    templates uniformly and retains the best templates found.
    """

    ALGORITHM_NAME: str = "Random Search (Monte Carlo)"

    def initialize_population(self) -> None:
        self.population.clear()
        pop_size = max(4, self.config.population_size)
        for idx in range(pop_size):
            genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
            cand = self.evaluate_genome(
                genome=genome,
                iteration=0,
                agent_id=idx,
                mode="tracing",
            )
            self.population.append(cand)

    def step(self, iteration: int) -> Dict[str, int]:
        pop_size = len(self.population)
        new_pop: List[CandidateSolution] = []
        # Keep top 25% found so far, resample 75% purely at random
        sorted_pop = sorted(self.population, key=lambda c: c.fitness, reverse=True)
        keep_n = max(1, pop_size // 4)
        for idx in range(keep_n):
            kept = sorted_pop[idx].copy()
            kept.mode = "seeking"
            new_pop.append(kept)

        for idx in range(keep_n, pop_size):
            genome = DivisionGenome.random(self.unit_pool, self.config, self.rng)
            cand = self.evaluate_genome(
                genome=genome,
                iteration=iteration,
                agent_id=idx,
                mode="tracing",
            )
            new_pop.append(cand)

        self.population = new_pop
        return {"seeking": keep_n, "tracing": pop_size - keep_n}

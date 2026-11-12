"""
optimizer/particle_swarm.py
===========================
Swarm Intelligence Optimizers (PSO & Grey Wolf Optimizer) for HOI4 Division Design.

All optimizers in this module implement the ``BaseDivisionOptimizer`` interface
and register themselves via ``@register_optimizer`` so they can be swapped in
for Cat Swarm Optimization (CSO) without changing a single line of the evaluator,
logger, web dashboard, or CLI:

1. ``ParticleSwarmOptimizer`` (``"pso"``):
   Kennedy & Eberhart (1995) / Shi & Eberhart (1998) Particle Swarm Optimization
   with cognitive (personal best ``P_i``) and social (global best ``G``) velocity
   updates in the continuous latent space ``[0, 1]^45``.
2. ``GreyWolfOptimizer`` (``"gwo"``):
   Mirjalili et al. (2014) Grey Wolf Optimizer (GWO), modeled on the social
   leadership hierarchy (Alpha, Beta, Delta, Omega) and hunting behavior of
   grey wolves — one of the flagship swarm algorithms compared against CSO in
   Aram M. Ahmed et al. (2020), PMC7204373.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from optimizer.base import (
    BaseDivisionOptimizer,
    CandidateSolution,
    DivisionGenome,
    GENOME_VECTOR_DIM,
    OptimizationConfig,
    register_optimizer,
)


@dataclass
class Particle:
    """Represents a single particle i in Particle Swarm Optimization (PSO)."""

    particle_id: int
    position: List[float]
    velocity: List[float]
    candidate: CandidateSolution
    pbest_position: List[float]
    pbest_fitness: float


@register_optimizer("pso", aliases=["particle_swarm", "particleswarm"])
class ParticleSwarmOptimizer(BaseDivisionOptimizer):
    """
    Inertia-Weighted Particle Swarm Optimization (PSO) engine for HOI4 division
    template discovery.
    """

    ALGORITHM_NAME: str = "Particle Swarm Optimization (PSO)"

    def __init__(self, config: OptimizationConfig, **kwargs) -> None:
        super().__init__(config, **kwargs)
        self.particles: List[Particle] = []

    def initialize_population(self) -> None:
        self.particles.clear()
        self.population.clear()
        vmax = float(self.config.get_param("pso_vmax", 0.35))
        archetypes = self.generate_archetype_genomes()
        pop_size = max(4, self.config.population_size)

        for i in range(pop_size):
            if i < len(archetypes):
                genome = archetypes[i].copy()
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
                agent_id=i,
                mode="seeking",
            )
            p = Particle(
                particle_id=i,
                position=list(cand.vector),
                velocity=vel,
                candidate=cand,
                pbest_position=list(cand.vector),
                pbest_fitness=cand.fitness,
            )
            self.particles.append(p)
            self.population.append(cand)

    def step(self, iteration: int) -> Dict[str, int]:
        w = float(self.config.get_param("pso_inertia_w", 0.72))
        c1 = float(self.config.get_param("pso_c1", 1.5))
        c2 = float(self.config.get_param("pso_c2", 1.7))
        vmax = float(self.config.get_param("pso_vmax", 0.35))

        gbest_vec = (
            self.best_candidate.vector
            if self.best_candidate is not None
            else self.particles[0].pbest_position
        )

        cognitive_dominant = 0
        social_dominant = 0

        for p in self.particles:
            new_vel: List[float] = []
            new_pos: List[float] = []
            cog_pull = 0.0
            soc_pull = 0.0

            for d in range(GENOME_VECTOR_DIM):
                r1 = self.rng.random()
                r2 = self.rng.random()
                cog_term = c1 * r1 * (p.pbest_position[d] - p.position[d])
                soc_term = c2 * r2 * (gbest_vec[d] - p.position[d])
                cog_pull += abs(cog_term)
                soc_pull += abs(soc_term)

                v_d = w * p.velocity[d] + cog_term + soc_term
                if abs(v_d) < 1e-4 and self.rng.random() < 0.15:
                    v_d += self.rng.uniform(-0.18, 0.18)
                v_d = max(-vmax, min(vmax, v_d))
                x_d = max(0.0, min(1.0, p.position[d] + v_d))
                new_vel.append(v_d)
                new_pos.append(x_d)

            mode = "seeking" if cog_pull >= soc_pull else "tracing"
            if mode == "seeking":
                cognitive_dominant += 1
            else:
                social_dominant += 1

            new_genome = DivisionGenome.from_vector(
                new_pos, self.unit_pool, self.config, rng=self.rng
            )
            sync_vec = new_genome.to_vector(self.unit_pool)
            cand = self.evaluate_genome(
                genome=new_genome,
                vector=sync_vec,
                iteration=iteration,
                agent_id=p.particle_id,
                mode=mode,
            )

            p.velocity = new_vel
            p.position = list(cand.vector)
            p.candidate = cand
            if cand.fitness >= p.pbest_fitness:
                p.pbest_fitness = cand.fitness
                p.pbest_position = list(cand.vector)

        self.population = [p.candidate for p in self.particles]
        return {"seeking": cognitive_dominant, "tracing": social_dominant}


@register_optimizer("gwo", aliases=["grey_wolf", "greywolf"])
class GreyWolfOptimizer(BaseDivisionOptimizer):
    """
    Grey Wolf Optimizer (GWO, Mirjalili et al. 2014) modeled on the Alpha,
    Beta, and Delta leadership hierarchy of grey wolves.
    """

    ALGORITHM_NAME: str = "Grey Wolf Optimizer (GWO)"

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
                mode="seeking",
            )
            self.population.append(cand)

    def step(self, iteration: int) -> Dict[str, int]:
        # Identify Alpha (best), Beta (2nd best), and Delta (3rd best) wolves
        sorted_wolves = sorted(self.population, key=lambda c: c.fitness, reverse=True)
        alpha_vec = sorted_wolves[0].vector
        beta_vec = sorted_wolves[min(1, len(sorted_wolves) - 1)].vector
        delta_vec = sorted_wolves[min(2, len(sorted_wolves) - 1)].vector

        # Control parameter 'a' decreases linearly from 2.0 to 0.0 over iterations
        max_iter = max(1, self.config.iterations)
        a = 2.0 - 2.0 * ((iteration - 1) / max_iter)

        new_pop: List[CandidateSolution] = []
        exploit_count = 0
        explore_count = 0

        for idx, wolf in enumerate(self.population):
            new_vec: List[float] = []
            a_mag_accum = 0.0
            for d in range(GENOME_VECTOR_DIM):
                r1_a, r2_a = self.rng.random(), self.rng.random()
                A1 = 2.0 * a * r1_a - a
                C1 = 2.0 * r2_a
                D_alpha = abs(C1 * alpha_vec[d] - wolf.vector[d])
                X1 = alpha_vec[d] - A1 * D_alpha

                r1_b, r2_b = self.rng.random(), self.rng.random()
                A2 = 2.0 * a * r1_b - a
                C2 = 2.0 * r2_b
                D_beta = abs(C2 * beta_vec[d] - wolf.vector[d])
                X2 = beta_vec[d] - A2 * D_beta

                r1_d, r2_d = self.rng.random(), self.rng.random()
                A3 = 2.0 * a * r1_d - a
                C3 = 2.0 * r2_d
                D_delta = abs(C3 * delta_vec[d] - wolf.vector[d])
                X3 = delta_vec[d] - A3 * D_delta

                a_mag_accum += (abs(A1) + abs(A2) + abs(A3)) / 3.0
                x_new = (X1 + X2 + X3) / 3.0
                new_vec.append(max(0.0, min(1.0, x_new)))

            avg_A = a_mag_accum / GENOME_VECTOR_DIM
            mode = "seeking" if avg_A < 1.0 else "tracing"
            if mode == "seeking":
                exploit_count += 1
            else:
                explore_count += 1

            new_genome = DivisionGenome.from_vector(
                new_vec, self.unit_pool, self.config, rng=self.rng
            )
            cand = self.evaluate_genome(
                genome=new_genome,
                vector=new_genome.to_vector(self.unit_pool),
                iteration=iteration,
                agent_id=idx,
                mode=mode,
            )
            new_pop.append(cand)

        self.population = new_pop
        return {"seeking": exploit_count, "tracing": explore_count}

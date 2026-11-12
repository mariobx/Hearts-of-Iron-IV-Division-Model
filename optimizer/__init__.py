"""
optimizer
=========
Algorithm-Agnostic Division Optimization Engine for Hearts of Iron IV (v1.19.4.2).

Exposes:
- Core abstractions: ``OptimizationConfig``, ``BaseDivisionOptimizer``, ``DivisionGenome``,
  ``RegimentColumnGene``, ``UnitPool``, ``FitnessMetrics``, ``CandidateSolution``,
  ``OPTIMIZER_REGISTRY``, ``register_optimizer``, ``serialize_division``
- Evaluator & objectives: ``DivisionEvaluator``, ``build_benchmark_opponents``,
  ``OBJECTIVE_DESCRIPTIONS``
- Swappable Metaheuristics:
  - ``CatSwarmOptimizer`` (``"cso"``, PMC7204373)
  - ``GeneticOptimizer`` (``"ga"``)
  - ``ParticleSwarmOptimizer`` (``"pso"``)
  - ``DifferentialEvolutionOptimizer`` (``"de"``)
  - ``GreyWolfOptimizer`` (``"gwo"``)
  - ``SimulatedAnnealingOptimizer`` (``"sa"``)
  - ``RandomSearchOptimizer`` (``"random"``)
- Factory & runner: ``create_optimizer``, ``run_optimization``, ``list_available_optimizers``
"""

from optimizer.base import (
    BATTALION_GROUPS,
    BaseDivisionOptimizer,
    CandidateSolution,
    DivisionGenome,
    FitnessMetrics,
    GENOME_VECTOR_DIM,
    OPTIMIZER_REGISTRY,
    OptimizationConfig,
    RegimentColumnGene,
    UnitPool,
    register_optimizer,
    serialize_division,
)
from optimizer.objectives import (
    DivisionEvaluator,
    OBJECTIVE_DESCRIPTIONS,
    build_benchmark_opponents,
    compute_terrain_width_efficiency,
)
from optimizer.cat_swarm import CatAgent, CatSwarmOptimizer
from optimizer.genetic import (
    DifferentialEvolutionOptimizer,
    GeneticOptimizer,
    RandomSearchOptimizer,
    SimulatedAnnealingOptimizer,
)
from optimizer.particle_swarm import (
    GreyWolfOptimizer,
    Particle,
    ParticleSwarmOptimizer,
)
from optimizer.setup import (
    CANONICAL_METHODS,
    build_config_from_kwargs,
    create_optimizer,
    list_available_optimizers,
    run_optimization,
)

__all__ = [
    "BATTALION_GROUPS",
    "BaseDivisionOptimizer",
    "CANONICAL_METHODS",
    "CandidateSolution",
    "CatAgent",
    "CatSwarmOptimizer",
    "DifferentialEvolutionOptimizer",
    "DivisionEvaluator",
    "DivisionGenome",
    "FitnessMetrics",
    "GENOME_VECTOR_DIM",
    "GeneticOptimizer",
    "GreyWolfOptimizer",
    "OBJECTIVE_DESCRIPTIONS",
    "OPTIMIZER_REGISTRY",
    "OptimizationConfig",
    "Particle",
    "ParticleSwarmOptimizer",
    "RandomSearchOptimizer",
    "RegimentColumnGene",
    "SimulatedAnnealingOptimizer",
    "UnitPool",
    "build_benchmark_opponents",
    "build_config_from_kwargs",
    "compute_terrain_width_efficiency",
    "create_optimizer",
    "list_available_optimizers",
    "register_optimizer",
    "run_optimization",
    "serialize_division",
]

"""
optimizer/setup.py
==================
Factory, Registry, and High-Level Runner for the Agnostic Optimization Engine.

Provides a unified entry point to instantiate or execute any registered
metaheuristic algorithm (`"cso"`, `"ga"`, `"pso"`, `"de"`, `"gwo"`, `"sa"`,
`"random"`, or custom user-registered plugins via ``@register_optimizer``).

Example Usage
-------------
>>> from optimizer.setup import create_optimizer, run_optimization, register_optimizer
>>> # 1. Run with Cat Swarm Optimization (CSO)
>>> result = run_optimization(method="cso", year="1940", objective="bang_for_buck", iterations=20)
>>> # 2. Swap to Genetic Algorithm (GA), Particle Swarm (PSO), or Differential Evolution (DE)
>>> result_ga = run_optimization(method="ga", year="1940", objective="bang_for_buck", iterations=20)
"""

from __future__ import annotations

from dataclasses import fields
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from optimizer.base import (
    BaseDivisionOptimizer,
    OPTIMIZER_REGISTRY,
    OptimizationConfig,
    register_optimizer,
)
from optimizer.objectives import DivisionEvaluator, OBJECTIVE_DESCRIPTIONS
from optimizer.cat_swarm import CatSwarmOptimizer
from optimizer.genetic import (
    DifferentialEvolutionOptimizer,
    GeneticOptimizer,
    RandomSearchOptimizer,
    SimulatedAnnealingOptimizer,
)
from optimizer.particle_swarm import (
    GreyWolfOptimizer,
    ParticleSwarmOptimizer,
)


CANONICAL_METHODS: Tuple[str, ...] = ("cso", "ga", "pso", "de", "gwo", "sa", "random")


def list_available_optimizers() -> Dict[str, str]:
    """
    Returns a dictionary mapping canonical optimizer method keys to their
    human-readable algorithm names.
    """
    result: Dict[str, str] = {}
    seen_classes = set()
    for key in CANONICAL_METHODS:
        if key in OPTIMIZER_REGISTRY:
            cls = OPTIMIZER_REGISTRY[key]
            result[key] = getattr(cls, "ALGORITHM_NAME", cls.__name__)
            seen_classes.add(cls)
    for key, cls in OPTIMIZER_REGISTRY.items():
        if cls not in seen_classes:
            result[key] = getattr(cls, "ALGORITHM_NAME", cls.__name__)
            seen_classes.add(cls)
    return result


def build_config_from_kwargs(
    config: Optional[OptimizationConfig] = None,
    **kwargs: Any,
) -> OptimizationConfig:
    """
    Constructs or updates an ``OptimizationConfig`` from arbitrary keyword
    arguments, routing unknown algorithm-specific keys into ``method_params``.
    """
    valid_field_names = {f.name for f in fields(OptimizationConfig)}
    if config is not None:
        cfg_dict = config.to_dict()
    else:
        cfg_dict = {}

    extra_params: Dict[str, Any] = dict(cfg_dict.get("method_params") or {})
    for k, v in kwargs.items():
        if v is None and k not in ("target_combat_width", "max_ic_cost", "max_manpower", "random_seed", "doctrine_mastery"):
            continue
        if k in valid_field_names:
            cfg_dict[k] = v
        else:
            extra_params[k] = v

    cfg_dict["method_params"] = extra_params
    return OptimizationConfig(**cfg_dict)


def create_optimizer(
    config: Union[OptimizationConfig, str, None] = None,
    evaluator: Optional[DivisionEvaluator] = None,
    on_step_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
    **kwargs: Any,
) -> BaseDivisionOptimizer:
    """
    Factory function that instantiates the requested ``BaseDivisionOptimizer``
    subclass from ``OPTIMIZER_REGISTRY``.

    Parameters
    ----------
    config : OptimizationConfig | str | None
        Either an ``OptimizationConfig`` instance, a method name string
        (e.g., ``"cso"``, ``"ga"``, ``"pso"``, ``"de"``, ``"gwo"``, ``"sa"``, ``"random"``),
        or ``None`` (in which case ``kwargs`` are used to build ``OptimizationConfig``).
    evaluator : DivisionEvaluator, optional
        Pre-constructed multi-terrain objective evaluator.
    on_step_callback : Callable[[dict], None], optional
        Telemetry hook called at the end of every iteration.
    **kwargs
        Any ``OptimizationConfig`` field overrides or custom ``method_params``.
    """
    if isinstance(config, str):
        kwargs["method"] = config
        cfg = build_config_from_kwargs(None, **kwargs)
    elif isinstance(config, OptimizationConfig):
        cfg = build_config_from_kwargs(config, **kwargs) if kwargs else config
    else:
        cfg = build_config_from_kwargs(None, **kwargs)

    method_key = cfg.method.lower().strip()
    if method_key not in OPTIMIZER_REGISTRY:
        available = ", ".join(sorted(OPTIMIZER_REGISTRY.keys()))
        raise ValueError(
            f"Unknown optimization method '{cfg.method}'. "
            f"Available registered methods: {available}"
        )

    optimizer_cls = OPTIMIZER_REGISTRY[method_key]
    return optimizer_cls(
        config=cfg,
        evaluator=evaluator,
        on_step_callback=on_step_callback,
    )


def run_optimization(
    config: Union[OptimizationConfig, str, None] = None,
    on_step_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
    enable_dashboard: bool = False,
    open_browser: bool = True,
    enable_logging: bool = False,
    log_dir: str = "logs",
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    High-level convenience function that creates an optimizer from ``config``
    (or keyword arguments), optionally launches the ``LiveDashboardServer``
    and ``TrainingTelemetryLogger``, runs the optimization to completion, and
    returns the final optimization results dictionary.
    """
    dashboard = None
    telemetry = None
    logger = None

    optimizer = create_optimizer(
        config=config,
        on_step_callback=None,
        **kwargs,
    )

    if enable_logging:
        from optimizer.logger import TrainingTelemetryLogger, setup_logger
        logger = setup_logger(name="hoi4_optimizer", log_dir=log_dir, console=True)
        telemetry = TrainingTelemetryLogger(log_dir=log_dir, logger=logger)
        telemetry.log_configuration(optimizer.config)

    if enable_dashboard:
        from optimizer.dashboard import LiveDashboardServer
        dashboard = LiveDashboardServer(
            open_browser=open_browser,
            logger=logger,
            initial_config=optimizer.config,
        )
        dashboard.start(open_browser=open_browser)

    def combined_callback(snapshot: Dict[str, Any]) -> None:
        if telemetry is not None:
            telemetry.log_iteration(snapshot)
        if dashboard is not None:
            dashboard.update_state(snapshot)
        if on_step_callback is not None:
            on_step_callback(snapshot)

    try:
        result = optimizer.run(on_step_callback=combined_callback)
        if dashboard is not None:
            dashboard.mark_completed(result)
        if telemetry is not None:
            telemetry.log_completion(result, elapsed_seconds=result.get("elapsed_seconds"))
        return result
    finally:
        if dashboard is not None:
            dashboard.stop()

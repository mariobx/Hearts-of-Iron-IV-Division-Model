#!/usr/bin/env python3
"""
Comprehensive Algorithm-Agnostic Command-Line Interface (CLI) for the
HOI4 v1.19.4.2 Division Template Optimizer & Combat Simulator.

This module provides a unified CLI (`cli.py`) supporting four primary workflows:
1. **`optimize`** (default subcommand):
   - Runs any registered optimization algorithm (`cso`, `ga`, `pso`, `de`, `sa`,
     `random`, or custom plugins registered in `OPTIMIZER_REGISTRY`) for a target
     technological era (`1934`, `1936`, `1939`, `1940`, `1945`) and strategic
     objective (`best_overall`, `bang_for_buck`, `offensive_breakthrough`,
     `defensive_wall`, `terrain_specialist`).
   - Automatically launches the zero-dependency `LiveDashboardServer` background
     web dashboard (`optimizer/dashboard.py`) and streams structured telemetry to
     `logs/` (`optimizer/logger.py`).
   - Accepts arbitrary algorithm-specific hyperparameters via `--param key=value`.

2. **`compare`**:
   - Runs multiple optimization algorithms head-to-head under identical era,
     objective, and evaluation budgets, streaming live progress to the web
     dashboard and exporting a comparative Markdown/JSON benchmark report.

3. **`battle`**:
   - Simulates a single detailed battle or a Monte Carlo series of battles between
     any two division templates across one or all 8 HOI4 terrains (`Plains`,
     `Forest`, `Hills`, `Jungle`, `Mountain`, `Marsh`, `Desert`, `Urban`).

4. **`units`**:
   - Lists and inspects official HOI4 v1.19.4.2 (`Operation Postern`) land
     battalions, Divisional Support companies, and Regimental Support companies
     for any supported year.
"""

from __future__ import annotations

import argparse
import inspect
import json
import logging
import os
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

# Ensure repository root is importable regardless of working directory
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import division_database
import doctrines
import tank_designer
from terrain import ALL_TERRAINS, Terrain
import unit_database
from optimizer.dashboard import LiveDashboardServer
from optimizer.logger import (
    METHOD_DISPLAY_NAMES,
    OBJECTIVE_DISPLAY_NAMES,
    STANDARD_TERRAINS,
    TrainingTelemetryLogger,
    extract_division_summary,
    setup_logger,
)


# ==============================================================================
# DYNAMIC REGISTRY DISCOVERY & HYPERPARAMETER PARSING
# ==============================================================================

DEFAULT_FALLBACK_METHODS: List[str] = ["cso", "ga", "pso", "de", "sa", "random"]

SUPPORTED_OBJECTIVES: List[str] = [
    "best_overall",
    "bang_for_buck",
    "offensive_breakthrough",
    "defensive_wall",
    "terrain_specialist",
]


def discover_available_methods() -> List[str]:
    """
    Dynamically discover all optimization algorithm keys registered in
    `optimizer.setup.OPTIMIZER_REGISTRY` or `optimizer.base.OPTIMIZER_REGISTRY`.
    Falls back gracefully to `DEFAULT_FALLBACK_METHODS` if modules are still loading.

    Returns
    -------
    List[str]
        Ordered list of canonical method identifiers.
    """
    discovered: List[str] = []
    try:
        from optimizer import setup as opt_setup
        reg = getattr(opt_setup, "OPTIMIZER_REGISTRY", None)
        if isinstance(reg, dict) and reg:
            discovered.extend(reg.keys())
    except Exception:
        pass

    if not discovered:
        try:
            from optimizer import base as opt_base
            reg = getattr(opt_base, "OPTIMIZER_REGISTRY", None)
            if isinstance(reg, dict) and reg:
                discovered.extend(reg.keys())
        except Exception:
            pass

    # Preserve canonical primary names first, then append any additional aliases/plugins
    ordered: List[str] = []
    for m in DEFAULT_FALLBACK_METHODS:
        if m not in ordered:
            ordered.append(m)
    for m in discovered:
        m_clean = str(m).lower().strip()
        if m_clean and m_clean not in ordered:
            ordered.append(m_clean)
    return ordered


def discover_supported_years() -> List[str]:
    """
    Discover all technological benchmark years available in `unit_database.py`.

    Returns
    -------
    List[str]
        Sorted list of year strings (e.g., `["1934", "1936", "1939", "1940", "1945"]`).
    """
    explicit_years = getattr(unit_database, "SUPPORTED_YEARS", None)
    if isinstance(explicit_years, (list, tuple)) and explicit_years:
        return [str(y) for y in explicit_years]

    all_bats = getattr(unit_database, "All_Battalions", {})
    years = sorted(str(y) for y in all_bats.keys())
    for must_have in ("1934", "1936", "1939", "1940", "1945"):
        if must_have not in years:
            years.append(must_have)
    return sorted(years)


def parse_key_value_params(param_list: Optional[List[str]]) -> Dict[str, Any]:
    """
    Parse repeatable `--param key=value` CLI arguments into typed Python values
    (`bool`, `int`, `float`, or `str`).

    Parameters
    ----------
    param_list : Optional[List[str]]
        List of `"key=value"` strings from `argparse`.

    Returns
    -------
    Dict[str, Any]
        Dictionary of parsed hyperparameter overrides.
    """
    parsed: Dict[str, Any] = {}
    if not param_list:
        return parsed

    for item in param_list:
        if "=" not in item:
            raise ValueError(
                f"Invalid --param '{item}': expected format KEY=VALUE (e.g., --param cso_smp=7)."
            )
        raw_key, raw_val = item.split("=", 1)
        key = raw_key.strip()
        val_str = raw_val.strip()
        if not key:
            continue

        lower_val = val_str.lower()
        if lower_val in ("true", "yes", "on"):
            parsed[key] = True
        elif lower_val in ("false", "no", "off"):
            parsed[key] = False
        elif lower_val in ("none", "null"):
            parsed[key] = None
        else:
            try:
                if "." in val_str or "e" in lower_val:
                    parsed[key] = float(val_str)
                else:
                    parsed[key] = int(val_str)
            except ValueError:
                parsed[key] = val_str

    return parsed


def parse_terrain_list(raw_terrains: Optional[List[str]]) -> List[str]:
    """
    Normalize a list of terrain arguments (supporting space-separated or
    comma-separated terrain names, or `'all'`).
    """
    if not raw_terrains:
        return list(ALL_TERRAINS.keys())

    tokens: List[str] = []
    for item in raw_terrains:
        for part in item.split(","):
            cleaned = part.strip()
            if cleaned:
                tokens.append(cleaned)

    if not tokens or any(t.lower() == "all" for t in tokens):
        return list(ALL_TERRAINS.keys())

    resolved: List[str] = []
    for tok in tokens:
        match = next((k for k in ALL_TERRAINS.keys() if k.lower() == tok.lower()), None)
        if match is None:
            valid_str = ", ".join(ALL_TERRAINS.keys())
            raise ValueError(f"Unknown terrain '{tok}'. Valid terrains are: {valid_str}")
        if match not in resolved:
            resolved.append(match)
    return resolved


# ==============================================================================
# OPTIMIZER INSTANTIATION HELPER
# ==============================================================================

def build_optimization_config(args: argparse.Namespace, method_override: Optional[str] = None) -> Any:
    """
    Construct an `OptimizationConfig` instance from parsed CLI arguments and any
    `--param key=value` algorithm hyperparameter overrides.
    """
    from optimizer.base import OptimizationConfig

    method_name = (method_override or getattr(args, "method", "cso") or "cso").lower().strip()
    terrains = parse_terrain_list(getattr(args, "terrains", None))
    extra_params = parse_key_value_params(getattr(args, "param", None))

    config_kwargs: Dict[str, Any] = {
        "method": method_name,
        "year": str(getattr(args, "year", "1945")),
        "objective": str(getattr(args, "objective", "best_overall")),
        "terrains": terrains,
        "doctrine": str(getattr(args, "doctrine", "none") or "none"),
        "doctrine_mastery": getattr(args, "doctrine_mastery", None),
        "tank_design_mode": str(getattr(args, "tank_mode", "historical") or "historical"),
        "population_size": int(getattr(args, "population", 24)),
        "iterations": int(getattr(args, "iterations", 30)),
        "battles_per_evaluation": int(getattr(args, "battles_per_eval", 3)),
        "target_combat_width": getattr(args, "target_width", None),
        "min_combat_width": float(getattr(args, "min_width", 10.0)),
        "max_combat_width": float(getattr(args, "max_width", 42.0)),
        "max_ic_cost": getattr(args, "max_ic", None),
        "max_manpower": getattr(args, "max_manpower", None),
        "allow_special_projects": not bool(getattr(args, "no_special_projects", False)),
        "allow_country_locked": bool(getattr(args, "allow_country_locked", False)),
        "allow_regimental_support": not bool(getattr(args, "no_regimental_support", False)),
        "random_seed": getattr(args, "seed", 42),
        "method_params": dict(extra_params),
    }

    # If any `--param key=value` matches a top-level field on OptimizationConfig, set it directly too
    valid_fields = set(OptimizationConfig.__dataclass_fields__.keys())
    for k, v in extra_params.items():
        if k in valid_fields and k != "method_params":
            config_kwargs[k] = v

    return OptimizationConfig(**config_kwargs)


def instantiate_optimizer(
    config: Any,
    on_step_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Any:
    """
    Instantiate the requested optimizer via `optimizer.setup.create_optimizer`
    (with fallback to `OPTIMIZER_REGISTRY` or direct algorithm module imports).
    """
    try:
        from optimizer import setup as opt_setup
        create_fn = getattr(opt_setup, "create_optimizer", None)
        if callable(create_fn):
            return create_fn(config, on_step_callback=on_step_callback)
    except Exception:
        pass

    # Fallback: check OPTIMIZER_REGISTRY in optimizer.base after importing modules
    for mod_name in ("cat_swarm", "genetic", "particle_swarm"):
        try:
            __import__(f"optimizer.{mod_name}")
        except Exception:
            pass

    from optimizer.base import OPTIMIZER_REGISTRY

    method_key = config.method.lower().strip()
    if method_key in OPTIMIZER_REGISTRY:
        opt_cls = OPTIMIZER_REGISTRY[method_key]
        return opt_cls(config=config, on_step_callback=on_step_callback)

    raise ValueError(
        f"Optimization method '{method_key}' is not registered. "
        f"Available methods: {', '.join( sorted(OPTIMIZER_REGISTRY.keys()) )}"
    )


# ==============================================================================
# SUBCOMMAND 1: `optimize` — SINGLE ALGORITHM DIVISION OPTIMIZATION
# ==============================================================================

def cmd_optimize(args: argparse.Namespace) -> int:
    """
    Execute a division optimization run with live web dashboard and structured
    telemetry logging.
    """
    log_level = logging.DEBUG if getattr(args, "verbose", False) else logging.INFO
    log_dir = getattr(args, "log_dir", "logs")
    logger = setup_logger(name="hoi4_optimizer", log_dir=log_dir, level=log_level, console=True)
    telemetry = TrainingTelemetryLogger(log_dir=log_dir, logger=logger)

    config = build_optimization_config(args)
    telemetry.log_configuration(config)

    open_browser = not bool(getattr(args, "no_browser", False))
    preferred_port = int(getattr(args, "port", 8765) or 8765)
    dashboard = LiveDashboardServer(
        preferred_port=preferred_port,
        open_browser=open_browser,
        logger=logger,
        initial_config=config,
    )
    dashboard_url = dashboard.start(open_browser=open_browser)
    logger.info("Live Training Webpage active at: %s", dashboard_url)

    def combined_step_callback(snapshot: Dict[str, Any]) -> None:
        telemetry.log_iteration(snapshot)
        dashboard.update_state(snapshot)

    try:
        optimizer = instantiate_optimizer(config, on_step_callback=combined_step_callback)
        result = optimizer.run(on_step_callback=combined_step_callback)
        dashboard.mark_completed(result)
        telemetry.log_completion(result, elapsed_seconds=result.get("elapsed_seconds"))

        # Print winning division grid & stats to console
        best_div = result.get("best_division")
        if best_div is not None and hasattr(best_div, "print_composition_grid"):
            print("\n")
            best_div.print_composition_grid()
            print("")
            best_div.print_stats_table()

        # Export Markdown and JSON reports
        output_arg = getattr(args, "output", None)
        if output_arg:
            if output_arg.endswith(".json"):
                json_path = telemetry.export_json_report(result, output_path=output_arg)
                md_path = telemetry.export_markdown_report(
                    result, output_path=os.path.splitext(output_arg)[0] + ".md"
                )
            elif output_arg.endswith(".md"):
                md_path = telemetry.export_markdown_report(result, output_path=output_arg)
                json_path = telemetry.export_json_report(
                    result, output_path=os.path.splitext(output_arg)[0] + ".json"
                )
            else:
                md_path = telemetry.export_markdown_report(result, output_path=output_arg + ".md")
                json_path = telemetry.export_json_report(result, output_path=output_arg + ".json")
        else:
            md_path = telemetry.export_markdown_report(result)
            json_path = telemetry.export_json_report(result)

        logger.info("Reports saved: Markdown=%s | JSON=%s", md_path, json_path)

        if getattr(args, "keep_alive", False):
            logger.info(
                "Dashboard server kept alive at %s — press Ctrl+C to exit.",
                dashboard_url,
            )
            try:
                while True:
                    time.sleep(0.5)
            except KeyboardInterrupt:
                logger.info("Received Ctrl+C, shutting down dashboard server.")
        return 0
    finally:
        dashboard.stop()


# ==============================================================================
# SUBCOMMAND 2: `compare` — MULTI-ALGORITHM HEAD-TO-HEAD BENCHMARK
# ==============================================================================

def cmd_compare(args: argparse.Namespace) -> int:
    """
    Run multiple optimization algorithms head-to-head on the same year and
    objective, streaming live updates to the web dashboard and generating a
    comparative leaderboard report.
    """
    log_level = logging.DEBUG if getattr(args, "verbose", False) else logging.INFO
    log_dir = getattr(args, "log_dir", "logs")
    logger = setup_logger(name="hoi4_optimizer", log_dir=log_dir, level=log_level, console=True)
    telemetry = TrainingTelemetryLogger(log_dir=log_dir, logger=logger)

    raw_methods = getattr(args, "methods", None) or ["cso", "ga", "pso", "sa", "random"]
    methods: List[str] = []
    for item in raw_methods:
        for part in str(item).split(","):
            m = part.strip().lower()
            if m and m not in methods:
                methods.append(m)

    first_config = build_optimization_config(args, method_override=methods[0])
    open_browser = not bool(getattr(args, "no_browser", False))
    preferred_port = int(getattr(args, "port", 8765) or 8765)

    dashboard = LiveDashboardServer(
        preferred_port=preferred_port,
        open_browser=open_browser,
        logger=logger,
        initial_config=first_config,
    )
    dashboard_url = dashboard.start(open_browser=open_browser)
    logger.info("Head-to-Head Comparison Live Webpage active at: %s", dashboard_url)

    comparison_results: Dict[str, Any] = {}
    try:
        for idx, method_key in enumerate(methods, start=1):
            logger.info(
                "=== [Comparison %d/%d] Running Algorithm: %s ===",
                idx,
                len(methods),
                METHOD_DISPLAY_NAMES.get(method_key, method_key.upper()),
            )
            config = build_optimization_config(args, method_override=method_key)
            telemetry.log_configuration(config)

            def step_cb(snapshot: Dict[str, Any]) -> None:
                telemetry.log_iteration(snapshot)
                dashboard.update_state(snapshot)

            optimizer = instantiate_optimizer(config, on_step_callback=step_cb)
            res = optimizer.run(on_step_callback=step_cb)
            comparison_results[method_key] = res
            dashboard.record_comparison_method(method_key, res)

        dashboard.mark_completed()
        md_path, json_path = telemetry.export_comparison_report(
            {"methods": comparison_results},
            output_path=getattr(args, "output", None),
        )

        # Print formatted head-to-head comparison table to stdout
        print("\n" + "=" * 105)
        print(
            f"HEAD-TO-HEAD ALGORITHM COMPARISON (Year: {first_config.year} | "
            f"Objective: {first_config.objective})"
        )
        print("=" * 105)
        print(
            f"{'Rank':<6} {'Method':<12} {'Fitness':>10} {'Win %':>9} "
            f"{'Att/Def %':>15} {'IC Cost':>9} {'Width':>7}  {'Winning Division Composition'}"
        )
        print("-" * 105)

        ranked = sorted(
            comparison_results.items(),
            key=lambda kv: extract_division_summary(kv[1].get("leader"))["total_fitness"],
            reverse=True,
        )
        for rank_idx, (m_key, m_res) in enumerate(ranked, start=1):
            summary = extract_division_summary(m_res.get("leader"))
            st = summary["stats"]
            att_def = f"{summary['attacker_win_rate']*100:.1f}/{summary['defender_win_rate']*100:.1f}%"
            print(
                f"#{rank_idx:<5} {m_key.upper():<12} {summary['total_fitness']:>10.4f} "
                f"{summary['win_rate']*100:>8.1f}% {att_def:>15} "
                f"{st['ic_cost']:>9.0f} {st['combat_width']:>7.0f}  {summary['composition_summary']}"
            )
        print("=" * 105)
        print(f"Comparison Markdown Report : {md_path}")
        print(f"Comparison JSON Report     : {json_path}\n")

        if getattr(args, "keep_alive", False):
            logger.info("Dashboard server kept alive at %s — press Ctrl+C to exit.", dashboard_url)
            try:
                while True:
                    time.sleep(0.5)
            except KeyboardInterrupt:
                pass
        return 0
    finally:
        dashboard.stop()


# ==============================================================================
# SUBCOMMAND 3: `battle` — TACTICAL BATTLE & MONTE CARLO SIMULATOR
# ==============================================================================

def _discover_preset_templates() -> Dict[str, Callable[[], Any]]:
    """
    Discover all `create_*` division factory functions in `division_database.py`
    and map convenient short aliases (e.g., `standard_infantry_1936`,
    `medium_armor_1940`) to their factory callables.
    """
    presets: Dict[str, Callable[[], Any]] = {}
    for attr_name, attr_val in inspect.getmembers(division_database, callable):
        if attr_name.startswith("create_"):
            short_key = attr_name[len("create_"):].lower()
            presets[short_key] = attr_val
            presets[attr_name.lower()] = attr_val
    return presets


def _resolve_division_template(name_or_key: str, presets: Dict[str, Callable[[], Any]]) -> Any:
    """Resolve a preset template name or partial match into a `Division` instance."""
    key = name_or_key.strip().lower().replace("-", "_").replace(" ", "_")
    if key in presets:
        return presets[key]()
    for p_key, factory in presets.items():
        if key in p_key:
            return factory()
    valid_keys = sorted(k for k in presets.keys() if not k.startswith("create_"))
    raise ValueError(
        f"Unknown division preset '{name_or_key}'. Available presets: {', '.join(valid_keys)}"
    )


def cmd_battle(args: argparse.Namespace) -> int:
    """
    Simulate a battle or Monte Carlo series of battles between two preset
    division templates across one or all terrains.
    """
    presets = _discover_preset_templates()
    if getattr(args, "list_presets", False):
        print("\nAvailable Preset Division Templates (`division_database.py`):")
        print("-" * 68)
        for key in sorted(k for k in presets.keys() if not k.startswith("create_")):
            div = presets[key]()
            st = div.calculate_stats()
            print(
                f"  {key:<32} | {div.name:<28} | Width={st.combat_width:>4.0f} | IC={st.ic_cost:>6.0f}"
            )
        print("-" * 68)
        return 0

    attacker = _resolve_division_template(args.attacker, presets)
    defender = _resolve_division_template(args.defender, presets)
    trials = max(1, int(getattr(args, "trials", 25)))
    terrains = parse_terrain_list(getattr(args, "terrain", None))

    att_stats = attacker.calculate_stats()
    def_stats = defender.calculate_stats()

    print("\n" + "=" * 84)
    print(f"HOI4 v1.19.4.2 TACTICAL BATTLE SIMULATION ({trials} Monte Carlo Trials / Terrain)")
    print("=" * 84)
    print(f"  Attacker : {attacker.name} (Width={att_stats.combat_width:.0f}, IC={att_stats.ic_cost:.1f}, ORG={att_stats.organization:.1f})")
    print(f"  Defender : {defender.name} (Width={def_stats.combat_width:.0f}, IC={def_stats.ic_cost:.1f}, ORG={def_stats.organization:.1f})")
    print("-" * 84)
    print(
        f"{'Terrain':<14} {'Attacker Win %':>15} {'Defender Win %':>15} "
        f"{'Avg Rem ORG (A/D)':>20} {'Avg Duration':>16}"
    )
    print("-" * 84)

    total_wins = 0
    total_battles = 0

    for t_name in terrains:
        terrain_obj: Terrain = ALL_TERRAINS[t_name]
        att_wins = 0
        rem_att_org = 0.0
        rem_def_org = 0.0
        total_days = 0.0

        for _ in range(trials):
            res = attacker.battle(defender, terrain_obj, verbose=False)
            if res["winner"] == attacker.name:
                att_wins += 1
            rem_att_org += float(res.get("attacker_final_org", 0.0))
            rem_def_org += float(res.get("defender_final_org", 0.0))
            total_days += float(res.get("duration_days", 0.0))

        win_pct = (att_wins / trials) * 100.0
        def_pct = 100.0 - win_pct
        avg_a_org = rem_att_org / trials
        avg_d_org = rem_def_org / trials
        avg_days = total_days / trials

        total_wins += att_wins
        total_battles += trials

        print(
            f"{t_name:<14} {win_pct:>14.1f}% {def_pct:>14.1f}% "
            f"{avg_a_org:>9.1f} / {avg_d_org:<8.1f} {avg_days:>11.1f} days"
        )

    overall_win_pct = (total_wins / max(1, total_battles)) * 100.0
    print("-" * 84)
    print(
        f"OVERALL ATTACKER WIN RATE ACROSS {len(terrains)} TERRAIN(S): {overall_win_pct:.1f}% "
        f"({total_wins}/{total_battles} battles won)"
    )
    print("=" * 84 + "\n")
    return 0


# ==============================================================================
# SUBCOMMAND 4: `units` — OFFICIAL HOI4 v1.19.4.2 UNIT DATABASE INSPECTOR
# ==============================================================================

def cmd_units(args: argparse.Namespace) -> int:
    """
    List and inspect official HOI4 v1.19.4.2 battalions, divisional support
    companies, regimental support companies, v1.19 Land Doctrines, or NSB Tank
    Designer blueprints for a given year.
    """
    year = str(getattr(args, "year", "1945"))

    if getattr(args, "list_doctrines", False):
        print("\n" + "=" * 112)
        print("OFFICIAL HOI4 v1.19.4.2 LAND DOCTRINES (4 Grand Doctrines & 36 Track Sub-Doctrines)")
        print("=" * 112)
        print("\n[A] CANONICAL DOCTRINE PRESETS (--doctrine <key>)")
        print("-" * 112)
        for k, name in doctrines.list_available_doctrines(include_subdoctrines=False).items():
            doc_summary = doctrines.get_doctrine_summary(k, year=year)
            subs = doc_summary.get("subdoctrines", {})
            sub_str = ", ".join(f"{tr}={sd}" for tr, sd in subs.items() if sd)
            print(f"  {k:<38} | {name:<44} | {sub_str}")

        print("\n[B] ALL 36 LAND SUB-DOCTRINES BY TRACK")
        print("-" * 112)
        for tr_key in ("infantry", "combat_support", "armor", "operations"):
            tr_subs = doctrines.list_all_subdoctrines(track=tr_key)
            print(f"  Track [{tr_key.upper()}] ({len(tr_subs)} sub-doctrines):")
            for sd_k, sd_name in sorted(tr_subs.items()):
                print(f"    - {sd_k:<34} : {sd_name}")
        print("=" * 112 + "\n")
        return 0

    if getattr(args, "design_tank", False):
        tank_mode = str(getattr(args, "tank_mode", "nsb_auto_optimize") or "nsb_auto_optimize")
        if tank_mode == "historical":
            tank_mode = "nsb_auto_optimize"
        print("\n" + "=" * 112)
        print(f"OFFICIAL HOI4 v1.19.4.2 NSB TANK DESIGNER BLUEPRINTS — YEAR {year} (Mode: {tank_mode})")
        print("=" * 112)
        for w_cls in ("light", "medium", "heavy", "super_heavy", "modern", "amphibious", "land_cruiser"):
            try:
                bp = tank_designer.optimize_tank_blueprint(
                    chassis_class=w_cls,
                    role="tank",
                    year=year,
                    objective=tank_mode,
                )
                eq = bp.calculate_equipment_stats()
                print(
                    f"  [{w_cls.upper():<12}] {bp.chassis_id:<26} | Turret={bp.turret_id:<26} | "
                    f"Gun={bp.main_armament_id}"
                )
                print(
                    f"                 SA={eq['soft_attack']:.1f} HA={eq['hard_attack']:.1f} "
                    f"Brk={eq['breakthrough']:.1f} Def={eq['defense']:.1f} "
                    f"Armor={eq['armor_value']:.1f} Pierc={eq['ap_attack']:.1f} "
                    f"Spd={eq['maximum_speed']:.1f} Rel={eq['reliability']*100:.0f}% IC={eq['build_cost_ic']:.1f}"
                )
            except Exception:
                continue
        print("=" * 112 + "\n")
        return 0

    category_filter = str(getattr(args, "category", "all")).lower()
    search_query = (getattr(args, "search", None) or "").lower().strip()
    allow_sp = not bool(getattr(args, "no_special_projects", False))
    allow_cl = bool(getattr(args, "allow_country_locked", False))
    doctrine_key = str(getattr(args, "doctrine", "none") or "none")
    doctrine_mastery = getattr(args, "doctrine_mastery", None)
    tank_mode = str(getattr(args, "tank_mode", "historical") or "historical")

    from optimizer.base import OptimizationConfig, UnitPool

    cfg = OptimizationConfig(
        year=year,
        doctrine=doctrine_key,
        doctrine_mastery=doctrine_mastery,
        tank_design_mode=tank_mode,
        allow_special_projects=allow_sp,
        allow_country_locked=allow_cl,
    )
    pool = UnitPool(cfg)

    print("\n" + "=" * 112)
    print(
        f"OFFICIAL HOI4 v1.19.4.2 UNIT DATABASE — YEAR {year} | "
        f"Doctrine: {doctrine_key} | Tank Mode: {tank_mode}"
    )
    print("=" * 112)

    if category_filter in ("all", "battalions", "battalion"):
        print(f"\n[1] LINE BATTALIONS ({len(pool.battalions_by_name)} units)")
        print("-" * 112)
        print(
            f"{'Unit Name':<34} {'Group':<10} {'Width':>5} {'ORG':>6} {'HP':>6} "
            f"{'SA':>6} {'HA':>6} {'Def':>6} {'Brk':>6} {'Armor':>6} {'Pierc':>6} {'IC Cost':>8}"
        )
        print("-" * 112)
        for name, bat in sorted(pool.battalions_by_name.items()):
            if search_query and search_query not in name.lower():
                continue
            s = bat.get_stats()
            grp = pool.get_battalion_group(bat)
            print(
                f"{name:<34} {grp:<10} {s.combat_width:>5.1f} {s.organization:>6.1f} {s.max_hp:>6.1f} "
                f"{s.soft_attack:>6.1f} {s.hard_attack:>6.1f} {s.defense:>6.1f} {s.breakthrough:>6.1f} "
                f"{s.armor:>6.1f} {s.piercing:>6.1f} {s.ic_cost:>8.1f}"
            )

    if category_filter in ("all", "divisional_support", "support"):
        print(f"\n[2] DIVISIONAL SUPPORT COMPANIES ({len(pool.divisional_supports_by_name)} units)")
        print("-" * 112)
        print(
            f"{'Support Company Name':<34} {'Family':<16} {'ORG':>6} {'HP':>5} "
            f"{'SA':>6} {'HA':>6} {'Def':>6} {'Brk':>6} {'Entr':>5} {'Rec':>5} {'IC Cost':>8}"
        )
        print("-" * 112)
        for name, sup in sorted(pool.divisional_supports_by_name.items()):
            if search_query and search_query not in name.lower():
                continue
            s = sup.get_stats()
            fam = pool.get_support_type(sup)
            print(
                f"{name:<34} {fam:<16} {s.organization:>6.1f} {s.max_hp:>5.1f} "
                f"{s.soft_attack:>6.1f} {s.hard_attack:>6.1f} {s.defense:>6.1f} {s.breakthrough:>6.1f} "
                f"{s.entrenchment:>5.1f} {s.recon:>5.1f} {s.ic_cost:>8.1f}"
            )

    if category_filter in ("all", "regimental_support", "regimental"):
        print(f"\n[3] HOI4 v1.19 REGIMENTAL SUPPORT COMPANIES ({len(pool.regimental_supports_by_name)} units)")
        print("-" * 112)
        print(
            f"{'Regimental Support Name':<34} {'Allowed Groups':<24} {'ORG':>6} "
            f"{'SA':>6} {'HA':>6} {'Def':>6} {'Brk':>6} {'Pierc':>6} {'IC Cost':>8}"
        )
        print("-" * 112)
        for name, rsup in sorted(pool.regimental_supports_by_name.items()):
            if search_query and search_query not in name.lower():
                continue
            s = rsup.get_stats()
            grps = ",".join(pool.get_allowed_regimental_groups(rsup))
            print(
                f"{name:<34} {grps:<24} {s.organization:>6.1f} "
                f"{s.soft_attack:>6.1f} {s.hard_attack:>6.1f} {s.defense:>6.1f} {s.breakthrough:>6.1f} "
                f"{s.piercing:>6.1f} {s.ic_cost:>8.1f}"
            )

    print("=" * 112 + "\n")
    return 0


# ==============================================================================
# ARGUMENT PARSER CONSTRUCTION
# ==============================================================================

def _add_common_optimization_arguments(parser: argparse.ArgumentParser) -> None:
    """Attach shared optimization arguments to `optimize`, `compare`, and root parser."""
    available_methods = discover_available_methods()
    supported_years = discover_supported_years()

    parser.add_argument(
        "--method",
        "-m",
        type=str,
        default="cso",
        help=(
            f"Optimization algorithm identifier. Discovered registry methods: "
            f"{', '.join(available_methods)} (default: cso)."
        ),
    )
    parser.add_argument(
        "--year",
        "-y",
        type=str,
        default="1945",
        choices=supported_years,
        help=f"Target HOI4 technological year: {', '.join(supported_years)} (default: 1945).",
    )
    parser.add_argument(
        "--doctrine",
        type=str,
        default="none",
        help=(
            "HOI4 v1.19.4.2 Land Doctrine preset (none, mobile_warfare, superior_firepower, "
            "grand_battleplan, mass_assault, etc.), single sub-doctrine key, or custom composite "
            "'<grand>:<infantry>,<combat_support>,<armor>,<operations>' (default: none)."
        ),
    )
    parser.add_argument(
        "--doctrine-mastery",
        type=float,
        default=None,
        help="Optional explicit doctrine mastery level in [0.0, 1.0] (default: year-based or 1.0).",
    )
    parser.add_argument(
        "--tank-mode",
        type=str,
        default="historical",
        choices=tank_designer.TANK_DESIGN_MODES,
        help=(
            f"NSB Tank Designer mode: {', '.join(tank_designer.TANK_DESIGN_MODES)} "
            "(default: historical)."
        ),
    )
    parser.add_argument(
        "--objective",
        "-o",
        type=str,
        default="best_overall",
        choices=SUPPORTED_OBJECTIVES,
        help=(
            "Strategic optimization objective: best_overall, bang_for_buck, "
            "offensive_breakthrough, defensive_wall, terrain_specialist (default: best_overall)."
        ),
    )
    parser.add_argument(
        "--terrains",
        "-t",
        nargs="+",
        default=None,
        help="Target terrain names (e.g., Plains Forest Mountain or 'all'). Defaults to all 8 terrains.",
    )
    parser.add_argument(
        "--iterations",
        "-i",
        type=int,
        default=30,
        help="Number of optimization iterations to execute (default: 30).",
    )
    parser.add_argument(
        "--population",
        "-p",
        type=int,
        default=24,
        help="Population / swarm size (default: 24).",
    )
    parser.add_argument(
        "--battles-per-eval",
        type=int,
        default=3,
        help="Monte Carlo battle trials per opponent-terrain pair (default: 3).",
    )
    parser.add_argument(
        "--target-width",
        type=float,
        default=None,
        help="Optional target combat width (e.g., 20, 30).",
    )
    parser.add_argument(
        "--min-width",
        type=float,
        default=10.0,
        help="Minimum allowed division combat width (default: 10.0).",
    )
    parser.add_argument(
        "--max-width",
        type=float,
        default=42.0,
        help="Maximum allowed division combat width (default: 42.0).",
    )
    parser.add_argument(
        "--max-ic",
        type=float,
        default=None,
        help="Optional maximum IC production cost cap for candidate divisions.",
    )
    parser.add_argument(
        "--max-manpower",
        type=float,
        default=None,
        help="Optional maximum manpower cap for candidate divisions.",
    )
    parser.add_argument(
        "--no-special-projects",
        action="store_true",
        help="Exclude Special Project units (Land Cruiser, Flame Tanks, Helicopters, etc.).",
    )
    parser.add_argument(
        "--allow-country-locked",
        action="store_true",
        help="Include country-specific units (Elephantry, Camelry, Bicycle, etc.).",
    )
    parser.add_argument(
        "--no-regimental-support",
        action="store_true",
        help="Disable HOI4 v1.19 Regimental Support company slots.",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not automatically pop up a web browser window when training starts.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8765,
        help="Preferred local TCP port for the live training web dashboard (default: 8765).",
    )
    parser.add_argument(
        "--keep-alive",
        action="store_true",
        help="Keep the live web dashboard server running after optimization finishes until Ctrl+C.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Deterministic random seed (default: 42).",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help=(
            "Repeatable algorithm-agnostic hyperparameter override "
            "(e.g., --param cso_smp=7 --param cso_mr=0.3 --param ga_mutation_rate=0.2)."
        ),
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional path for exported Markdown/JSON report files.",
    )
    parser.add_argument(
        "--log-dir",
        type=str,
        default="logs",
        help="Directory for structured logs and telemetry JSONL streams (default: logs).",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose DEBUG logging.",
    )


def build_arg_parser() -> argparse.ArgumentParser:
    """Build and return the top-level `argparse.ArgumentParser` for `cli.py`."""
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description=(
            "HOI4 v1.19.4.2 Algorithm-Agnostic Division Optimizer, Live Telemetry "
            "Web Dashboard & Multi-Terrain Combat Simulator."
        ),
    )
    _add_common_optimization_arguments(parser)

    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    # 1. `optimize` subcommand
    opt_parser = subparsers.add_parser(
        "optimize",
        help="Optimize a division template using any registered metaheuristic algorithm.",
    )
    _add_common_optimization_arguments(opt_parser)

    # 2. `compare` subcommand
    cmp_parser = subparsers.add_parser(
        "compare",
        help="Compare multiple optimization algorithms head-to-head on the same year/objective.",
    )
    _add_common_optimization_arguments(cmp_parser)
    cmp_parser.add_argument(
        "--methods",
        nargs="+",
        default=["cso", "ga", "pso", "sa", "random"],
        help="List of optimization methods to compare head-to-head (e.g., --methods cso ga pso de sa random).",
    )

    # 3. `battle` subcommand
    bat_parser = subparsers.add_parser(
        "battle",
        help="Simulate single or Monte Carlo battles between two preset division templates.",
    )
    bat_parser.add_argument(
        "--attacker",
        "-a",
        type=str,
        default="medium_armor_1940",
        help="Attacker preset template name (e.g., medium_armor_1940, offensive_infantry_1936).",
    )
    bat_parser.add_argument(
        "--defender",
        "-d",
        type=str,
        default="standard_infantry_1936",
        help="Defender preset template name (e.g., standard_infantry_1936, heavy_infantry_1940).",
    )
    bat_parser.add_argument(
        "--terrain",
        "-t",
        nargs="+",
        default=["all"],
        help="Terrain name(s) or 'all' (default: all).",
    )
    bat_parser.add_argument(
        "--trials",
        "-n",
        type=int,
        default=25,
        help="Number of Monte Carlo battle trials per terrain (default: 25).",
    )
    bat_parser.add_argument(
        "--list-presets",
        action="store_true",
        help="List all available preset division templates and exit.",
    )

    # 4. `units` subcommand
    unit_parser = subparsers.add_parser(
        "units",
        help="Inspect official HOI4 v1.19.4.2 battalions, support companies, doctrines, and NSB tank designs.",
    )
    unit_parser.add_argument(
        "--year",
        "-y",
        type=str,
        default="1945",
        choices=discover_supported_years(),
        help="Technological benchmark year (default: 1945).",
    )
    unit_parser.add_argument(
        "--doctrine",
        type=str,
        default="none",
        help="Optional v1.19 Land Doctrine key to apply to unit stats (default: none).",
    )
    unit_parser.add_argument(
        "--doctrine-mastery",
        type=float,
        default=None,
        help="Optional explicit doctrine mastery level in [0.0, 1.0].",
    )
    unit_parser.add_argument(
        "--tank-mode",
        type=str,
        default="historical",
        choices=tank_designer.TANK_DESIGN_MODES,
        help="Optional NSB Tank Designer mode to apply to tank units (default: historical).",
    )
    unit_parser.add_argument(
        "--list-doctrines",
        action="store_true",
        help="List all official v1.19 Land Doctrines and 36 Sub-Doctrines and exit.",
    )
    unit_parser.add_argument(
        "--design-tank",
        action="store_true",
        help="Generate and display optimal NSB Tank Designer blueprints for the target year and exit.",
    )
    unit_parser.add_argument(
        "--category",
        "-c",
        type=str,
        default="all",
        choices=["all", "battalions", "divisional_support", "regimental_support"],
        help="Filter by unit category (default: all).",
    )
    unit_parser.add_argument(
        "--search",
        "-s",
        type=str,
        default=None,
        help="Case-insensitive substring filter on unit name.",
    )
    unit_parser.add_argument(
        "--no-special-projects",
        action="store_true",
        help="Exclude Special Project units.",
    )
    unit_parser.add_argument(
        "--allow-country-locked",
        action="store_true",
        help="Include country-locked units.",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main CLI entrypoint. Dispatches to `optimize` (default), `compare`, `battle`,
    or `units`.
    """
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    subcmd = getattr(args, "subcommand", None) or "optimize"
    if subcmd == "optimize":
        return cmd_optimize(args)
    if subcmd == "compare":
        return cmd_compare(args)
    if subcmd == "battle":
        return cmd_battle(args)
    if subcmd == "units":
        return cmd_units(args)

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())

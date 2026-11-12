"""
Extensive Structured Logging & Telemetry System for the HOI4 Division Optimizer.

This module provides a zero-external-dependency, thread-safe logging and telemetry
infrastructure designed for agnostic metaheuristic optimization experiments (including
Cat Swarm Optimization per PMC7204373, Genetic Algorithms, Particle Swarm Optimization,
Simulated Annealing, and Random Search).

Key Features
------------
1. **Dual-Sink Structured Logging (`setup_logger`)**:
   - Configures a hierarchical Python `logging.Logger` writing timestamped, structured
     messages to both a persistent log file (`logs/hoi4_optimizer_<timestamp>.log`)
     and standard output (with optional ANSI color formatting on interactive terminals).
   - Maintains a `logs/hoi4_optimizer_latest.log` copy/reference for quick inspection.

2. **Real-Time JSONL Iteration Telemetry (`TrainingTelemetryLogger`)**:
   - Streams every optimization step snapshot to `logs/telemetry_<timestamp>.jsonl`
     in JSON Lines (JSONL) format with immediate disk flushing so no telemetry is lost
     if a long training run is interrupted.
   - Implements `on_step(snapshot)` and `__call__(snapshot)` so an instance can be wired
     directly into `BaseDivisionOptimizer.on_step_callback` (or chained alongside
     `LiveDashboardServer.update_state`).

3. **Agnostic Object Normalization (`serialize_for_telemetry`, `extract_division_summary`)**:
   - Transparently serializes `Division`, `CandidateSolution`, `FitnessMetrics`,
     `OptimizationConfig`, `BaseStatistics`, `TerrainModifier`, `Battalion`,
     `SupportCompany`, dataclasses, and arbitrary dictionaries into clean JSON-safe
     structures.

4. **Automated Post-Training Reports (`export_markdown_report`, `export_json_report`,
   `export_comparison_report`)**:
   - Generates comprehensive Markdown and JSON reports detailing the winning division's
     5x5 Brigade/Regiment Grid, Divisional Support slots, HOI4 v1.19 Regimental Support
     slots, full combat statistics, multi-terrain win-rate breakdown, convergence curve,
     and Hall of Fame leaderboard.
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
import json
import logging
import os
from pathlib import Path
import sys
import threading
import time
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union


# ==============================================================================
# MODULE CONSTANTS & HUMAN-READABLE LABELS
# ==============================================================================

METHOD_DISPLAY_NAMES: Dict[str, str] = {
    "cso": "Cat Swarm Optimization (CSO — PMC7204373)",
    "cat_swarm": "Cat Swarm Optimization (CSO — PMC7204373)",
    "ga": "Genetic Algorithm (GA)",
    "genetic": "Genetic Algorithm (GA)",
    "pso": "Particle Swarm Optimization (PSO)",
    "particle_swarm": "Particle Swarm Optimization (PSO)",
    "de": "Differential Evolution (DE)",
    "differential_evolution": "Differential Evolution (DE)",
    "gwo": "Grey Wolf Optimizer (GWO)",
    "grey_wolf": "Grey Wolf Optimizer (GWO)",
    "sa": "Simulated Annealing (SA)",
    "simulated_annealing": "Simulated Annealing (SA)",
    "random": "Random Search Baseline",
    "random_search": "Random Search Baseline",
}

OBJECTIVE_DISPLAY_NAMES: Dict[str, str] = {
    "best_overall": "Best Overall (Multi-Terrain Attacker & Defender Dominance)",
    "bang_for_buck": "Bang for Buck (Combat Effectiveness per IC Cost)",
    "offensive_breakthrough": "Offensive Breakthrough (Shock, Armor & Speed of Victory)",
    "defensive_wall": "Defensive Wall (Entrenchment, Defense & ORG Retention)",
    "terrain_specialist": "Terrain Specialist (Targeted Theatre Dominance)",
}

STANDARD_TERRAINS: List[str] = [
    "Plains",
    "Forest",
    "Hills",
    "Jungle",
    "Mountain",
    "Marsh",
    "Desert",
    "Urban",
]


# ==============================================================================
# ANSI COLOR FORMATTER FOR CONSOLE LOGGING
# ==============================================================================

class ConsoleColorFormatter(logging.Formatter):
    """
    Custom log formatter that applies subtle ANSI color highlights to log levels
    when outputting to an interactive terminal (TTY), while keeping file logs
    pure plain text.
    """

    LEVEL_COLORS: Dict[int, str] = {
        logging.DEBUG: "\033[36m",     # Cyan
        logging.INFO: "\033[32m",      # Green
        logging.WARNING: "\033[33m",   # Yellow
        logging.ERROR: "\033[31m",     # Red
        logging.CRITICAL: "\033[1;31m" # Bold Red
    }
    RESET_CODE: str = "\033[0m"

    def __init__(self, fmt: str, datefmt: str = "%Y-%m-%d %H:%M:%S", use_color: bool = True) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)
        self.use_color = use_color and hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified log record with optional ANSI level coloring."""
        if not self.use_color:
            return super().format(record)

        original_levelname = record.levelname
        color_prefix = self.LEVEL_COLORS.get(record.levelno, "")
        if color_prefix:
            record.levelname = f"{color_prefix}{original_levelname:<8}{self.RESET_CODE}"
        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname


# ==============================================================================
# LOGGER SETUP & ACCESSORS
# ==============================================================================

_LOGGER_LOCK = threading.Lock()
_ACTIVE_LOG_FILES: Dict[str, str] = {}


def setup_logger(
    name: str = "hoi4_optimizer",
    log_dir: str = "logs",
    level: int = logging.INFO,
    console: bool = True,
    log_filename: Optional[str] = None,
) -> logging.Logger:
    """
    Configure and return a structured Python `logging.Logger` writing to both
    console and a timestamped log file in `log_dir`.

    Parameters
    ----------
    name : str, default="hoi4_optimizer"
        The name of the logger instance in Python's logging hierarchy.
    log_dir : str, default="logs"
        Directory path where timestamped `.log` files will be created.
    level : int, default=logging.INFO
        Minimum logging severity level (e.g., `logging.DEBUG`, `logging.INFO`).
    console : bool, default=True
        Whether to attach a console `StreamHandler` writing to `sys.stdout`.
    log_filename : Optional[str], default=None
        Explicit filename for the log file. If `None`, automatically generates
        `hoi4_optimizer_<YYYYMMDD_HHMMSS>.log`.

    Returns
    -------
    logging.Logger
        Configured logger instance with `.log_file_path` attribute attached.
    """
    with _LOGGER_LOCK:
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        resolved_filename = log_filename or f"hoi4_optimizer_{timestamp_str}.log"
        log_file_path = os.path.abspath(os.path.join(log_dir, resolved_filename))

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = False

        # Close and remove existing handlers to prevent duplicate log lines on re-init
        for existing_handler in list(logger.handlers):
            try:
                existing_handler.flush()
                existing_handler.close()
            except Exception:
                pass
            logger.removeHandler(existing_handler)

        file_format = (
            "%(asctime)s | %(levelname)-8s | %(name)s | "
            "%(module)s:%(funcName)s:%(lineno)d | %(message)s"
        )
        console_format = "%(asctime)s | %(levelname)-8s | %(message)s"

        # 1. Timestamped File Handler (always captures DEBUG and above if logger allows)
        file_handler = logging.FileHandler(log_file_path, mode="a", encoding="utf-8")
        file_handler.setLevel(min(level, logging.DEBUG))
        file_handler.setFormatter(logging.Formatter(fmt=file_format, datefmt="%Y-%m-%d %H:%M:%S"))
        logger.addHandler(file_handler)

        # 2. Also maintain a `hoi4_optimizer_latest.log` file handler for convenience
        latest_log_path = os.path.abspath(os.path.join(log_dir, "hoi4_optimizer_latest.log"))
        if latest_log_path != log_file_path:
            try:
                latest_handler = logging.FileHandler(latest_log_path, mode="w", encoding="utf-8")
                latest_handler.setLevel(min(level, logging.DEBUG))
                latest_handler.setFormatter(logging.Formatter(fmt=file_format, datefmt="%Y-%m-%d %H:%M:%S"))
                logger.addHandler(latest_handler)
            except OSError:
                pass

        # 3. Optional Console Handler
        if console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(level)
            console_handler.setFormatter(ConsoleColorFormatter(fmt=console_format))
            logger.addHandler(console_handler)

        # Attach metadata attributes for inspection by CLI and tests
        setattr(logger, "log_file_path", log_file_path)
        setattr(logger, "log_dir", os.path.abspath(log_dir))
        _ACTIVE_LOG_FILES[name] = log_file_path

        logger.debug("Initialized structured logger '%s' -> %s", name, log_file_path)
        return logger


def get_logger(name: str = "hoi4_optimizer") -> logging.Logger:
    """
    Retrieve an active logger by name, initializing it with default settings
    if it has no handlers attached yet.

    Parameters
    ----------
    name : str, default="hoi4_optimizer"
        Logger name to retrieve.

    Returns
    -------
    logging.Logger
        Active logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name=name)
    return logger


# ==============================================================================
# AGNOSTIC DATA SERIALIZATION & DIVISION SUMMARY EXTRACTION
# ==============================================================================

def serialize_for_telemetry(obj: Any, _depth: int = 0) -> Any:
    """
    Recursively convert arbitrary simulation/optimizer objects into JSON-serializable
    Python primitives (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`).

    Handles:
    - Objects implementing `.to_dict()` (e.g., `Division`, `CandidateSolution`, `FitnessMetrics`)
    - Python `@dataclass` instances (e.g., `BaseStatistics`, `OptimizationConfig`, `TerrainModifier`)
    - `Battalion` and `SupportCompany` objects
    - Standard mappings, sequences, sets, and primitive values

    Parameters
    ----------
    obj : Any
        Object to serialize.
    _depth : int, default=0
        Internal recursion depth guard.

    Returns
    -------
    Any
        JSON-serializable structure.
    """
    if _depth > 12:
        return str(obj)

    if obj is None or isinstance(obj, (bool, int, str)):
        return obj

    if isinstance(obj, float):
        if obj != obj or obj == float("inf") or obj == float("-inf"):
            return 0.0
        return round(obj, 6)

    # Prefer explicit `.to_dict()` if defined on custom classes
    if hasattr(obj, "to_dict") and callable( getattr(obj, "to_dict") ):
        try:
            return serialize_for_telemetry(obj.to_dict(), _depth + 1)
        except Exception:
            pass

    # Handle Division objects that may not yet have `.to_dict()`
    if hasattr(obj, "battalions") and hasattr(obj, "support_companies") and hasattr(obj, "calculate_stats"):
        return _serialize_division_fallback(obj, _depth + 1)

    # Handle Battalion / SupportCompany objects
    if hasattr(obj, "base_stats") and hasattr(obj, "name"):
        unit_dict: Dict[str, Any] = {
            "name": getattr(obj, "name", ""),
            "group": getattr(obj, "group", "support" if hasattr(obj, "is_divisional") else "infantry"),
        }
        if hasattr(obj, "is_divisional"):
            unit_dict["is_divisional"] = bool(getattr(obj, "is_divisional", True))
            unit_dict["is_regimental"] = bool(getattr(obj, "is_regimental", False))
        return unit_dict

    if is_dataclass(obj) and not isinstance(obj, type):
        try:
            return serialize_for_telemetry(asdict(obj), _depth + 1)
        except Exception:
            return {
                k: serialize_for_telemetry(getattr(obj, k), _depth + 1)
                for k in obj.__dataclass_fields__
            }

    if isinstance(obj, dict):
        return {
            str(k): serialize_for_telemetry(v, _depth + 1)
            for k, v in obj.items()
        }

    if isinstance(obj, (list, tuple, set)):
        return [serialize_for_telemetry(item, _depth + 1) for item in obj]

    if hasattr(obj, "__dict__"):
        return {
            str(k): serialize_for_telemetry(v, _depth + 1)
            for k, v in vars(obj).items()
            if not str(k).startswith("_")
        }

    return str(obj)


def _infer_unit_group(unit_name: str, unit_obj: Any = None) -> str:
    """
    Infer the official HOI4 v1.19 battalion group (`infantry`, `combat_support`,
    `mobile`, `mobile_combat_support`, `armor`, `armor_combat_support`) for a
    battalion from its attributes or name.
    """
    if unit_obj is not None:
        explicit_group = getattr(unit_obj, "group", None)
        if isinstance(explicit_group, str) and explicit_group:
            return explicit_group
        if isinstance(unit_obj, dict) and unit_obj.get("group"):
            return str(unit_obj["group"])

    lower = (unit_name or "").lower()
    if any(k in lower for k in ["sp anti-air", "sp artillery", "tank destroyer", "sp rocket", "self-propelled", "assault gun"]):
        return "armor_combat_support"
    if any(k in lower for k in ["tank", "land cruiser"]):
        return "armor"
    if any(k in lower for k in ["mot. r.", "motorized rocket", "motorized artillery", "motorized anti-tank", "motorized anti-air", "mot_"]):
        return "mobile_combat_support"
    if any(k in lower for k in ["motorized", "mechanized", "cavalry", "camelry", "bicycle", "amtrac", "armored car", "elephantry"]):
        return "mobile"
    if any(k in lower for k in ["artillery", "anti-air", "anti-tank", "rocket"]):
        return "combat_support"
    return "infantry"


def _serialize_division_fallback(division: Any, _depth: int = 0) -> Dict[str, Any]:
    """
    Fallback serializer for `Division` instances in case `division.to_dict()` is
    not available or returns a partial dictionary.
    """
    stats_obj = division.calculate_stats()
    stats_dict = serialize_for_telemetry(stats_obj, _depth + 1)

    battalion_counts: Dict[str, int] = {}
    for bat in getattr(division, "battalions", []):
        b_name = getattr(bat, "name", str(bat))
        battalion_counts[b_name] = battalion_counts.get(b_name, 0) + 1

    support_names = [
        getattr(comp, "name", str(comp))
        for comp in getattr(division, "support_companies", [])
        if comp is not None
    ]

    regimental_support_raw = getattr(division, "regimental_support_companies", [None] * 5)
    regimental_support_names = [
        getattr(comp, "name", str(comp)) if comp is not None else None
        for comp in regimental_support_raw
    ]

    # Build 5x5 regiment columns with group metadata
    raw_regiments = getattr(division, "regiments", None)
    if not raw_regiments:
        grid_data = division.get_composition_grid() if hasattr(division, "get_composition_grid") else {}
        raw_regiments = grid_data.get("regiments", [])

    regiment_columns: List[List[Dict[str, str]]] = []
    column_groups: List[Optional[str]] = []
    for col_idx in range(5):
        if col_idx < len(raw_regiments) and raw_regiments[col_idx]:
            col_units = []
            for bat in raw_regiments[col_idx][:5]:
                b_name = bat.get("name", "") if isinstance(bat, dict) else getattr(bat, "name", str(bat))
                b_group = _infer_unit_group(b_name, bat)
                col_units.append({"name": b_name, "group": b_group})
            regiment_columns.append(col_units)
            column_groups.append(col_units[0]["group"] if col_units else None)
        else:
            regiment_columns.append([])
            column_groups.append(None)

    terrain_mods: Dict[str, Dict[str, float]] = {}
    if hasattr(division, "calculate_terrain_modifiers"):
        try:
            raw_mods = division.calculate_terrain_modifiers()
            terrain_mods = serialize_for_telemetry(raw_mods, _depth + 1)
        except Exception:
            terrain_mods = {}

    is_valid = True
    violations: List[str] = []
    if hasattr(division, "validate_division_rules"):
        try:
            is_valid, violations = division.validate_division_rules()
        except Exception:
            pass

    return {
        "name": getattr(division, "name", "Candidate Division"),
        "stats": stats_dict,
        "terrain_modifiers": terrain_mods,
        "battalion_counts": battalion_counts,
        "support_names": support_names,
        "regimental_support_names": regimental_support_names,
        "grid": {
            "support": support_names[:5],
            "regiments": regiment_columns,
            "column_groups": column_groups,
            "regimental_support": regimental_support_names[:5],
        },
        "is_valid": is_valid,
        "violations": violations,
    }


def extract_division_summary(candidate: Any) -> Dict[str, Any]:
    """
    Normalize any candidate representation (`CandidateSolution`, `Division`, or `dict`)
    into a unified dictionary structure used by both `TrainingTelemetryLogger` and
    `LiveDashboardServer`.

    Guaranteed Return Keys
    ----------------------
    - `name`: str
    - `total_fitness`: float
    - `win_rate`: float (0.0 to 1.0)
    - `attacker_win_rate`: float (0.0 to 1.0)
    - `defender_win_rate`: float (0.0 to 1.0)
    - `avg_org_remaining_ratio`: float
    - `avg_hp_remaining_ratio`: float
    - `ic_efficiency_score`: float
    - `bang_for_buck_score`: float
    - `terrain_win_rates`: Dict[str, float]
    - `stats`: Dict[str, float] (all 19 `BaseStatistics` fields)
    - `terrain_modifiers`: Dict[str, Dict[str, float]]
    - `battalion_counts`: Dict[str, int]
    - `support_names`: List[str]
    - `regimental_support_names`: List[Optional[str]]
    - `grid`: Dict[str, Any] (`support`, `regiments`, `column_groups`, `regimental_support`)
    - `composition_summary`: str
    - `is_valid`: bool
    """
    if candidate is None:
        return _empty_division_summary()

    raw = serialize_for_telemetry(candidate)
    if not isinstance(raw, dict):
        return _empty_division_summary()

    # Extract nested division & metrics dicts if present
    div_dict = raw.get("division") if isinstance(raw.get("division"), dict) else raw
    metrics_dict = raw.get("metrics") if isinstance(raw.get("metrics"), dict) else raw

    # Extract stats dictionary from any supported location
    stats_src = (
        div_dict.get("stats")
        or raw.get("stats")
        or metrics_dict.get("combat_stats_summary")
        or raw.get("combat_stats_summary")
        or {}
    )
    if not isinstance(stats_src, dict):
        stats_src = {}

    default_stat_keys = [
        "soft_attack", "hard_attack", "defense", "breakthrough",
        "max_hp", "organization", "combat_width", "supply_use",
        "ic_cost", "manpower", "armor", "piercing", "hardness",
        "air_attack", "entrenchment", "initiative", "recon",
        "supply_consumption_factor", "recovery_rate",
    ]
    stats: Dict[str, float] = {
        k: float(stats_src.get(k, 0.0) or 0.0) for k in default_stat_keys
    }

    # Extract fitness & win rates
    total_fitness = float(
        metrics_dict.get("total_fitness")
        if metrics_dict.get("total_fitness") is not None
        else raw.get("total_fitness", raw.get("fitness", 0.0)) or 0.0
    )
    win_rate = float(
        metrics_dict.get("win_rate")
        if metrics_dict.get("win_rate") is not None
        else raw.get("win_rate", 0.0) or 0.0
    )
    attacker_win_rate = float(
        metrics_dict.get("attacker_win_rate")
        if metrics_dict.get("attacker_win_rate") is not None
        else raw.get("attacker_win_rate", win_rate) or 0.0
    )
    defender_win_rate = float(
        metrics_dict.get("defender_win_rate")
        if metrics_dict.get("defender_win_rate") is not None
        else raw.get("defender_win_rate", win_rate) or 0.0
    )
    avg_org_ratio = float(
        metrics_dict.get("avg_org_remaining_ratio", raw.get("avg_org_remaining_ratio", 0.0)) or 0.0
    )
    avg_hp_ratio = float(
        metrics_dict.get("avg_hp_remaining_ratio", raw.get("avg_hp_remaining_ratio", 0.0)) or 0.0
    )

    ic_cost = stats["ic_cost"]
    ic_eff = float(
        metrics_dict.get("ic_efficiency_score")
        or metrics_dict.get("bang_for_buck_score")
        or metrics_dict.get("Bang_for_buck_score")
        or raw.get("ic_efficiency_score")
        or raw.get("bang_for_buck_score")
        or (total_fitness / max(0.1, ic_cost / 1000.0) if ic_cost > 0 else 0.0)
    )

    # Terrain win rates
    raw_terrain_wr = (
        metrics_dict.get("terrain_win_rates")
        or raw.get("terrain_win_rates")
        or {}
    )
    terrain_win_rates: Dict[str, float] = {}
    if isinstance(raw_terrain_wr, dict):
        for t_name in STANDARD_TERRAINS:
            if t_name in raw_terrain_wr:
                terrain_win_rates[t_name] = float(raw_terrain_wr[t_name] or 0.0)
        for k, v in raw_terrain_wr.items():
            if k not in terrain_win_rates:
                terrain_win_rates[str(k)] = float(v or 0.0)

    # Extract grid, battalions, and supports
    comp_dict = raw.get("composition") if isinstance(raw.get("composition"), dict) else {}
    raw_grid = div_dict.get("grid") or raw.get("grid") or {}
    columns_meta = (
        div_dict.get("columns")
        or comp_dict.get("columns")
        or raw.get("columns")
        or []
    )

    support_names: List[str] = list(
        div_dict.get("support_names")
        or div_dict.get("support_companies")
        or comp_dict.get("support_companies")
        or raw.get("support_names")
        or raw.get("support_companies")
        or raw_grid.get("support")
        or []
    )
    support_names = [
        s.get("name", str(s)) if isinstance(s, dict) else str(s)
        for s in support_names
        if s
    ][:5]

    # Extract regimental supports per column (up to 5 columns)
    reg_support_raw: List[Any] = []
    if isinstance(columns_meta, list) and len(columns_meta) > 0 and isinstance(columns_meta[0], dict):
        reg_support_raw = [col_d.get("regimental_support") for col_d in columns_meta[:5]]
    else:
        reg_support_raw = list(
            div_dict.get("regimental_support_names")
            or raw.get("regimental_support_names")
            or raw_grid.get("regimental_support")
            or [None] * 5
        )
    regimental_support_names: List[Optional[str]] = []
    for idx in range(5):
        item = reg_support_raw[idx] if idx < len(reg_support_raw) else None
        if item is None or item == "-" or item == "" or item == "none":
            regimental_support_names.append(None)
        elif isinstance(item, dict):
            regimental_support_names.append(str(item.get("name") or "") or None)
        else:
            regimental_support_names.append(str(item))

    # Normalize 5x5 regiment columns
    raw_regiments = raw_grid.get("regiments") or div_dict.get("regiments") or []
    if not raw_regiments and isinstance(columns_meta, list) and columns_meta:
        raw_regiments = []
        for col_d in columns_meta[:5]:
            if isinstance(col_d, dict):
                col_grp = str(col_d.get("group") or "")
                col_bats = col_d.get("battalions") or []
                raw_regiments.append([
                    {
                        "name": b.get("name", str(b)) if isinstance(b, dict) else str(b),
                        "group": (
                            col_grp
                            if col_grp and col_grp != "none"
                            else _infer_unit_group(b.get("name", str(b)) if isinstance(b, dict) else str(b))
                        ),
                    }
                    for b in col_bats
                    if b
                ])
            else:
                raw_regiments.append([])

    normalized_regiments: List[List[Dict[str, str]]] = []
    column_groups: List[Optional[str]] = []

    battalion_counts: Dict[str, int] = dict(
        div_dict.get("battalion_counts")
        or comp_dict.get("battalion_counts")
        or raw.get("battalion_counts")
        or {}
    )

    # If raw_regiments is empty but battalion_counts exists, reconstruct columns
    if not raw_regiments and battalion_counts:
        flat_units: List[Tuple[str, str]] = []
        for b_name, count in battalion_counts.items():
            b_group = _infer_unit_group(str(b_name))
            for _ in range(int(count)):
                flat_units.append((str(b_name), b_group))
        # Group into columns by battalion group (max 5 per column, max 5 columns)
        cols_temp: List[List[Dict[str, str]]] = []
        for b_name, b_group in flat_units[:25]:
            placed = False
            for col in cols_temp:
                if len(col) < 5 and col[0]["group"] == b_group:
                    col.append({"name": b_name, "group": b_group})
                    placed = True
                    break
            if not placed and len(cols_temp) < 5:
                cols_temp.append([{"name": b_name, "group": b_group}])
        raw_regiments = cols_temp

    for col_idx in range(5):
        col_data = raw_regiments[col_idx] if col_idx < len(raw_regiments) else []
        col_units: List[Dict[str, str]] = []
        if isinstance(col_data, list):
            for cell in col_data[:5]:
                if cell is None or cell == "-" or cell == "":
                    continue
                if isinstance(cell, dict):
                    u_name = str(cell.get("name", ""))
                    u_group = str(cell.get("group") or _infer_unit_group(u_name, cell))
                else:
                    u_name = str(cell)
                    u_group = _infer_unit_group(u_name)
                if u_name:
                    col_units.append({"name": u_name, "group": u_group})
        normalized_regiments.append(col_units)
        column_groups.append(col_units[0]["group"] if col_units else None)

    # Recompute battalion_counts if it was empty
    if not battalion_counts:
        for col in normalized_regiments:
            for cell in col:
                u_name = cell["name"]
                battalion_counts[u_name] = battalion_counts.get(u_name, 0) + 1

    # Build human-readable composition summary string
    bat_parts = [
        f"{cnt}x {name}"
        for name, cnt in sorted(battalion_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        if cnt > 0
    ]
    bat_str = ", ".join(bat_parts) if bat_parts else "Empty Brigade"
    sup_str = ", ".join(support_names) if support_names else "None"
    active_reg_sup = [r for r in regimental_support_names if r]
    reg_sup_str = f" | Reg.Sup: {', '.join(active_reg_sup)}" if active_reg_sup else ""
    composition_summary = f"{bat_str} | Sup: {sup_str}{reg_sup_str}"

    div_name = str(
        div_dict.get("name")
        or raw.get("name")
        or "Optimized Division"
    )

    return {
        "name": div_name,
        "method": str(raw.get("method", "")),
        "total_fitness": round(total_fitness, 4),
        "win_rate": round(win_rate, 4),
        "attacker_win_rate": round(attacker_win_rate, 4),
        "defender_win_rate": round(defender_win_rate, 4),
        "avg_org_remaining_ratio": round(avg_org_ratio, 4),
        "avg_hp_remaining_ratio": round(avg_hp_ratio, 4),
        "ic_efficiency_score": round(ic_eff, 4),
        "bang_for_buck_score": round(ic_eff, 4),
        "terrain_win_rates": terrain_win_rates,
        "stats": stats,
        "terrain_modifiers": div_dict.get("terrain_modifiers") or raw.get("terrain_modifiers") or {},
        "battalion_counts": battalion_counts,
        "support_names": support_names,
        "regimental_support_names": regimental_support_names,
        "grid": {
            "support": support_names,
            "regiments": normalized_regiments,
            "column_groups": column_groups,
            "regimental_support": regimental_support_names,
        },
        "composition_summary": composition_summary,
        "is_valid": bool(div_dict.get("is_valid", raw.get("is_valid", True))),
    }


def _empty_division_summary() -> Dict[str, Any]:
    """Return a safe empty division summary structure prior to iteration 1."""
    return {
        "name": "Awaiting First Evaluation...",
        "method": "",
        "total_fitness": 0.0,
        "win_rate": 0.0,
        "attacker_win_rate": 0.0,
        "defender_win_rate": 0.0,
        "avg_org_remaining_ratio": 0.0,
        "avg_hp_remaining_ratio": 0.0,
        "ic_efficiency_score": 0.0,
        "bang_for_buck_score": 0.0,
        "terrain_win_rates": {t: 0.0 for t in STANDARD_TERRAINS},
        "stats": {
            "soft_attack": 0.0, "hard_attack": 0.0, "defense": 0.0, "breakthrough": 0.0,
            "max_hp": 0.0, "organization": 0.0, "combat_width": 0.0, "supply_use": 0.0,
            "ic_cost": 0.0, "manpower": 0.0, "armor": 0.0, "piercing": 0.0, "hardness": 0.0,
            "air_attack": 0.0, "entrenchment": 0.0, "initiative": 0.0, "recon": 0.0,
            "supply_consumption_factor": 0.0, "recovery_rate": 0.0,
        },
        "terrain_modifiers": {},
        "battalion_counts": {},
        "support_names": [],
        "regimental_support_names": [None] * 5,
        "grid": {
            "support": [],
            "regiments": [[], [], [], [], []],
            "column_groups": [None] * 5,
            "regimental_support": [None] * 5,
        },
        "composition_summary": "Initializing population...",
        "is_valid": True,
    }


# ==============================================================================
# TRAINING TELEMETRY LOGGER CLASS
# ==============================================================================

class TrainingTelemetryLogger:
    """
    Structured telemetry recorder and report generator for division optimization runs.

    Every iteration's snapshot is:
    1. Normalized into a schema-consistent dictionary.
    2. Written as a JSON line to `logs/telemetry_<timestamp>.jsonl` with immediate flush.
    3. Logged as a concise, high-signal summary line to the active `logging.Logger`.

    At the end of training, `export_markdown_report()` and `export_json_report()`
    produce human-readable and machine-readable artifacts.
    """

    def __init__(
        self,
        log_dir: str = "logs",
        logger: Optional[logging.Logger] = None,
        telemetry_filename: Optional[str] = None,
    ) -> None:
        """
        Initialize the telemetry logger and create the JSONL telemetry file.

        Parameters
        ----------
        log_dir : str, default="logs"
            Directory where telemetry `.jsonl` and exported reports are stored.
        logger : Optional[logging.Logger], default=None
            Python logger instance. If `None`, retrieves or creates `"hoi4_optimizer"`.
        telemetry_filename : Optional[str], default=None
            Custom filename for the JSONL telemetry stream.
        """
        self.log_dir = os.path.abspath(log_dir)
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)

        self.logger = logger or get_logger("hoi4_optimizer")
        self.timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        jsonl_name = telemetry_filename or f"telemetry_{self.timestamp_str}.jsonl"
        self.telemetry_file_path = os.path.join(self.log_dir, jsonl_name)

        self._lock = threading.Lock()
        self._start_time = time.time()
        self.snapshots: List[Dict[str, Any]] = []
        self.config_record: Dict[str, Any] = {}

        # Touch the JSONL file immediately so external watchers can tail it
        with open(self.telemetry_file_path, "a", encoding="utf-8"):
            pass

        self.logger.info(
            "Telemetry JSONL stream initialized at: %s",
            self.telemetry_file_path,
        )

    def _append_jsonl(self, record: Dict[str, Any]) -> None:
        """Thread-safely append a single JSON record to the JSONL telemetry file."""
        payload = json.dumps(serialize_for_telemetry(record), ensure_ascii=False)
        with self._lock:
            with open(self.telemetry_file_path, "a", encoding="utf-8") as fh:
                fh.write(payload + "\n")
                fh.flush()

    def log_configuration(self, config: Any) -> Dict[str, Any]:
        """
        Record the optimization configuration at the beginning of a training run.

        Parameters
        ----------
        config : Any
            `OptimizationConfig` dataclass or dictionary of parameters.

        Returns
        -------
        Dict[str, Any]
            Serialized configuration dictionary.
        """
        config_dict = serialize_for_telemetry(config)
        if not isinstance(config_dict, dict):
            config_dict = {"raw_config": str(config)}

        self.config_record = config_dict
        event = {
            "event_type": "configuration",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "config": config_dict,
        }
        self._append_jsonl(event)

        method_key = str(config_dict.get("method", "cso")).lower()
        method_label = METHOD_DISPLAY_NAMES.get(method_key, method_key.upper())
        year = config_dict.get("year", "1940")
        objective_key = str(config_dict.get("objective", "best_overall")).lower()
        objective_label = OBJECTIVE_DISPLAY_NAMES.get(objective_key, objective_key)

        self.logger.info("=" * 88)
        self.logger.info("STARTING HOI4 v1.19.4.2 DIVISION OPTIMIZATION")
        self.logger.info("  Method            : %s", method_label)
        self.logger.info("  Target Year       : %s", year)
        self.logger.info("  Objective         : %s", objective_label)
        self.logger.info(
            "  Population / Iter : pop=%s, iterations=%s, battles_per_eval=%s",
            config_dict.get("population_size", 24),
            config_dict.get("iterations", 30),
            config_dict.get("battles_per_evaluation", 3),
        )
        self.logger.info(
            "  Width Constraints : target=%s, min=%s, max=%s | max_ic=%s",
            config_dict.get("target_combat_width", "Any"),
            config_dict.get("min_combat_width", 10.0),
            config_dict.get("max_combat_width", 42.0),
            config_dict.get("max_ic_cost", "Unbounded"),
        )
        # Log active algorithm-specific parameters and any custom `method_params`
        prefix_map = {
            "cso": "cso_",
            "cat_swarm": "cso_",
            "ga": "ga_",
            "genetic": "ga_",
            "pso": "pso_",
            "particle_swarm": "pso_",
            "sa": "sa_",
            "simulated_annealing": "sa_",
            "de": "de_",
            "differential_evolution": "de_",
        }
        algo_prefix = prefix_map.get(method_key, f"{method_key}_")
        algo_params = {
            k: v for k, v in config_dict.items()
            if k.startswith(algo_prefix)
        }
        custom_method_params = config_dict.get("method_params") or {}
        if isinstance(custom_method_params, dict):
            algo_params.update(custom_method_params)
        if algo_params:
            params_str = ", ".join(f"{k}={v}" for k, v in sorted(algo_params.items()))
            self.logger.info("  Method Parameters : %s", params_str)
        self.logger.info("=" * 88)
        return config_dict

    def log_iteration(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        """
        Record an optimization iteration snapshot to JSONL and log a formatted
        iteration summary to the logger.

        Parameters
        ----------
        snapshot : Dict[str, Any]
            Telemetry dictionary emitted by `BaseDivisionOptimizer` after an iteration.

        Returns
        -------
        Dict[str, Any]
            Normalized snapshot dictionary.
        """
        raw_snapshot = serialize_for_telemetry(snapshot)
        if not isinstance(raw_snapshot, dict):
            raw_snapshot = {"raw": raw_snapshot}

        iteration = int(raw_snapshot.get("iteration", len(self.snapshots) + 1))
        total_iterations = int(
            raw_snapshot.get("total_iterations")
            or self.config_record.get("iterations")
            or max(iteration, 1)
        )
        method_key = str(
            raw_snapshot.get("method")
            or self.config_record.get("method")
            or "cso"
        ).lower()
        year = str(raw_snapshot.get("year") or self.config_record.get("year") or "1940")
        objective = str(
            raw_snapshot.get("objective")
            or self.config_record.get("objective")
            or "best_overall"
        )
        elapsed = float(
            raw_snapshot.get("elapsed_seconds")
            if raw_snapshot.get("elapsed_seconds") is not None
            else (time.time() - self._start_time)
        )

        leader_summary = extract_division_summary(raw_snapshot.get("leader"))
        if not leader_summary.get("method"):
            leader_summary["method"] = method_key.upper()

        # Extract population average fitness if available (supports both `mean_fitness` and `avg_fitness`)
        avg_fitness = float(
            raw_snapshot.get("mean_fitness")
            if raw_snapshot.get("mean_fitness") is not None
            else (raw_snapshot.get("avg_fitness", 0.0) or 0.0)
        )
        fitness_history = raw_snapshot.get("fitness_history", [])
        if avg_fitness == 0.0 and isinstance(fitness_history, list) and fitness_history:
            last_entry = fitness_history[-1]
            if isinstance(last_entry, dict):
                avg_fitness = float(last_entry.get("avg_fitness", last_entry.get("mean_fitness", 0.0)) or 0.0)

        mode_counts = raw_snapshot.get("mode_counts") or {}
        algorithm_metadata = raw_snapshot.get("algorithm_metadata") or {}
        custom_metrics = raw_snapshot.get("custom_metrics") or {}
        algorithm_name = str(
            raw_snapshot.get("algorithm_name")
            or METHOD_DISPLAY_NAMES.get(method_key, method_key.upper())
        )

        normalized_record: Dict[str, Any] = {
            "event_type": "iteration",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "iteration": iteration,
            "total_iterations": total_iterations,
            "method": method_key,
            "algorithm_name": algorithm_name,
            "year": year,
            "objective": objective,
            "elapsed_seconds": round(elapsed, 3),
            "best_fitness": leader_summary["total_fitness"],
            "avg_fitness": round(avg_fitness, 4),
            "win_rate": leader_summary["win_rate"],
            "attacker_win_rate": leader_summary["attacker_win_rate"],
            "defender_win_rate": leader_summary["defender_win_rate"],
            "ic_cost": leader_summary["stats"]["ic_cost"],
            "combat_width": leader_summary["stats"]["combat_width"],
            "leader": leader_summary,
            "mode_counts": mode_counts,
            "algorithm_metadata": algorithm_metadata,
            "custom_metrics": custom_metrics,
        }

        with self._lock:
            self.snapshots.append(normalized_record)

        self._append_jsonl(normalized_record)

        # Build concise console/file log line
        mode_suffix = ""
        if isinstance(mode_counts, dict) and mode_counts:
            mode_parts = [f"{k}={v}" for k, v in mode_counts.items()]
            mode_suffix = f" | Modes({', '.join(mode_parts)})"

        self.logger.info(
            "[%s | %s | %s] Iter %d/%d (%.1fs) | BestFit: %.4f (Avg: %.4f) | "
            "Win: %.1f%% (Att: %.1f%%, Def: %.1f%%) | IC: %.0f | Width: %.0f | "
            "Leader: %s%s",
            method_key.upper(),
            year,
            objective,
            iteration,
            total_iterations,
            elapsed,
            leader_summary["total_fitness"],
            avg_fitness,
            leader_summary["win_rate"] * 100.0,
            leader_summary["attacker_win_rate"] * 100.0,
            leader_summary["defender_win_rate"] * 100.0,
            leader_summary["stats"]["ic_cost"],
            leader_summary["stats"]["combat_width"],
            leader_summary["composition_summary"],
            mode_suffix,
        )
        return normalized_record

    # Alias `on_step` and `__call__` so `TrainingTelemetryLogger` can be used directly as callback
    on_step = log_iteration
    __call__ = log_iteration

    def log_completion(
        self,
        final_result: Any = None,
        elapsed_seconds: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Log a comprehensive final summary banner upon training completion and write
        a completion event to the JSONL telemetry file.

        Parameters
        ----------
        final_result : Any, optional
            Final `CandidateSolution`, `Division`, or result dictionary.
        elapsed_seconds : Optional[float], optional
            Total wall-clock training duration in seconds.

        Returns
        -------
        Dict[str, Any]
            Completion summary record.
        """
        elapsed = (
            float(elapsed_seconds)
            if elapsed_seconds is not None
            else (time.time() - self._start_time)
        )

        # Determine leader from final_result or last recorded snapshot
        leader_candidate = None
        if isinstance(final_result, dict) and "leader" in final_result:
            leader_candidate = final_result["leader"]
        elif hasattr(final_result, "leader"):
            leader_candidate = getattr(final_result, "leader")
        elif hasattr(final_result, "best_candidate"):
            leader_candidate = getattr(final_result, "best_candidate")
        elif final_result is not None:
            leader_candidate = final_result
        elif self.snapshots:
            leader_candidate = self.snapshots[-1].get("leader")

        leader_summary = extract_division_summary(leader_candidate)
        stats = leader_summary["stats"]

        completion_record = {
            "event_type": "completion",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "elapsed_seconds": round(elapsed, 3),
            "total_iterations_logged": len(self.snapshots),
            "leader": leader_summary,
        }
        self._append_jsonl(completion_record)

        self.logger.info("=" * 88)
        self.logger.info("OPTIMIZATION COMPLETED IN %.2f SECONDS", elapsed)
        self.logger.info("  #1 Leader Division : %s", leader_summary["name"])
        self.logger.info("  Composition        : %s", leader_summary["composition_summary"])
        self.logger.info(
            "  Combat Performance : Fitness=%.4f | Overall Win=%.1f%% (Attacker=%.1f%%, Defender=%.1f%%)",
            leader_summary["total_fitness"],
            leader_summary["win_rate"] * 100.0,
            leader_summary["attacker_win_rate"] * 100.0,
            leader_summary["defender_win_rate"] * 100.0,
        )
        self.logger.info(
            "  Core Statistics    : Width=%.0f | IC=%.1f | Manpower=%.0f | ORG=%.1f | HP=%.1f | Supply=%.2f",
            stats["combat_width"],
            stats["ic_cost"],
            stats["manpower"],
            stats["organization"],
            stats["max_hp"],
            stats["supply_use"],
        )
        self.logger.info(
            "  Firepower & Armor  : SA=%.1f | HA=%.1f | Def=%.1f | Brk=%.1f | Armor=%.1f | Piercing=%.1f | Hardness=%.1f%%",
            stats["soft_attack"],
            stats["hard_attack"],
            stats["defense"],
            stats["breakthrough"],
            stats["armor"],
            stats["piercing"],
            stats["hardness"] * 100.0,
        )
        self.logger.info("  Telemetry JSONL    : %s", self.telemetry_file_path)
        self.logger.info("=" * 88)
        return completion_record

    def export_json_report(
        self,
        result_or_snapshot: Any = None,
        output_path: Optional[str] = None,
    ) -> str:
        """
        Export a complete, formatted JSON report of the optimization run.

        Parameters
        ----------
        result_or_snapshot : Any, optional
            Final optimizer state or snapshot dictionary. Defaults to latest recorded state.
        output_path : Optional[str], optional
            Destination path for the JSON file. If `None`, writes to
            `logs/report_<timestamp>.json`.

        Returns
        -------
        str
            Absolute path to the written JSON report file.
        """
        resolved_path = os.path.abspath(
            output_path or os.path.join(self.log_dir, f"report_{self.timestamp_str}.json")
        )
        Path(os.path.dirname(resolved_path)).mkdir(parents=True, exist_ok=True)

        report_payload = self._build_consolidated_report_dict(result_or_snapshot)
        with open(resolved_path, "w", encoding="utf-8") as fh:
            json.dump(report_payload, fh, indent=2, ensure_ascii=False)

        self.logger.info("Exported JSON optimization report to: %s", resolved_path)
        return resolved_path

    def export_markdown_report(
        self,
        result_or_snapshot: Any = None,
        output_path: Optional[str] = None,
    ) -> str:
        """
        Export a comprehensive GitHub-Flavored Markdown report of the optimization run,
        including the 5x5 Regiment + Divisional Support + Regimental Support grid,
        full stat breakdown, terrain win rates, convergence history, and Hall of Fame.

        Parameters
        ----------
        result_or_snapshot : Any, optional
            Final optimizer state or snapshot dictionary.
        output_path : Optional[str], optional
            Destination path for the `.md` file. If `None`, writes to
            `logs/report_<timestamp>.md`.

        Returns
        -------
        str
            Absolute path to the written Markdown report file.
        """
        resolved_path = os.path.abspath(
            output_path or os.path.join(self.log_dir, f"report_{self.timestamp_str}.md")
        )
        Path(os.path.dirname(resolved_path)).mkdir(parents=True, exist_ok=True)

        report_data = self._build_consolidated_report_dict(result_or_snapshot)
        leader = report_data["leader"]
        stats = leader["stats"]
        grid = leader["grid"]
        method_key = str(report_data.get("method", "cso")).lower()
        method_display = METHOD_DISPLAY_NAMES.get(method_key, method_key.upper())
        obj_key = str(report_data.get("objective", "best_overall")).lower()
        obj_display = OBJECTIVE_DISPLAY_NAMES.get(obj_key, obj_key)

        lines: List[str] = [
            "# HOI4 v1.19.4.2 Division Optimization Report",
            "",
            "## 1. Training Configuration & Run Metadata",
            "",
            "| Parameter | Value |",
            "| :--- | :--- |",
            f"| **Optimization Algorithm** | {method_display} |",
            f"| **Target Tech Year** | `{report_data.get('year', '1940')}` |",
            f"| **Objective Function** | {obj_display} |",
            f"| **Iterations Completed** | `{report_data.get('iterations_completed', len(self.snapshots))}` |",
            f"| **Elapsed Time** | `{report_data.get('elapsed_seconds', 0.0):.2f}s` |",
            f"| **Telemetry Stream** | `{self.telemetry_file_path}` |",
            "",
            "---",
            "",
            f"## 2. #1 Leader Division: `{leader['name']}`",
            "",
            f"- **Composition Summary**: `{leader['composition_summary']}`",
            f"- **Total Fitness Score**: `{leader['total_fitness']:.4f}`",
            f"- **Overall Win Rate**: `{leader['win_rate'] * 100.0:.1f}%` "
            f"(**Attacker**: `{leader['attacker_win_rate'] * 100.0:.1f}%`, "
            f"**Defender**: `{leader['defender_win_rate'] * 100.0:.1f}%`)",
            f"- **Bang-for-Buck (IC Efficiency)**: `{leader['bang_for_buck_score']:.4f}`",
            "",
            "### 2.1 HOI4 v1.19.4.2 Division Designer Grid (5x5 Regiments + Support)",
            "",
        ]

        # Build the 5x5 Regiment + Support Markdown table
        col_headers = []
        for c_idx in range(5):
            grp = grid["column_groups"][c_idx]
            grp_tag = f" ({grp})" if grp else ""
            col_headers.append(f"Regiment {c_idx + 1}{grp_tag}")

        lines.append(
            f"| Row | Divisional Support | {' | '.join(col_headers)} |"
        )
        lines.append("| :---: | :--- | :--- | :--- | :--- | :--- | :--- |")

        for row_idx in range(5):
            sup_cell = (
                grid["support"][row_idx]
                if row_idx < len(grid["support"]) and grid["support"][row_idx]
                else "-"
            )
            reg_cells: List[str] = []
            for col_idx in range(5):
                col_list = grid["regiments"][col_idx] if col_idx < len(grid["regiments"]) else []
                if row_idx < len(col_list) and col_list[row_idx]:
                    unit_entry = col_list[row_idx]
                    u_name = unit_entry["name"] if isinstance(unit_entry, dict) else str(unit_entry)
                    reg_cells.append(u_name)
                else:
                    reg_cells.append("-")
            lines.append(
                f"| **Slot {row_idx + 1}** | {sup_cell} | {' | '.join(reg_cells)} |"
            )

        # Regimental support row (new in HOI4 v1.19)
        reg_sup_cells = [
            grid["regimental_support"][c_idx] or "-"
            for c_idx in range(5)
        ]
        lines.append(
            f"| **Regimental Support (v1.19)** | *(Requires >=3 Bats)* | {' | '.join(reg_sup_cells)} |"
        )
        lines.append("")

        # Complete Division Statistics Table
        lines.extend([
            "### 2.2 Complete Division Combat Statistics",
            "",
            "| Statistic | Value | Statistic | Value |",
            "| :--- | ---: | :--- | ---: |",
            f"| **Soft Attack** | `{stats['soft_attack']:.2f}` | **IC Cost** | `{stats['ic_cost']:.1f}` |",
            f"| **Hard Attack** | `{stats['hard_attack']:.2f}` | **Combat Width** | `{stats['combat_width']:.1f}` |",
            f"| **Defense** | `{stats['defense']:.2f}` | **Manpower** | `{stats['manpower']:.0f}` |",
            f"| **Breakthrough** | `{stats['breakthrough']:.2f}` | **Supply Use** | `{stats['supply_use']:.2f}` |",
            f"| **Organization** | `{stats['organization']:.2f}` | **Max HP** | `{stats['max_hp']:.2f}` |",
            f"| **Armor** | `{stats['armor']:.2f}` | **Piercing** | `{stats['piercing']:.2f}` |",
            f"| **Hardness** | `{stats['hardness'] * 100.0:.1f}%` | **Recovery Rate** | `{stats['recovery_rate']:.2f}` |",
            f"| **Entrenchment** | `{stats['entrenchment']:.2f}` | **Initiative** | `{stats['initiative']:.2f}` |",
            f"| **Recon** | `{stats['recon']:.2f}` | **Air Attack** | `{stats['air_attack']:.2f}` |",
            "",
            "---",
            "",
            "## 3. Multi-Terrain Win-Rate Breakdown",
            "",
            "| Terrain | Win Rate (%) | Visual Bar |",
            "| :--- | ---: | :--- |",
        ])

        for t_name, wr_val in leader["terrain_win_rates"].items():
            pct = max(0.0, min(100.0, float(wr_val) * 100.0))
            filled_blocks = int(round(pct / 5.0))
            bar_str = "█" * filled_blocks + "░" * (20 - filled_blocks)
            lines.append(f"| **{t_name}** | `{pct:.1f}%` | `{bar_str}` |")

        lines.extend([
            "",
            "---",
            "",
            "## 4. Hall of Fame — Top Candidate Divisions",
            "",
            "| Rank | Division Name | Fitness | Win Rate | IC Cost | Width | ORG | Soft/Hard Atk | Composition |",
            "| :---: | :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |",
        ])

        top_candidates = report_data.get("top_candidates", [])
        if not top_candidates:
            top_candidates = [leader]

        for rank_idx, cand in enumerate(top_candidates[:10], start=1):
            c_stats = cand.get("stats", {})
            lines.append(
                f"| **#{rank_idx}** | {cand.get('name', 'Candidate')} | "
                f"`{cand.get('total_fitness', 0.0):.4f}` | "
                f"`{cand.get('win_rate', 0.0) * 100.0:.1f}%` | "
                f"`{c_stats.get('ic_cost', 0.0):.0f}` | "
                f"`{c_stats.get('combat_width', 0.0):.0f}` | "
                f"`{c_stats.get('organization', 0.0):.1f}` | "
                f"`{c_stats.get('soft_attack', 0.0):.0f}/{c_stats.get('hard_attack', 0.0):.0f}` | "
                f"{cand.get('composition_summary', '')} |"
            )

        lines.append("")
        markdown_content = "\n".join(lines)
        with open(resolved_path, "w", encoding="utf-8") as fh:
            fh.write(markdown_content)

        self.logger.info("Exported Markdown optimization report to: %s", resolved_path)
        return resolved_path

    def export_comparison_report(
        self,
        comparison_results: Dict[str, Any],
        output_path: Optional[str] = None,
    ) -> Tuple[str, str]:
        """
        Export both Markdown and JSON reports comparing multiple optimization algorithms
        head-to-head on the same year and objective.

        Parameters
        ----------
        comparison_results : Dict[str, Any]
            Dictionary mapping method keys (`"cso"`, `"ga"`, `"pso"`, etc.) to their
            final optimization results or snapshots.
        output_path : Optional[str], optional
            Base output path (either `.md` or `.json`). Both `.md` and `.json` files
            will be created.

        Returns
        -------
        Tuple[str, str]
            Tuple of `(markdown_report_path, json_report_path)`.
        """
        base_path = output_path or os.path.join(self.log_dir, f"comparison_{self.timestamp_str}")
        if base_path.endswith(".md") or base_path.endswith(".json"):
            base_stem = os.path.splitext(os.path.abspath(base_path))[0]
        else:
            base_stem = os.path.abspath(base_path)

        md_path = base_stem + ".md"
        json_path = base_stem + ".json"
        Path(os.path.dirname(md_path)).mkdir(parents=True, exist_ok=True)

        serialized_results = serialize_for_telemetry(comparison_results)
        with open(json_path, "w", encoding="utf-8") as j_fh:
            json.dump(serialized_results, j_fh, indent=2, ensure_ascii=False)

        # Build Markdown comparison table
        md_lines = [
            "# Multi-Algorithm Head-to-Head Comparison Report",
            "",
            "| Rank | Algorithm | Best Fitness | Win Rate (%) | Att / Def Win (%) | IC Cost | Width | Winning Composition |",
            "| :---: | :--- | ---: | ---: | ---: | ---: | ---: | :--- |",
        ]

        entries: List[Tuple[str, Dict[str, Any], float]] = []
        if isinstance(serialized_results, dict):
            runs_dict = serialized_results.get("methods", serialized_results)
            if isinstance(runs_dict, dict):
                for m_key, m_val in runs_dict.items():
                    if not isinstance(m_val, dict):
                        continue
                    leader_obj = m_val.get("leader", m_val.get("best_candidate", m_val))
                    summary = extract_division_summary(leader_obj)
                    elapsed_val = float(m_val.get("elapsed_seconds", 0.0) or 0.0)
                    entries.append((str(m_key), summary, elapsed_val))

        entries.sort(key=lambda item: item[1]["total_fitness"], reverse=True)

        for rank_idx, (m_key, summary, elapsed_val) in enumerate(entries, start=1):
            m_label = METHOD_DISPLAY_NAMES.get(m_key.lower(), m_key.upper())
            st = summary["stats"]
            md_lines.append(
                f"| **#{rank_idx}** | {m_label} (`{elapsed_val:.1f}s`) | "
                f"`{summary['total_fitness']:.4f}` | "
                f"`{summary['win_rate'] * 100.0:.1f}%` | "
                f"`{summary['attacker_win_rate'] * 100.0:.1f}% / {summary['defender_win_rate'] * 100.0:.1f}%` | "
                f"`{st['ic_cost']:.0f}` | `{st['combat_width']:.0f}` | "
                f"{summary['composition_summary']} |"
            )

        md_lines.append("")
        with open(md_path, "w", encoding="utf-8") as m_fh:
            m_fh.write("\n".join(md_lines))

        self.logger.info("Exported comparison reports: %s and %s", md_path, json_path)
        return md_path, json_path

    def _build_consolidated_report_dict(self, result_or_snapshot: Any = None) -> Dict[str, Any]:
        """Combine configuration, snapshots, and final result into a unified report dict."""
        raw = serialize_for_telemetry(result_or_snapshot) if result_or_snapshot is not None else {}
        if not isinstance(raw, dict):
            raw = {}

        last_snap = self.snapshots[-1] if self.snapshots else {}
        leader_raw = (
            raw.get("leader")
            or raw.get("best_candidate")
            or (raw if "stats" in raw or "total_fitness" in raw else None)
            or last_snap.get("leader")
        )
        leader_summary = extract_division_summary(leader_raw)

        raw_top = raw.get("top_candidates") or raw.get("hall_of_fame") or []
        top_candidates = [extract_division_summary(c) for c in raw_top] if isinstance(raw_top, list) else []
        if not top_candidates and leader_summary["total_fitness"] > 0:
            top_candidates = [leader_summary]

        history = raw.get("fitness_history") or [
            {
                "iteration": s["iteration"],
                "best_fitness": s["best_fitness"],
                "avg_fitness": s["avg_fitness"],
                "win_rate": s["win_rate"],
            }
            for s in self.snapshots
        ]

        return {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "method": raw.get("method") or last_snap.get("method") or self.config_record.get("method", "cso"),
            "year": raw.get("year") or last_snap.get("year") or self.config_record.get("year", "1940"),
            "objective": raw.get("objective") or last_snap.get("objective") or self.config_record.get("objective", "best_overall"),
            "iterations_completed": raw.get("iteration") or last_snap.get("iteration") or len(self.snapshots),
            "elapsed_seconds": round(
                float(raw.get("elapsed_seconds") or last_snap.get("elapsed_seconds") or (time.time() - self._start_time)),
                3,
            ),
            "config": self.config_record,
            "leader": leader_summary,
            "top_candidates": top_candidates,
            "fitness_history": history,
            "telemetry_file_path": self.telemetry_file_path,
        }

"""
optimizer/base.py
=================
Algorithm-Agnostic Optimization Architecture & Valid HOI4 Genome Encoding.

This module defines the core abstractions for optimizing Hearts of Iron IV
(v1.19.4.2) division templates across arbitrary metaheuristic algorithms:
1. ``OptimizationConfig``: Complete hyperparameter and constraint specification,
   including Cat Swarm Optimization (CSO) parameters from Aram M. Ahmed et al.
   (2020), PMC7204373, as well as Genetic Algorithm (GA), Particle Swarm
   Optimization (PSO), Simulated Annealing (SA), and Random Search settings.
2. ``UnitPool``: Era-aware unit database adapter with full HOI4 v1.19.4.2 rules
   support (regiment column brigade groups, divisional support mutual exclusion,
   regimental fire-support unlocking at >= 3 battalions per column, special
   projects, and country-locked filtering).
3. ``DivisionGenome``: Dual continuous-discrete representation of a 5-column
   HOI4 division template that maps deterministically between a continuous
   latent vector x in [0, 1]^D (for velocity-based metaheuristics like CSO
   Tracing Mode and PSO) and discrete regiment/support slots (for CSO Seeking
   Mode, GA, and SA), always decoding to a 100% legal ``Division`` instance.
4. ``FitnessMetrics`` & ``CandidateSolution``: Rich combat evaluation records
   with full JSON-ready serialization for the live web dashboard and run logger.
5. ``BaseDivisionOptimizer``: Abstract base class providing population management,
   top-K elite archiving, convergence tracking, and an algorithm-agnostic
   ``on_step_callback`` telemetry hook.
"""

from __future__ import annotations

import abc
import copy
import hashlib
import math
import random
import statistics
import time
from dataclasses import dataclass, field, asdict
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from battalion import Battalion
from division import Division
import doctrines
from stats import BaseStatistics
from support_company import SupportCompany
import tank_designer
from terrain import ALL_TERRAINS
import unit_database


# =============================================================================
# Constants & Authoritative HOI4 v1.19.4.2 Rule Tables (Fallback Metadata)
# =============================================================================

BATTALION_GROUPS: Tuple[str, ...] = (
    "infantry",
    "combat_support",
    "mobile",
    "mobile_combat_support",
    "armor",
    "armor_combat_support",
)

# Authoritative mapping of battalion names to their HOI4 brigade column group
# Used when a Battalion object does not explicitly carry a `.group` attribute.
FALLBACK_BATTALION_GROUP_MAP: Dict[str, str] = {
    # Infantry Brigade Group (Foot infantry, special forces, towed line support)
    "Infantry": "infantry",
    "Irregular Infantry": "infantry",
    "Militia": "infantry",
    "Penal Battalion": "infantry",
    "Bicycle": "infantry",
    "Bicycle Battalion": "infantry",
    "Mountain": "infantry",
    "Mountaineers": "infantry",
    "Marines": "infantry",
    "Marine Commandos": "infantry",
    "Paratrooper": "infantry",
    "Paratroopers": "infantry",
    "Artillery": "infantry",
    "Anti-Air": "infantry",
    "Anti-Tank": "infantry",
    "Rocket Artillery": "infantry",
    "Super-Heavy Artillery": "infantry",
    "Assault Battalion": "infantry",
    "Sturmtruppe Battalion": "infantry",
    # Mobile Brigade Group (Mounted, motorized, mechanized, motorized line support)
    "Cavalry": "mobile",
    "Camelry": "mobile",
    "Elephantry": "mobile",
    "Motorized Infantry": "mobile",
    "Mechanized Infantry": "mobile",
    "Amtrac Battalion": "mobile",
    "Armored Car": "mobile",
    "Motorized Artillery": "mobile",
    "Motorized Anti-Air": "mobile",
    "Motorized Anti-Tank": "mobile",
    "Mot. R. Artillery": "mobile",
    "Truck-drawn Rocket Artillery": "mobile",
    # Armor Brigade Group (Tanks, SPGs, TDs, SPAAs, Amphibious Tanks)
    "Light Tank": "armor",
    "Medium Tank": "armor",
    "Heavy Tank": "armor",
    "Modern Tank": "armor",
    "Super Heavy Tank": "armor",
    "Amphibious Tank Battalion": "armor",
    "Light Amphibious Tank Battalion": "armor",
    "Medium Amphibious Tank Battalion": "armor",
    "Heavy Amphibious Tank Battalion": "armor",
    "Light SP Artillery": "armor",
    "Medium SP Artillery": "armor",
    "Heavy SP Artillery": "armor",
    "Modern SP Artillery": "armor",
    "Super Heavy SP Artillery": "armor",
    "Light Tank Destroyer": "armor",
    "Medium Tank Destroyer": "armor",
    "Heavy Tank Destroyer": "armor",
    "Modern Tank Destroyer": "armor",
    "Super Heavy Tank Destroyer": "armor",
    "Light SP Anti-Air": "armor",
    "Medium SP Anti-Air": "armor",
    "Heavy SP Anti-Air": "armor",
    "Modern SP Anti-Air": "armor",
    "Super Heavy SP Anti-Air": "armor",
}

# Authoritative Support Company Mutual Exclusion Families (`same_support_type`)
FALLBACK_SUPPORT_TYPE_MAP: Dict[str, str] = {
    "Engineer Company": "engineer",
    "Pioneers": "engineer",
    "Jungle Pioneers": "engineer",
    "Assault Engineer Company": "engineer",
    "Armored Engineer Company": "engineer",
    "Amphibious Tank Engineer Company": "engineer",
    "Light Tank Engineer Company": "engineer",
    "Medium Tank Engineer Company": "engineer",
    "Heavy Tank Engineer Company": "engineer",
    "Super Heavy Tank Engineer Company": "engineer",
    "Modern Tank Engineer Company": "engineer",
    "Recon Company": "recon",
    "Cavalry Recon Company": "recon",
    "Motorized Recon Company": "recon",
    "Armored Car Recon Company": "recon",
    "Armoured Car Recon Company": "recon",
    "Light Tank Recon Company": "recon",
    "Medium Tank Recon Company": "recon",
    "Heavy Tank Recon Company": "recon",
    "Super Heavy Tank Recon Company": "recon",
    "Modern Tank Recon Company": "recon",
    "Camel Recon Company": "recon",
    "Bicycle Recon Company": "recon",
    "Motorcycle Recon Company": "recon",
    "Long Range Patrol Company": "recon",
    "Rangers": "recon",
    "Airborne Light armour": "recon",
    "Helicopter Recon": "recon",
    "Military Police": "military_police",
    "Motorized Military Police": "military_police",
    "Logistics Company": "logistics",
    "Winter Logistics Company": "logistics",
    "Airborne Logistics Company": "logistics",
    "Helicopter Transports": "logistics",
    "Maintenance Company": "maintenance",
    "Armored Maintenance Company": "maintenance",
    "Field Hospital": "field_hospital",
    "Helicopter Med-Evac": "field_hospital",
    "Signal Company": "signal",
    "Armored Signal Company": "signal",
    "Light Flame Tank Company": "flame_tank",
    "Medium Flame Tank Company": "flame_tank",
    "Heavy Flame Tank Company": "flame_tank",
    "Support Artillery": "support_artillery",
    "Support Anti-Air": "support_aa",
    "Support Anti-Tank": "support_at",
    "Support Rocket Artillery": "support_rocket",
    "Super-Heavy Artillery": "super_heavy_arty",
    "Self-Propelled Super-Heavy Artillery": "super_heavy_arty",
    "Helicopter Brigade": "helicopter_brigade",
    "Land Cruiser": "land_cruiser",
}

# Special project units and country-locked units for filtering when requested
SPECIAL_PROJECT_UNITS = {
    "Land Cruiser",
    "Self-Propelled Super-Heavy Artillery",
    "Super-Heavy Artillery",
    "Super Heavy Tank",
    "Super Heavy SP Artillery",
    "Super Heavy Tank Destroyer",
    "Super Heavy SP Anti-Air",
    "Light Flame Tank Company",
    "Medium Flame Tank Company",
    "Heavy Flame Tank Company",
    "Helicopter Brigade",
    "Helicopter Med-Evac",
    "Helicopter Recon",
    "Helicopter Transports",
    "Armored Engineer Company",
    "Assault Engineer Company",
    "Armored Maintenance Company",
    "Armored Signal Company",
}

COUNTRY_LOCKED_UNITS = {
    "Elephantry",
    "Camelry",
    "Bicycle",
    "Bicycle Battalion",
    "Penal Battalion",
    "Irregular Infantry",
    "Militia",
    "Sturmtruppe Battalion",
    "Assault Battalion",
    "Marine Commandos",
    "Jungle Pioneers",
    "Pioneers",
    "Winter Logistics Company",
    "Long Range Patrol Company",
    "Rangers",
    "Motorized Military Police",
    "Airborne Light armour",
}

# Historical minimum unlock years for strict era filtering
UNIT_MIN_YEAR_MAP: Dict[str, int] = {
    "Infantry": 1934,
    "Cavalry": 1934,
    "Artillery": 1934,
    "Anti-Air": 1934,
    "Anti-Tank": 1936,
    "Motorized Infantry": 1936,
    "Mountain": 1934,
    "Mountaineers": 1934,
    "Marines": 1936,
    "Paratrooper": 1936,
    "Paratroopers": 1936,
    "Light Tank": 1934,
    "Light SP Artillery": 1936,
    "Light Tank Destroyer": 1936,
    "Light SP Anti-Air": 1936,
    "Medium Tank": 1939,
    "Medium SP Artillery": 1939,
    "Medium Tank Destroyer": 1939,
    "Medium SP Anti-Air": 1939,
    "Heavy Tank": 1936,
    "Heavy SP Artillery": 1939,
    "Heavy Tank Destroyer": 1939,
    "Heavy SP Anti-Air": 1939,
    "Mechanized Infantry": 1940,
    "Rocket Artillery": 1940,
    "Mot. R. Artillery": 1940,
    "Truck-drawn Rocket Artillery": 1940,
    "Motorized Artillery": 1936,
    "Motorized Anti-Air": 1936,
    "Motorized Anti-Tank": 1936,
    "Armored Car": 1936,
    "Amphibious Tank Battalion": 1940,
    "Amtrac Battalion": 1940,
    "Modern Tank": 1945,
    "Modern SP Artillery": 1945,
    "Modern Tank Destroyer": 1945,
    "Modern SP Anti-Air": 1945,
    "Super Heavy Tank": 1940,
    "Super Heavy SP Artillery": 1940,
    "Super Heavy Tank Destroyer": 1940,
    "Super Heavy SP Anti-Air": 1940,
    "Land Cruiser": 1945,
    "Helicopter Brigade": 1945,
    "Helicopter Med-Evac": 1945,
    "Helicopter Recon": 1945,
    "Helicopter Transports": 1945,
    "Support Rocket Artillery": 1940,
    "Light Flame Tank Company": 1939,
    "Medium Flame Tank Company": 1939,
    "Heavy Flame Tank Company": 1939,
    "Field Hospital": 1936,
    "Logistics Company": 1936,
    "Maintenance Company": 1936,
    "Signal Company": 1936,
    "Military Police": 1936,
}

# Genome continuous vector layout constants:
# 5 columns * 7 dims (group, count, 5 slot choices) = 35
# + 5 divisional support dims = 40
# + 5 regimental support dims = 45
GENOME_VECTOR_DIM: int = 45


# =============================================================================
# Configuration Dataclass
# =============================================================================

@dataclass
class OptimizationConfig:
    """
    Complete configuration for an algorithm-agnostic division optimization run.

    Includes general problem constraints (year, terrains, combat width, IC/manpower
    caps, unit unlock rules) as well as algorithm-specific hyperparameters for:
    - Cat Swarm Optimization (CSO, following Aram M. Ahmed et al. 2020, PMC7204373)
    - Genetic Algorithm (GA)
    - Particle Swarm Optimization (PSO)
    - Simulated Annealing (SA)
    """

    # Core problem settings
    method: str = "cso"  # "cso", "ga", "pso", "de", "gwo", "sa", "random"
    year: str = "1945"   # "1934", "1936", "1939", "1940", "1945" (defaults to 1945 per user requirement)
    objective: str = "best_overall"  # "best_overall", "bang_for_buck", "offensive_breakthrough", "defensive_wall", "terrain_specialist"
    terrains: List[str] = field(default_factory=lambda: list(ALL_TERRAINS.keys()))
    terrain_weights: Dict[str, float] = field(default_factory=dict)

    # HOI4 v1.19.4.2 Land Doctrine & NSB Tank Designer settings
    doctrine: str = "none"  # "none", "mobile_warfare", "superior_firepower", "grand_battleplan", "mass_assault", sub-doctrine, or "<grand>:<inf>,<sup_art>,<armor>,<ops>"
    doctrine_mastery: Optional[float] = None  # None uses year-based default mastery (or 1.0 when explicit doctrine is chosen)
    tank_design_mode: str = "historical"  # "historical", "nsb_meta_soft_attack", "nsb_meta_hard_attack", "nsb_meta_armor_brick", "nsb_budget", "nsb_auto_optimize"

    # Search budget
    population_size: int = 24
    iterations: int = 30
    battles_per_evaluation: int = 3

    # Division structural constraints
    target_combat_width: Optional[float] = None
    min_combat_width: float = 10.0
    max_combat_width: float = 42.0
    max_ic_cost: Optional[float] = None
    max_manpower: Optional[float] = None

    # HOI4 v1.19.4.2 unit pool filters
    allow_special_projects: bool = True
    allow_country_locked: bool = False
    allow_regimental_support: bool = True
    strict_year_unlock: bool = True
    random_seed: Optional[int] = 42

    # Cat Swarm Optimization (CSO) Hyperparameters (PMC7204373)
    cso_smp: int = 5          # Seeking Memory Pool: candidate copies generated per cat in Seeking Mode
    cso_srd: float = 0.25     # Seeking Range of the Selected Dimension: mutation step size in [0, 1]
    cso_cdc: float = 0.30     # Counts of Dimension to Change: fraction of dimensions mutated in Seeking Mode
    cso_spc: bool = True      # Self-Position Considering: include current cat position in SMP
    cso_mr: float = 0.25      # Mixture Ratio: fraction of cats assigned to Tracing Mode vs Seeking Mode
    cso_c1: float = 1.8       # Tracing Mode acceleration constant toward X_best
    cso_inertia_w: float = 0.7  # Tracing Mode velocity inertia weight
    cso_vmax: float = 0.35    # Maximum velocity magnitude per dimension in Tracing Mode

    # Genetic Algorithm (GA) Hyperparameters
    ga_mutation_rate: float = 0.18
    ga_crossover_rate: float = 0.80
    ga_elite_fraction: float = 0.15
    ga_tournament_size: int = 3

    # Particle Swarm Optimization (PSO) Hyperparameters
    pso_c1: float = 1.5       # Cognitive (personal best) acceleration coefficient
    pso_c2: float = 1.7       # Social (global best) acceleration coefficient
    pso_inertia_w: float = 0.72  # Velocity inertia weight
    pso_vmax: float = 0.35

    # Simulated Annealing (SA) Hyperparameters
    sa_initial_temp: float = 10.0
    sa_cooling_rate: float = 0.90

    # Differential Evolution (DE) Hyperparameters
    de_mutation_factor: float = 0.70
    de_crossover_prob: float = 0.85

    # Algorithm-agnostic parameter dictionary for arbitrary / custom optimizers
    method_params: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.method = self.method.lower().strip()
        if not self.terrains:
            self.terrains = list(ALL_TERRAINS.keys())
        # Normalize terrain names (e.g. "plains" -> "Plains")
        normalized_terrains = []
        for t in self.terrains:
            matched = next((k for k in ALL_TERRAINS if k.lower() == t.lower()), t)
            if matched in ALL_TERRAINS and matched not in normalized_terrains:
                normalized_terrains.append(matched)
        self.terrains = normalized_terrains or list(ALL_TERRAINS.keys())

        if self.target_combat_width is not None and self.target_combat_width > 0:
            self.min_combat_width = max(2.0, self.target_combat_width - 2.0)
            self.max_combat_width = min(50.0, self.target_combat_width + 2.0)

    def get_param(self, key: str, default: Any = None) -> Any:
        """
        Retrieves an algorithm hyperparameter in an agnostic manner:
        checks ``self.method_params[key]`` first, then ``getattr(self, key)``,
        falling back to ``default``.
        """
        if key in self.method_params:
            return self.method_params[key]
        return getattr(self, key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Returns a JSON-serializable dictionary of all configuration settings."""
        return asdict(self)


# =============================================================================
# Unit Pool Adapter (Bridges unit_database.py with HOI4 v1.19.4.2 Rules)
# =============================================================================

class UnitPool:
    """
    Manages the filtered pool of available Battalions, Divisional Support Companies,
    and Regimental Support Companies for a configured year and rule set.
    """

    def __init__(self, config: OptimizationConfig) -> None:
        self.config = config
        self.year = str(config.year)
        self.year_int = int(self.year) if self.year.isdigit() else 1940

        self.battalions_by_name: Dict[str, Battalion] = {}
        self.battalions_by_group: Dict[str, List[Battalion]] = {
            g: [] for g in BATTALION_GROUPS
        }
        self.divisional_supports: List[SupportCompany] = []
        self.divisional_supports_by_name: Dict[str, SupportCompany] = {}
        self.regimental_supports_by_group: Dict[str, List[SupportCompany]] = {
            g: [] for g in BATTALION_GROUPS
        }
        self.regimental_supports_by_name: Dict[str, SupportCompany] = {}

        self._load_pool()

    @staticmethod
    def get_battalion_group(unit: Any) -> str:
        """Determines the brigade column group of a battalion."""
        name = getattr(unit, "name", str(unit))
        grp = getattr(unit, "group", None) or getattr(unit, "battalion_group", None)
        if isinstance(grp, str):
            grp_clean = grp.lower().strip()
            # If unit has an explicit non-default group in BATTALION_GROUPS, honor it
            if grp_clean in BATTALION_GROUPS and (
                grp_clean != "infantry" or name not in FALLBACK_BATTALION_GROUP_MAP
            ):
                return grp_clean
        if name in FALLBACK_BATTALION_GROUP_MAP:
            return FALLBACK_BATTALION_GROUP_MAP[name]
        lower_name = name.lower()
        if any(k in lower_name for k in ("tank", "sp ", "armor", "armour", "amphibious")):
            return "armor"
        if any(k in lower_name for k in ("motor", "mechanized", "cavalry", "camel", "elephant", "truck", "amtrac", "armored car")):
            return "mobile"
        return "infantry"

    @staticmethod
    def get_support_types(company: Any) -> List[str]:
        """Returns all mutual-exclusion family tags ('same_support_type') of a support company."""
        st = getattr(company, "same_support_type", None) or getattr(company, "support_type", None)
        if isinstance(st, list) and st:
            return [str(x).strip().lower() for x in st if str(x).strip()]
        if isinstance(st, str) and st.strip():
            return [st.strip().lower()]
        name = getattr(company, "name", str(company))
        if name in FALLBACK_SUPPORT_TYPE_MAP:
            return [FALLBACK_SUPPORT_TYPE_MAP[name]]
        support_types = getattr(Division, "SUPPORT_TYPES", {})
        for family, members in support_types.items():
            if name in members:
                return [family.lower()]
        return [name.lower()]

    @staticmethod
    def get_support_type(company: Any) -> str:
        """Determines the primary mutual-exclusion family ('same_support_type') of a support company."""
        tags = UnitPool.get_support_types(company)
        return tags[0] if tags else getattr(company, "name", str(company)).lower()

    @staticmethod
    def get_allowed_regimental_groups(company: Any) -> List[str]:
        """Returns which battalion column groups can host this regimental support company."""
        allowed = getattr(company, "allowed_battalion_groups", None)
        if allowed:
            expanded = set()
            for g in allowed:
                g_low = g.lower().strip()
                if g_low in BATTALION_GROUPS:
                    expanded.add(g_low)
                if g_low == "infantry":
                    expanded.add("combat_support")
                elif g_low == "mobile":
                    expanded.add("mobile_combat_support")
                elif g_low == "armor":
                    expanded.add("armor_combat_support")
            if expanded:
                return list(expanded)
        name = getattr(company, "name", str(company))
        lower_name = name.lower()
        if any(k in lower_name for k in ("tank", "sp ", "self-propelled", "armored", "armoured", "flame", "land cruiser")):
            return ["armor", "armor_combat_support", "mobile", "mobile_combat_support"]
        if any(k in lower_name for k in ("motor", "truck", "helicopter", "cavalry")):
            return ["mobile", "mobile_combat_support", "infantry", "combat_support"]
        return list(BATTALION_GROUPS)

    def _is_unit_allowed(self, unit: Any) -> bool:
        """Applies special project, country-locked, year-unlock, and zero-stat filters."""
        name = getattr(unit, "name", "")
        stats: Optional[BaseStatistics] = getattr(unit, "base_stats", None) or (
            unit.get_stats() if hasattr(unit, "get_stats") else None
        )

        # Exclude unresearched placeholder battalions that have 0 attack, 0 defense, and 0 IC cost
        if isinstance(unit, Battalion) and stats is not None:
            if (
                stats.soft_attack <= 0.0
                and stats.hard_attack <= 0.0
                and stats.defense <= 0.0
                and stats.breakthrough <= 0.0
                and stats.ic_cost <= 0.0
            ):
                return False

        # Check special project flag
        is_sp = bool(
            getattr(unit, "is_special_project", False)
            or getattr(unit, "special_project", False)
            or (name in SPECIAL_PROJECT_UNITS)
        )
        if is_sp and not self.config.allow_special_projects:
            return False

        # Check country locked flag
        is_cl = bool(
            getattr(unit, "is_country_locked", False)
            or getattr(unit, "country_locked", False)
            or (name in COUNTRY_LOCKED_UNITS)
        )
        if is_cl and not self.config.allow_country_locked:
            return False

        # Check strict historical unlock year
        if self.config.strict_year_unlock:
            min_yr = getattr(unit, "year_unlocked", None) or getattr(unit, "min_year", None) or getattr(unit, "unlock_year", None)
            if min_yr is None or int(min_yr) <= 1918:
                min_yr = UNIT_MIN_YEAR_MAP.get(name, min_yr or 1918)
            try:
                if int(min_yr) > self.year_int:
                    return False
            except (ValueError, TypeError):
                pass

        return True

    def _resolve_era_dict(self, db_dict: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Resolves the closest available year dictionary in unit_database."""
        if self.year in db_dict:
            return db_dict[self.year]
        # Fallback: find closest year <= self.year_int, or earliest available
        available_years = sorted(
            (int(y), y) for y in db_dict.keys() if str(y).isdigit()
        )
        if not available_years:
            return next(iter(db_dict.values())) if db_dict else {}
        chosen_key = available_years[0][1]
        for yr_int, yr_key in available_years:
            if yr_int <= self.year_int:
                chosen_key = yr_key
        return db_dict[chosen_key]

    def _load_pool(self) -> None:
        """Populates available battalions, divisional supports, and regimental supports."""
        # 1. Load Raw Battalions
        get_avail_bat = getattr(unit_database, "get_available_battalions", None)
        raw_battalions: Dict[str, Battalion] = {}
        if callable(get_avail_bat):
            try:
                res = get_avail_bat(
                    self.year,
                    allow_special_projects=self.config.allow_special_projects,
                    allow_country_locked=self.config.allow_country_locked,
                    strict_year_unlock=self.config.strict_year_unlock,
                )
                if isinstance(res, dict):
                    raw_battalions = dict(res)
                elif isinstance(res, list):
                    raw_battalions = {b.name: b for b in res}
            except TypeError:
                try:
                    res = get_avail_bat(self.year)
                    raw_battalions = dict(res) if isinstance(res, dict) else {b.name: b for b in res}
                except Exception:
                    raw_battalions = {}

        if not raw_battalions:
            all_bats = getattr(unit_database, "All_Battalions", {})
            raw_battalions = dict(self._resolve_era_dict(all_bats))

        # 2. Load Raw Divisional Support Companies
        get_avail_div_sup = getattr(unit_database, "get_available_divisional_supports", None)
        raw_div_supports: Dict[str, SupportCompany] = {}
        if callable(get_avail_div_sup):
            try:
                res = get_avail_div_sup(
                    self.year,
                    allow_special_projects=self.config.allow_special_projects,
                    allow_country_locked=self.config.allow_country_locked,
                    strict_year_unlock=self.config.strict_year_unlock,
                )
                raw_div_supports = dict(res) if isinstance(res, dict) else {s.name: s for s in res}
            except TypeError:
                try:
                    res = get_avail_div_sup(self.year)
                    raw_div_supports = dict(res) if isinstance(res, dict) else {s.name: s for s in res}
                except Exception:
                    raw_div_supports = {}

        if not raw_div_supports:
            sup_db = getattr(unit_database, "Support_Companies", {})
            raw_div_supports = dict(self._resolve_era_dict(sup_db))

        # 3. Load Raw Regimental Support Companies (HOI4 v1.19.4.2 feature)
        raw_reg_supports: Dict[str, SupportCompany] = {}
        if self.config.allow_regimental_support:
            get_avail_reg_sup = getattr(unit_database, "get_available_regimental_supports", None)
            if callable(get_avail_reg_sup):
                try:
                    res = get_avail_reg_sup(
                        self.year,
                        allow_special_projects=self.config.allow_special_projects,
                        allow_country_locked=self.config.allow_country_locked,
                        strict_year_unlock=self.config.strict_year_unlock,
                    )
                    raw_reg_supports = dict(res) if isinstance(res, dict) else {s.name: s for s in res}
                except TypeError:
                    try:
                        res = get_avail_reg_sup(self.year)
                        raw_reg_supports = dict(res) if isinstance(res, dict) else {s.name: s for s in res}
                    except Exception:
                        raw_reg_supports = {}

            if not raw_reg_supports:
                reg_db = getattr(unit_database, "Regimental_Support_Companies", None)
                if isinstance(reg_db, dict) and reg_db:
                    raw_reg_supports = dict(self._resolve_era_dict(reg_db))

            # Fallback if Regimental_Support_Companies is not yet populated in unit_database:
            if not raw_reg_supports:
                sup_db = getattr(unit_database, "Support_Companies", {})
                era_sups = self._resolve_era_dict(sup_db)
                regimental_candidates = [
                    "Support Artillery",
                    "Support Anti-Air",
                    "Support Anti-Tank",
                    "Support Rocket Artillery",
                    "Assault Battalion",
                    "Sturmtruppe Battalion",
                    "Pioneers",
                    "Jungle Pioneers",
                    "Rangers",
                    "Long Range Patrol Company",
                    "Light Flame Tank Company",
                    "Medium Flame Tank Company",
                    "Heavy Flame Tank Company",
                ]
                for cand_name in regimental_candidates:
                    if cand_name in era_sups:
                        raw_reg_supports[cand_name] = era_sups[cand_name]

        # 4. Apply NSB Tank Designer blueprints if tank_design_mode != "historical"
        tank_mode = getattr(self.config, "tank_design_mode", "historical") or "historical"
        if tank_mode.lower().strip() not in ("historical", "default", "none", "preset"):
            raw_battalions, raw_div_supports, raw_reg_supports = (
                tank_designer.apply_tank_design_mode_to_pool(
                    raw_battalions,
                    raw_div_supports,
                    raw_reg_supports,
                    year=self.year,
                    mode=tank_mode,
                    objective=self.config.objective,
                )
            )

        # 5. Apply HOI4 v1.19.4.2 Land Doctrine modifiers if doctrine != "none"
        doc_key = getattr(self.config, "doctrine", "none") or "none"
        if doc_key.lower().strip() not in ("none", ""):
            raw_battalions, raw_div_supports, raw_reg_supports = (
                doctrines.apply_doctrine_to_pool(
                    raw_battalions,
                    raw_div_supports,
                    raw_reg_supports,
                    doctrine_key=doc_key,
                    year=self.year,
                    mastery_level=getattr(self.config, "doctrine_mastery", None),
                )
            )

        # 6. Populate filtered Battalion dictionaries
        for name, bat in sorted(raw_battalions.items()):
            if self._is_unit_allowed(bat):
                self.battalions_by_name[name] = bat
                grp = self.get_battalion_group(bat)
                self.battalions_by_group[grp].append(bat)

        # Ensure every group has at least one fallback if possible
        if not self.battalions_by_group["infantry"] and raw_battalions:
            first_bat = next(iter(raw_battalions.values()))
            self.battalions_by_name[first_bat.name] = first_bat
            self.battalions_by_group["infantry"].append(first_bat)

        # Exclude line battalions that were accidentally placed in Support_Companies in older DB versions
        NON_SUPPORT_BATTALIONS = {
            "Super Heavy Tank",
            "Super Heavy SP Artillery",
            "Super Heavy Tank Destroyer",
            "Super Heavy SP Anti-Air",
            "Assault Battalion",
            "Sturmtruppe Battalion",
        }

        # 7. Populate filtered Divisional Support dictionaries
        for name, sup in sorted(raw_div_supports.items()):
            is_reg = getattr(sup, "is_regimental", getattr(sup, "is_regimental_support", False))
            is_div = getattr(sup, "is_divisional", getattr(sup, "is_divisional_support", True))
            if is_reg and not is_div:
                continue
            if name in NON_SUPPORT_BATTALIONS and not getattr(sup, "is_divisional_support", False):
                continue
            if self._is_unit_allowed(sup):
                self.divisional_supports.append(sup)
                self.divisional_supports_by_name[name] = sup

        # 8. Populate filtered Regimental Support dictionaries
        if self.config.allow_regimental_support:
            for name, reg_sup in sorted(raw_reg_supports.items()):
                if self._is_unit_allowed(reg_sup):
                    self.regimental_supports_by_name[name] = reg_sup
                    for grp in self.get_allowed_regimental_groups(reg_sup):
                        if grp in self.regimental_supports_by_group:
                            self.regimental_supports_by_group[grp].append(reg_sup)

    def get_active_groups(self) -> List[str]:
        """Returns all brigade groups that have at least one available battalion."""
        return [g for g in BATTALION_GROUPS if self.battalions_by_group.get(g)]


# =============================================================================
# DivisionGenome — Dual Continuous/Discrete HOI4 Template Representation
# =============================================================================

@dataclass
class RegimentColumnGene:
    """
    Represents one of the 5 regiment columns in a HOI4 division template.

    - ``group``: ``"none"``, ``"infantry"``, ``"mobile"``, or ``"armor"``
    - ``battalions``: Up to 5 battalion names belonging to ``group``
    - ``regimental_support``: Optional regimental support company name
      (unlocked in HOI4 v1.19.4.2 only when ``len(battalions) >= 3`` and
      compatible with ``group``).
    """

    group: str = "none"
    battalions: List[str] = field(default_factory=list)
    regimental_support: Optional[str] = None

    def is_empty(self) -> bool:
        return self.group == "none" or len(self.battalions) == 0


@dataclass
class DivisionGenome:
    """
    Represents a complete, valid HOI4 division template genome:
    - 5 ``RegimentColumnGene`` objects (up to 5 battalions + 1 regimental support each)
    - Up to 5 Divisional Support company names (mutually exclusive by ``same_support_type``)

    Provides deterministic bi-directional mapping between:
    1. Continuous vector ``x in [0, 1]^45`` (for CSO Tracing Mode & PSO)
    2. Discrete gene structure (for CSO Seeking Mode, GA crossover/mutation, SA)
    3. Valid ``Division`` instance via ``to_division(unit_pool)``
    """

    columns: List[RegimentColumnGene] = field(
        default_factory=lambda: [RegimentColumnGene() for _ in range(5)]
    )
    divisional_supports: List[Optional[str]] = field(
        default_factory=lambda: [None] * 5
    )

    def copy(self) -> DivisionGenome:
        return DivisionGenome(
            columns=[
                RegimentColumnGene(
                    group=c.group,
                    battalions=list(c.battalions),
                    regimental_support=c.regimental_support,
                )
                for c in self.columns
            ],
            divisional_supports=list(self.divisional_supports),
        )

    def signature(self) -> str:
        """
        Returns a canonical, order-invariant composition signature string for
        fitness caching and top-candidate deduplication.
        """
        non_empty_cols = []
        for col in self.columns:
            if not col.is_empty():
                bats_str = ",".join(sorted(col.battalions))
                reg_str = col.regimental_support or "-"
                non_empty_cols.append(f"{col.group}:[{bats_str}]@{reg_str}")
        non_empty_cols.sort()
        sups = sorted(s for s in self.divisional_supports if s is not None)
        return f"COLS({'|'.join(non_empty_cols)})_SUPS({','.join(sups)})"

    def repair(self, unit_pool: UnitPool, config: OptimizationConfig, rng: random.Random) -> None:
        """
        Enforces all HOI4 v1.19.4.2 structural rules and combat width constraints:
        1. Every battalion in column ``c`` must exist in ``unit_pool`` and match ``c.group``.
        2. Each column has ``0..5`` battalions; at least 1 column is non-empty.
        3. Regimental support in column ``c`` is allowed only if ``config.allow_regimental_support``
           is True, ``len(c.battalions) >= 3``, and its ``allowed_battalion_groups`` includes ``c.group``.
        4. Divisional supports have at most 5 slots and no duplicate ``same_support_type``.
        5. Total combat width is repaired into ``[config.min_combat_width, config.max_combat_width]``
           (and division Organization is kept >= 15 so 0-ORG artillery-only templates are repaired).
        """
        active_groups = unit_pool.get_active_groups()
        if not active_groups:
            return

        # 1. Repair each column's group, battalions, and regimental support
        for col in self.columns:
            if col.group not in active_groups or len(col.battalions) == 0:
                col.group = "none"
                col.battalions = []
                col.regimental_support = None
                continue

            group_pool = unit_pool.battalions_by_group[col.group]
            group_names = {b.name for b in group_pool}
            valid_bats = []
            for b_name in col.battalions[:5]:
                if b_name in group_names:
                    valid_bats.append(b_name)
                else:
                    valid_bats.append(rng.choice(group_pool).name)
            col.battalions = valid_bats

            # Validate Regimental Support (requires >= 3 battalions in column)
            if not config.allow_regimental_support or len(col.battalions) < 3:
                col.regimental_support = None
            elif col.regimental_support is not None:
                compat_regs = unit_pool.regimental_supports_by_group.get(col.group, [])
                compat_names = {r.name for r in compat_regs}
                if col.regimental_support not in compat_names:
                    col.regimental_support = None

        # 2. Ensure at least one non-empty column exists
        if all(col.is_empty() for col in self.columns):
            default_grp = "infantry" if "infantry" in active_groups else active_groups[0]
            default_bat = unit_pool.battalions_by_group[default_grp][0].name
            self.columns[0].group = default_grp
            self.columns[0].battalions = [default_bat] * 3

        # 3. Repair Divisional Supports (enforce mutual exclusion via same_support_type)
        used_types = set()
        used_names = set()
        repaired_supports: List[Optional[str]] = [None] * 5
        for idx, sup_name in enumerate(self.divisional_supports[:5]):
            if sup_name is None or sup_name not in unit_pool.divisional_supports_by_name:
                continue
            sup_obj = unit_pool.divisional_supports_by_name[sup_name]
            sup_tags = unit_pool.get_support_types(sup_obj)
            if not any(t in used_types for t in sup_tags) and sup_name not in used_names:
                used_types.update(sup_tags)
                used_names.add(sup_name)
                repaired_supports[idx] = sup_name
        self.divisional_supports = repaired_supports

        # 4. Repair Combat Width & Minimum Organization (Line Infantry/Mobile backbone)
        def _current_width_and_org() -> Tuple[float, float]:
            width = 0.0
            orgs = []
            for col in self.columns:
                for b_name in col.battalions:
                    b_stats = unit_pool.battalions_by_name[b_name].get_stats()
                    width += b_stats.combat_width
                    orgs.append(b_stats.organization)
                if col.regimental_support and col.regimental_support in unit_pool.regimental_supports_by_name:
                    r_stats = unit_pool.regimental_supports_by_name[col.regimental_support].get_stats()
                    width += r_stats.combat_width
                    orgs.append(r_stats.organization)
            for s_name in self.divisional_supports:
                if s_name and s_name in unit_pool.divisional_supports_by_name:
                    s_stats = unit_pool.divisional_supports_by_name[s_name].get_stats()
                    orgs.append(s_stats.organization)
            avg_org = statistics.fmean(orgs) if orgs else 0.0
            return width, avg_org

        # Add battalions if below min_combat_width
        for _ in range(25):
            width, _ = _current_width_and_org()
            if width >= config.min_combat_width:
                break
            # Find a column with < 5 battalions or an empty column
            candidate_cols = [c for c in self.columns if not c.is_empty() and len(c.battalions) < 5]
            if candidate_cols:
                col = rng.choice(candidate_cols)
                # Prefer high-ORG line battalion in that group so width AND org stay healthy
                high_org_pool = [
                    b for b in unit_pool.battalions_by_group[col.group]
                    if b.get_stats().organization >= 30.0
                ] or unit_pool.battalions_by_group[col.group]
                col.battalions.append(rng.choice(high_org_pool).name)
            else:
                empty_cols = [c for c in self.columns if c.is_empty()]
                if not empty_cols:
                    break
                col = empty_cols[0]
                col.group = rng.choice(active_groups)
                high_org_pool = [
                    b for b in unit_pool.battalions_by_group[col.group]
                    if b.get_stats().organization >= 30.0
                ] or unit_pool.battalions_by_group[col.group]
                col.battalions = [rng.choice(high_org_pool).name]

        # Trim battalions if above max_combat_width
        for _ in range(25):
            width, _ = _current_width_and_org()
            if width <= config.max_combat_width:
                break
            non_empty_cols = [c for c in self.columns if not c.is_empty()]
            total_bats = sum(len(c.battalions) for c in non_empty_cols)
            if total_bats <= 1:
                break
            col = rng.choice(non_empty_cols)
            col.battalions.pop()
            if len(col.battalions) < 3:
                col.regimental_support = None
            if len(col.battalions) == 0:
                col.group = "none"

        # Ensure division has a viable organization backbone (>= 18 ORG)
        _, avg_org = _current_width_and_org()
        if avg_org < 18.0:
            for col in self.columns:
                if col.is_empty():
                    continue
                high_org_pool = [
                    b for b in unit_pool.battalions_by_group[col.group]
                    if b.get_stats().organization >= 40.0
                ]
                if not high_org_pool and "infantry" in unit_pool.battalions_by_group:
                    col.group = "infantry"
                    col.regimental_support = None
                    high_org_pool = [
                        b for b in unit_pool.battalions_by_group["infantry"]
                        if b.get_stats().organization >= 40.0
                    ] or unit_pool.battalions_by_group["infantry"]
                if high_org_pool:
                    for i in range(len(col.battalions)):
                        b_obj = unit_pool.battalions_by_name[col.battalions[i]]
                        if b_obj.get_stats().organization < 20.0:
                            col.battalions[i] = rng.choice(high_org_pool).name
                        _, new_org = _current_width_and_org()
                        if new_org >= 22.0:
                            break

    @classmethod
    def from_vector(
        cls,
        vector: List[float],
        unit_pool: UnitPool,
        config: OptimizationConfig,
        rng: Optional[random.Random] = None,
    ) -> DivisionGenome:
        """
        Deterministically decodes a continuous vector ``x in [0, 1]^45`` into a
        valid ``DivisionGenome``.
        """
        rng = rng or random.Random(0)
        vec = [max(0.0, min(1.0, float(v))) for v in vector]
        if len(vec) < GENOME_VECTOR_DIM:
            vec.extend([0.0] * (GENOME_VECTOR_DIM - len(vec)))

        active_groups = unit_pool.get_active_groups()
        columns: List[RegimentColumnGene] = []

        for c in range(5):
            base = c * 7
            g_val = vec[base + 0]
            cnt_val = vec[base + 1]
            slot_vals = vec[base + 2 : base + 7]

            # First 2 columns have lower activation threshold so divisions aren't trivially tiny
            empty_threshold = 0.08 if c < 2 else 0.32
            if g_val < empty_threshold or not active_groups:
                columns.append(RegimentColumnGene(group="none", battalions=[], regimental_support=None))
                continue

            # Map [empty_threshold, 1.0] across active_groups
            norm_g = (g_val - empty_threshold) / max(1e-6, 1.0 - empty_threshold)
            grp_idx = min(len(active_groups) - 1, int(norm_g * len(active_groups)))
            grp = active_groups[grp_idx]

            # Count of battalions in column: 1..5
            count = max(1, min(5, 1 + int(cnt_val * 5.0 - 1e-9)))
            group_pool = unit_pool.battalions_by_group[grp]
            bats: List[str] = []
            for r in range(count):
                s_val = slot_vals[r]
                b_idx = min(len(group_pool) - 1, int(s_val * len(group_pool)))
                bats.append(group_pool[b_idx].name)

            # Regimental support gene at index 40 + c
            reg_val = vec[40 + c]
            reg_sup_name: Optional[str] = None
            if config.allow_regimental_support and count >= 3 and reg_val >= 0.35:
                compat_regs = unit_pool.regimental_supports_by_group.get(grp, [])
                if compat_regs:
                    norm_r = (reg_val - 0.35) / 0.65
                    r_idx = min(len(compat_regs) - 1, int(norm_r * len(compat_regs)))
                    reg_sup_name = compat_regs[r_idx].name

            columns.append(
                RegimentColumnGene(group=grp, battalions=bats, regimental_support=reg_sup_name)
            )

        # Decode 5 Divisional Support slots (indices 35..39)
        div_supports: List[Optional[str]] = [None] * 5
        sup_pool = unit_pool.divisional_supports
        used_types = set()
        used_names = set()
        if sup_pool:
            for s in range(5):
                s_val = vec[35 + s]
                if s_val < 0.25:
                    continue
                norm_s = (s_val - 0.25) / 0.75
                start_idx = min(len(sup_pool) - 1, int(norm_s * len(sup_pool)))
                # Scan from start_idx for the nearest support company that doesn't violate mutual exclusion
                for offset in range(len(sup_pool)):
                    cand = sup_pool[(start_idx + offset) % len(sup_pool)]
                    cand_tags = unit_pool.get_support_types(cand)
                    if not any(t in used_types for t in cand_tags) and cand.name not in used_names:
                        div_supports[s] = cand.name
                        used_types.update(cand_tags)
                        used_names.add(cand.name)
                        break

        genome = cls(columns=columns, divisional_supports=div_supports)
        genome.repair(unit_pool, config, rng)
        return genome

    def to_vector(self, unit_pool: UnitPool) -> List[float]:
        """
        Encodes this discrete ``DivisionGenome`` back into a continuous vector
        ``x in [0, 1]^45`` so continuous-space metaheuristics stay synchronized
        after discrete mutations or repairs.
        """
        vec = [0.0] * GENOME_VECTOR_DIM
        active_groups = unit_pool.get_active_groups()

        for c in range(5):
            base = c * 7
            col = self.columns[c]
            empty_threshold = 0.08 if c < 2 else 0.32
            if col.is_empty() or col.group not in active_groups:
                vec[base + 0] = empty_threshold * 0.5
                vec[base + 1] = 0.0
                continue

            grp_idx = active_groups.index(col.group)
            span = (1.0 - empty_threshold) / len(active_groups)
            vec[base + 0] = min(1.0, empty_threshold + (grp_idx + 0.5) * span)
            vec[base + 1] = min(1.0, (len(col.battalions) - 0.5) / 5.0)

            group_pool = unit_pool.battalions_by_group[col.group]
            name_to_idx = {b.name: i for i, b in enumerate(group_pool)}
            for r in range(5):
                if r < len(col.battalions):
                    idx = name_to_idx.get(col.battalions[r], 0)
                    vec[base + 2 + r] = (idx + 0.5) / max(1, len(group_pool))
                else:
                    vec[base + 2 + r] = 0.0

            # Regimental support
            if col.regimental_support is not None:
                compat_regs = unit_pool.regimental_supports_by_group.get(col.group, [])
                r_names = [r.name for r in compat_regs]
                if col.regimental_support in r_names:
                    r_idx = r_names.index(col.regimental_support)
                    vec[40 + c] = 0.35 + 0.65 * ((r_idx + 0.5) / max(1, len(compat_regs)))
                else:
                    vec[40 + c] = 0.15
            else:
                vec[40 + c] = 0.15

        # Divisional supports
        sup_pool = unit_pool.divisional_supports
        sup_names = [s.name for s in sup_pool]
        for s in range(5):
            s_name = self.divisional_supports[s]
            if s_name is not None and s_name in sup_names:
                s_idx = sup_names.index(s_name)
                vec[35 + s] = 0.25 + 0.75 * ((s_idx + 0.5) / max(1, len(sup_pool)))
            else:
                vec[35 + s] = 0.10

        return [max(0.0, min(1.0, v)) for v in vec]

    @classmethod
    def random(
        cls,
        unit_pool: UnitPool,
        config: OptimizationConfig,
        rng: random.Random,
    ) -> DivisionGenome:
        """Generates a diverse, valid random ``DivisionGenome``."""
        vec = [rng.random() for _ in range(GENOME_VECTOR_DIM)]
        # Encourage cohesive columns (same unit repeated within a column) 60% of the time
        if rng.random() < 0.65:
            for c in range(5):
                base = c * 7
                primary_unit_val = rng.random()
                for r in range(5):
                    if rng.random() < 0.75:
                        vec[base + 2 + r] = primary_unit_val
        return cls.from_vector(vec, unit_pool, config, rng=rng)

    def to_division(self, unit_pool: UnitPool, name: str = "Optimized Division") -> Division:
        """
        Instantiates a ``Division`` object from this genome, compatible with both
        the legacy ``Division`` class and the v1.19.4.2 column-aware ``Division`` class.
        """
        div = Division(name)

        # Check if Division supports column-aware add_battalion(bat, column=c)
        for c_idx, col in enumerate(self.columns):
            if col.is_empty():
                continue
            for b_name in col.battalions:
                bat_obj = unit_pool.battalions_by_name.get(b_name)
                if bat_obj is None:
                    continue
                try:
                    div.add_battalion(bat_obj, column=c_idx)  # type: ignore[call-arg]
                except TypeError:
                    div.add_battalion(bat_obj)

            if col.regimental_support and col.regimental_support in unit_pool.regimental_supports_by_name:
                reg_obj = unit_pool.regimental_supports_by_name[col.regimental_support]
                add_reg_fn = getattr(div, "add_regimental_support", None)
                if callable(add_reg_fn):
                    try:
                        add_reg_fn(reg_obj, column=c_idx)
                    except TypeError:
                        try:
                            add_reg_fn(c_idx, reg_obj)
                        except Exception:
                            pass
                else:
                    # Fallback if Division does not yet have add_regimental_support:
                    # store in div.regimental_support_companies list if not exceeding support cap
                    if not hasattr(div, "regimental_support_companies"):
                        setattr(div, "regimental_support_companies", {})
                    getattr(div, "regimental_support_companies")[c_idx] = reg_obj

        for s_name in self.divisional_supports:
            if s_name and s_name in unit_pool.divisional_supports_by_name:
                sup_obj = unit_pool.divisional_supports_by_name[s_name]
                try:
                    div.add_support_company(sup_obj)
                except Exception:
                    pass

        # Attach structured genome metadata for exact 5x5 grid & regimental support serialization
        setattr(
            div,
            "_genome_metadata",
            {
                "columns": [
                    {
                        "column_index": idx,
                        "group": col.group,
                        "battalions": list(col.battalions),
                        "regimental_support": col.regimental_support,
                    }
                    for idx, col in enumerate(self.columns)
                ],
                "divisional_supports": [s for s in self.divisional_supports if s is not None],
                "signature": self.signature(),
            },
        )
        return div


# =============================================================================
# Fallback Serializer & Fitness / Candidate Dataclasses
# =============================================================================

def serialize_division(div: Division) -> Dict[str, Any]:
    """
    Serializes a ``Division`` instance to a comprehensive, JSON-ready dictionary.
    Uses ``div.to_dict()`` if implemented on ``Division``, and enriches it with
    structured 5-column regiment grid, regimental supports, divisional supports,
    aggregate combat statistics, and terrain modifiers.
    """
    base_dict: Dict[str, Any] = {}
    if hasattr(div, "to_dict") and callable(getattr(div, "to_dict")):
        try:
            res = div.to_dict()
            if isinstance(res, dict):
                base_dict.update(res)
        except Exception:
            pass

    stats = div.calculate_stats()
    terrain_mods = div.calculate_terrain_modifiers()

    stats_dict = {
        "soft_attack": round(stats.soft_attack, 2),
        "hard_attack": round(stats.hard_attack, 2),
        "defense": round(stats.defense, 2),
        "breakthrough": round(stats.breakthrough, 2),
        "max_hp": round(stats.max_hp, 2),
        "organization": round(stats.organization, 2),
        "combat_width": round(stats.combat_width, 2),
        "supply_use": round(stats.supply_use, 3),
        "ic_cost": round(stats.ic_cost, 2),
        "manpower": round(stats.manpower, 0),
        "armor": round(stats.armor, 2),
        "piercing": round(stats.piercing, 2),
        "hardness": round(stats.hardness, 3),
        "air_attack": round(stats.air_attack, 2),
        "entrenchment": round(stats.entrenchment, 2),
        "initiative": round(stats.initiative, 3),
        "recon": round(stats.recon, 2),
        "supply_consumption_factor": round(stats.supply_consumption_factor, 3),
        "recovery_rate": round(getattr(stats, "recovery_rate", 0.0), 3),
    }

    terrain_mods_dict = {
        t_name: {
            "attack": round(mod.attack, 3),
            "defense": round(mod.defense, 3),
        }
        for t_name, mod in terrain_mods.items()
    }

    genome_meta = getattr(div, "_genome_metadata", None)
    if genome_meta:
        columns_data = genome_meta["columns"]
        div_supports = genome_meta["divisional_supports"]
    else:
        grid = div.get_composition_grid() if hasattr(div, "get_composition_grid") else {}
        raw_regs = grid.get("regiments", [])
        columns_data = []
        for idx in range(5):
            col_bats = [b.name for b in raw_regs[idx]] if idx < len(raw_regs) else []
            grp = UnitPool.get_battalion_group(raw_regs[idx][0]) if (idx < len(raw_regs) and raw_regs[idx]) else "none"
            reg_sup = None
            reg_sups_attr = getattr(div, "regimental_supports", None) or getattr(div, "regimental_support_companies", None)
            if isinstance(reg_sups_attr, dict) and idx in reg_sups_attr and reg_sups_attr[idx]:
                reg_sup = getattr(reg_sups_attr[idx], "name", str(reg_sups_attr[idx]))
            elif isinstance(reg_sups_attr, list) and idx < len(reg_sups_attr) and reg_sups_attr[idx]:
                reg_sup = getattr(reg_sups_attr[idx], "name", str(reg_sups_attr[idx]))
            columns_data.append(
                {
                    "column_index": idx,
                    "group": grp if col_bats else "none",
                    "battalions": col_bats,
                    "regimental_support": reg_sup,
                }
            )
        div_supports = [c.name for c in getattr(div, "support_companies", [])]

    battalion_counts: Dict[str, int] = {}
    for b in getattr(div, "battalions", []):
        battalion_counts[b.name] = battalion_counts.get(b.name, 0) + 1

    regimental_supports_list = [
        c["regimental_support"] for c in columns_data if c.get("regimental_support")
    ]

    base_dict.update(
        {
            "name": div.name,
            "stats": stats_dict,
            "terrain_modifiers": terrain_mods_dict,
            "battalions": [b.name for b in getattr(div, "battalions", [])],
            "battalion_counts": battalion_counts,
            "support_companies": div_supports,
            "regimental_supports": regimental_supports_list,
            "columns": columns_data,
        }
    )
    return base_dict


@dataclass
class FitnessMetrics:
    """
    Comprehensive multi-terrain combat performance metrics for a candidate division.
    """

    total_fitness: float = 0.0
    win_rate: float = 0.0
    attacker_win_rate: float = 0.0
    defender_win_rate: float = 0.0
    avg_org_remaining_ratio: float = 0.0
    avg_hp_remaining_ratio: float = 0.0
    avg_battle_duration_hours: float = 0.0
    ic_efficiency_score: float = 0.0
    bang_for_buck_score: float = 0.0
    terrain_win_rates: Dict[str, float] = field(default_factory=dict)
    terrain_scores: Dict[str, float] = field(default_factory=dict)
    combat_stats_summary: Dict[str, float] = field(default_factory=dict)
    constraint_penalty: float = 0.0

    @property
    def Bang_for_buck_score(self) -> float:
        """Alias matching legacy/contract capital-B casing."""
        return self.bang_for_buck_score

    @Bang_for_buck_score.setter
    def Bang_for_buck_score(self, value: float) -> None:
        self.bang_for_buck_score = value

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["Bang_for_buck_score"] = self.bang_for_buck_score
        return d


@dataclass
class CandidateSolution:
    """
    Encapsulates a candidate division genome, its instantiated ``Division``,
    its ``FitnessMetrics``, its latent continuous vector, and search metadata.
    """

    genome: DivisionGenome
    division: Division
    metrics: FitnessMetrics
    vector: List[float]
    iteration_found: int = 0
    agent_id: int = 0
    mode: str = "seeking"

    @property
    def fitness(self) -> float:
        return self.metrics.total_fitness

    @property
    def signature(self) -> str:
        return self.genome.signature()

    def copy(self) -> CandidateSolution:
        return CandidateSolution(
            genome=self.genome.copy(),
            division=self.division,
            metrics=copy.deepcopy(self.metrics),
            vector=list(self.vector),
            iteration_found=self.iteration_found,
            agent_id=self.agent_id,
            mode=self.mode,
        )

    def to_dict(self) -> Dict[str, Any]:
        div_dict = serialize_division(self.division)
        metrics_dict = self.metrics.to_dict()
        return {
            "name": self.division.name,
            "signature": self.signature,
            "fitness": round(self.metrics.total_fitness, 4),
            "total_fitness": round(self.metrics.total_fitness, 4),
            "win_rate": round(self.metrics.win_rate, 4),
            "attacker_win_rate": round(self.metrics.attacker_win_rate, 4),
            "defender_win_rate": round(self.metrics.defender_win_rate, 4),
            "avg_org_remaining_ratio": round(self.metrics.avg_org_remaining_ratio, 4),
            "avg_hp_remaining_ratio": round(self.metrics.avg_hp_remaining_ratio, 4),
            "avg_battle_duration_hours": round(self.metrics.avg_battle_duration_hours, 2),
            "ic_efficiency_score": round(self.metrics.ic_efficiency_score, 4),
            "bang_for_buck_score": round(self.metrics.bang_for_buck_score, 4),
            "Bang_for_buck_score": round(self.metrics.bang_for_buck_score, 4),
            "terrain_win_rates": {
                k: round(v, 4) for k, v in self.metrics.terrain_win_rates.items()
            },
            "terrain_scores": {
                k: round(v, 4) for k, v in self.metrics.terrain_scores.items()
            },
            "combat_stats_summary": self.metrics.combat_stats_summary,
            "stats": div_dict["stats"],
            "composition": {
                "columns": div_dict["columns"],
                "battalions": div_dict["battalions"],
                "battalion_counts": div_dict["battalion_counts"],
                "support_companies": div_dict["support_companies"],
                "regimental_supports": div_dict["regimental_supports"],
            },
            "division": div_dict,
            "metrics": metrics_dict,
            "iteration_found": self.iteration_found,
            "agent_id": self.agent_id,
            "mode": self.mode,
        }


# =============================================================================
# BaseDivisionOptimizer — Abstract Algorithm-Agnostic Engine
# =============================================================================

class BaseDivisionOptimizer(abc.ABC):
    """
    Abstract base class for all division template optimization algorithms.

    Provides a unified lifecycle (``initialize_population()``, ``step(iteration)``,
    ``run(on_step_callback)``) and emits a standardized telemetry dictionary after
    every iteration so the web dashboard and run logger remain 100% decoupled from
    the specific optimization algorithm.
    """

    ALGORITHM_NAME: str = "Base Optimizer"

    def __init__(
        self,
        config: OptimizationConfig,
        evaluator: Optional[Any] = None,
        on_step_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
    ) -> None:
        self.config = config
        self.rng = random.Random(config.random_seed)
        self.unit_pool = UnitPool(config)

        if evaluator is None:
            from optimizer.objectives import DivisionEvaluator
            evaluator = DivisionEvaluator(config, self.unit_pool)
        self.evaluator = evaluator
        self.on_step_callback = on_step_callback

        self.population: List[CandidateSolution] = []
        self.best_candidate: Optional[CandidateSolution] = None
        self.top_candidates: List[CandidateSolution] = []
        self.fitness_history: List[Dict[str, Any]] = []
        self.current_iteration: int = 0
        self.start_time: float = 0.0

    def evaluate_genome(
        self,
        genome: DivisionGenome,
        vector: Optional[List[float]] = None,
        iteration: int = 0,
        agent_id: int = 0,
        mode: str = "seeking",
    ) -> CandidateSolution:
        """
        Repairs a ``DivisionGenome``, converts it to a ``Division``, evaluates its
        fitness across the multi-terrain benchmark pool, and updates the elite archive.
        """
        genome.repair(self.unit_pool, self.config, self.rng)
        sync_vec = vector if vector is not None else genome.to_vector(self.unit_pool)
        div_name = f"{self.config.method.upper()}-{self.config.year}-Iter{iteration}-Agent{agent_id}"
        division = genome.to_division(self.unit_pool, name=div_name)
        metrics = self.evaluator.evaluate(division, signature=genome.signature())

        candidate = CandidateSolution(
            genome=genome,
            division=division,
            metrics=metrics,
            vector=sync_vec,
            iteration_found=iteration,
            agent_id=agent_id,
            mode=mode,
        )
        self._update_archive(candidate)
        return candidate

    def _update_archive(self, candidate: CandidateSolution) -> None:
        """Updates the global best candidate and deduplicated top-12 archive."""
        if (
            self.best_candidate is None
            or candidate.fitness > self.best_candidate.fitness
        ):
            self.best_candidate = candidate.copy()
            self.best_candidate.division.name = (
                f"Best {self.config.year} {self.config.objective.replace('_', ' ').title()} Division"
            )

        sig = candidate.signature
        existing_idx = next(
            (i for i, c in enumerate(self.top_candidates) if c.signature == sig),
            None,
        )
        if existing_idx is not None:
            if candidate.fitness > self.top_candidates[existing_idx].fitness:
                self.top_candidates[existing_idx] = candidate.copy()
        else:
            self.top_candidates.append(candidate.copy())

        self.top_candidates.sort(key=lambda c: c.fitness, reverse=True)
        if len(self.top_candidates) > 12:
            self.top_candidates = self.top_candidates[:12]

    @abc.abstractmethod
    def initialize_population(self) -> None:
        """Initializes the starting population of candidate solutions."""

    @abc.abstractmethod
    def step(self, iteration: int) -> Dict[str, int]:
        """
        Executes a single optimization iteration and returns a dictionary of
        behavioral mode counts (e.g., ``{"seeking": 18, "tracing": 6}``).
        """

    def build_telemetry_snapshot(
        self,
        iteration: int,
        mode_counts: Dict[str, int],
    ) -> Dict[str, Any]:
        """
        Constructs the standardized iteration snapshot dictionary consumed by
        the live web dashboard and logger.
        """
        elapsed = time.time() - self.start_time if self.start_time > 0 else 0.0
        fitness_values = [c.fitness for c in self.population] if self.population else [0.0]
        best_fit = self.best_candidate.fitness if self.best_candidate else max(fitness_values)
        mean_fit = statistics.fmean(fitness_values)
        min_fit = min(fitness_values)
        std_fit = statistics.pstdev(fitness_values) if len(fitness_values) > 1 else 0.0

        leader_dict = self.best_candidate.to_dict() if self.best_candidate else {}
        leader_stats = leader_dict.get("stats", {})

        history_entry = {
            "iteration": iteration,
            "best_fitness": round(best_fit, 4),
            "mean_fitness": round(mean_fit, 4),
            "min_fitness": round(min_fit, 4),
            "std_fitness": round(std_fit, 4),
            "win_rate": round(self.best_candidate.metrics.win_rate, 4) if self.best_candidate else 0.0,
            "attacker_win_rate": round(self.best_candidate.metrics.attacker_win_rate, 4) if self.best_candidate else 0.0,
            "defender_win_rate": round(self.best_candidate.metrics.defender_win_rate, 4) if self.best_candidate else 0.0,
            "bang_for_buck_score": round(self.best_candidate.metrics.bang_for_buck_score, 4) if self.best_candidate else 0.0,
            "ic_cost": leader_stats.get("ic_cost", 0.0),
            "combat_width": leader_stats.get("combat_width", 0.0),
            "seeking_count": mode_counts.get("seeking", 0),
            "tracing_count": mode_counts.get("tracing", 0),
            "mode_counts": dict(mode_counts),
            "elapsed_seconds": round(elapsed, 2),
        }
        self.fitness_history.append(history_entry)

        return {
            "iteration": iteration,
            "total_iterations": self.config.iterations,
            "method": self.config.method,
            "algorithm_name": self.ALGORITHM_NAME,
            "year": self.config.year,
            "objective": self.config.objective,
            "terrains": self.config.terrains,
            "best_fitness": round(best_fit, 4),
            "mean_fitness": round(mean_fit, 4),
            "min_fitness": round(min_fit, 4),
            "std_fitness": round(std_fit, 4),
            "leader": leader_dict,
            "best_candidate": leader_dict,
            "top_candidates": [c.to_dict() for c in self.top_candidates[:10]],
            "population": [c.to_dict() for c in self.population],
            "fitness_history": list(self.fitness_history),
            "mode_counts": dict(mode_counts),
            "elapsed_seconds": round(elapsed, 2),
            "total_evaluations": getattr(self.evaluator, "total_evaluations", 0),
            "cache_hits": getattr(self.evaluator, "cache_hits", 0),
        }

    def run(
        self,
        on_step_callback: Optional[Callable[[Dict[str, Any]], None]] = None,
    ) -> Dict[str, Any]:
        """
        Runs the complete optimization process for ``config.iterations`` steps.
        Invokes ``on_step_callback(snapshot)`` after initialization and after
        every iteration.
        """
        callback = on_step_callback or self.on_step_callback
        self.start_time = time.time()
        self.fitness_history.clear()

        self.initialize_population()

        for iteration in range(1, self.config.iterations + 1):
            self.current_iteration = iteration
            mode_counts = self.step(iteration)
            snapshot = self.build_telemetry_snapshot(iteration, mode_counts)
            if callback is not None:
                callback(snapshot)

        elapsed = time.time() - self.start_time
        leader_dict = self.best_candidate.to_dict() if self.best_candidate else {}
        return {
            "method": self.config.method,
            "algorithm_name": self.ALGORITHM_NAME,
            "year": self.config.year,
            "objective": self.config.objective,
            "config": self.config.to_dict(),
            "leader": leader_dict,
            "best_candidate": leader_dict,
            "best_division": self.best_candidate.division if self.best_candidate else None,
            "top_candidates": [c.to_dict() for c in self.top_candidates[:10]],
            "fitness_history": list(self.fitness_history),
            "elapsed_seconds": round(elapsed, 2),
            "total_evaluations": getattr(self.evaluator, "total_evaluations", 0),
            "cache_hits": getattr(self.evaluator, "cache_hits", 0),
        }

    def generate_archetype_genomes(self) -> List[DivisionGenome]:
        """
        Generates a small set of era-valid domain archetype genomes (Infantry/Artillery,
        Armor/Tank, Mobile/Motorized, Special Forces) that any optimization algorithm
        can optionally use to seed a portion of its initial population.
        """
        seeds: List[DivisionGenome] = []
        bats = self.unit_pool.battalions_by_name
        active_groups = self.unit_pool.get_active_groups()

        def _pick_sups(*preferred: str) -> List[Optional[str]]:
            chosen: List[Optional[str]] = [None] * 5
            idx = 0
            for p in preferred:
                if p in self.unit_pool.divisional_supports_by_name and idx < 5:
                    chosen[idx] = p
                    idx += 1
            return chosen

        # 1. Classic Infantry + Artillery template
        if "infantry" in active_groups and "Infantry" in bats:
            art_name = "Artillery" if "Artillery" in bats else "Infantry"
            art_grp = self.unit_pool.get_battalion_group(bats[art_name])
            seeds.append(
                DivisionGenome(
                    columns=[
                        RegimentColumnGene("infantry", ["Infantry"] * 3),
                        RegimentColumnGene("infantry", ["Infantry"] * 3),
                        RegimentColumnGene("infantry", ["Infantry"] * 2),
                        RegimentColumnGene(art_grp, [art_name] * 2),
                        RegimentColumnGene(),
                    ],
                    divisional_supports=_pick_sups(
                        "Engineer Company",
                        "Support Artillery",
                        "Support Anti-Air",
                        "Recon Company",
                    ),
                )
            )

        # 2. Armored Breakthrough template
        if "armor" in active_groups and "mobile" in active_groups:
            tank_pool = self.unit_pool.battalions_by_group["armor"]
            mob_pool = self.unit_pool.battalions_by_group["mobile"]
            t_name = next(
                (b.name for b in tank_pool if "Medium Tank" in b.name or "Light Tank" in b.name),
                tank_pool[0].name,
            )
            m_name = next(
                (b.name for b in mob_pool if "Motorized" in b.name or "Mechanized" in b.name),
                mob_pool[0].name,
            )
            seeds.append(
                DivisionGenome(
                    columns=[
                        RegimentColumnGene("armor", [t_name] * 3),
                        RegimentColumnGene("armor", [t_name] * 3),
                        RegimentColumnGene("mobile", [m_name] * 4),
                        RegimentColumnGene(),
                        RegimentColumnGene(),
                    ],
                    divisional_supports=_pick_sups(
                        "Engineer Company",
                        "Motorized Recon Company",
                        "Support Artillery",
                        "Support Anti-Air",
                        "Logistics Company",
                    ),
                )
            )

        # 3. Mobile / Motorized template
        if "mobile" in active_groups:
            mob_pool = self.unit_pool.battalions_by_group["mobile"]
            m_name = next(
                (b.name for b in mob_pool if "Motorized Infantry" in b.name or "Cavalry" in b.name),
                mob_pool[0].name,
            )
            seeds.append(
                DivisionGenome(
                    columns=[
                        RegimentColumnGene("mobile", [m_name] * 3),
                        RegimentColumnGene("mobile", [m_name] * 3),
                        RegimentColumnGene("mobile", [m_name] * 3),
                        RegimentColumnGene(),
                        RegimentColumnGene(),
                    ],
                    divisional_supports=_pick_sups(
                        "Engineer Company",
                        "Motorized Recon Company",
                        "Support Artillery",
                        "Support Anti-Tank",
                    ),
                )
            )

        # 4. Special Forces / Terrain Specialist template
        if "infantry" in active_groups:
            inf_pool = self.unit_pool.battalions_by_group["infantry"]
            sf_name = next(
                (b.name for b in inf_pool if b.name in ("Mountaineers", "Mountain", "Marines")),
                inf_pool[0].name,
            )
            seeds.append(
                DivisionGenome(
                    columns=[
                        RegimentColumnGene("infantry", [sf_name] * 3),
                        RegimentColumnGene("infantry", [sf_name] * 3),
                        RegimentColumnGene("infantry", [sf_name] * 3),
                        RegimentColumnGene(),
                        RegimentColumnGene(),
                    ],
                    divisional_supports=_pick_sups(
                        "Engineer Company",
                        "Support Artillery",
                        "Rangers",
                        "Support Anti-Air",
                    ),
                )
            )

        return seeds


# =============================================================================
# Pluggable Optimizer Registry & Decorator
# =============================================================================

OPTIMIZER_REGISTRY: Dict[str, Type[BaseDivisionOptimizer]] = {}


def register_optimizer(
    name: str,
    optimizer_cls: Optional[Type[BaseDivisionOptimizer]] = None,
    *,
    aliases: Optional[List[str]] = None,
) -> Any:
    """
    Registers a ``BaseDivisionOptimizer`` subclass under ``name`` (and optional
    ``aliases``) so it can be instantiated dynamically via ``create_optimizer``
    or ``run_optimization`` without modifying the core engine.

    Can be used either as a class decorator::

        @register_optimizer("cso", aliases=["cat_swarm", "catswarm"])
        class CatSwarmOptimizer(BaseDivisionOptimizer):
            ...

    or as a direct registration call::

        register_optimizer("custom_algo", MyCustomOptimizer)
    """
    def _decorator(cls: Type[BaseDivisionOptimizer]) -> Type[BaseDivisionOptimizer]:
        OPTIMIZER_REGISTRY[name.lower().strip()] = cls
        for alias in (aliases or []):
            OPTIMIZER_REGISTRY[alias.lower().strip()] = cls
        return cls

    if optimizer_cls is not None:
        return _decorator(optimizer_cls)
    return _decorator


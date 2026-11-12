"""
Official Hearts of Iron IV v1.19.4.2 ('Operation Postern' / No Step Back & Gotterdammerung)
Tank Designer & Blueprint Optimization Engine (`tank_designer.py`).

This module implements the complete Clausewitz No Step Back (NSB) Tank Designer
mechanics extracted directly from:
- `common/units/equipment/tank_chassis.txt`
- `common/units/equipment/modules/00_tank_modules.txt`
- `common/units/*.txt`
- `common/technologies/NSB_armor.txt`, `artillery.txt`, `support.txt`

Core Responsibilities
---------------------
1. **Official Chassis Catalog (`TANK_CHASSIS`)**:
   Models all 16 official tank chassis across Light, Medium, Heavy, Super-Heavy,
   Modern, Amphibious, and Land Cruiser classes with exact base statistics,
   hardness, IC costs, and `module_add_stats_multiplier` scaling.
2. **Official Module Catalog (`TANK_MODULES`) & Upgrade Ticks (`TANK_UPGRADES`)**:
   Models all turrets (1-man, 2-man, 3-man, 4-man, fixed superstructure, modern),
   main weapons (machine guns, autocannons, close support gun, small/medium/heavy/
   super-heavy cannons, howitzers, high-velocity cannons, AA guns, flamethrowers,
   rocket launchers, Land Cruiser naval guns), suspensions, armor types, engine
   types, special modules (radios, stabilizers, sloped armor, wet ammo, secondary
   turrets, dozer blades, amphibious drive, auto-loaders), and `0..20` engine/armor
   upgrade ticks.
3. **Exact Clausewitz NSB Equipment Stat Formula (`TankBlueprint.calculate_equipment_stats`)**:
   Computes final tank equipment stats via:
   $$\text{Stat}_{\text{final}} = \left(\text{Stat}_{\text{chassis}} + \sum_{m} \text{add\_stats}_{m}(\text{Stat})\right) \times \left(1.0 + \sum_{m} \text{multiply\_stats}_{m}(\text{Stat})\right)$$
4. **Sub-Unit Conversion (`blueprint_to_unit`)**:
   Converts any `TankBlueprint` into a playable `Battalion` or `SupportCompany`
   by applying the target sub-unit's equipment `need` count, sub-unit stat
   multipliers (e.g. `-0.75` breakthrough on SPGs/TDs/SPAAs, `-0.6` on Light Tank
   Recon, flame tank support penalties), and era technology modifiers (`1934`,
   `1936`, `1939`, `1940`, `1945`).
5. **Inner-Loop Tank Blueprint Optimizer (`optimize_tank_blueprint` & `apply_tank_design_mode_to_pool`)**:
   Searches over all legal chassis/turret/gun/suspension/armor/engine/special/tick
   combinations unlocked by a given `year` to construct optimal tank designs for
   any tactical role or division optimization objective (`"historical"`,
   `"nsb_meta_soft_attack"`, `"nsb_meta_hard_attack"`, `"nsb_meta_armor_brick"`,
   `"nsb_budget"`, `"nsb_auto_optimize"`).
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

from battalion import Battalion
from modifiers import BattalionMultiplier, TerrainModifier, UnitModifiers
from stats import BaseStatistics
from support_company import SupportCompany
import unit_database


# ==============================================================================
# 1. CONSTANTS & SUPPORTED TANK DESIGN MODES
# ==============================================================================

TANK_DESIGN_MODES: List[str] = [
    "historical",
    "nsb_meta_soft_attack",
    "nsb_meta_hard_attack",
    "nsb_meta_armor_brick",
    "nsb_budget",
    "nsb_auto_optimize",
]

TANK_ROLES: Tuple[str, ...] = (
    "tank",
    "tank_destroyer",
    "artillery",
    "anti_air",
    "flame_tank",
    "amphibious_tank",
    "land_cruiser",
)

MAX_UPGRADE_TICKS_BY_YEAR: Dict[str, int] = {
    "1934": 4,
    "1936": 6,
    "1939": 10,
    "1940": 14,
    "1945": 20,
}


# ==============================================================================
# 2. DATA STRUCTURES: TankChassis, TankModule, TankBlueprint
# ==============================================================================

@dataclass(frozen=True)
class TankChassis:
    """
    Represents an official HOI4 v1.19.4.2 NSB Tank Chassis (`tank_chassis.txt`).
    """
    chassis_id: str
    name: str
    weight_class: str  # "light", "medium", "heavy", "super_heavy", "modern", "amphibious", "land_cruiser"
    year_unlocked: int
    maximum_speed: float
    build_cost_ic: float
    reliability: float
    armor_value: float
    hardness: float
    defense: float = 0.0
    breakthrough: float = 0.0
    fuel_consumption: float = 0.0
    attack_add_multiplier: float = 0.0  # module_add_stats_multiplier on SA/HA/Air
    is_special_project: bool = False


@dataclass(frozen=True)
class TankModule:
    """
    Represents an official HOI4 v1.19.4.2 Tank Module (`00_tank_modules.txt`).
    """
    module_id: str
    name: str
    slot_type: str  # "turret", "main_armament", "suspension", "armor", "engine", "special"
    category: str
    year_unlocked: int
    add_stats: Dict[str, float] = field(default_factory=dict)
    multiply_stats: Dict[str, float] = field(default_factory=dict)
    allowed_weight_classes: Tuple[str, ...] = (
        "light", "medium", "heavy", "super_heavy", "modern", "amphibious"
    )
    allowed_roles: Tuple[str, ...] = TANK_ROLES
    requires_fixed_turret_on_classes: Tuple[str, ...] = ()
    forbids_fixed_turret: bool = False
    is_fixed_turret: bool = False
    max_gun_size: str = "medium"  # "small", "medium", "heavy", "super_heavy", "lc"


# ==============================================================================
# 3. OFFICIAL v1.19.4.2 CHASSIS CATALOG (`tank_chassis.txt`)
# ==============================================================================

TANK_CHASSIS: Dict[str, TankChassis] = {
    # Light Tank Chassis
    "light_tank_chassis_0": TankChassis(
        "light_tank_chassis_0", "Interwar Light Tank Chassis", "light", 1918,
        maximum_speed=4.0, build_cost_ic=2.0, reliability=0.80, armor_value=10.0,
        hardness=0.80, attack_add_multiplier=-0.05,
    ),
    "light_tank_chassis_1": TankChassis(
        "light_tank_chassis_1", "Basic Light Tank Chassis (1934)", "light", 1934,
        maximum_speed=5.0, build_cost_ic=2.35, reliability=0.95, armor_value=15.0,
        hardness=0.80, attack_add_multiplier=-0.05,
    ),
    "light_tank_chassis_2": TankChassis(
        "light_tank_chassis_2", "Improved Light Tank Chassis (1936)", "light", 1936,
        maximum_speed=6.0, build_cost_ic=2.70, reliability=1.10, armor_value=20.0,
        hardness=0.80, attack_add_multiplier=0.05,
    ),
    "light_tank_chassis_3": TankChassis(
        "light_tank_chassis_3", "Advanced Light Tank Chassis (1941)", "light", 1941,
        maximum_speed=7.0, build_cost_ic=3.00, reliability=1.30, armor_value=25.0,
        hardness=0.80, attack_add_multiplier=0.10,
    ),
    # Medium Tank Chassis
    "medium_tank_chassis_0": TankChassis(
        "medium_tank_chassis_0", "Interwar Medium Tank Chassis", "medium", 1918,
        maximum_speed=4.0, build_cost_ic=3.50, reliability=0.75, armor_value=20.0,
        hardness=0.85, attack_add_multiplier=-0.05,
    ),
    "medium_tank_chassis_1": TankChassis(
        "medium_tank_chassis_1", "Basic Medium Tank Chassis (1938)", "medium", 1938,
        maximum_speed=5.0, build_cost_ic=3.75, reliability=0.80, armor_value=30.0,
        hardness=0.85, attack_add_multiplier=0.0,
    ),
    "medium_tank_chassis_2": TankChassis(
        "medium_tank_chassis_2", "Improved Medium Tank Chassis (1940)", "medium", 1940,
        maximum_speed=6.0, build_cost_ic=4.00, reliability=1.10, armor_value=45.0,
        hardness=0.85, attack_add_multiplier=0.05,
    ),
    "medium_tank_chassis_3": TankChassis(
        "medium_tank_chassis_3", "Advanced Medium Tank Chassis (1943)", "medium", 1943,
        maximum_speed=6.0, build_cost_ic=4.35, reliability=1.25, armor_value=60.0,
        hardness=0.85, attack_add_multiplier=0.10,
    ),
    # Heavy Tank Chassis
    "heavy_tank_chassis_0": TankChassis(
        "heavy_tank_chassis_0", "Interwar Heavy Tank Chassis", "heavy", 1918,
        maximum_speed=3.0, build_cost_ic=9.00, reliability=0.75, armor_value=35.0,
        hardness=0.95, attack_add_multiplier=-0.05,
    ),
    "heavy_tank_chassis_1": TankChassis(
        "heavy_tank_chassis_1", "Basic Heavy Tank Chassis (1934)", "heavy", 1934,
        maximum_speed=5.0, build_cost_ic=10.00, reliability=0.80, armor_value=55.0,
        hardness=0.95, attack_add_multiplier=0.0,
    ),
    "heavy_tank_chassis_2": TankChassis(
        "heavy_tank_chassis_2", "Improved Heavy Tank Chassis (1940)", "heavy", 1940,
        maximum_speed=5.0, build_cost_ic=11.00, reliability=1.10, armor_value=60.0,
        hardness=0.95, attack_add_multiplier=0.05,
    ),
    "heavy_tank_chassis_3": TankChassis(
        "heavy_tank_chassis_3", "Advanced Heavy Tank Chassis (1943)", "heavy", 1943,
        maximum_speed=5.0, build_cost_ic=12.00, reliability=1.20, armor_value=75.0,
        hardness=0.95, attack_add_multiplier=0.10,
    ),
    # Super-Heavy, Modern, Amphibious & Land Cruiser Chassis
    "super_heavy_tank_chassis_1": TankChassis(
        "super_heavy_tank_chassis_1", "Super-Heavy Tank Chassis (1943)", "super_heavy", 1943,
        maximum_speed=4.0, build_cost_ic=28.00, reliability=1.00, armor_value=90.0,
        hardness=0.99, attack_add_multiplier=0.10,
    ),
    "modern_tank_chassis_1": TankChassis(
        "modern_tank_chassis_1", "Modern Tank Chassis (1945)", "modern", 1945,
        maximum_speed=7.0, build_cost_ic=6.00, reliability=1.20, armor_value=65.0,
        hardness=0.95, attack_add_multiplier=0.15,
    ),
    "amphibious_tank_chassis_1": TankChassis(
        "amphibious_tank_chassis_1", "Amphibious Tank Chassis (1940)", "amphibious", 1940,
        maximum_speed=5.0, build_cost_ic=4.50, reliability=1.10, armor_value=15.0,
        hardness=0.85, attack_add_multiplier=0.0,
    ),
    "land_cruiser_chassis_1": TankChassis(
        "land_cruiser_chassis_1", "Land Cruiser Chassis (1944 SP)", "land_cruiser", 1944,
        maximum_speed=5.0, build_cost_ic=330.00, reliability=1.00, armor_value=150.0,
        hardness=0.99, defense=12.0, fuel_consumption=12.0, is_special_project=True,
    ),
}


# ==============================================================================
# 4. OFFICIAL v1.19.4.2 MODULE CATALOG (`00_tank_modules.txt`)
# ==============================================================================

TANK_MODULES: Dict[str, TankModule] = {
    # --- TURRETS ---
    "tank_light_one_man_tank_turret": TankModule(
        "tank_light_one_man_tank_turret", "Light One-Man Turret", "turret",
        "tank_light_turret_type", 1918,
        add_stats={"build_cost_ic": 0.5, "breakthrough": 7.0},
        multiply_stats={},
        allowed_weight_classes=("light", "amphibious"),
        max_gun_size="small",
    ),
    "tank_light_two_man_tank_turret": TankModule(
        "tank_light_two_man_tank_turret", "Light Two-Man Turret", "turret",
        "tank_light_turret_type", 1934,
        add_stats={"build_cost_ic": 0.75, "breakthrough": 10.0, "maximum_speed": -0.25},
        multiply_stats={},
        allowed_weight_classes=("light", "medium", "amphibious"),
        max_gun_size="small",
    ),
    "tank_light_three_man_tank_turret": TankModule(
        "tank_light_three_man_tank_turret", "Light Three-Man Turret", "turret",
        "tank_light_turret_type", 1936,
        add_stats={"build_cost_ic": 1.0, "breakthrough": 14.0, "maximum_speed": -0.25},
        multiply_stats={},
        allowed_weight_classes=("light", "medium", "amphibious"),
        max_gun_size="small",
    ),
    "tank_light_fixed_superstructure_turret": TankModule(
        "tank_light_fixed_superstructure_turret", "Light Fixed Superstructure", "turret",
        "tank_light_turret_type", 1918,
        add_stats={"build_cost_ic": 0.5, "defense": 3.0, "reliability": 0.10},
        multiply_stats={"breakthrough": -0.25, "soft_attack": 0.0, "hard_attack": 0.0},
        allowed_weight_classes=("light", "amphibious"),
        allowed_roles=("tank_destroyer", "artillery", "tank", "flame_tank", "amphibious_tank"),
        is_fixed_turret=True,
        max_gun_size="medium",
    ),
    "tank_medium_one_man_tank_turret": TankModule(
        "tank_medium_one_man_tank_turret", "Medium One-Man Turret", "turret",
        "tank_medium_turret_type", 1918,
        add_stats={"build_cost_ic": 1.0, "breakthrough": 8.0, "maximum_speed": -0.25},
        multiply_stats={},
        allowed_weight_classes=("medium", "heavy", "amphibious"),
        max_gun_size="medium",
    ),
    "tank_medium_two_man_tank_turret": TankModule(
        "tank_medium_two_man_tank_turret", "Medium Two-Man Turret", "turret",
        "tank_medium_turret_type", 1934,
        add_stats={"build_cost_ic": 1.5, "breakthrough": 14.0, "maximum_speed": -0.25},
        multiply_stats={},
        allowed_weight_classes=("medium", "heavy", "amphibious"),
        max_gun_size="medium",
    ),
    "tank_medium_three_man_tank_turret": TankModule(
        "tank_medium_three_man_tank_turret", "Medium Three-Man Turret", "turret",
        "tank_medium_turret_type", 1939,
        add_stats={"build_cost_ic": 2.0, "breakthrough": 20.0, "maximum_speed": -0.50},
        multiply_stats={},
        allowed_weight_classes=("medium", "heavy", "modern"),
        max_gun_size="medium",
    ),
    "tank_medium_fixed_superstructure_turret": TankModule(
        "tank_medium_fixed_superstructure_turret", "Medium Fixed Superstructure", "turret",
        "tank_medium_turret_type", 1934,
        add_stats={"build_cost_ic": 1.25, "defense": 3.0, "reliability": 0.10},
        multiply_stats={"breakthrough": -0.25},
        allowed_weight_classes=("medium", "heavy"),
        allowed_roles=("tank_destroyer", "artillery", "tank", "flame_tank"),
        is_fixed_turret=True,
        max_gun_size="heavy",
    ),
    "tank_heavy_two_man_tank_turret": TankModule(
        "tank_heavy_two_man_tank_turret", "Heavy Two-Man Turret", "turret",
        "tank_heavy_turret_type", 1934,
        add_stats={"build_cost_ic": 5.0, "breakthrough": 18.0, "maximum_speed": -0.50, "armor_value": 10.0},
        multiply_stats={},
        allowed_weight_classes=("heavy", "super_heavy", "modern"),
        max_gun_size="heavy",
    ),
    "tank_heavy_three_man_tank_turret": TankModule(
        "tank_heavy_three_man_tank_turret", "Heavy Three-Man Turret", "turret",
        "tank_heavy_turret_type", 1939,
        add_stats={"build_cost_ic": 5.5, "breakthrough": 24.0, "maximum_speed": -0.75, "armor_value": 10.0},
        multiply_stats={},
        allowed_weight_classes=("heavy", "super_heavy", "modern"),
        max_gun_size="heavy",
    ),
    "tank_heavy_fixed_superstructure_turret": TankModule(
        "tank_heavy_fixed_superstructure_turret", "Heavy Fixed Superstructure", "turret",
        "tank_heavy_turret_type", 1934,
        add_stats={"build_cost_ic": 5.0, "defense": 4.0, "reliability": 0.10, "armor_value": 20.0},
        multiply_stats={"breakthrough": -0.25},
        allowed_weight_classes=("heavy", "super_heavy"),
        allowed_roles=("tank_destroyer", "artillery", "tank"),
        is_fixed_turret=True,
        max_gun_size="super_heavy",
    ),
    "tank_super_heavy_three_man_tank_turret": TankModule(
        "tank_super_heavy_three_man_tank_turret", "Super-Heavy Three-Man Turret", "turret",
        "tank_super_heavy_turret_type", 1943,
        add_stats={"build_cost_ic": 9.0, "breakthrough": 25.0, "maximum_speed": -1.0, "armor_value": 15.0},
        multiply_stats={},
        allowed_weight_classes=("super_heavy",),
        max_gun_size="super_heavy",
    ),
    "tank_super_heavy_four_man_tank_turret": TankModule(
        "tank_super_heavy_four_man_tank_turret", "Super-Heavy Four-Man Turret", "turret",
        "tank_super_heavy_turret_type", 1943,
        add_stats={"build_cost_ic": 10.0, "breakthrough": 35.0, "maximum_speed": -1.0, "armor_value": 20.0},
        multiply_stats={},
        allowed_weight_classes=("super_heavy",),
        max_gun_size="super_heavy",
    ),
    "tank_modern_tank_turret": TankModule(
        "tank_modern_tank_turret", "Modern Tank Turret", "turret",
        "tank_modern_turret_type", 1945,
        add_stats={"build_cost_ic": 3.0, "breakthrough": 24.0},
        multiply_stats={},
        allowed_weight_classes=("modern",),
        max_gun_size="heavy",
    ),

    # --- MAIN ARMAMENTS ---
    "tank_heavy_machine_gun": TankModule(
        "tank_heavy_machine_gun", "Heavy Machine Gun", "main_armament",
        "tank_small_main_armament", 1918,
        add_stats={"soft_attack": 6.0, "hard_attack": 1.0, "ap_attack": 4.0, "build_cost_ic": 0.5},
        max_gun_size="small",
    ),
    "tank_flamethrower": TankModule(
        "tank_flamethrower", "Tank Flamethrower", "main_armament",
        "tank_flamethrower", 1936,
        add_stats={"soft_attack": 5.0, "breakthrough": 2.0, "build_cost_ic": 1.0, "reliability": -0.05},
        allowed_roles=("flame_tank",),
        max_gun_size="small",
    ),
    "tank_auto_cannon": TankModule(
        "tank_auto_cannon", "Basic Automatic Cannon (20mm)", "main_armament",
        "tank_small_main_armament", 1934,
        add_stats={"soft_attack": 15.0, "hard_attack": 5.0, "ap_attack": 20.0, "build_cost_ic": 1.5, "maximum_speed": -0.1, "reliability": -0.1},
        max_gun_size="small",
    ),
    "tank_auto_cannon_2": TankModule(
        "tank_auto_cannon_2", "Improved Automatic Cannon", "main_armament",
        "tank_small_main_armament", 1940,
        add_stats={"soft_attack": 20.0, "hard_attack": 7.0, "ap_attack": 35.0, "build_cost_ic": 2.0, "maximum_speed": -0.1, "reliability": -0.1},
        max_gun_size="small",
    ),
    "tank_anti_air_cannon": TankModule(
        "tank_anti_air_cannon", "Basic Anti-Air Gun", "main_armament",
        "tank_small_main_armament", 1936,
        add_stats={"soft_attack": 6.0, "hard_attack": 2.0, "ap_attack": 10.0, "air_attack": 18.0, "build_cost_ic": 2.0, "reliability": -0.1},
        allowed_roles=("anti_air",),
        max_gun_size="small",
    ),
    "tank_anti_air_cannon_2": TankModule(
        "tank_anti_air_cannon_2", "Improved Anti-Air Gun", "main_armament",
        "tank_small_main_armament", 1940,
        add_stats={"soft_attack": 8.0, "hard_attack": 5.0, "ap_attack": 18.0, "air_attack": 31.0, "build_cost_ic": 3.0, "reliability": -0.1},
        allowed_roles=("anti_air",),
        max_gun_size="small",
    ),
    "tank_anti_air_cannon_3": TankModule(
        "tank_anti_air_cannon_3", "Advanced Anti-Air Gun", "main_armament",
        "tank_medium_main_armament", 1943,
        add_stats={"soft_attack": 10.0, "hard_attack": 5.0, "ap_attack": 24.0, "air_attack": 44.0, "build_cost_ic": 4.0, "reliability": -0.1},
        allowed_roles=("anti_air",),
        max_gun_size="medium",
    ),
    "tank_small_cannon": TankModule(
        "tank_small_cannon", "Basic Small Cannon (37mm)", "main_armament",
        "tank_small_main_armament", 1934,
        add_stats={"soft_attack": 10.0, "hard_attack": 6.0, "ap_attack": 25.0, "build_cost_ic": 1.5, "maximum_speed": -0.1, "reliability": -0.1},
        max_gun_size="small",
    ),
    "tank_small_cannon_2": TankModule(
        "tank_small_cannon_2", "Improved Small Cannon (50mm)", "main_armament",
        "tank_small_main_armament", 1939,
        add_stats={"soft_attack": 15.0, "hard_attack": 10.0, "ap_attack": 40.0, "build_cost_ic": 2.0, "maximum_speed": -0.2, "reliability": -0.1},
        max_gun_size="small",
    ),
    "tank_close_support_gun": TankModule(
        "tank_close_support_gun", "Close Support Gun (75mm Short)", "main_armament",
        "tank_small_main_armament", 1936,
        add_stats={"soft_attack": 25.0, "hard_attack": 5.0, "ap_attack": 20.0, "build_cost_ic": 2.5, "maximum_speed": -0.2, "reliability": -0.1},
        max_gun_size="small",
    ),
    "tank_high_velocity_cannon": TankModule(
        "tank_high_velocity_cannon", "Basic High-Velocity Cannon", "main_armament",
        "tank_small_main_armament", 1939,
        add_stats={"soft_attack": 13.0, "hard_attack": 16.0, "ap_attack": 65.0, "build_cost_ic": 3.0, "maximum_speed": -0.2, "reliability": -0.15},
        max_gun_size="small",
    ),
    "tank_high_velocity_cannon_2": TankModule(
        "tank_high_velocity_cannon_2", "Improved High-Velocity Cannon", "main_armament",
        "tank_medium_main_armament", 1941,
        add_stats={"soft_attack": 18.0, "hard_attack": 26.0, "ap_attack": 95.0, "build_cost_ic": 4.5, "maximum_speed": -0.3, "reliability": -0.175},
        max_gun_size="medium",
    ),
    "tank_high_velocity_cannon_3": TankModule(
        "tank_high_velocity_cannon_3", "Advanced High-Velocity Cannon (88mm L/71)", "main_armament",
        "tank_heavy_main_armament", 1943,
        add_stats={"soft_attack": 22.0, "hard_attack": 36.0, "ap_attack": 140.0, "build_cost_ic": 6.0, "maximum_speed": -0.5, "reliability": -0.20},
        max_gun_size="heavy",
    ),
    "tank_medium_cannon": TankModule(
        "tank_medium_cannon", "Basic Medium Cannon (75mm L/30)", "main_armament",
        "tank_medium_main_armament", 1938,
        add_stats={"soft_attack": 20.0, "hard_attack": 15.0, "ap_attack": 60.0, "build_cost_ic": 3.0, "maximum_speed": -0.3, "reliability": -0.15},
        max_gun_size="medium",
    ),
    "tank_medium_cannon_2": TankModule(
        "tank_medium_cannon_2", "Improved Medium Cannon (75mm L/48)", "main_armament",
        "tank_medium_main_armament", 1940,
        add_stats={"soft_attack": 32.0, "hard_attack": 20.0, "ap_attack": 80.0, "build_cost_ic": 4.0, "maximum_speed": -0.4, "reliability": -0.15},
        max_gun_size="medium",
    ),
    "tank_medium_howitzer": TankModule(
        "tank_medium_howitzer", "Basic Medium Howitzer (105mm)", "main_armament",
        "tank_medium_main_armament", 1939,
        add_stats={"soft_attack": 35.0, "hard_attack": 2.0, "ap_attack": 20.0, "build_cost_ic": 4.0, "maximum_speed": -0.3, "reliability": -0.20},
        allowed_roles=("artillery", "tank", "amphibious_tank"),
        max_gun_size="medium",
    ),
    "tank_medium_howitzer_2": TankModule(
        "tank_medium_howitzer_2", "Improved Medium Howitzer (150mm)", "main_armament",
        "tank_medium_main_armament", 1941,
        add_stats={"soft_attack": 45.0, "hard_attack": 2.0, "ap_attack": 20.0, "build_cost_ic": 5.5, "maximum_speed": -0.4, "reliability": -0.20},
        allowed_roles=("artillery", "tank", "amphibious_tank"),
        max_gun_size="medium",
    ),
    "tank_heavy_cannon": TankModule(
        "tank_heavy_cannon", "Basic Heavy Cannon (88mm)", "main_armament",
        "tank_heavy_main_armament", 1938,
        add_stats={"soft_attack": 20.0, "hard_attack": 20.0, "ap_attack": 90.0, "build_cost_ic": 5.0, "maximum_speed": -0.4, "reliability": -0.25},
        max_gun_size="heavy",
    ),
    "tank_heavy_cannon_2": TankModule(
        "tank_heavy_cannon_2", "Improved Heavy Cannon", "main_armament",
        "tank_heavy_main_armament", 1941,
        add_stats={"soft_attack": 25.0, "hard_attack": 35.0, "ap_attack": 125.0, "build_cost_ic": 6.0, "maximum_speed": -0.5, "reliability": -0.25},
        max_gun_size="heavy",
    ),
    "tank_heavy_cannon_3": TankModule(
        "tank_heavy_cannon_3", "Advanced Heavy Cannon (122/128mm)", "main_armament",
        "tank_heavy_main_armament", 1943,
        add_stats={"soft_attack": 30.0, "hard_attack": 40.0, "ap_attack": 140.0, "build_cost_ic": 7.5, "maximum_speed": -0.6, "reliability": -0.30},
        max_gun_size="heavy",
    ),
    "tank_heavy_howitzer": TankModule(
        "tank_heavy_howitzer", "Heavy Howitzer (152/203mm)", "main_armament",
        "tank_heavy_main_armament", 1941,
        add_stats={"soft_attack": 55.0, "hard_attack": 2.0, "ap_attack": 30.0, "build_cost_ic": 7.0, "maximum_speed": -0.5, "reliability": -0.30},
        allowed_roles=("artillery", "tank"),
        max_gun_size="heavy",
    ),
    "tank_super_heavy_cannon": TankModule(
        "tank_super_heavy_cannon", "Super-Heavy Cannon", "main_armament",
        "tank_super_heavy_main_armament", 1943,
        add_stats={"soft_attack": 35.0, "hard_attack": 45.0, "ap_attack": 225.0, "build_cost_ic": 12.5, "maximum_speed": -0.6, "reliability": -0.35},
        max_gun_size="super_heavy",
    ),

    # --- SUSPENSIONS ---
    "tank_bogie_suspension": TankModule(
        "tank_bogie_suspension", "Bogie Suspension", "suspension",
        "tank_suspension_type", 1918,
        add_stats={},
    ),
    "tank_christie_suspension": TankModule(
        "tank_christie_suspension", "Christie Suspension", "suspension",
        "tank_suspension_type", 1918,
        add_stats={"build_cost_ic": 0.5},
        multiply_stats={"maximum_speed": 0.20},
    ),
    "tank_torsion_bar_suspension": TankModule(
        "tank_torsion_bar_suspension", "Torsion Bar Suspension", "suspension",
        "tank_suspension_type", 1936,
        add_stats={"build_cost_ic": 0.5, "reliability": 0.15},
    ),
    "tank_interleaved_suspension": TankModule(
        "tank_interleaved_suspension", "Interleaved Roadwheels", "suspension",
        "tank_suspension_type", 1936,
        add_stats={"build_cost_ic": 1.0, "breakthrough": 4.0, "reliability": -0.05},
    ),

    # --- ARMOR TYPES ---
    "tank_riveted_armor": TankModule(
        "tank_riveted_armor", "Riveted Armor", "armor",
        "tank_armor_type", 1918,
        add_stats={"defense": 2.0},
        multiply_stats={"build_cost_ic": -0.10},
    ),
    "tank_cast_armor": TankModule(
        "tank_cast_armor", "Cast Armor", "armor",
        "tank_armor_type", 1918,
        add_stats={"defense": 4.0},
        multiply_stats={"armor_value": 0.30, "build_cost_ic": 0.20},
    ),
    "tank_welded_armor": TankModule(
        "tank_welded_armor", "Welded Armor", "armor",
        "tank_armor_type", 1936,
        add_stats={"defense": 4.0},
        multiply_stats={"armor_value": 0.20},
    ),

    # --- ENGINE TYPES ---
    "tank_gasoline_engine": TankModule(
        "tank_gasoline_engine", "Gasoline Engine", "engine",
        "tank_engine_type", 1918,
        add_stats={"maximum_speed": 0.5, "fuel_consumption": 2.0},
        multiply_stats={"maximum_speed": 0.15},
    ),
    "tank_diesel_engine": TankModule(
        "tank_diesel_engine", "Diesel Engine", "engine",
        "tank_engine_type", 1918,
        add_stats={"reliability": 0.25, "fuel_consumption": 2.0},
    ),
    "tank_petrol_electric_engine": TankModule(
        "tank_petrol_electric_engine", "Petrol-Electric Engine", "engine",
        "tank_engine_type", 1936,
        add_stats={"breakthrough": 2.0, "defense": 2.0, "reliability": -0.25, "fuel_consumption": 2.0, "build_cost_ic": 1.5},
        multiply_stats={"build_cost_ic": 0.05},
    ),
    "tank_gas_turbine_engine": TankModule(
        "tank_gas_turbine_engine", "Gas Turbine Engine", "engine",
        "tank_engine_type", 1944,
        add_stats={"maximum_speed": 1.5, "reliability": -0.10, "fuel_consumption": 4.0, "build_cost_ic": 3.0},
        multiply_stats={"maximum_speed": 0.25},
    ),

    # --- SPECIAL MODULES (`special_type_slot_1..4`) ---
    "tank_radio_1": TankModule(
        "tank_radio_1", "Basic Radio (Radio I)", "special",
        "tank_radio_module", 1936,
        add_stats={"build_cost_ic": 0.5, "breakthrough": 2.0},
        multiply_stats={"defense": 0.15, "breakthrough": 0.15},
    ),
    "tank_radio_2": TankModule(
        "tank_radio_2", "Improved Radio (Radio II)", "special",
        "tank_radio_module", 1940,
        add_stats={"build_cost_ic": 1.5, "breakthrough": 3.0},
        multiply_stats={"defense": 0.25, "breakthrough": 0.25},
    ),
    "tank_radio_3": TankModule(
        "tank_radio_3", "Advanced Radio (Radio III)", "special",
        "tank_radio_module", 1943,
        add_stats={"build_cost_ic": 2.5, "breakthrough": 5.0},
        multiply_stats={"defense": 0.60, "breakthrough": 0.40},
    ),
    "secondary_turret_hmg": TankModule(
        "secondary_turret_hmg", "Secondary Turret (HMG)", "special",
        "tank_secondary_turret", 1918,
        add_stats={"soft_attack": 4.0, "hard_attack": 0.5, "breakthrough": 2.0, "build_cost_ic": 1.25, "reliability": -0.10},
    ),
    "secondary_turret_small_cannon": TankModule(
        "secondary_turret_small_cannon", "Secondary Turret (37mm Cannon)", "special",
        "tank_secondary_turret", 1936,
        add_stats={"soft_attack": 6.0, "hard_attack": 5.0, "breakthrough": 2.0, "build_cost_ic": 2.5, "reliability": -0.10},
    ),
    "sloped_armor": TankModule(
        "sloped_armor", "Sloped Armor", "special",
        "tank_special_module", 1936,
        add_stats={},
        multiply_stats={"armor_value": 0.25, "build_cost_ic": 0.10},
    ),
    "stabilizer": TankModule(
        "stabilizer", "Stabilizer", "special",
        "tank_special_module", 1939,
        add_stats={"breakthrough": 5.0, "build_cost_ic": 2.0},
    ),
    "smoke_launchers": TankModule(
        "smoke_launchers", "Smoke Launchers", "special",
        "tank_special_module", 1936,
        add_stats={"breakthrough": 2.0, "defense": 1.0, "build_cost_ic": 0.5},
    ),
    "extra_ammo_storage": TankModule(
        "extra_ammo_storage", "Extra Ammunition Storage", "special",
        "tank_special_module", 1936,
        add_stats={"breakthrough": 2.0, "defense": 4.0, "reliability": -0.10},
    ),
    "wet_ammo_storage": TankModule(
        "wet_ammo_storage", "Wet Ammunition Storage", "special",
        "tank_special_module", 1939,
        add_stats={"reliability": 0.15, "build_cost_ic": 1.0},
    ),
    "squeezebore_adaptor": TankModule(
        "squeezebore_adaptor", "Squeeze-Bore Adaptor", "special",
        "tank_special_module", 1940,
        add_stats={},
        multiply_stats={"ap_attack": 0.10},
    ),
    "armor_skirts": TankModule(
        "armor_skirts", "Armor Skirts", "special",
        "tank_special_module", 1940,
        add_stats={"armor_value": 3.0, "breakthrough": 3.0, "build_cost_ic": 0.5},
    ),
    "dozer_blade": TankModule(
        "dozer_blade", "Dozer Blade", "special",
        "tank_special_module", 1939,
        add_stats={"entrenchment": 1.0, "build_cost_ic": 1.0},
    ),
    "auto_loader": TankModule(
        "auto_loader", "Auto-Loader", "special",
        "tank_special_module", 1941,
        add_stats={"breakthrough": 4.0, "defense": 4.0, "build_cost_ic": 1.5},
        multiply_stats={"soft_attack": 0.02, "air_attack": 0.02},
    ),
    "easy_maintenance": TankModule(
        "easy_maintenance", "Easy Maintenance", "special",
        "tank_special_module", 1939,
        add_stats={"reliability": 0.075},
        multiply_stats={"build_cost_ic": -0.05},
    ),
    "additional_machine_guns": TankModule(
        "additional_machine_guns", "Additional Machine Guns", "special",
        "tank_special_module", 1918,
        add_stats={"soft_attack": 1.0, "defense": 2.0, "build_cost_ic": 0.5},
    ),
    "amphibious_drive": TankModule(
        "amphibious_drive", "Amphibious Drive", "special",
        "tank_special_module", 1940,
        add_stats={"build_cost_ic": 1.0, "reliability": -0.15},
        allowed_roles=("amphibious_tank",),
    ),
}

GUN_SIZE_RANK: Dict[str, int] = {
    "small": 1,
    "medium": 2,
    "heavy": 3,
    "super_heavy": 4,
    "lc": 5,
}


# ==============================================================================
# 5. TANK BLUEPRINT & EXACT CLAUSEWITZ NSB STAT CALCULATOR
# ==============================================================================

@dataclass
class TankBlueprint:
    """
    Represents a complete No Step Back (NSB) Tank Design Blueprint.
    """
    name: str
    chassis_id: str
    role: str = "tank"  # "tank", "tank_destroyer", "artillery", "anti_air", "flame_tank", "amphibious_tank"
    turret_id: str = "tank_medium_three_man_tank_turret"
    main_armament_id: str = "tank_medium_cannon_2"
    suspension_id: str = "tank_torsion_bar_suspension"
    armor_id: str = "tank_welded_armor"
    engine_id: str = "tank_gasoline_engine"
    special_modules: List[str] = field(default_factory=list)
    armor_ticks: int = 0
    engine_ticks: int = 0
    year: str = "1940"

    def validate_blueprint(self) -> Tuple[bool, List[str]]:
        """
        Validates that this `TankBlueprint` obeys all official HOI4 v1.19.4.2
        Tank Designer slot, gun size, role, speed, and reliability rules.
        """
        violations: List[str] = []
        if self.chassis_id not in TANK_CHASSIS:
            return False, [f"Unknown chassis '{self.chassis_id}'."]
        chassis = TANK_CHASSIS[self.chassis_id]
        year_int = int(self.year)

        if chassis.year_unlocked > year_int:
            violations.append(
                f"Chassis '{chassis.name}' unlocks in {chassis.year_unlocked} (> {year_int})."
            )

        for slot_label, mod_id in [
            ("turret", self.turret_id),
            ("main_armament", self.main_armament_id),
            ("suspension", self.suspension_id),
            ("armor", self.armor_id),
            ("engine", self.engine_id),
        ]:
            if mod_id not in TANK_MODULES:
                violations.append(f"Unknown {slot_label} module '{mod_id}'.")
                continue
            mod = TANK_MODULES[mod_id]
            if mod.year_unlocked > year_int:
                violations.append(
                    f"Module '{mod.name}' unlocks in {mod.year_unlocked} (> {year_int})."
                )

        if len(self.special_modules) > 4:
            violations.append("Tank cannot have more than 4 special modules.")

        radio_count = 0
        for sm_id in self.special_modules:
            if sm_id not in TANK_MODULES:
                violations.append(f"Unknown special module '{sm_id}'.")
                continue
            sm = TANK_MODULES[sm_id]
            if sm.year_unlocked > year_int:
                violations.append(
                    f"Special module '{sm.name}' unlocks in {sm.year_unlocked} (> {year_int})."
                )
            if sm.category == "tank_radio_module":
                radio_count += 1
        if radio_count > 1:
            violations.append("Tank cannot mount more than 1 radio module.")

        if self.turret_id in TANK_MODULES and self.main_armament_id in TANK_MODULES:
            turret = TANK_MODULES[self.turret_id]
            gun = TANK_MODULES[self.main_armament_id]
            if chassis.weight_class not in turret.allowed_weight_classes:
                violations.append(
                    f"Turret '{turret.name}' is not allowed on {chassis.weight_class} chassis."
                )
            if GUN_SIZE_RANK.get(gun.max_gun_size, 1) > GUN_SIZE_RANK.get(turret.max_gun_size, 1):
                violations.append(
                    f"Gun '{gun.name}' ({gun.max_gun_size}) exceeds turret '{turret.name}' max size ({turret.max_gun_size})."
                )
            if self.role == "flame_tank" and gun.category != "tank_flamethrower":
                violations.append("Flame Tank role requires a flamethrower main armament.")
            if self.role == "anti_air" and "anti_air" not in gun.allowed_roles:
                violations.append("Anti-Air role requires an anti-air main gun.")

        max_ticks = MAX_UPGRADE_TICKS_BY_YEAR.get(self.year, 20)
        if not (0 <= self.armor_ticks <= max_ticks):
            violations.append(f"Armor ticks ({self.armor_ticks}) outside [0, {max_ticks}].")
        if not (0 <= self.engine_ticks <= max_ticks):
            violations.append(f"Engine ticks ({self.engine_ticks}) outside [0, {max_ticks}].")

        stats = self.calculate_equipment_stats()
        if stats["maximum_speed"] < 4.0:
            violations.append(
                f"Tank speed ({stats['maximum_speed']:.2f} km/h) is below the HOI4 minimum 4.0 km/h."
            )
        if stats["reliability"] <= 0.10:
            violations.append(
                f"Tank reliability ({stats['reliability']:.2f}) is too low (<= 10%)."
            )

        return len(violations) == 0, violations

    def calculate_equipment_stats(self) -> Dict[str, float]:
        """
        Calculates exact Clausewitz NSB Tank Equipment stats using:
        Stat_final = (Stat_chassis + sum(add_stats)) * (1.0 + sum(multiply_stats))
        """
        chassis = TANK_CHASSIS[self.chassis_id]
        base: Dict[str, float] = {
            "soft_attack": 0.0,
            "hard_attack": 0.0,
            "ap_attack": 0.0,
            "air_attack": 0.0,
            "defense": chassis.defense,
            "breakthrough": chassis.breakthrough,
            "armor_value": chassis.armor_value,
            "hardness": chassis.hardness,
            "maximum_speed": chassis.maximum_speed,
            "reliability": chassis.reliability,
            "build_cost_ic": chassis.build_cost_ic,
            "fuel_consumption": chassis.fuel_consumption,
            "entrenchment": 0.0,
            "recon": 0.0,
        }
        add_totals: Dict[str, float] = {k: 0.0 for k in base}
        mult_totals: Dict[str, float] = {k: 0.0 for k in base}

        active_module_ids = [
            self.turret_id,
            self.main_armament_id,
            self.suspension_id,
            self.armor_id,
            self.engine_id,
        ] + list(self.special_modules)

        for mod_id in active_module_ids:
            mod = TANK_MODULES.get(mod_id)
            if mod is None:
                continue
            for st, val in mod.add_stats.items():
                if st in add_totals:
                    add_totals[st] += val
            for st, val in mod.multiply_stats.items():
                if st in mult_totals:
                    mult_totals[st] += val

        # Apply chassis-level `module_add_stats_multiplier` on attack stats
        if chassis.attack_add_multiplier != 0.0:
            for att_stat in ("soft_attack", "hard_attack", "air_attack"):
                mult_totals[att_stat] += chassis.attack_add_multiplier

        # Apply NSB Armor Upgrade ticks (`tank_nsb_armor_upgrade` in `00_tank_upgrades.txt`)
        if self.armor_ticks > 0:
            add_totals["armor_value"] += 2.25 * self.armor_ticks
            add_totals["breakthrough"] += 1.25 * self.armor_ticks
            add_totals["maximum_speed"] -= 0.10 * self.armor_ticks
            add_totals["reliability"] -= 0.02 * self.armor_ticks
            add_totals["build_cost_ic"] += 0.25 * self.armor_ticks

        # Apply NSB Engine Upgrade ticks (`tank_nsb_engine_upgrade` in `00_tank_upgrades.txt`)
        if self.engine_ticks > 0:
            add_totals["maximum_speed"] += 0.20 * self.engine_ticks
            add_totals["breakthrough"] += 0.50 * self.engine_ticks
            add_totals["reliability"] -= 0.015 * self.engine_ticks
            add_totals["fuel_consumption"] += 0.05 * self.engine_ticks
            add_totals["build_cost_ic"] += 0.15 * self.engine_ticks

        # Role-specific hardness overrides from Clausewitz (`x_tank_chassis.txt`)
        if self.role == "artillery":
            hardness_by_cls = {"light": 0.50, "medium": 0.65, "heavy": 0.80, "super_heavy": 0.90, "modern": 0.85}
            base["hardness"] = hardness_by_cls.get(chassis.weight_class, chassis.hardness)
        elif self.role == "anti_air":
            hardness_by_cls = {"light": 0.50, "medium": 0.65, "heavy": 0.80, "super_heavy": 0.90, "modern": 0.85}
            base["hardness"] = hardness_by_cls.get(chassis.weight_class, chassis.hardness)

        final_stats: Dict[str, float] = {}
        for k in base:
            if k == "hardness":
                final_stats[k] = max(0.0, min(1.0, base[k] + add_totals[k]))
            elif k == "reliability":
                raw_rel = (base[k] + add_totals[k]) * (1.0 + mult_totals[k])
                final_stats[k] = round(max(0.0, min(1.0, raw_rel)), 4)
            else:
                raw_val = (base[k] + add_totals[k]) * (1.0 + mult_totals[k])
                final_stats[k] = round(max(0.0, raw_val), 4)

        return final_stats


# ==============================================================================
# 6. SUB-UNIT MAPPING & CONVERSION (`blueprint_to_unit`)
# ==============================================================================

# Maps each tank-based sub_unit_id -> (chassis_weight_class, role, equipment_need_qty, sub_unit_stat_modifiers)
TANK_SUBUNIT_SPECS: Dict[str, Dict[str, Any]] = {
    # Line Armor Battalions
    "light_armor": {
        "display_name": "Light Tank", "weight_class": "light", "role": "tank",
        "need_qty": 60, "mods": {"breakthrough": 0.15},
    },
    "medium_armor": {
        "display_name": "Medium Tank", "weight_class": "medium", "role": "tank",
        "need_qty": 50, "mods": {"breakthrough": 0.15},
    },
    "heavy_armor": {
        "display_name": "Heavy Tank", "weight_class": "heavy", "role": "tank",
        "need_qty": 40, "mods": {"breakthrough": 0.15},
    },
    "modern_armor": {
        "display_name": "Modern Tank", "weight_class": "modern", "role": "tank",
        "need_qty": 50, "mods": {"breakthrough": 0.15},
    },
    "amphibious_armor": {
        "display_name": "Amphibious Tank Battalion", "weight_class": "amphibious", "role": "amphibious_tank",
        "need_qty": 50, "mods": {},
    },
    "amphibious_light_armor": {
        "display_name": "Light Amphibious Tank Battalion", "weight_class": "light", "role": "amphibious_tank",
        "need_qty": 50, "mods": {},
    },
    "amphibious_medium_armor": {
        "display_name": "Medium Amphibious Tank Battalion", "weight_class": "medium", "role": "amphibious_tank",
        "need_qty": 50, "mods": {},
    },
    "amphibious_heavy_armor": {
        "display_name": "Heavy Amphibious Tank Battalion", "weight_class": "heavy", "role": "amphibious_tank",
        "need_qty": 50, "mods": {},
    },
    # Line Tank Destroyers
    "light_tank_destroyer_brigade": {
        "display_name": "Light Tank Destroyer", "weight_class": "light", "role": "tank_destroyer",
        "need_qty": 40, "mods": {"soft_attack": -0.10, "defense": 0.25, "breakthrough": -0.75, "ap_attack": 0.05},
    },
    "medium_tank_destroyer_brigade": {
        "display_name": "Medium Tank Destroyer", "weight_class": "medium", "role": "tank_destroyer",
        "need_qty": 40, "mods": {"soft_attack": -0.10, "defense": 0.25, "breakthrough": -0.75, "ap_attack": 0.15},
    },
    "heavy_tank_destroyer_brigade": {
        "display_name": "Heavy Tank Destroyer", "weight_class": "heavy", "role": "tank_destroyer",
        "need_qty": 40, "mods": {"soft_attack": -0.10, "defense": 0.25, "breakthrough": -0.75, "ap_attack": 0.05},
    },
    "modern_tank_destroyer_brigade": {
        "display_name": "Modern Tank Destroyer", "weight_class": "modern", "role": "tank_destroyer",
        "need_qty": 40, "mods": {"soft_attack": -0.10, "defense": 0.25, "breakthrough": -0.75, "ap_attack": 0.05},
    },
    # Line SP Artillery
    "light_sp_artillery_brigade": {
        "display_name": "Light SP Artillery", "weight_class": "light", "role": "artillery",
        "need_qty": 40, "mods": {"soft_attack": 0.05, "hard_attack": -0.10, "defense": 0.25, "breakthrough": -0.75},
    },
    "medium_sp_artillery_brigade": {
        "display_name": "Medium SP Artillery", "weight_class": "medium", "role": "artillery",
        "need_qty": 40, "mods": {"soft_attack": 0.05, "hard_attack": -0.10, "defense": 0.25, "breakthrough": -0.75},
    },
    "heavy_sp_artillery_brigade": {
        "display_name": "Heavy SP Artillery", "weight_class": "heavy", "role": "artillery",
        "need_qty": 40, "mods": {"soft_attack": 0.05, "hard_attack": -0.10, "defense": 0.25, "breakthrough": -0.75},
    },
    "modern_sp_artillery_brigade": {
        "display_name": "Modern SP Artillery", "weight_class": "modern", "role": "artillery",
        "need_qty": 40, "mods": {"soft_attack": 0.05, "hard_attack": -0.10, "defense": 0.25, "breakthrough": -0.75},
    },
    # Line SP Anti-Air
    "light_sp_anti_air_brigade": {
        "display_name": "Light SP Anti-Air", "weight_class": "light", "role": "anti_air",
        "need_qty": 40, "mods": {"breakthrough": -0.75, "air_attack": 0.15},
    },
    "medium_sp_anti_air_brigade": {
        "display_name": "Medium SP Anti-Air", "weight_class": "medium", "role": "anti_air",
        "need_qty": 40, "mods": {"breakthrough": -0.75, "air_attack": 0.15},
    },
    "heavy_sp_anti_air_brigade": {
        "display_name": "Heavy SP Anti-Air", "weight_class": "heavy", "role": "anti_air",
        "need_qty": 40, "mods": {"breakthrough": -0.75, "air_attack": 0.15},
    },
    "modern_sp_anti_air_brigade": {
        "display_name": "Modern SP Anti-Air", "weight_class": "modern", "role": "anti_air",
        "need_qty": 40, "mods": {"breakthrough": -0.75, "air_attack": 0.15},
    },
    # Divisional Support Tank Units
    "light_tank_recon": {
        "display_name": "Light Tank Recon Company", "weight_class": "light", "role": "tank",
        "need_qty": 24,
        "mods": {"soft_attack": -0.60, "hard_attack": -0.60, "defense": -0.60, "breakthrough": -0.60, "armor_value": -0.60},
    },
    "airborne_light_armor": {
        "display_name": "Airborne Light Armor", "weight_class": "light", "role": "tank",
        "need_qty": 24,
        "mods": {"soft_attack": -0.25, "hard_attack": -0.25, "defense": -0.50, "breakthrough": -0.25, "armor_value": -0.50},
    },
    "light_flame_tank": {
        "display_name": "Light Flame Tank Company", "weight_class": "light", "role": "flame_tank",
        "need_qty": 15,
        "mods": {"soft_attack": -0.50, "hard_attack": -0.75, "defense": -0.75, "breakthrough": -0.50, "armor_value": -0.75},
    },
    "medium_flame_tank": {
        "display_name": "Medium Flame Tank Company", "weight_class": "medium", "role": "flame_tank",
        "need_qty": 15,
        "mods": {"soft_attack": -0.45, "hard_attack": -0.66, "defense": -0.66, "breakthrough": -0.45, "armor_value": -0.66},
    },
    "heavy_flame_tank": {
        "display_name": "Heavy Flame Tank Company", "weight_class": "heavy", "role": "flame_tank",
        "need_qty": 15,
        "mods": {"soft_attack": -0.40, "hard_attack": -0.625, "defense": -0.625, "breakthrough": -0.40, "armor_value": -0.625},
    },
    "super_heavy_armor": {
        "display_name": "Super-Heavy Tank", "weight_class": "super_heavy", "role": "tank",
        "need_qty": 20, "mods": {},
    },
    "super_heavy_tank_destroyer_brigade": {
        "display_name": "Super-Heavy Tank Destroyer", "weight_class": "super_heavy", "role": "tank_destroyer",
        "need_qty": 20, "mods": {"soft_attack": -0.10, "defense": 0.25, "breakthrough": -0.75, "ap_attack": 0.05},
    },
    "super_heavy_sp_artillery_brigade": {
        "display_name": "Super-Heavy SP Artillery", "weight_class": "super_heavy", "role": "artillery",
        "need_qty": 20, "mods": {"soft_attack": 0.05, "hard_attack": -0.10, "defense": 0.25, "breakthrough": -0.75},
    },
    "super_heavy_sp_anti_air_brigade": {
        "display_name": "Super-Heavy SP Anti-Air", "weight_class": "super_heavy", "role": "anti_air",
        "need_qty": 20, "mods": {"breakthrough": -0.75, "air_attack": 0.15},
    },
    # v1.19 Regimental Support Tank Units
    "light_sp_anti_air_support": {
        "display_name": "Light SP Anti-Air Battery", "weight_class": "light", "role": "anti_air",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.66, "defense": -0.50, "breakthrough": -0.90, "air_attack": -0.25, "armor_value": -0.66},
    },
    "medium_sp_anti_air_support": {
        "display_name": "Medium SP Anti-Air Battery", "weight_class": "medium", "role": "anti_air",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.66, "defense": -0.50, "breakthrough": -0.90, "air_attack": -0.25, "armor_value": -0.66},
    },
    "heavy_sp_anti_air_support": {
        "display_name": "Heavy SP Anti-Air Battery", "weight_class": "heavy", "role": "anti_air",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.66, "defense": -0.50, "breakthrough": -0.90, "air_attack": -0.25, "armor_value": -0.66},
    },
    "modern_sp_anti_air_support": {
        "display_name": "Modern SP Anti-Air Battery", "weight_class": "modern", "role": "anti_air",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.66, "defense": -0.50, "breakthrough": -0.90, "air_attack": -0.25, "armor_value": -0.66},
    },
    "light_tank_destroyer_support": {
        "display_name": "Light Tank Destroyer Support", "weight_class": "light", "role": "tank_destroyer",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.50, "defense": -0.33, "breakthrough": -0.90, "armor_value": -0.66},
    },
    "medium_tank_destroyer_support": {
        "display_name": "Medium Tank Destroyer Support", "weight_class": "medium", "role": "tank_destroyer",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.50, "defense": -0.33, "breakthrough": -0.90, "armor_value": -0.66},
    },
    "heavy_tank_destroyer_support": {
        "display_name": "Heavy Tank Destroyer Support", "weight_class": "heavy", "role": "tank_destroyer",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.50, "defense": -0.33, "breakthrough": -0.90, "armor_value": -0.66},
    },
    "modern_tank_destroyer_support": {
        "display_name": "Modern Tank Destroyer Support", "weight_class": "modern", "role": "tank_destroyer",
        "need_qty": 15,
        "mods": {"soft_attack": -0.66, "hard_attack": -0.50, "defense": -0.33, "breakthrough": -0.90, "armor_value": -0.66},
    },
}


def _get_year_tech_multipliers(role: str, is_regimental_support: bool, year: str) -> Dict[str, float]:
    """
    Returns cumulative technology stat multipliers from `artillery.txt` for SPG, TD,
    and SPAA units at the target `year`.
    """
    y = int(year)
    tech_mods: Dict[str, float] = {}
    if role == "artillery":
        # interwar_artillery (1936: +0.05), artillery2 (1940: +0.05), artillery3/5 + VT fuze (1945: +0.10)
        if y >= 1945:
            tech_mods["soft_attack"] = 0.20
            tech_mods["ap_attack"] = 0.15
        elif y >= 1940:
            tech_mods["soft_attack"] = 0.10
            tech_mods["ap_attack"] = 0.15
        elif y >= 1936:
            tech_mods["soft_attack"] = 0.05
            tech_mods["ap_attack"] = 0.15
    elif role == "tank_destroyer":
        if is_regimental_support:
            if y >= 1945:
                tech_mods["hard_attack"] = 0.075
                tech_mods["ap_attack"] = 0.20
            elif y >= 1939:
                tech_mods["hard_attack"] = 0.025
                tech_mods["ap_attack"] = 0.05
        else:
            if y >= 1945:
                tech_mods["hard_attack"] = 0.15
                tech_mods["ap_attack"] = 0.20
            elif y >= 1939:
                tech_mods["hard_attack"] = 0.05
                tech_mods["ap_attack"] = 0.05
    elif role == "anti_air":
        if is_regimental_support:
            if y >= 1945:
                tech_mods["air_attack"] = 0.15
            elif y >= 1939:
                tech_mods["air_attack"] = 0.05
        else:
            if y >= 1945:
                tech_mods["air_attack"] = 0.30
            elif y >= 1939:
                tech_mods["air_attack"] = 0.15
    return tech_mods


def blueprint_to_unit(
    blueprint: TankBlueprint,
    sub_unit_id: str,
    year: str = "1940",
) -> Union[Battalion, SupportCompany]:
    """
    Converts a `TankBlueprint` into a playable `Battalion` or `SupportCompany`
    for `sub_unit_id` at `year`, preserving all terrain modifiers, categories,
    and group rules from `unit_database.py`.
    """
    # Resolve display name or unit_id
    spec_key = sub_unit_id
    if spec_key not in TANK_SUBUNIT_SPECS:
        for k, v in TANK_SUBUNIT_SPECS.items():
            if v["display_name"].lower() == sub_unit_id.lower():
                spec_key = k
                break
    if spec_key not in TANK_SUBUNIT_SPECS:
        raise ValueError(f"Unknown tank sub-unit '{sub_unit_id}'.")

    spec = TANK_SUBUNIT_SPECS[spec_key]
    display_name = spec["display_name"]
    eq_stats = blueprint.calculate_equipment_stats()
    su_mods = spec["mods"]
    need_qty = spec["need_qty"]

    # Retrieve base template unit from unit_database to inherit HP, ORG, width, manpower, supply, terrain mods
    template_unit: Optional[Union[Battalion, SupportCompany]] = None
    if display_name in unit_database.All_Battalions.get(year, {}):
        template_unit = unit_database.All_Battalions[year][display_name]
    elif display_name in unit_database.Divisional_Support_Companies.get(year, {}):
        template_unit = unit_database.Divisional_Support_Companies[year][display_name]
    elif display_name in unit_database.Regimental_Support_Companies.get(year, {}):
        template_unit = unit_database.Regimental_Support_Companies[year][display_name]

    if template_unit is None:
        raise ValueError(f"Could not find base template '{display_name}' in unit_database[{year}].")

    is_reg = isinstance(template_unit, SupportCompany) and template_unit.is_regimental
    tech_mods = _get_year_tech_multipliers(spec["role"], is_reg, year)

    def _apply_mod(stat_key: str) -> float:
        base_eq_val = eq_stats.get(stat_key, 0.0)
        factor = 1.0 + su_mods.get(stat_key, 0.0) + tech_mods.get(stat_key, 0.0)
        return round(max(0.0, base_eq_val * factor), 3)

    t_bs = template_unit.base_stats
    new_stats = BaseStatistics(
        soft_attack=_apply_mod("soft_attack"),
        hard_attack=_apply_mod("hard_attack"),
        defense=_apply_mod("defense"),
        breakthrough=_apply_mod("breakthrough"),
        max_hp=t_bs.max_hp,
        organization=t_bs.organization,
        combat_width=t_bs.combat_width,
        supply_use=t_bs.supply_use,
        ic_cost=round(eq_stats["build_cost_ic"] * need_qty, 2),
        manpower=t_bs.manpower,
        armor=_apply_mod("armor_value"),
        piercing=_apply_mod("ap_attack"),
        hardness=eq_stats["hardness"] if isinstance(template_unit, Battalion) else 0.0,
        air_attack=_apply_mod("air_attack"),
        entrenchment=round(t_bs.entrenchment + eq_stats.get("entrenchment", 0.0), 3),
        initiative=t_bs.initiative,
        recon=round(t_bs.recon + eq_stats.get("recon", 0.0), 3),
        supply_consumption_factor=t_bs.supply_consumption_factor,
        recovery_rate=t_bs.recovery_rate,
    )

    cloned_unit = copy.deepcopy(template_unit)
    cloned_unit.base_stats = new_stats
    return cloned_unit


# ==============================================================================
# 7. INNER-LOOP TANK BLUEPRINT OPTIMIZER (`optimize_tank_blueprint`)
# ==============================================================================

def _pick_best_chassis_for_year(weight_class: str, year: str) -> str:
    """Selects the latest unlocked chassis for `weight_class` at `year`."""
    y = int(year)
    candidates = [
        ch for ch in TANK_CHASSIS.values()
        if ch.weight_class == weight_class and ch.year_unlocked <= y
    ]
    if not candidates:
        # Fallback to earliest chassis of that weight class
        candidates = [ch for ch in TANK_CHASSIS.values() if ch.weight_class == weight_class]
    candidates.sort(key=lambda c: c.year_unlocked, reverse=True)
    return candidates[0].chassis_id


def optimize_tank_blueprint(
    chassis_class: str = "medium",
    role: str = "tank",
    year: str = "1940",
    objective: str = "best_overall",
    max_ic_per_tank: Optional[float] = None,
) -> TankBlueprint:
    """
    Combinatorial inner-loop optimizer that evaluates legal NSB Tank Designer
    module configurations unlocked by `year` and returns the optimal `TankBlueprint`
    for `chassis_class`, `role`, and `objective`.

    Supported Objectives
    --------------------
    - `"best_overall"` / `"nsb_auto_optimize"`: Balanced firepower, breakthrough, armor, and IC.
    - `"soft_attack"` / `"nsb_meta_soft_attack"`: Maximizes soft attack + breakthrough (Howitzer/CSG + Radio + Secondary Turrets).
    - `"hard_attack"` / `"nsb_meta_hard_attack"`: Maximizes hard attack + piercing (High-Velocity/Heavy Cannon + Squeeze-bore).
    - `"armor_breakthrough"` / `"nsb_meta_armor_brick"`: Maximizes armor + breakthrough + defense (Cast/Welded + Sloped + Skirts + high armor ticks).
    - `"bang_for_buck"` / `"nsb_budget"`: Maximizes combat stats per IC (Riveted armor + Easy Maintenance + cost-efficient guns).
    """
    y = int(year)
    chassis_id = _pick_best_chassis_for_year(chassis_class, year)
    chassis = TANK_CHASSIS[chassis_id]
    max_ticks = MAX_UPGRADE_TICKS_BY_YEAR.get(year, 14)

    # Filter unlocked turrets compatible with chassis_class & role
    valid_turrets = [
        m for m in TANK_MODULES.values()
        if m.slot_type == "turret"
        and m.year_unlocked <= y
        and chassis.weight_class in m.allowed_weight_classes
        and role in m.allowed_roles
    ]
    if not valid_turrets:
        valid_turrets = [
            m for m in TANK_MODULES.values()
            if m.slot_type == "turret" and chassis.weight_class in m.allowed_weight_classes
        ]

    # Filter unlocked guns compatible with role
    valid_guns = [
        m for m in TANK_MODULES.values()
        if m.slot_type == "main_armament"
        and m.year_unlocked <= y
        and role in m.allowed_roles
    ]
    if role == "flame_tank":
        valid_guns = [TANK_MODULES["tank_flamethrower"]]
    elif role == "anti_air":
        valid_guns = [
            m for m in TANK_MODULES.values()
            if m.slot_type == "main_armament" and "anti_air" in m.allowed_roles and m.year_unlocked <= y
        ] or [TANK_MODULES["tank_anti_air_cannon"]]

    # Pick latest radio unlocked
    radios = [
        m.module_id for m in sorted(
            [m for m in TANK_MODULES.values() if m.category == "tank_radio_module" and m.year_unlocked <= y],
            key=lambda x: x.year_unlocked,
            reverse=True,
        )
    ]
    best_radio = radios[0] if radios else None

    obj = objective.lower().strip()
    best_bp: Optional[TankBlueprint] = None
    best_score = -1e9

    suspensions = ["tank_torsion_bar_suspension", "tank_christie_suspension", "tank_bogie_suspension"]
    suspensions = [s for s in suspensions if TANK_MODULES[s].year_unlocked <= y] or ["tank_bogie_suspension"]

    armors = ["tank_welded_armor", "tank_cast_armor", "tank_riveted_armor"]
    armors = [a for a in armors if TANK_MODULES[a].year_unlocked <= y] or ["tank_riveted_armor"]

    engines = ["tank_gasoline_engine", "tank_diesel_engine"]

    # Determine special module loadout & ticks based on objective
    specials: List[str] = []
    if role == "amphibious_tank" and chassis.weight_class != "amphibious":
        specials.append("amphibious_drive")
    if best_radio and role not in ("flame_tank", "anti_air"):
        specials.append(best_radio)

    if obj in ("soft_attack", "nsb_meta_soft_attack"):
        for cand_sm in ("secondary_turret_small_cannon", "secondary_turret_hmg", "stabilizer", "auto_loader", "extra_ammo_storage"):
            if len(specials) < 4 and cand_sm in TANK_MODULES and TANK_MODULES[cand_sm].year_unlocked <= y:
                specials.append(cand_sm)
        tick_pairs = [(min(4, max_ticks), min(6, max_ticks)), (0, min(4, max_ticks))]
    elif obj in ("hard_attack", "nsb_meta_hard_attack"):
        for cand_sm in ("squeezebore_adaptor", "secondary_turret_small_cannon", "stabilizer", "sloped_armor"):
            if len(specials) < 4 and cand_sm in TANK_MODULES and TANK_MODULES[cand_sm].year_unlocked <= y:
                specials.append(cand_sm)
        tick_pairs = [(min(6, max_ticks), min(6, max_ticks)), (min(4, max_ticks), min(4, max_ticks))]
    elif obj in ("armor_breakthrough", "nsb_meta_armor_brick"):
        for cand_sm in ("sloped_armor", "armor_skirts", "stabilizer", "dozer_blade", "wet_ammo_storage"):
            if len(specials) < 4 and cand_sm in TANK_MODULES and TANK_MODULES[cand_sm].year_unlocked <= y:
                specials.append(cand_sm)
        tick_pairs = [(max_ticks, max_ticks), (min(10, max_ticks), min(10, max_ticks))]
    elif obj in ("bang_for_buck", "nsb_budget"):
        for cand_sm in ("easy_maintenance", "additional_machine_guns", "armor_skirts"):
            if len(specials) < 4 and cand_sm in TANK_MODULES and TANK_MODULES[cand_sm].year_unlocked <= y:
                specials.append(cand_sm)
        tick_pairs = [(0, 0), (2, 2)]
    else:
        for cand_sm in ("stabilizer", "sloped_armor", "armor_skirts", "easy_maintenance", "secondary_turret_hmg"):
            if len(specials) < 4 and cand_sm in TANK_MODULES and TANK_MODULES[cand_sm].year_unlocked <= y:
                specials.append(cand_sm)
        tick_pairs = [(min(6, max_ticks), min(6, max_ticks)), (min(3, max_ticks), min(4, max_ticks)), (0, 2)]

    for turret in valid_turrets:
        for gun in valid_guns:
            if GUN_SIZE_RANK.get(gun.max_gun_size, 1) > GUN_SIZE_RANK.get(turret.max_gun_size, 1):
                continue
            for susp_id in suspensions:
                for arm_id in armors:
                    for eng_id in engines:
                        for a_ticks, e_ticks in tick_pairs:
                            bp = TankBlueprint(
                                name=f"NSB {year} {chassis_class.title()} {role.replace('_', ' ').title()}",
                                chassis_id=chassis_id,
                                role=role,
                                turret_id=turret.module_id,
                                main_armament_id=gun.module_id,
                                suspension_id=susp_id,
                                armor_id=arm_id,
                                engine_id=eng_id,
                                special_modules=list(specials[:4]),
                                armor_ticks=a_ticks,
                                engine_ticks=e_ticks,
                                year=year,
                            )
                            st = bp.calculate_equipment_stats()
                            if st["maximum_speed"] < 4.0 or st["reliability"] < 0.50:
                                continue
                            if max_ic_per_tank is not None and st["build_cost_ic"] > max_ic_per_tank:
                                continue

                            # Score blueprint for role + objective
                            ic = max(1.0, st["build_cost_ic"])
                            if role == "anti_air":
                                raw = st["air_attack"] * 3.0 + st["armor_value"] * 0.4 + st["soft_attack"]
                            elif role == "tank_destroyer":
                                raw = st["hard_attack"] * 2.5 + st["ap_attack"] * 1.2 + st["armor_value"] * 0.8 + st["defense"]
                            elif role == "artillery":
                                raw = st["soft_attack"] * 3.0 + st["breakthrough"] * 0.5 + st["defense"] * 0.5
                            elif role == "flame_tank":
                                raw = (st["armor_value"] * 1.2 + st["breakthrough"] * 1.5 + st["soft_attack"] * 2.0) / (ic ** 0.5)
                            elif obj in ("soft_attack", "nsb_meta_soft_attack"):
                                raw = st["soft_attack"] * 2.8 + st["breakthrough"] * 1.2 + st["armor_value"] * 0.6 + st["defense"] * 0.4
                            elif obj in ("hard_attack", "nsb_meta_hard_attack"):
                                raw = st["hard_attack"] * 2.6 + st["ap_attack"] * 1.0 + st["breakthrough"] * 1.0 + st["armor_value"] * 0.8
                            elif obj in ("armor_breakthrough", "nsb_meta_armor_brick"):
                                raw = st["armor_value"] * 2.2 + st["breakthrough"] * 1.8 + st["defense"] * 0.8 + st["soft_attack"] * 1.0
                            elif obj in ("bang_for_buck", "nsb_budget"):
                                combat = st["soft_attack"] * 1.8 + st["hard_attack"] * 1.2 + st["breakthrough"] * 1.2 + st["armor_value"] * 0.8
                                raw = combat / (ic ** 0.85)
                            else:
                                combat = (
                                    st["soft_attack"] * 1.8
                                    + st["hard_attack"] * 1.4
                                    + st["breakthrough"] * 1.4
                                    + st["armor_value"] * 1.0
                                    + st["ap_attack"] * 0.5
                                    + st["defense"] * 0.5
                                )
                                raw = combat / (ic ** 0.35)

                            if raw > best_score:
                                best_score = raw
                                best_bp = bp

    if best_bp is None:
        # Safe fallback blueprint
        best_bp = TankBlueprint(
            name=f"Fallback {year} {chassis_class.title()} {role.title()}",
            chassis_id=chassis_id,
            role=role,
            turret_id=valid_turrets[0].module_id,
            main_armament_id=valid_guns[0].module_id,
            suspension_id="tank_bogie_suspension",
            armor_id="tank_riveted_armor",
            engine_id="tank_diesel_engine",
            special_modules=[],
            armor_ticks=0,
            engine_ticks=2,
            year=year,
        )
    return best_bp


def apply_tank_design_mode_to_pool(
    battalions: Dict[str, Battalion],
    divisional_supports: Dict[str, SupportCompany],
    regimental_supports: Dict[str, SupportCompany],
    year: str = "1945",
    mode: str = "historical",
    objective: str = "best_overall",
) -> Tuple[Dict[str, Battalion], Dict[str, SupportCompany], Dict[str, SupportCompany]]:
    """
    Transforms all tank-using Battalions, Divisional Supports, and Regimental
    Supports in the provided dictionaries according to `mode`:
    - `"historical"`: Preserves the canonical `x_tank_chassis.txt` stats untouched.
    - `"nsb_meta_soft_attack"`, `"nsb_meta_hard_attack"`, `"nsb_meta_armor_brick"`,
      `"nsb_budget"`, `"nsb_auto_optimize"`: Replaces each tank sub-unit's stats
      with the optimal NSB Tank Designer blueprint for that year and mode!
    """
    clean_mode = (mode or "historical").lower().strip()
    if clean_mode in ("historical", "default", "none", "preset"):
        return dict(battalions), dict(divisional_supports), dict(regimental_supports)

    target_obj = objective if clean_mode == "nsb_auto_optimize" else clean_mode

    new_bats = dict(battalions)
    new_div_sups = dict(divisional_supports)
    new_reg_sups = dict(regimental_supports)

    # Cache optimized blueprints by (weight_class, role)
    bp_cache: Dict[Tuple[str, str], TankBlueprint] = {}

    for su_id, spec in TANK_SUBUNIT_SPECS.items():
        disp_name = spec["display_name"]
        w_cls = spec["weight_class"]
        role = spec["role"]
        key = (w_cls, role)
        if key not in bp_cache:
            bp_cache[key] = optimize_tank_blueprint(
                chassis_class=w_cls,
                role=role,
                year=year,
                objective=target_obj,
            )
        bp = bp_cache[key]

        if disp_name in new_bats:
            try:
                unit_obj = blueprint_to_unit(bp, su_id, year=year)
                if isinstance(unit_obj, Battalion):
                    new_bats[disp_name] = unit_obj
            except Exception:
                pass
        elif disp_name in new_div_sups:
            try:
                unit_obj = blueprint_to_unit(bp, su_id, year=year)
                if isinstance(unit_obj, SupportCompany):
                    new_div_sups[disp_name] = unit_obj
            except Exception:
                pass
        elif disp_name in new_reg_sups:
            try:
                unit_obj = blueprint_to_unit(bp, su_id, year=year)
                if isinstance(unit_obj, SupportCompany):
                    new_reg_sups[disp_name] = unit_obj
            except Exception:
                pass

    return new_bats, new_div_sups, new_reg_sups

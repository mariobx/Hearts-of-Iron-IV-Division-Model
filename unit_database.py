"""
Official Hearts of Iron IV v1.19.4.2 (`Operation Postern`) Unit Database.

Auto-generated directly from the official Clausewitz game files:
- `common/units/*.txt` (sub-unit definitions, groups, categories, equipment needs, terrain modifiers, battalion_mult)
- `common/units/equipment/*.txt` (equipment archetypes, variants, NSB tank/flame/amphibious syntheses)
- `common/technologies/*.txt` (historical equipment unlocks and cumulative unit/category stat modifiers)

Covers 5 benchmark technology years (`SUPPORTED_YEARS = ["1934", "1936", "1939", "1940", "1945"]`):
- 45 Line Battalions (`All_Battalions`) across all 6 brigade groups (`infantry`, `combat_support`,
  `mobile`, `mobile_combat_support`, `armor`, `armor_combat_support`).
- 43 Divisional Support Companies (`Divisional_Support_Companies` / `Support_Companies`), including
  Special Projects (Land Cruiser, Super-Heavy Artillery, SP Super-Heavy Artillery, Flame Tanks,
  Assault/Armored Engineers, Armored Maintenance/Signal, Motorized Military Police, Helicopters)
  and Super-Heavy Tank/TD/SPAA/SPArt support companies.
- 14 Regimental Support Companies (`Regimental_Support_Companies`) introduced in HOI4 v1.19
  (`Fire Support Team`, `Motorized Fire Support Team`, `Field Gun Battery`, `Rocket Artillery Battery`,
  `Anti-Air Battery`, `Anti-Tank Battery`, `Light/Medium/Heavy/Modern SP Anti-Air Battery`,
  `Light/Medium/Heavy/Modern Tank Destroyer Support`).
"""

from typing import Dict, List
from battalion import Battalion
from support_company import SupportCompany
from stats import BaseStatistics
from modifiers import UnitModifiers, TerrainModifier, BattalionMultiplier

SUPPORTED_YEARS: List[str] = ["1934", "1936", "1939", "1940", "1945"]

All_Battalions: Dict[str, Dict[str, Battalion]] = {
    "1934": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks', 'category_marines_and_amphibious'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.75, defense=46.0, breakthrough=6.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=443.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="amphibious_mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup', 'category_marines_and_amphibious'], year_unlocked=1941, is_special_project=False, is_country_locked=False),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=1.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_air_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=0.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_tank_brigade", group="combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=6.6, hard_attack=2.0, defense=2.0, breakthrough=12.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=180.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.3, defense=0.0)}), unit_id="armored_car", group="mobile", categories=['category_front_line', 'category_army', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=26.0, hard_attack=2.0, defense=11.0, breakthrough=10.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=84.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Bicycle": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=63.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=63.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05, movement=0.1), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Urban": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05)}), unit_id="camelry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.4,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=51.6, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=-0.05, defense=0.0)}), unit_id="cavalry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=1300.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=4.0, defense=2.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=19.55, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=57.75, hard_attack=0.9, defense=5.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.9, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=25.0, defense=5.0, breakthrough=0.25,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=100.8,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=2.85, hard_attack=0.5, defense=17.0, breakthrough=2.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=34.4, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.25, defense=0.1), "Forest": TerrainModifier(attack=0.15, defense=0.05), "Hills": TerrainModifier(attack=0.15, defense=0.05), "Mountain": TerrainModifier(attack=0.15, defense=0.05)}), unit_id="irregular_infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=450.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=2.0, hard_attack=1.0, defense=2.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=400.0, manpower=500.0, armor=5.0, piercing=5.0,
                hardness=0.5, air_attack=17.25, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=35.7, hard_attack=0.45, defense=5.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=320.0, manpower=500.0, armor=5.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=29.9,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=10.0, defense=5.0, breakthrough=0.25,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=320.0, manpower=500.0, armor=10.0, piercing=52.5,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine_commando", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=3.0, hard_attack=2.5, defense=46.0, breakthrough=8.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=363.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=650.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=3.0, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=25.3, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=44.1, hard_attack=0.9, defense=6.25, breakthrough=0.75,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=4.5, hard_attack=20.0, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=60.0, piercing=101.2,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="militia", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_militia'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=9.0, hard_attack=7.5, defense=4.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=57.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=84.0, hard_attack=2.7, defense=10.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=42.0, defense=10.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1120.0, manpower=500.0, armor=130.0, piercing=173.25,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=232.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="motorized_rocket_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_air_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_tank_brigade", group="mobile_combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_mobile_and_mobile_combat_sup', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=26.0, hard_attack=2.0, defense=11.0, breakthrough=15.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=174.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=7.0,
                max_hp=27.5, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=130.5, manpower=1200.0, armor=0.0, piercing=1.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Urban": TerrainModifier(attack=-0.1, defense=0.0)}), unit_id="motorized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountain": Battalion("Mountaineers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratrooper": Battalion("Paratroopers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=36.55, manpower=850.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="penal_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Ranger Battalion": Battalion("Ranger Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.1, movement=0.15), "Jungle": TerrainModifier(attack=0.2, defense=0.1, movement=0.15)}), unit_id="ranger_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_rangers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=17.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="rocket_artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=22.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_rocket_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1936": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks', 'category_marines_and_amphibious'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.5, defense=48.0, breakthrough=7.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=450.0, manpower=1200.0, armor=10.0, piercing=15.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="amphibious_mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup', 'category_marines_and_amphibious'], year_unlocked=1941, is_special_project=False, is_country_locked=False),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=1.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_air_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=0.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_tank_brigade", group="combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=6.6, hard_attack=2.2, defense=2.0, breakthrough=12.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=180.0, manpower=500.0, armor=3.0, piercing=6.6,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.3, defense=0.0)}), unit_id="armored_car", group="mobile", categories=['category_front_line', 'category_army', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=28.6, hard_attack=2.0, defense=11.0, breakthrough=10.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=84.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Bicycle": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=75.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05, movement=0.1), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Urban": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05)}), unit_id="camelry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.6,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=60.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=-0.05, defense=0.0)}), unit_id="cavalry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=1300.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=4.0, defense=2.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=19.55, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=60.5, hard_attack=0.9, defense=5.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.9, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=25.0, defense=5.0, breakthrough=0.25,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=100.8,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=50.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=5.7, hard_attack=1.0, defense=18.7, breakthrough=3.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=40.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.25, defense=0.1), "Forest": TerrainModifier(attack=0.15, defense=0.05), "Hills": TerrainModifier(attack=0.15, defense=0.05), "Mountain": TerrainModifier(attack=0.15, defense=0.05)}), unit_id="irregular_infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=1.5, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=440.0, manpower=500.0, armor=10.0, piercing=20.0,
                hardness=0.5, air_attack=19.55, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=46.2, hard_attack=0.9, defense=6.25, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=360.0, manpower=500.0, armor=10.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=540.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=16.0, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=360.0, manpower=500.0, armor=15.0, piercing=80.85,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine_commando", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=6.0, hard_attack=5.0, defense=48.0, breakthrough=9.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=370.0, manpower=1200.0, armor=10.0, piercing=15.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=650.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=3.0, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=25.3, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=46.2, hard_attack=0.9, defense=6.25, breakthrough=0.75,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=4.5, hard_attack=20.0, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=60.0, piercing=101.2,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=50.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="militia", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_militia'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=9.0, hard_attack=7.5, defense=4.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=57.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=88.0, hard_attack=2.7, defense=10.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=42.0, defense=10.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1120.0, manpower=500.0, armor=130.0, piercing=173.25,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=232.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="motorized_rocket_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_air_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_tank_brigade", group="mobile_combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_mobile_and_mobile_combat_sup', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=28.6, hard_attack=2.0, defense=11.0, breakthrough=15.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=174.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=8.0,
                max_hp=27.5, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=137.5, manpower=1200.0, armor=0.0, piercing=4.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Urban": TerrainModifier(attack=-0.1, defense=0.0)}), unit_id="motorized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountain": Battalion("Mountaineers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratrooper": Battalion("Paratroopers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=65.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=65.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=42.5, manpower=850.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="penal_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Ranger Battalion": Battalion("Ranger Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.1, movement=0.15), "Jungle": TerrainModifier(attack=0.2, defense=0.1, movement=0.15)}), unit_id="ranger_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_rangers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=17.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="rocket_artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=22.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_rocket_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1939": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks', 'category_marines_and_amphibious'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=2.25, defense=54.0, breakthrough=8.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=458.0, manpower=1200.0, armor=10.0, piercing=16.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="amphibious_mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup', 'category_marines_and_amphibious'], year_unlocked=1941, is_special_project=False, is_country_locked=False),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=1.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=20.9, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_air_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=22.0, defense=4.0, breakthrough=0.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=72.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_tank_brigade", group="combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=7.2, hard_attack=2.2, defense=2.0, breakthrough=12.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=180.0, manpower=500.0, armor=3.0, piercing=6.6,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.3, defense=0.0)}), unit_id="armored_car", group="mobile", categories=['category_front_line', 'category_army', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=33.0, hard_attack=3.0, defense=15.0, breakthrough=13.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Bicycle": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=78.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=78.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05, movement=0.1), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Urban": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05)}), unit_id="camelry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.8,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=69.6, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=-0.05, defense=0.0)}), unit_id="cavalry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=1300.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=4.0, defense=2.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=22.1, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=60.5, hard_attack=0.9, defense=5.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.9, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=26.25, defense=5.0, breakthrough=0.25,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=105.6,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=58.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=23.8, breakthrough=4.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=46.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.25, defense=0.1), "Forest": TerrainModifier(attack=0.15, defense=0.05), "Hills": TerrainModifier(attack=0.15, defense=0.05), "Mountain": TerrainModifier(attack=0.15, defense=0.05)}), unit_id="irregular_infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=1.5, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=440.0, manpower=500.0, armor=10.0, piercing=20.0,
                hardness=0.5, air_attack=22.1, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=46.2, hard_attack=0.9, defense=6.25, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=360.0, manpower=500.0, armor=10.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=540.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=16.8, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=360.0, manpower=500.0, armor=15.0, piercing=84.7,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine_commando", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=9.9, hard_attack=7.5, defense=54.0, breakthrough=10.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=378.0, manpower=1200.0, armor=10.0, piercing=16.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=650.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=3.0, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=28.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=46.2, hard_attack=0.9, defense=6.25, breakthrough=0.75,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=4.5, hard_attack=21.0, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=60.0, piercing=105.6,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=58.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="militia", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_militia'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=9.0, hard_attack=7.5, defense=4.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=65.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=88.0, hard_attack=2.7, defense=10.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=44.1, defense=10.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1120.0, manpower=500.0, armor=130.0, piercing=181.5,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=232.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="motorized_rocket_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=20.9, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_air_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=22.0, defense=4.0, breakthrough=5.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=72.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_tank_brigade", group="mobile_combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_mobile_and_mobile_combat_sup', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=33.0, hard_attack=3.0, defense=15.0, breakthrough=18.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=7.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=9.0,
                max_hp=27.5, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=145.5, manpower=1200.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Urban": TerrainModifier(attack=-0.1, defense=0.0)}), unit_id="motorized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountain": Battalion("Mountaineers", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratrooper": Battalion("Paratroopers", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=22.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=22.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=49.3, manpower=850.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="penal_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Ranger Battalion": Battalion("Ranger Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.1, movement=0.15), "Jungle": TerrainModifier(attack=0.2, defense=0.1, movement=0.15)}), unit_id="ranger_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_rangers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=17.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="rocket_artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=22.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_rocket_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1940": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks', 'category_marines_and_amphibious'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=10.8, hard_attack=2.25, defense=54.0, breakthrough=8.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=458.0, manpower=1200.0, armor=10.0, piercing=16.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="amphibious_mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup', 'category_marines_and_amphibious'], year_unlocked=1941, is_special_project=False, is_country_locked=False),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.5, hard_attack=11.0, defense=4.0, breakthrough=1.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=180.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=27.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_air_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=24.2, defense=4.0, breakthrough=0.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=180.0, manpower=500.0, armor=0.0, piercing=108.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_tank_brigade", group="combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=15.6, hard_attack=4.8, defense=3.0, breakthrough=16.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=270.0, manpower=500.0, armor=10.0, piercing=9.6,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.3, defense=0.0)}), unit_id="armored_car", group="mobile", categories=['category_front_line', 'category_army', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=3.0, defense=15.0, breakthrough=13.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Bicycle": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=78.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=78.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05, movement=0.1), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Urban": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05)}), unit_id="camelry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.8,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=69.6, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=-0.05, defense=0.0)}), unit_id="cavalry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=1300.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=4.0, defense=2.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=22.1, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=63.25, hard_attack=0.9, defense=5.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=1000.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.9, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=26.25, defense=5.0, breakthrough=0.25,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=105.6,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=58.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=9.45, hard_attack=1.5, defense=23.8, breakthrough=4.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=46.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.25, defense=0.1), "Forest": TerrainModifier(attack=0.15, defense=0.05), "Hills": TerrainModifier(attack=0.15, defense=0.05), "Mountain": TerrainModifier(attack=0.15, defense=0.05)}), unit_id="irregular_infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=1.5, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=440.0, manpower=500.0, armor=10.0, piercing=20.0,
                hardness=0.5, air_attack=22.1, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=48.3, hard_attack=0.9, defense=6.25, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=360.0, manpower=500.0, armor=10.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=540.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=5.4, hard_attack=16.8, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=360.0, manpower=500.0, armor=15.0, piercing=84.7,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine_commando", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=87.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=10.8, hard_attack=7.5, defense=54.0, breakthrough=10.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=378.0, manpower=1200.0, armor=10.0, piercing=16.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=650.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=3.0, defense=2.5, breakthrough=0.625,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=28.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=48.3, hard_attack=0.9, defense=6.25, breakthrough=0.75,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=480.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=4.5, hard_attack=21.0, defense=6.25, breakthrough=0.325,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=60.0, piercing=105.6,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=58.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="militia", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_militia'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=9.0, hard_attack=7.5, defense=4.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=65.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=92.0, hard_attack=2.7, defense=10.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=44.1, defense=10.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1120.0, manpower=500.0, armor=130.0, piercing=181.5,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=232.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="motorized_rocket_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.5, hard_attack=11.0, defense=4.0, breakthrough=6.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=270.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.2, air_attack=27.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_air_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=24.2, defense=4.0, breakthrough=5.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=270.0, manpower=500.0, armor=0.0, piercing=108.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_tank_brigade", group="mobile_combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_mobile_and_mobile_combat_sup', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=3.0, defense=15.0, breakthrough=18.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=7.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=10.8, hard_attack=1.5, defense=28.0, breakthrough=9.0,
                max_hp=27.5, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=145.5, manpower=1200.0, armor=0.0, piercing=5.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Urban": TerrainModifier(attack=-0.1, defense=0.0)}), unit_id="motorized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountain": Battalion("Mountaineers", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratrooper": Battalion("Paratroopers", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=22.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=22.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=75.4, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=49.3, manpower=850.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="penal_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Ranger Battalion": Battalion("Ranger Battalion", BaseStatistics(
                soft_attack=10.35, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=20.0, organization=75.0, combat_width=2.0, supply_use=0.05,
                ic_cost=81.2, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.1, movement=0.15), "Jungle": TerrainModifier(attack=0.2, defense=0.1, movement=0.15)}), unit_id="ranger_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_rangers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=17.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=96.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="rocket_artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=32.0, hard_attack=1.0, defense=13.0, breakthrough=22.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=186.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_rocket_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1945": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=650.0, manpower=500.0, armor=80.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks', 'category_marines_and_amphibious'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=15.6, hard_attack=4.0, defense=64.0, breakthrough=10.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=569.0, manpower=1200.0, armor=15.0, piercing=78.0,
                hardness=0.7, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="amphibious_mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup', 'category_marines_and_amphibious'], year_unlocked=1941, is_special_project=False, is_country_locked=False),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=4.0, hard_attack=15.0, defense=4.0, breakthrough=1.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=88.0,
                hardness=0.0, air_attack=41.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_air_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=39.0, defense=4.0, breakthrough=0.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=175.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="anti_tank_brigade", group="combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=20.8, hard_attack=10.4, defense=5.0, breakthrough=28.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=360.0, manpower=500.0, armor=20.0, piercing=46.8,
                hardness=0.7, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.3, defense=0.0)}), unit_id="armored_car", group="mobile", categories=['category_front_line', 'category_army', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=47.6, hard_attack=4.0, defense=19.0, breakthrough=16.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=108.0, manpower=500.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Bicycle": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=89.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=89.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=0.0, defense=0.0, movement=0.2)}), unit_id="bicycle_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=13.8, hard_attack=2.4, defense=34.0, breakthrough=5.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=103.5, manpower=1000.0, armor=0.0, piercing=18.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05, movement=0.1), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Urban": TerrainModifier(attack=-0.05, defense=0.0, movement=-0.05)}), unit_id="camelry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=13.8, hard_attack=2.4, defense=34.0, breakthrough=6.0,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=82.8, manpower=1000.0, armor=0.0, piercing=18.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.05), "Urban": TerrainModifier(attack=-0.05, defense=0.0)}), unit_id="cavalry", group="mobile", categories=['category_front_line', 'category_cavalry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=35.0, hard_attack=40.0, defense=10.0, breakthrough=67.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=1550.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=7.5, hard_attack=6.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1200.0, manpower=500.0, armor=90.0, piercing=88.0,
                hardness=0.8, air_attack=63.8, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=96.0, hard_attack=2.25, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=1200.0, manpower=500.0, armor=90.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=35.0, hard_attack=40.0, defense=9.0, breakthrough=77.05,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1200.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.9, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=69.0, defense=8.75, breakthrough=0.45,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1200.0, manpower=500.0, armor=130.0, piercing=192.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.05, defense=0.0), "Hills": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.6, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "River": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.5, defense=-0.2)}), unit_id="heavy_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=69.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_infantry_and_bicycle'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=13.2, hard_attack=3.0, defense=28.9, breakthrough=5.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=55.2, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.25, defense=0.1), "Forest": TerrainModifier(attack=0.15, defense=0.05), "Hills": TerrainModifier(attack=0.15, defense=0.05), "Mountain": TerrainModifier(attack=0.15, defense=0.05)}), unit_id="irregular_infantry", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=20.0, hard_attack=9.0, defense=6.0, breakthrough=46.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=550.0, manpower=500.0, armor=30.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=4.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=480.0, manpower=500.0, armor=25.0, piercing=35.0,
                hardness=0.5, air_attack=46.4, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=55.2, hard_attack=1.35, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=400.0, manpower=500.0, armor=25.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=22.0, hard_attack=9.0, defense=6.0, breakthrough=52.9,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=600.0, manpower=500.0, armor=30.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=7.2, hard_attack=27.6, defense=8.75, breakthrough=0.45,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=400.0, manpower=500.0, armor=30.0, piercing=118.8,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="light_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=6.5,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=103.5, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine_commando", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=6.5,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=103.5, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.5, defense=0.0), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "River": TerrainModifier(attack=0.3, defense=0.0)}), unit_id="marine", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_marines', 'category_special_forces_leg_infantry', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=17.4, hard_attack=11.3, defense=68.0, breakthrough=15.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=549.0, manpower=1200.0, armor=20.0, piercing=93.0,
                hardness=0.75, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.2, defense=-0.05)}), unit_id="mechanized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=32.0, hard_attack=24.0, defense=9.0, breakthrough=66.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=750.0, manpower=500.0, armor=90.0, piercing=91.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.4), "Jungle": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Plains": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "River": TerrainModifier(attack=0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="amphibious_medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army', 'category_amphibious_tanks'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=7.5, hard_attack=6.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=560.0, manpower=500.0, armor=58.0, piercing=70.0,
                hardness=0.65, air_attack=62.35, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=66.0, hard_attack=1.8, defense=8.75, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=560.0, manpower=500.0, armor=58.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=32.0, hard_attack=24.0, defense=9.0, breakthrough=75.9,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=700.0, manpower=500.0, armor=90.0, piercing=91.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.8, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=7.2, hard_attack=36.8, defense=8.75, breakthrough=0.45,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=560.0, manpower=500.0, armor=90.0, piercing=156.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="medium_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=69.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="militia", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_militia'], year_unlocked=1918, is_special_project=False, is_country_locked=True),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=9.0, hard_attack=7.5, defense=4.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=72.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_anti_air_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=96.0, hard_attack=2.7, defense=10.0, breakthrough=1.0,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_sp_artillery_brigade", group="armor_combat_support", categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_armor", group="armor", categories=['category_tanks', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=9.0, hard_attack=48.3, defense=10.0, breakthrough=0.5,
                max_hp=0.5, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1120.0, manpower=500.0, armor=130.0, piercing=198.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)}), unit_id="modern_tank_destroyer_brigade", group="armor_combat_support", categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=59.4, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=232.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="motorized_rocket_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=4.0, hard_attack=15.0, defense=4.0, breakthrough=6.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=306.0, manpower=500.0, armor=0.0, piercing=88.0,
                hardness=0.2, air_attack=41.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_air_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_anti_air', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=39.0, defense=4.0, breakthrough=5.0,
                max_hp=1.6, organization=0.0, combat_width=1.0, supply_use=0.15,
                ic_cost=306.0, manpower=500.0, armor=0.0, piercing=175.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_anti_tank_brigade", group="mobile_combat_support", categories=['category_front_line', 'category_army', 'category_line_artillery', 'category_mobile_and_mobile_combat_sup', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=47.6, hard_attack=4.0, defense=19.0, breakthrough=21.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=198.0, manpower=500.0, armor=0.0, piercing=9.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=15.6, hard_attack=3.0, defense=34.0, breakthrough=10.0,
                max_hp=27.5, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=156.5, manpower=1200.0, armor=0.0, piercing=30.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.5), "Jungle": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "River": TerrainModifier(attack=-0.1, defense=0.0, movement=-0.1), "Urban": TerrainModifier(attack=-0.1, defense=0.0)}), unit_id="motorized", group="mobile", categories=['category_front_line', 'category_all_infantry', 'category_army', 'category_vehicle_infantry', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountain": Battalion("Mountaineers", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=6.5,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=96.6, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=6.5,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=96.6, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Hills": TerrainModifier(attack=0.2, defense=0.05, movement=0.1), "Mountain": TerrainModifier(attack=0.35, defense=0.1, movement=0.2)}), unit_id="mountaineers", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_mountaineers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratrooper": Battalion("Paratroopers", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=22.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=89.7, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=22.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=89.7, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="paratrooper", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_paratroopers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=58.65, manpower=850.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), unit_id="penal_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Ranger Battalion": Battalion("Ranger Battalion", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=34.0, breakthrough=6.5,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.05,
                ic_cost=96.6, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.1, movement=0.15), "Jungle": TerrainModifier(attack=0.2, defense=0.1, movement=0.15)}), unit_id="ranger_battalion", group="infantry", categories=['category_front_line', 'category_light_infantry', 'category_all_infantry', 'category_army', 'category_special_forces', 'category_rangers', 'category_special_forces_leg_infantry'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=54.0, hard_attack=1.0, defense=16.0, breakthrough=20.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=120.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.2), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="rocket_artillery_brigade", group="combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=54.0, hard_attack=1.0, defense=16.0, breakthrough=25.0,
                max_hp=1.6, organization=0.0, combat_width=3.0, supply_use=0.25,
                ic_cost=210.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.5), "Fort": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=-0.05), "Jungle": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.5), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.3), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=-0.2), "River": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2)}), unit_id="mot_rocket_artillery_brigade", group="mobile_combat_support", categories=['category_army', 'category_line_artillery', 'category_artillery', 'category_rocket_artillery', 'category_mobile_and_mobile_combat_sup'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
}

Divisional_Support_Companies: Dict[str, Dict[str, SupportCompany]] = {
    "1934": {
        "Airborne Light Armor": SupportCompany("Airborne Light Armor", BaseStatistics(
                soft_attack=9.75, hard_attack=3.0, defense=2.0, breakthrough=19.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=5.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}), unit_id="airborne_light_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_paratroopers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car Recon Company": SupportCompany("Armored Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="armored_car_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=420.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.2, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.1), "Fort": TerrainModifier(attack=0.15, defense=0.25), "Hills": TerrainModifier(attack=0.0, defense=0.1, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.15, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.15, movement=0.2), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.1, defense=0.15, movement=0.4), "Urban": TerrainModifier(attack=0.2, defense=0.1, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05), BattalionMultiplier(category="category_all_infantry", entrenchment=0.2, additive=True)]), unit_id="armored_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", max_hp=0.1, additive=True)]), unit_id="armored_maintenance", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05)]), unit_id="armored_signal", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="blackshirt_assault_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=320.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.1), "Fort": TerrainModifier(attack=0.25, defense=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Jungle": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1, movement=0.1), "River": TerrainModifier(attack=0.05, defense=0.1, movement=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.0, movement=0.05)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", breakthrough=0.1)]), unit_id="assault_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Elephantry Recon": SupportCompany("Elephantry Recon", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=8.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.06,
                ic_cost=161.5, manpower=700.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.1, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Urban": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.15, supply_use=-0.3)]), unit_id="elephantry", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=124.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.05), "Fort": TerrainModifier(attack=0.1, defense=0.25), "Hills": TerrainModifier(attack=0.0, defense=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.25, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", entrenchment=0.2, additive=True)]), unit_id="engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.1)]), unit_id="field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.0, defense=1.875, breakthrough=13.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=183.75, manpower=300.0, armor=20.625, piercing=5.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.25, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="heavy_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=-0.05, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.03)]), unit_id="helicopter_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['helicopter_recon', 'helicopter_transport', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.05, recovery_rate=0.1)]), unit_id="helicopter_field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=26.0, breakthrough=10.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=228.6, manpower=500.0, armor=4.0, piercing=12.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.15)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="helicopter_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon', 'helicopter_recon'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.0,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.15, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.05)}), unit_id="helicopter_transport", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company', 'helicopter_transport'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=21.0, breakthrough=2.6,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=164.3, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.05, movement=0.3), "Jungle": TerrainModifier(attack=0.1, defense=0.2, movement=0.3), "River": TerrainModifier(attack=0.1, defense=0.25, movement=0.25)}), unit_id="jungle_pioneers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=75.0, hard_attack=62.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=330.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=1.0, air_attack=30.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.2), "Fort": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=-0.2, defense=-0.2, movement=-0.25), "Jungle": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.35), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.5), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "River": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.5), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="land_cruiser", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=2.5, hard_attack=0.0, defense=0.75, breakthrough=4.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=65.25, manpower=300.0, armor=2.5, piercing=5.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Fort": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="light_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=5.2, hard_attack=1.6, defense=1.6, breakthrough=10.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=4.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", hard_attack=0.1)]), unit_id="light_tank_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.3
            ), unit_id="logistics_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Snow": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", initiative=0.02, additive=True)]), unit_id="long_range_patrol_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="maintenance_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=2.75, hard_attack=0.0, defense=1.2, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=94.5, manpower=300.0, armor=10.5, piercing=5.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.2, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="medium_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=3.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=58.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="motorized_military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=18.2, breakthrough=3.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=107.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="mot_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Northern Territory Recon": SupportCompany("Northern Territory Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.04,
                ic_cost=48.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Hills": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="northern_territory_recon_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=164.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.15, defense=0.2), "Marsh": TerrainModifier(attack=0.1, defense=0.2, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.2, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_marines", breakthrough=0.15)]), unit_id="pioneer_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_marines', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=77.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="rangers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=10.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="self_propelled_super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.1,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="signal_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=104.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.1)]), unit_id="sturmtruppe_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Anti-Air": SupportCompany("Super-Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=57.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_anti_air_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Artillery": SupportCompany("Super-Heavy SP Artillery", BaseStatistics(
                soft_attack=89.25, hard_attack=2.7, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_artillery_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank": SupportCompany("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.3), "Fort": TerrainModifier(attack=0.1, defense=0.05), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Jungle": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.3), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "River": TerrainModifier(attack=-0.25, defense=-0.25, movement=-0.3), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="super_heavy_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1941, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank Destroyer": SupportCompany("Super-Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.8, hard_attack=70.0, defense=8.75, breakthrough=0.45,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=178.5,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_tank_destroyer_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers', 'category_support_battalions', 'category_divisional_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=1.8, hard_attack=4.2, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=15.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_divisional_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.4, hard_attack=10.0, defense=2.4, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=51.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=13.0, hard_attack=1.0, defense=5.5, breakthrough=5.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=42.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=16.0, hard_attack=0.5, defense=6.5, breakthrough=8.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=20.0, breakthrough=1.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Snow": TerrainModifier(attack=0.25, defense=0.25, movement=0.3)}), unit_id="winter_logistics_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
    },
    "1936": {
        "Airborne Light Armor": SupportCompany("Airborne Light Armor", BaseStatistics(
                soft_attack=12.0, hard_attack=4.5, defense=2.5, breakthrough=27.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=7.5, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}), unit_id="airborne_light_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_paratroopers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car Recon Company": SupportCompany("Armored Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="armored_car_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=420.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.2, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.1), "Fort": TerrainModifier(attack=0.15, defense=0.25), "Hills": TerrainModifier(attack=0.0, defense=0.1, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.15, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.15, movement=0.2), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.1, defense=0.15, movement=0.4), "Urban": TerrainModifier(attack=0.2, defense=0.1, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05), BattalionMultiplier(category="category_all_infantry", entrenchment=0.2, additive=True)]), unit_id="armored_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", max_hp=0.1, additive=True)]), unit_id="armored_maintenance", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05)]), unit_id="armored_signal", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=6.6, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=90.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="blackshirt_assault_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=320.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.1), "Fort": TerrainModifier(attack=0.25, defense=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Jungle": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1, movement=0.1), "River": TerrainModifier(attack=0.05, defense=0.1, movement=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.0, movement=0.05)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", breakthrough=0.1)]), unit_id="assault_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Elephantry Recon": SupportCompany("Elephantry Recon", BaseStatistics(
                soft_attack=0.6, hard_attack=0.1, defense=8.8, breakthrough=1.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.06,
                ic_cost=165.0, manpower=700.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.1, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Urban": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.15, supply_use=-0.3)]), unit_id="elephantry", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=24.2, breakthrough=4.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=125.0, manpower=300.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.05), "Fort": TerrainModifier(attack=0.1, defense=0.25), "Hills": TerrainModifier(attack=0.0, defense=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.25, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", entrenchment=0.2, additive=True)]), unit_id="engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.1)]), unit_id="field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.0, defense=1.875, breakthrough=13.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=183.75, manpower=300.0, armor=20.625, piercing=5.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.25, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="heavy_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=-0.05, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.03)]), unit_id="helicopter_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['helicopter_recon', 'helicopter_transport', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.05, recovery_rate=0.1)]), unit_id="helicopter_field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=28.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=230.0, manpower=500.0, armor=4.0, piercing=15.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.15)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="helicopter_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon', 'helicopter_recon'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.0,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.15, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.05)}), unit_id="helicopter_transport", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company', 'helicopter_transport'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=23.1, breakthrough=3.9,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=165.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.05, movement=0.3), "Jungle": TerrainModifier(attack=0.1, defense=0.2, movement=0.3), "River": TerrainModifier(attack=0.1, defense=0.25, movement=0.25)}), unit_id="jungle_pioneers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=75.0, hard_attack=62.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=330.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=1.0, air_attack=30.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.2), "Fort": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=-0.2, defense=-0.2, movement=-0.25), "Jungle": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.35), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.5), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "River": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.5), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="land_cruiser", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=2.5, hard_attack=0.0, defense=1.0, breakthrough=5.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.75, manpower=300.0, armor=3.75, piercing=5.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Fort": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="light_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=6.4, hard_attack=2.4, defense=2.0, breakthrough=14.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=6.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", hard_attack=0.1)]), unit_id="light_tank_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.3
            ), unit_id="logistics_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=6.6, hard_attack=1.0, defense=22.0, breakthrough=3.9,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Snow": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", initiative=0.02, additive=True)]), unit_id="long_range_patrol_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="maintenance_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=2.75, hard_attack=0.0, defense=1.2, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=94.5, manpower=300.0, armor=10.5, piercing=5.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.2, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="medium_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=4.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="motorized_military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.6, hard_attack=0.1, defense=20.02, breakthrough=4.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=110.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="mot_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Northern Territory Recon": SupportCompany("Northern Territory Recon", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.04,
                ic_cost=50.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Hills": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="northern_territory_recon_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=24.2, breakthrough=4.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=165.0, manpower=300.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.15, defense=0.2), "Marsh": TerrainModifier(attack=0.1, defense=0.2, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.2, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_marines", breakthrough=0.15)]), unit_id="pioneer_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_marines', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=80.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="rangers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.6, hard_attack=0.1, defense=11.0, breakthrough=1.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="self_propelled_super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.1,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="signal_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=6.6, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=115.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.1)]), unit_id="sturmtruppe_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Anti-Air": SupportCompany("Super-Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=57.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_anti_air_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Artillery": SupportCompany("Super-Heavy SP Artillery", BaseStatistics(
                soft_attack=93.5, hard_attack=2.7, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_artillery_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank": SupportCompany("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.3), "Fort": TerrainModifier(attack=0.1, defense=0.05), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Jungle": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.3), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "River": TerrainModifier(attack=-0.25, defense=-0.25, movement=-0.3), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="super_heavy_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1941, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank Destroyer": SupportCompany("Super-Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.8, hard_attack=70.0, defense=8.75, breakthrough=0.45,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=178.5,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_tank_destroyer_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers', 'category_support_battalions', 'category_divisional_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=1.8, hard_attack=4.2, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=15.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_divisional_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.4, hard_attack=10.0, defense=2.4, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=51.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=14.3, hard_attack=1.0, defense=5.5, breakthrough=5.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=42.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=16.0, hard_attack=0.5, defense=6.5, breakthrough=8.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=22.0, breakthrough=1.5,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Snow": TerrainModifier(attack=0.25, defense=0.25, movement=0.3)}), unit_id="winter_logistics_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
    },
    "1939": {
        "Airborne Light Armor": SupportCompany("Airborne Light Armor", BaseStatistics(
                soft_attack=12.0, hard_attack=4.5, defense=2.5, breakthrough=27.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=7.5, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}), unit_id="airborne_light_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_paratroopers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car Recon Company": SupportCompany("Armored Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=4.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="armored_car_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=420.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=4.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.2, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.1), "Fort": TerrainModifier(attack=0.15, defense=0.4), "Hills": TerrainModifier(attack=0.0, defense=0.1, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.15, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.15, movement=0.2), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.1, defense=0.15, movement=0.4), "Urban": TerrainModifier(attack=0.2, defense=0.1, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05), BattalionMultiplier(category="category_all_infantry", entrenchment=0.2, additive=True)]), unit_id="armored_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.33
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", max_hp=0.1, additive=True)]), unit_id="armored_maintenance", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.2,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.06)]), unit_id="armored_signal", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=98.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="blackshirt_assault_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.8,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=320.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.1), "Fort": TerrainModifier(attack=0.4, defense=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Jungle": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1, movement=0.1), "River": TerrainModifier(attack=0.05, defense=0.1, movement=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.0, movement=0.05)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", breakthrough=0.1)]), unit_id="assault_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Elephantry Recon": SupportCompany("Elephantry Recon", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=11.2, breakthrough=2.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.06,
                ic_cost=169.0, manpower=700.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.1, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Urban": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.15, supply_use=-0.3)]), unit_id="elephantry", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=30.8, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=125.8, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.05), "Fort": TerrainModifier(attack=0.2, defense=0.35), "Hills": TerrainModifier(attack=0.0, defense=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.25, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", entrenchment=0.2, additive=True)]), unit_id="engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.1)]), unit_id="field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.0, defense=1.875, breakthrough=13.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=183.75, manpower=300.0, armor=20.625, piercing=5.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.25, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="heavy_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=-0.05, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.03)]), unit_id="helicopter_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['helicopter_recon', 'helicopter_transport', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.05, recovery_rate=0.15)]), unit_id="helicopter_field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=34.0, breakthrough=12.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=231.6, manpower=500.0, armor=4.0, piercing=16.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=5.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.15)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="helicopter_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon', 'helicopter_recon'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.0,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.3, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.05)}), unit_id="helicopter_transport", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company', 'helicopter_transport'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=29.4, breakthrough=5.2,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=165.8, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.05, movement=0.3), "Jungle": TerrainModifier(attack=0.1, defense=0.2, movement=0.3), "River": TerrainModifier(attack=0.1, defense=0.25, movement=0.25)}), unit_id="jungle_pioneers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=75.0, hard_attack=62.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=330.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=1.0, air_attack=30.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.2), "Fort": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=-0.2, defense=-0.2, movement=-0.25), "Jungle": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.35), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.5), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "River": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.5), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="land_cruiser", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=2.5, hard_attack=0.0, defense=1.0, breakthrough=5.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.75, manpower=300.0, armor=3.75, piercing=5.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Fort": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="light_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=6.4, hard_attack=2.4, defense=2.0, breakthrough=14.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=6.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", hard_attack=0.1)]), unit_id="light_tank_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.2, recovery_rate=0.3
            ), unit_id="logistics_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=4.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Snow": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", initiative=0.02, additive=True)]), unit_id="long_range_patrol_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="maintenance_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=2.75, hard_attack=0.0, defense=1.8, breakthrough=13.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=120.75, manpower=300.0, armor=15.0, piercing=5.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.2, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="medium_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=5.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=61.6, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2), BattalionMultiplier(category="category_vehicle_infantry", recovery_rate=0.05)]), unit_id="motorized_military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=25.48, breakthrough=4.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=113.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.5, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="mot_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Northern Territory Recon": SupportCompany("Northern Territory Recon", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.04,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Hills": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="northern_territory_recon_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=30.8, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=165.8, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.15, defense=0.2), "Marsh": TerrainModifier(attack=0.1, defense=0.2, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.2, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_marines", breakthrough=0.15)]), unit_id="pioneer_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_marines', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="rangers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=14.0, breakthrough=2.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="self_propelled_super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.22,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="signal_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=127.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.1)]), unit_id="sturmtruppe_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Anti-Air": SupportCompany("Super-Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=65.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_anti_air_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Artillery": SupportCompany("Super-Heavy SP Artillery", BaseStatistics(
                soft_attack=93.5, hard_attack=2.7, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_artillery_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank": SupportCompany("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.3), "Fort": TerrainModifier(attack=0.1, defense=0.05), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Jungle": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.3), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "River": TerrainModifier(attack=-0.25, defense=-0.25, movement=-0.3), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="super_heavy_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1941, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank Destroyer": SupportCompany("Super-Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.8, hard_attack=73.5, defense=8.75, breakthrough=0.45,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=187.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_tank_destroyer_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers', 'category_support_battalions', 'category_divisional_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=1.8, hard_attack=4.2, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=17.1, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_divisional_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.4, hard_attack=12.0, defense=2.4, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=63.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=16.5, hard_attack=1.5, defense=7.5, breakthrough=6.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=16.0, hard_attack=0.5, defense=6.5, breakthrough=8.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=4.5, hard_attack=0.75, defense=28.0, breakthrough=2.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Snow": TerrainModifier(attack=0.25, defense=0.25, movement=0.3)}), unit_id="winter_logistics_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
    },
    "1940": {
        "Airborne Light Armor": SupportCompany("Airborne Light Armor", BaseStatistics(
                soft_attack=12.0, hard_attack=4.5, defense=2.5, breakthrough=27.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=7.5, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}), unit_id="airborne_light_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_paratroopers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car Recon Company": SupportCompany("Armored Car Recon Company", BaseStatistics(
                soft_attack=6.5, hard_attack=2.0, defense=1.5, breakthrough=12.8,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=108.0, manpower=500.0, armor=10.0, piercing=8.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=4.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="armored_car_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=420.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=4.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.2, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.1), "Fort": TerrainModifier(attack=0.15, defense=0.4), "Hills": TerrainModifier(attack=0.0, defense=0.1, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.15, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.15, movement=0.2), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.1, defense=0.15, movement=0.4), "Urban": TerrainModifier(attack=0.2, defense=0.1, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05), BattalionMultiplier(category="category_all_infantry", entrenchment=0.2, additive=True)]), unit_id="armored_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.33
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", max_hp=0.1, additive=True)]), unit_id="armored_maintenance", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.2,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.06)]), unit_id="armored_signal", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=98.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="blackshirt_assault_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.8,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=320.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.1), "Fort": TerrainModifier(attack=0.4, defense=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Jungle": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1, movement=0.1), "River": TerrainModifier(attack=0.05, defense=0.1, movement=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.0, movement=0.05)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", breakthrough=0.1)]), unit_id="assault_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Elephantry Recon": SupportCompany("Elephantry Recon", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=11.2, breakthrough=2.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.06,
                ic_cost=169.0, manpower=700.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.1, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Urban": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.15, supply_use=-0.3)]), unit_id="elephantry", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=30.8, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=125.8, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.05), "Fort": TerrainModifier(attack=0.2, defense=0.35), "Hills": TerrainModifier(attack=0.0, defense=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25, movement=0.2), "River": TerrainModifier(attack=0.0, defense=0.25, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", entrenchment=0.2, additive=True)]), unit_id="engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.1)]), unit_id="field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.0, defense=2.25, breakthrough=14.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=198.75, manpower=300.0, armor=26.25, piercing=5.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.25, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="heavy_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=-0.05, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.03)]), unit_id="helicopter_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['helicopter_recon', 'helicopter_transport', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.05, recovery_rate=0.15)]), unit_id="helicopter_field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=34.0, breakthrough=12.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=231.6, manpower=500.0, armor=4.0, piercing=16.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=5.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.15)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="helicopter_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon', 'helicopter_recon'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.0,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.3, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.05)}), unit_id="helicopter_transport", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company', 'helicopter_transport'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=29.4, breakthrough=5.2,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=165.8, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.05, movement=0.3), "Jungle": TerrainModifier(attack=0.1, defense=0.2, movement=0.3), "River": TerrainModifier(attack=0.1, defense=0.25, movement=0.25)}), unit_id="jungle_pioneers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=75.0, hard_attack=62.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=330.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=1.0, air_attack=30.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.2), "Fort": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=-0.2, defense=-0.2, movement=-0.25), "Jungle": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.35), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.5), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "River": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.5), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="land_cruiser", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=2.5, hard_attack=0.0, defense=1.0, breakthrough=5.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=72.75, manpower=300.0, armor=3.75, piercing=5.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Fort": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="light_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=6.4, hard_attack=2.4, defense=2.0, breakthrough=14.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=216.0, manpower=500.0, armor=6.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", hard_attack=0.1)]), unit_id="light_tank_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.2, recovery_rate=0.3
            ), unit_id="logistics_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=5.2,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=4.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Snow": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", initiative=0.02, additive=True)]), unit_id="long_range_patrol_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="maintenance_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=2.75, hard_attack=0.0, defense=1.8, breakthrough=13.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=120.75, manpower=300.0, armor=15.0, piercing=5.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.2, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="medium_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=5.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=61.6, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2), BattalionMultiplier(category="category_vehicle_infantry", recovery_rate=0.05)]), unit_id="motorized_military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=25.48, breakthrough=4.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=113.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.5, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="mot_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Northern Territory Recon": SupportCompany("Northern Territory Recon", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.04,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Hills": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="northern_territory_recon_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=30.8, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=165.8, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.15, defense=0.2), "Marsh": TerrainModifier(attack=0.1, defense=0.2, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.2, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_marines", breakthrough=0.15)]), unit_id="pioneer_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_marines', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="rangers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.9, hard_attack=0.15, defense=14.0, breakthrough=2.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="self_propelled_super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.22,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="signal_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=127.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.1)]), unit_id="sturmtruppe_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Anti-Air": SupportCompany("Super-Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=65.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_anti_air_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Artillery": SupportCompany("Super-Heavy SP Artillery", BaseStatistics(
                soft_attack=97.75, hard_attack=2.7, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_artillery_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank": SupportCompany("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.3), "Fort": TerrainModifier(attack=0.1, defense=0.05), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Jungle": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.3), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "River": TerrainModifier(attack=-0.25, defense=-0.25, movement=-0.3), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="super_heavy_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1941, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank Destroyer": SupportCompany("Super-Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.8, hard_attack=73.5, defense=8.75, breakthrough=0.45,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=187.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_tank_destroyer_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers', 'category_support_battalions', 'category_divisional_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=2.1, hard_attack=6.6, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=120.0, manpower=300.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=22.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_divisional_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.4, hard_attack=13.2, defense=2.4, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=120.0, manpower=300.0, armor=0.0, piercing=94.5,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=18.0, hard_attack=1.5, defense=7.5, breakthrough=6.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=16.0, hard_attack=0.5, defense=6.5, breakthrough=8.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=4.5, hard_attack=0.75, defense=28.0, breakthrough=2.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=63.2, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Snow": TerrainModifier(attack=0.25, defense=0.25, movement=0.3)}), unit_id="winter_logistics_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
    },
    "1945": {
        "Airborne Light Armor": SupportCompany("Airborne Light Armor", BaseStatistics(
                soft_attack=16.5, hard_attack=6.75, defense=3.0, breakthrough=34.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=240.0, manpower=500.0, armor=15.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}), unit_id="airborne_light_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_paratroopers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Car Recon Company": SupportCompany("Armored Car Recon Company", BaseStatistics(
                soft_attack=8.0, hard_attack=4.0, defense=2.5, breakthrough=22.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=144.0, manpower=500.0, armor=20.0, piercing=36.0,
                hardness=0.7, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=8.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="armored_car_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=420.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=6.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.2, defense=0.0), "Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.1), "Fort": TerrainModifier(attack=0.15, defense=0.4), "Hills": TerrainModifier(attack=0.0, defense=0.1, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.15, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.15, movement=0.2), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.15, defense=0.2, movement=0.55), "Urban": TerrainModifier(attack=0.2, defense=0.25, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.05), BattalionMultiplier(category="category_all_infantry", entrenchment=0.2, additive=True)]), unit_id="armored_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.39
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", max_hp=0.1, additive=True)]), unit_id="armored_maintenance", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=300.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.36,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_armor", breakthrough=0.08)]), unit_id="armored_signal", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=13.2, hard_attack=2.0, defense=34.0, breakthrough=6.5,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=109.0, manpower=1000.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="blackshirt_assault_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=8.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=320.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.1), "Fort": TerrainModifier(attack=0.4, defense=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Jungle": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1, movement=0.1), "River": TerrainModifier(attack=0.15, defense=0.1, movement=0.25), "Urban": TerrainModifier(attack=0.3, defense=0.0, movement=0.05)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", breakthrough=0.1)]), unit_id="assault_engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Elephantry Recon": SupportCompany("Elephantry Recon", BaseStatistics(
                soft_attack=1.2, hard_attack=0.2, defense=13.6, breakthrough=2.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.06,
                ic_cost=174.5, manpower=700.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=6.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.1, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=0.1, defense=0.0, movement=0.1), "Urban": TerrainModifier(attack=-0.2, defense=0.0, movement=-0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.15, supply_use=-0.3)]), unit_id="elephantry", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=37.4, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=126.9, manpower=300.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=3.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.15, defense=0.0), "Forest": TerrainModifier(attack=0.0, defense=0.25, movement=0.05), "Fort": TerrainModifier(attack=0.2, defense=0.35), "Hills": TerrainModifier(attack=0.0, defense=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.35, movement=0.25), "Urban": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", entrenchment=0.2, additive=True)]), unit_id="engineer", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.1)]), unit_id="field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=3.0, hard_attack=0.0, defense=3.375, breakthrough=19.2,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=279.75, manpower=300.0, armor=41.25, piercing=5.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.45, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.2, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="heavy_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=3.0, supply_consumption_factor=-0.17, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.03, recovery_rate=0.05)]), unit_id="helicopter_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['helicopter_recon', 'helicopter_transport', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", max_hp=0.05, recovery_rate=0.25)]), unit_id="helicopter_field_hospital", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['field_hospital', 'helicopter_field_hospital'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=40.0, breakthrough=13.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=233.8, manpower=500.0, armor=4.0, piercing=21.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=12.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.15)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="helicopter_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon', 'helicopter_recon'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=6.0, breakthrough=8.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.0,
                ic_cost=195.0, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.4, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.6, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.05)}), unit_id="helicopter_transport", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company', 'helicopter_transport'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_helicopter_support_companies'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=35.7, breakthrough=6.5,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=166.9, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.1, defense=0.05, movement=0.3), "Jungle": TerrainModifier(attack=0.1, defense=0.2, movement=0.3), "River": TerrainModifier(attack=0.1, defense=0.25, movement=0.25)}), unit_id="jungle_pioneers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=75.0, hard_attack=62.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=330.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=1.0, air_attack=30.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.7, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.2), "Fort": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=-0.2, defense=-0.2, movement=-0.25), "Jungle": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.35), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4, movement=-0.5), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "River": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.5), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="land_cruiser", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=2.5, hard_attack=0.0, defense=1.25, breakthrough=7.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=91.5, manpower=300.0, armor=7.5, piercing=5.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Fort": TerrainModifier(attack=0.3, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.2, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="light_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=8.8, hard_attack=3.6, defense=2.4, breakthrough=18.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=240.0, manpower=500.0, armor=12.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=7.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_all_armor", hard_attack=0.1)]), unit_id="light_tank_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_all_armor', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.4, recovery_rate=0.3
            ), unit_id="logistics_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=13.2, hard_attack=2.0, defense=34.0, breakthrough=6.5,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=67.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=8.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Snow": TerrainModifier(attack=0.1, defense=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_light_infantry", initiative=0.02, additive=True)]), unit_id="long_range_patrol_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="maintenance_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['maintenance_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=2.75, hard_attack=0.0, defense=2.4, breakthrough=15.4,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=159.75, manpower=300.0, armor=21.0, piercing=5.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=0.1, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Fort": TerrainModifier(attack=0.4, defense=0.0, movement=0.1), "Hills": TerrainModifier(attack=0.05, defense=0.0), "Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "River": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.25, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.05)]), unit_id="medium_flame_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['flame'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_tanks', 'category_all_armor', 'category_army'], year_unlocked=1939, is_special_project=True, is_country_locked=False),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=34.0, breakthrough=5.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=67.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2)]), unit_id="military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=34.0, breakthrough=6.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=63.8, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", recovery_rate=0.2), BattalionMultiplier(category="category_vehicle_infantry", recovery_rate=0.15)]), unit_id="motorized_military_police", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['military_police'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1938, is_special_project=True, is_country_locked=False),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=1.2, hard_attack=0.2, defense=30.94, breakthrough=5.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=117.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=7.5, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.2), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.15), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="mot_recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Northern Territory Recon": SupportCompany("Northern Territory Recon", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=34.0, breakthrough=5.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.04,
                ic_cost=53.8, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=7.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Hills": TerrainModifier(attack=0.075, defense=0.0, movement=0.2), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="northern_territory_recon_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=37.4, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=166.9, manpower=300.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.15, defense=0.2), "Marsh": TerrainModifier(attack=0.1, defense=0.2, movement=0.2), "River": TerrainModifier(attack=0.1, defense=0.2, movement=0.25)}, battalion_multipliers=[BattalionMultiplier(category="category_marines", breakthrough=0.15)]), unit_id="pioneer_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['engineer'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_marines', 'category_marines_and_amphibious'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=34.0, breakthrough=5.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=87.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=7.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Hills": TerrainModifier(attack=0.05, defense=0.0, movement=0.15), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.05, movement=0.1), "Plains": TerrainModifier(attack=0.05, defense=0.0, movement=0.1)}), unit_id="rangers_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon', 'category_mountaineers', 'category_rangers'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=1.2, hard_attack=0.2, defense=17.0, breakthrough=2.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=67.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=7.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Desert": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Forest": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "Hills": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Jungle": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Marsh": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Mountain": TerrainModifier(attack=0.0, defense=0.0, movement=0.1), "Plains": TerrainModifier(attack=0.0, defense=0.0, movement=0.05), "River": TerrainModifier(attack=0.0, defense=0.0, movement=0.1)}, battalion_multipliers=[BattalionMultiplier(category="category_artillery", soft_attack=0.1)]), unit_id="recon", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['recon'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_recon'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="self_propelled_super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.46,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), unit_id="signal_company", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['signal_company'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=13.2, hard_attack=2.0, defense=34.0, breakthrough=5.0,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=143.5, manpower=1000.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Fort": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0)}, battalion_multipliers=[BattalionMultiplier(category="category_all_infantry", breakthrough=0.1)]), unit_id="sturmtruppe_battalion", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="super_heavy_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['super_heavy_artillery'], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1940, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Anti-Air": SupportCompany("Super-Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=72.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_anti_air_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_anti_air', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy SP Artillery": SupportCompany("Super-Heavy SP Artillery", BaseStatistics(
                soft_attack=102.0, hard_attack=2.7, defense=8.75, breakthrough=0.875,
                max_hp=0.5, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_sp_artillery_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_self_propelled_artillery', 'category_divisional_support_battalions', 'category_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank": SupportCompany("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.25, defense=0.0, movement=-0.3), "Fort": TerrainModifier(attack=0.1, defense=0.05), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Jungle": TerrainModifier(attack=-0.35, defense=-0.35, movement=-0.3), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3, movement=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "River": TerrainModifier(attack=-0.25, defense=-0.25, movement=-0.3), "Urban": TerrainModifier(attack=-0.3, defense=-0.3)}), unit_id="super_heavy_armor", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_tanks', 'category_support_battalions', 'category_divisional_support_battalions', 'category_front_line', 'category_all_armor', 'category_army'], year_unlocked=1941, is_special_project=True, is_country_locked=False),
        "Super-Heavy Tank Destroyer": SupportCompany("Super-Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.8, hard_attack=80.5, defense=8.75, breakthrough=0.45,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=204.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Amphibious": TerrainModifier(attack=-1.0, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.4), "Fort": TerrainModifier(attack=0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.7, defense=0.0, movement=-0.4), "Marsh": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.2), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "River": TerrainModifier(attack=-0.5, defense=0.0, movement=-0.5), "Urban": TerrainModifier(attack=-0.6, defense=-0.2)}), unit_id="super_heavy_tank_destroyer_brigade", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_tank_destroyers', 'category_support_battalions', 'category_divisional_support_battalions'], year_unlocked=1943, is_special_project=True, is_country_locked=False),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=2.4, hard_attack=9.0, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=144.0, manpower=300.0, armor=0.0, piercing=88.0,
                hardness=0.0, air_attack=35.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_divisional_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.4, hard_attack=24.0, defense=2.4, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=144.0, manpower=300.0, armor=0.0, piercing=156.25,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=23.8, hard_attack=2.0, defense=9.5, breakthrough=8.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=54.0, manpower=300.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=34.0, hard_attack=0.5, defense=8.0, breakthrough=10.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=60.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_artillery", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=[], categories=['category_support_battalions', 'category_divisional_support_battalions', 'category_army', 'category_artillery', 'category_support_artillery', 'category_rocket_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=34.0, breakthrough=2.5,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=67.6, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Snow": TerrainModifier(attack=0.25, defense=0.25, movement=0.3)}), unit_id="winter_logistics_support", is_divisional=True, is_regimental=False, allowed_battalion_groups=[], same_support_type=['logistics_company'], categories=['category_front_line', 'category_support_battalions', 'category_divisional_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=True),
    },
}

Regimental_Support_Companies: Dict[str, Dict[str, SupportCompany]] = {
    "1934": {
        "Anti-Air Battery": SupportCompany("Anti-Air Battery", BaseStatistics(
                soft_attack=1.2, hard_attack=2.8, defense=1.6, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=7.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_regimental_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank Battery": SupportCompany("Anti-Tank Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=7.0, defense=1.6, breakthrough=0.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=48.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Gun Battery": SupportCompany("Field Gun Battery", BaseStatistics(
                soft_attack=6.5, hard_attack=0.5, defense=2.75, breakthrough=2.5,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=21.0, manpower=180.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="field_guns", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Fire Support Team": SupportCompany("Fire Support Team", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=15.0, breakthrough=2.0,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=32.9, manpower=240.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air Battery": SupportCompany("Heavy SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.36, defense=1.0, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=375.0, manpower=180.0, armor=15.3, piercing=25.0,
                hardness=0.8, air_attack=12.75, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer Support": SupportCompany("Heavy Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=12.5, defense=2.68, breakthrough=0.1,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.09,
                ic_cost=375.0, manpower=180.0, armor=23.8, piercing=96.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air Battery": SupportCompany("Light SP Anti-Air Battery", BaseStatistics(
                soft_attack=0.68, hard_attack=0.34, defense=1.0, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.05,
                ic_cost=150.0, manpower=180.0, armor=1.7, piercing=5.0,
                hardness=0.5, air_attack=11.25, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer Support": SupportCompany("Light Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=5.0, defense=2.68, breakthrough=0.1,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=120.0, manpower=180.0, armor=3.4, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air Battery": SupportCompany("Medium SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.02, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=180.0, manpower=180.0, armor=15.3, piercing=40.0,
                hardness=0.65, air_attack=16.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer Support": SupportCompany("Medium Tank Destroyer Support", BaseStatistics(
                soft_attack=1.7, hard_attack=10.0, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=180.0, manpower=180.0, armor=20.4, piercing=88.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Modern SP Anti-Air Battery": SupportCompany("Modern SP Anti-Air Battery", BaseStatistics(
                soft_attack=3.06, hard_attack=2.55, defense=2.0, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=420.0, manpower=180.0, armor=30.6, piercing=100.0,
                hardness=0.85, air_attack=37.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer Support": SupportCompany("Modern Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=21.0, defense=5.36, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=420.0, manpower=180.0, armor=44.2, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Motorized Fire Support Team": SupportCompany("Motorized Fire Support Team", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=15.0, breakthrough=5.25,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=45.4, manpower=240.0, armor=0.0, piercing=1.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="mot_fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support', 'mobile_combat_support', 'armor', 'armor_combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery Battery": SupportCompany("Rocket Artillery Battery", BaseStatistics(
                soft_attack=8.0, hard_attack=0.25, defense=3.25, breakthrough=4.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_regimental_support_battalions', 'category_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1936": {
        "Anti-Air Battery": SupportCompany("Anti-Air Battery", BaseStatistics(
                soft_attack=1.2, hard_attack=2.8, defense=1.6, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=7.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_regimental_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank Battery": SupportCompany("Anti-Tank Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=7.0, defense=1.6, breakthrough=0.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=48.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Gun Battery": SupportCompany("Field Gun Battery", BaseStatistics(
                soft_attack=7.8, hard_attack=0.5, defense=2.75, breakthrough=2.5,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=21.0, manpower=180.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="field_guns", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Fire Support Team": SupportCompany("Fire Support Team", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=16.5, breakthrough=3.0,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=35.0, manpower=240.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air Battery": SupportCompany("Heavy SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.36, defense=1.0, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=375.0, manpower=180.0, armor=15.3, piercing=25.0,
                hardness=0.8, air_attack=12.75, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer Support": SupportCompany("Heavy Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=12.5, defense=2.68, breakthrough=0.1,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.09,
                ic_cost=375.0, manpower=180.0, armor=23.8, piercing=96.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air Battery": SupportCompany("Light SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.02, hard_attack=0.51, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.05,
                ic_cost=165.0, manpower=180.0, armor=3.4, piercing=20.0,
                hardness=0.5, air_attack=12.75, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer Support": SupportCompany("Light Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=8.0, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=135.0, manpower=180.0, armor=5.1, piercing=77.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air Battery": SupportCompany("Medium SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.02, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=180.0, manpower=180.0, armor=15.3, piercing=40.0,
                hardness=0.65, air_attack=16.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer Support": SupportCompany("Medium Tank Destroyer Support", BaseStatistics(
                soft_attack=1.7, hard_attack=10.0, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=180.0, manpower=180.0, armor=20.4, piercing=88.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Modern SP Anti-Air Battery": SupportCompany("Modern SP Anti-Air Battery", BaseStatistics(
                soft_attack=3.06, hard_attack=2.55, defense=2.0, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=420.0, manpower=180.0, armor=30.6, piercing=100.0,
                hardness=0.85, air_attack=37.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer Support": SupportCompany("Modern Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=21.0, defense=5.36, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=420.0, manpower=180.0, armor=44.2, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Motorized Fire Support Team": SupportCompany("Motorized Fire Support Team", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=16.5, breakthrough=6.8,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=47.5, manpower=240.0, armor=0.0, piercing=4.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="mot_fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support', 'mobile_combat_support', 'armor', 'armor_combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery Battery": SupportCompany("Rocket Artillery Battery", BaseStatistics(
                soft_attack=8.0, hard_attack=0.25, defense=3.25, breakthrough=4.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_regimental_support_battalions', 'category_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1939": {
        "Anti-Air Battery": SupportCompany("Anti-Air Battery", BaseStatistics(
                soft_attack=1.2, hard_attack=2.8, defense=1.6, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=9.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_regimental_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank Battery": SupportCompany("Anti-Tank Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=9.0, defense=1.6, breakthrough=0.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=64.0, manpower=180.0, armor=0.0, piercing=60.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Gun Battery": SupportCompany("Field Gun Battery", BaseStatistics(
                soft_attack=9.0, hard_attack=0.75, defense=3.75, breakthrough=3.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="field_guns", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Fire Support Team": SupportCompany("Fire Support Team", BaseStatistics(
                soft_attack=5.4, hard_attack=0.75, defense=25.2, breakthrough=4.6,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=37.4, manpower=240.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air Battery": SupportCompany("Heavy SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.36, defense=1.0, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=375.0, manpower=180.0, armor=15.3, piercing=25.0,
                hardness=0.8, air_attack=13.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer Support": SupportCompany("Heavy Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=13.125, defense=2.68, breakthrough=0.1,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.09,
                ic_cost=375.0, manpower=180.0, armor=23.8, piercing=100.8,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air Battery": SupportCompany("Light SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.02, hard_attack=0.51, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.05,
                ic_cost=165.0, manpower=180.0, armor=3.4, piercing=20.0,
                hardness=0.5, air_attack=13.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer Support": SupportCompany("Light Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=8.4, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=135.0, manpower=180.0, armor=5.1, piercing=80.85,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air Battery": SupportCompany("Medium SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.02, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=180.0, manpower=180.0, armor=15.3, piercing=40.0,
                hardness=0.65, air_attack=17.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer Support": SupportCompany("Medium Tank Destroyer Support", BaseStatistics(
                soft_attack=1.7, hard_attack=10.5, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=180.0, manpower=180.0, armor=20.4, piercing=92.4,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Modern SP Anti-Air Battery": SupportCompany("Modern SP Anti-Air Battery", BaseStatistics(
                soft_attack=3.06, hard_attack=2.55, defense=2.0, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=420.0, manpower=180.0, armor=30.6, piercing=100.0,
                hardness=0.85, air_attack=40.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer Support": SupportCompany("Modern Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=22.05, defense=5.36, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=420.0, manpower=180.0, armor=44.2, piercing=173.25,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Motorized Fire Support Team": SupportCompany("Motorized Fire Support Team", BaseStatistics(
                soft_attack=5.4, hard_attack=0.75, defense=25.2, breakthrough=8.1,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=49.9, manpower=240.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="mot_fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support', 'mobile_combat_support', 'armor', 'armor_combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery Battery": SupportCompany("Rocket Artillery Battery", BaseStatistics(
                soft_attack=8.0, hard_attack=0.25, defense=3.25, breakthrough=4.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_regimental_support_battalions', 'category_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1940": {
        "Anti-Air Battery": SupportCompany("Anti-Air Battery", BaseStatistics(
                soft_attack=1.4, hard_attack=4.4, defense=1.6, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=80.0, manpower=180.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=12.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_regimental_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank Battery": SupportCompany("Anti-Tank Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=9.9, defense=1.6, breakthrough=0.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=80.0, manpower=180.0, armor=0.0, piercing=90.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Gun Battery": SupportCompany("Field Gun Battery", BaseStatistics(
                soft_attack=10.5, hard_attack=0.75, defense=3.75, breakthrough=3.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="field_guns", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Fire Support Team": SupportCompany("Fire Support Team", BaseStatistics(
                soft_attack=6.3, hard_attack=0.75, defense=29.4, breakthrough=5.2,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=37.4, manpower=240.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air Battery": SupportCompany("Heavy SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.36, defense=1.0, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=375.0, manpower=180.0, armor=15.3, piercing=25.0,
                hardness=0.8, air_attack=13.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer Support": SupportCompany("Heavy Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=13.125, defense=2.68, breakthrough=0.1,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.09,
                ic_cost=375.0, manpower=180.0, armor=23.8, piercing=100.8,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air Battery": SupportCompany("Light SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.02, hard_attack=0.51, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.05,
                ic_cost=165.0, manpower=180.0, armor=3.4, piercing=20.0,
                hardness=0.5, air_attack=13.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer Support": SupportCompany("Light Tank Destroyer Support", BaseStatistics(
                soft_attack=2.04, hard_attack=8.4, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=135.0, manpower=180.0, armor=5.1, piercing=80.85,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air Battery": SupportCompany("Medium SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.02, defense=1.25, breakthrough=0.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=180.0, manpower=180.0, armor=15.3, piercing=40.0,
                hardness=0.65, air_attack=17.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer Support": SupportCompany("Medium Tank Destroyer Support", BaseStatistics(
                soft_attack=1.7, hard_attack=10.5, defense=3.35, breakthrough=0.13,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=180.0, manpower=180.0, armor=20.4, piercing=92.4,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Modern SP Anti-Air Battery": SupportCompany("Modern SP Anti-Air Battery", BaseStatistics(
                soft_attack=3.06, hard_attack=2.55, defense=2.0, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=420.0, manpower=180.0, armor=30.6, piercing=100.0,
                hardness=0.85, air_attack=40.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer Support": SupportCompany("Modern Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=22.05, defense=5.36, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=420.0, manpower=180.0, armor=44.2, piercing=173.25,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Motorized Fire Support Team": SupportCompany("Motorized Fire Support Team", BaseStatistics(
                soft_attack=6.75, hard_attack=0.75, defense=29.4, breakthrough=9.45,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=49.9, manpower=240.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="mot_fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support', 'mobile_combat_support', 'armor', 'armor_combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery Battery": SupportCompany("Rocket Artillery Battery", BaseStatistics(
                soft_attack=8.0, hard_attack=0.25, defense=3.25, breakthrough=4.25,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=24.0, manpower=180.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_regimental_support_battalions', 'category_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
    "1945": {
        "Anti-Air Battery": SupportCompany("Anti-Air Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=6.0, defense=1.6, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=96.0, manpower=180.0, armor=0.0, piercing=88.0,
                hardness=0.0, air_attack=22.4, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_air_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_army', 'category_anti_air', 'category_regimental_support_battalions'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Anti-Tank Battery": SupportCompany("Anti-Tank Battery", BaseStatistics(
                soft_attack=1.6, hard_attack=19.5, defense=1.6, breakthrough=0.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=96.0, manpower=180.0, armor=0.0, piercing=150.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="anti_tank_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_front_line', 'category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_anti_tank', 'category_mobile_anti_tank'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Field Gun Battery": SupportCompany("Field Gun Battery", BaseStatistics(
                soft_attack=15.3, hard_attack=1.0, defense=4.75, breakthrough=4.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=27.0, manpower=180.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="field_guns", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Fire Support Team": SupportCompany("Fire Support Team", BaseStatistics(
                soft_attack=9.6, hard_attack=1.6, defense=40.8, breakthrough=7.25,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=40.7, manpower=240.0, armor=0.0, piercing=20.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1918, is_special_project=False, is_country_locked=False),
        "Heavy SP Anti-Air Battery": SupportCompany("Heavy SP Anti-Air Battery", BaseStatistics(
                soft_attack=2.55, hard_attack=2.04, defense=1.75, breakthrough=0.35,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=450.0, manpower=180.0, armor=30.6, piercing=88.0,
                hardness=0.8, air_attack=39.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Heavy Tank Destroyer Support": SupportCompany("Heavy Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=34.5, defense=4.69, breakthrough=0.18,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.09,
                ic_cost=450.0, manpower=180.0, armor=44.2, piercing=184.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="heavy_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light SP Anti-Air Battery": SupportCompany("Light SP Anti-Air Battery", BaseStatistics(
                soft_attack=1.53, hard_attack=1.36, defense=1.75, breakthrough=0.35,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.05,
                ic_cost=180.0, manpower=180.0, armor=8.5, piercing=35.0,
                hardness=0.5, air_attack=28.8, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Light Tank Destroyer Support": SupportCompany("Light Tank Destroyer Support", BaseStatistics(
                soft_attack=2.72, hard_attack=13.8, defense=4.69, breakthrough=0.18,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=150.0, manpower=180.0, armor=10.2, piercing=113.85,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="light_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1934, is_special_project=False, is_country_locked=False),
        "Medium SP Anti-Air Battery": SupportCompany("Medium SP Anti-Air Battery", BaseStatistics(
                soft_attack=2.55, hard_attack=2.04, defense=1.75, breakthrough=0.35,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=210.0, manpower=180.0, armor=19.72, piercing=70.0,
                hardness=0.65, air_attack=38.7, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Medium Tank Destroyer Support": SupportCompany("Medium Tank Destroyer Support", BaseStatistics(
                soft_attack=2.72, hard_attack=18.4, defense=4.69, breakthrough=0.18,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.07,
                ic_cost=210.0, manpower=180.0, armor=30.6, piercing=138.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="medium_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1939, is_special_project=False, is_country_locked=False),
        "Modern SP Anti-Air Battery": SupportCompany("Modern SP Anti-Air Battery", BaseStatistics(
                soft_attack=3.06, hard_attack=2.55, defense=2.0, breakthrough=0.4,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.06,
                ic_cost=420.0, manpower=180.0, armor=30.6, piercing=100.0,
                hardness=0.85, air_attack=45.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_sp_anti_air_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_self_propelled_anti_air_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Modern Tank Destroyer Support": SupportCompany("Modern Tank Destroyer Support", BaseStatistics(
                soft_attack=3.4, hard_attack=24.15, defense=5.36, breakthrough=0.2,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=420.0, manpower=180.0, armor=44.2, piercing=189.75,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="modern_tank_destroyer_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['armor', 'mobile_combat_support', 'armor_combat_support'], same_support_type=[], categories=['category_front_line', 'category_all_armor', 'category_army', 'category_support_battalions', 'category_regimental_support_battalions', 'category_tank_destroyer_regimental_support'], year_unlocked=1945, is_special_project=False, is_country_locked=False),
        "Motorized Fire Support Team": SupportCompany("Motorized Fire Support Team", BaseStatistics(
                soft_attack=11.4, hard_attack=1.6, defense=40.8, breakthrough=13.0,
                max_hp=0.6, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=53.2, manpower=240.0, armor=0.0, piercing=20.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.2
            ), unit_id="mot_fire_support", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support', 'mobile_combat_support', 'armor', 'armor_combat_support'], same_support_type=[], categories=['category_support_battalions', 'category_regimental_support_battalions', 'category_army'], year_unlocked=1936, is_special_project=False, is_country_locked=False),
        "Rocket Artillery Battery": SupportCompany("Rocket Artillery Battery", BaseStatistics(
                soft_attack=18.0, hard_attack=0.25, defense=4.0, breakthrough=5.0,
                max_hp=0.1, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=30.0, manpower=180.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), unit_id="rocket_battery", is_divisional=False, is_regimental=True, allowed_battalion_groups=['infantry', 'mobile', 'combat_support'], same_support_type=[], categories=['category_regimental_support_battalions', 'category_support_battalions', 'category_army', 'category_regimental_support_artillery'], year_unlocked=1940, is_special_project=False, is_country_locked=False),
    },
}

# Backward-compatible alias dictionary for Divisional Support Companies
_DIVISIONAL_SUPPORT_ALIASES: Dict[str, str] = {
    "Airborne Light armour": "Airborne Light Armor",
    "Armoured Car Recon Company": "Armored Car Recon Company",
    "Cavalry Recon Company": "Recon Company",
    "Elephantry": "Elephantry Recon",
    "Super Heavy SP Anti-Air": "Super-Heavy SP Anti-Air",
    "Super Heavy SP Artillery": "Super-Heavy SP Artillery",
    "Super Heavy Tank": "Super-Heavy Tank",
    "Super Heavy Tank Destroyer": "Super-Heavy Tank Destroyer",
}

Support_Companies: Dict[str, Dict[str, SupportCompany]] = {
    year: {
        **Divisional_Support_Companies[year],
        **{alias: Divisional_Support_Companies[year][target] for alias, target in _DIVISIONAL_SUPPORT_ALIASES.items()},
    }
    for year in SUPPORTED_YEARS
}

All_Support_Companies: Dict[str, Dict[str, SupportCompany]] = {
    year: {
        **Support_Companies[year],
        **Regimental_Support_Companies[year],
    }
    for year in SUPPORTED_YEARS
}


def get_available_battalions(
    year: str,
    allow_special_projects: bool = True,
    allow_country_locked: bool = False,
    strict_year_unlock: bool = True,
) -> Dict[str, Battalion]:
    """
    Returns a dictionary of canonical line battalions available in ``year`` matching
    the requested filter rules (deduplicating backward-compatible alias keys).
    """
    if year not in All_Battalions:
        raise ValueError(f"Unsupported year {year!r}. Choose from {SUPPORTED_YEARS}.")
    year_int = int(year)
    result: Dict[str, Battalion] = {}
    seen_ids = set()
    for name, bat in All_Battalions[year].items():
        if name != bat.name:
            continue
        if bat.unit_id in seen_ids:
            continue
        if strict_year_unlock and bat.year_unlocked > year_int:
            continue
        if not allow_special_projects and bat.is_special_project:
            continue
        if not allow_country_locked and bat.is_country_locked:
            continue
        seen_ids.add(bat.unit_id)
        result[name] = bat
    return result


def get_available_divisional_supports(
    year: str,
    allow_special_projects: bool = True,
    allow_country_locked: bool = False,
    strict_year_unlock: bool = True,
) -> Dict[str, SupportCompany]:
    """
    Returns a dictionary of canonical divisional support companies available in ``year``
    matching the requested filter rules.
    """
    if year not in Divisional_Support_Companies:
        raise ValueError(f"Unsupported year {year!r}. Choose from {SUPPORTED_YEARS}.")
    year_int = int(year)
    result: Dict[str, SupportCompany] = {}
    for name, comp in Divisional_Support_Companies[year].items():
        if strict_year_unlock and comp.year_unlocked > year_int:
            continue
        if not allow_special_projects and comp.is_special_project:
            continue
        if not allow_country_locked and comp.is_country_locked:
            continue
        result[name] = comp
    return result


def get_available_regimental_supports(
    year: str,
    allow_special_projects: bool = True,
    allow_country_locked: bool = False,
    strict_year_unlock: bool = True,
) -> Dict[str, SupportCompany]:
    """
    Returns a dictionary of canonical v1.19 regimental support companies available in ``year``
    matching the requested filter rules.
    """
    if year not in Regimental_Support_Companies:
        raise ValueError(f"Unsupported year {year!r}. Choose from {SUPPORTED_YEARS}.")
    year_int = int(year)
    result: Dict[str, SupportCompany] = {}
    for name, comp in Regimental_Support_Companies[year].items():
        if strict_year_unlock and comp.year_unlocked > year_int:
            continue
        if not allow_special_projects and comp.is_special_project:
            continue
        if not allow_country_locked and comp.is_country_locked:
            continue
        result[name] = comp
    return result

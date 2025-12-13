from typing import Dict
from battalion import Battalion
from support_company import SupportCompany
from stats import BaseStatistics
from modifiers import UnitModifiers, TerrainModifier

All_Battalions: Dict[str, Dict[str, Battalion]] = {
    "1934": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.75, defense=46.0, breakthrough=6.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=450.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=120.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=0.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=2.0, breakthrough=12.0,
                max_hp=5.0, organization=20.0, combat_width=2.0, supply_use=0.14,
                ic_cost=210.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=25.0, hard_attack=2.0, defense=10.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.21,
                ic_cost=126.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Bicycle": Battalion("Bicycle", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05)})),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.12,
                ic_cost=51.6, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Elephantry": Battalion("Elephantry", BaseStatistics(
                soft_attack=23.2, hard_attack=2.5, defense=32.0, breakthrough=11.7,
                max_hp=30.0, organization=55.0, combat_width=2.0, supply_use=0.12,
                ic_cost=235.0, manpower=1100.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=6.75, hard_attack=4.0, defense=2.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=200.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=17.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=55.0, hard_attack=1.0, defense=4.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.6,
                ic_cost=600.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.32,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=25.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=500.0, manpower=500.0, armor=70.0, piercing=96.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=2.85, hard_attack=0.5, defense=17.0, breakthrough=2.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=34.4, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=2.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=150.0, manpower=500.0, armor=5.0, piercing=5.0,
                hardness=0.5, air_attack=15.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=34.0, hard_attack=0.5, defense=4.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.42,
                ic_cost=288.0, manpower=500.0, armor=5.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=29.9,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=480.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=10.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=240.0, manpower=500.0, armor=10.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.3, defense=0.0)})),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=3.3, hard_attack=2.5, defense=46.0, breakthrough=8.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=443.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.05)})),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=6.75, hard_attack=3.0, defense=2.5, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=22.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=42.0, hard_attack=1.0, defense=5.0, breakthrough=3.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=432.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=5.0, hard_attack=20.0, defense=5.0, breakthrough=1.3,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=288.0, manpower=500.0, armor=60.0, piercing=88.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=13.5, hard_attack=7.5, defense=4.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=336.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=80.0, hard_attack=3.0, defense=8.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=10.0, hard_attack=42.0, defense=8.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=672.0, manpower=500.0, armor=130.0, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=15.0, breakthrough=17.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=277.5, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=245.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=269.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=25.0, hard_attack=2.0, defense=10.0, breakthrough=11.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=7.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.065,
                ic_cost=130.5, manpower=1200.0, armor=0.0, piercing=1.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mountain": Battalion("Mountain", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Mountain": TerrainModifier(attack=0.35, defense=0.1), "Hills": TerrainModifier(attack=0.2, defense=0.05)})),
        "Paratrooper": Battalion("Paratrooper", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=36.55, manpower=850.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=9.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=14.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1936": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.75, defense=46.0, breakthrough=6.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=450.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=120.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=15.0, defense=4.0, breakthrough=0.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=75.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=2.0, breakthrough=12.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.14,
                ic_cost=240.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=27.5, hard_attack=2.0, defense=10.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.2,
                ic_cost=126.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Bicycle": Battalion("Bicycle", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=90.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05)})),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.4, breakthrough=3.1,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.12,
                ic_cost=60.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Elephantry": Battalion("Elephantry", BaseStatistics(
                soft_attack=23.2, hard_attack=2.5, defense=32.0, breakthrough=11.7,
                max_hp=30.0, organization=55.0, combat_width=2.0, supply_use=0.12,
                ic_cost=235.0, manpower=1100.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=6.8, hard_attack=4.0, defense=2.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=200.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=17.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=55.0, hard_attack=1.0, defense=4.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.6,
                ic_cost=600.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=25.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=500.0, manpower=500.0, armor=70.0, piercing=96.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=23.1, breakthrough=3.2,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=50.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=2.85, hard_attack=0.5, defense=17.0, breakthrough=2.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=34.4, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=2.5, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=165.0, manpower=500.0, armor=10.0, piercing=20.0,
                hardness=0.5, air_attack=17.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=42.0, hard_attack=1.0, defense=5.0, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.4,
                ic_cost=324.0, manpower=500.0, armor=10.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=540.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=16.0, defense=5.0, breakthrough=1.3,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=270.0, manpower=500.0, armor=15.0, piercing=77.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.7, breakthrough=4.0,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=75.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.3, defense=0.0)})),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=3.3, hard_attack=2.5, defense=46.0, breakthrough=8.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.14,
                ic_cost=443.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.05)})),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=6.75, hard_attack=3.0, defense=2.5, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=22.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=42.0, hard_attack=1.0, defense=5.0, breakthrough=3.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.46,
                ic_cost=432.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=41.4,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=5.0, hard_attack=20.0, defense=5.0, breakthrough=1.3,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=288.0, manpower=500.0, armor=60.0, piercing=88.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=13.5, hard_attack=7.5, defense=4.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=336.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=80.0, hard_attack=3.0, defense=8.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=10.0, hard_attack=42.0, defense=8.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=672.0, manpower=500.0, armor=130.0, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=15.0, breakthrough=17.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=277.5, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=245.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=269.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=25.0, hard_attack=2.0, defense=10.0, breakthrough=11.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=23.1, breakthrough=3.2,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.11,
                ic_cost=175.0, manpower=1200.0, armor=0.0, piercing=4.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mountain": Battalion("Mountain", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Mountain": TerrainModifier(attack=0.35, defense=0.1), "Hills": TerrainModifier(attack=0.2, defense=0.05)})),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.7, breakthrough=4.0,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.07,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Paratrooper": Battalion("Paratrooper", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.7, breakthrough=3.1,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.06,
                ic_cost=65.0, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=36.55, manpower=850.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=9.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.22,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=14.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1940": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.75, defense=46.0, breakthrough=6.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=450.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=3.5, hard_attack=11.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=150.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=27.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=24.2, defense=4.0, breakthrough=0.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=180.0, manpower=500.0, armor=0.0, piercing=105.6,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=3.0, breakthrough=16.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.14,
                ic_cost=360.0, manpower=500.0, armor=10.0, piercing=8.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=2.0, defense=15.0, breakthrough=7.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.2,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Bicycle": Battalion("Bicycle", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=100.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05)})),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=29.7, breakthrough=4.2,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.12,
                ic_cost=72.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Elephantry": Battalion("Elephantry", BaseStatistics(
                soft_attack=23.2, hard_attack=2.5, defense=32.0, breakthrough=11.7,
                max_hp=30.0, organization=55.0, combat_width=2.0, supply_use=0.12,
                ic_cost=235.0, manpower=1100.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=6.8, hard_attack=4.0, defense=2.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=200.0, manpower=500.0, armor=45.0, piercing=25.0,
                hardness=0.8, air_attack=17.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=55.0, hard_attack=1.0, defense=4.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.6,
                ic_cost=600.0, manpower=500.0, armor=45.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=15.0, hard_attack=12.0, defense=6.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1000.0, manpower=500.0, armor=70.0, piercing=35.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=25.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=500.0, manpower=500.0, armor=70.0, piercing=96.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=32.2, breakthrough=4.6,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=60.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=2.85, hard_attack=0.5, defense=17.0, breakthrough=2.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=34.4, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=2.5, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=165.0, manpower=500.0, armor=10.0, piercing=20.0,
                hardness=0.5, air_attack=17.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=42.0, hard_attack=1.0, defense=5.0, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.4,
                ic_cost=324.0, manpower=500.0, armor=10.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=16.0, hard_attack=6.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=540.0, manpower=500.0, armor=15.0, piercing=30.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=6.0, hard_attack=16.0, defense=5.0, breakthrough=1.3,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=270.0, manpower=500.0, armor=15.0, piercing=77.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=10.3, hard_attack=1.5, defense=31.9, breakthrough=5.6,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.06,
                ic_cost=90.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.3, defense=0.0)})),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=10.8, hard_attack=7.5, defense=62.1, breakthrough=9.2,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=460.0, manpower=1200.0, armor=10.0, piercing=16.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.05)})),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=6.8, hard_attack=3.0, defense=2.5, breakthrough=2.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=144.0, manpower=500.0, armor=45.0, piercing=40.0,
                hardness=0.65, air_attack=22.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=42.0, hard_attack=1.0, defense=5.0, breakthrough=3.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.44,
                ic_cost=432.0, manpower=500.0, armor=45.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=19.0, hard_attack=14.0, defense=5.0, breakthrough=36.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=600.0, manpower=500.0, armor=60.0, piercing=61.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=5.0, hard_attack=20.0, defense=5.0, breakthrough=1.3,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=288.0, manpower=500.0, armor=60.0, piercing=88.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=13.5, hard_attack=7.5, defense=4.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.1,
                ic_cost=336.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=80.0, hard_attack=3.0, defense=8.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=96.6,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=10.0, hard_attack=42.0, defense=8.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=672.0, manpower=500.0, armor=130.0, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=15.0, breakthrough=17.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=277.5, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=245.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=269.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=25.0, hard_attack=2.0, defense=10.0, breakthrough=11.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=9.9, hard_attack=1.5, defense=32.2, breakthrough=4.6,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.11,
                ic_cost=185.0, manpower=1200.0, armor=0.0, piercing=5.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Motorized Rocket Artillery": Battalion("Motorized Rocket Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=15.0, breakthrough=12.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.28,
                ic_cost=277.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Mountain": Battalion("Mountain", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Mountain": TerrainModifier(attack=0.35, defense=0.1), "Hills": TerrainModifier(attack=0.2, defense=0.05)})),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=10.3, hard_attack=1.5, defense=31.9, breakthrough=5.6,
                max_hp=20.0, organization=80.0, combat_width=2.0, supply_use=0.07,
                ic_cost=84.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Paratrooper": Battalion("Paratrooper", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=10.3, hard_attack=1.5, defense=31.9, breakthrough=4.4,
                max_hp=22.0, organization=80.0, combat_width=2.0, supply_use=0.06,
                ic_cost=78.0, manpower=1000.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=36.55, manpower=850.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=9.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.2,
                ic_cost=144.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=14.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1945": {
        "Amphibious Tank Battalion": Battalion("Amphibious Tank Battalion", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=4.0, breakthrough=26.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=500.0, manpower=500.0, armor=20.0, piercing=10.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Amtrac Battalion": Battalion("Amtrac Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.75, defense=46.0, breakthrough=6.0,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=450.0, manpower=1200.0, armor=10.0, piercing=12.0,
                hardness=0.6, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Anti-Air": Battalion("Anti-Air", BaseStatistics(
                soft_attack=4.0, hard_attack=15.0, defense=4.0, breakthrough=1.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=180.0, manpower=500.0, armor=0.0, piercing=88.0,
                hardness=0.0, air_attack=41.6, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Anti-Tank": Battalion("Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=39.0, defense=4.0, breakthrough=0.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=151.2,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Armored Car": Battalion("Armored Car", BaseStatistics(
                soft_attack=13.0, hard_attack=4.0, defense=3.0, breakthrough=16.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.14,
                ic_cost=360.0, manpower=500.0, armor=10.0, piercing=8.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Artillery": Battalion("Artillery", BaseStatistics(
                soft_attack=47.6, hard_attack=2.0, defense=18.0, breakthrough=8.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.2,
                ic_cost=162.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Bicycle": Battalion("Bicycle", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Bicycle Battalion": Battalion("Bicycle Battalion", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=34.0, breakthrough=5.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=110.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Camelry": Battalion("Camelry", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=30.0, organization=70.0, combat_width=2.0, supply_use=0.1,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0), "Desert": TerrainModifier(attack=0.05, defense=0.05)})),
        "Cavalry": Battalion("Cavalry", BaseStatistics(
                soft_attack=14.4, hard_attack=2.0, defense=36.7, breakthrough=5.4,
                max_hp=25.0, organization=70.0, combat_width=2.0, supply_use=0.12,
                ic_cost=84.0, manpower=1000.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Elephantry": Battalion("Elephantry", BaseStatistics(
                soft_attack=23.2, hard_attack=2.5, defense=32.0, breakthrough=11.7,
                max_hp=30.0, organization=55.0, combat_width=2.0, supply_use=0.12,
                ic_cost=235.0, manpower=1100.0, armor=0.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.05, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Hills": TerrainModifier(attack=-0.05, defense=0.0)})),
        "Heavy Amphibious Tank Battalion": Battalion("Heavy Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Heavy SP Anti-Air": Battalion("Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.2, hard_attack=6.0, defense=3.5, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=240.0, manpower=500.0, armor=90.0, piercing=88.0,
                hardness=0.8, air_attack=44.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy SP Artillery": Battalion("Heavy SP Artillery", BaseStatistics(
                soft_attack=80.0, hard_attack=2.5, defense=7.0, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.6,
                ic_cost=720.0, manpower=500.0, armor=90.0, piercing=8.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank": Battalion("Heavy Tank", BaseStatistics(
                soft_attack=35.0, hard_attack=40.0, defense=9.0, breakthrough=67.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.3,
                ic_cost=1200.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Heavy Tank Destroyer": Battalion("Heavy Tank Destroyer", BaseStatistics(
                soft_attack=10.0, hard_attack=60.0, defense=7.0, breakthrough=1.8,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.3,
                ic_cost=600.0, manpower=500.0, armor=130.0, piercing=160.0,
                hardness=0.95, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.6, defense=0.0), "Marsh": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.3, defense=0.0), "Forest": TerrainModifier(attack=-0.4, defense=0.0), "Urban": TerrainModifier(attack=-0.5, defense=-0.2), "Hills": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Infantry": Battalion("Infantry", BaseStatistics(
                soft_attack=13.8, hard_attack=3.0, defense=40.8, breakthrough=6.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.07,
                ic_cost=70.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Irregular Infantry": Battalion("Irregular Infantry", BaseStatistics(
                soft_attack=2.85, hard_attack=0.5, defense=17.0, breakthrough=2.0,
                max_hp=30.0, organization=45.0, combat_width=2.0, supply_use=0.04,
                ic_cost=34.4, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light Amphibious Tank Battalion": Battalion("Light Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Light SP Anti-Air": Battalion("Light SP Anti-Air", BaseStatistics(
                soft_attack=6.8, hard_attack=4.0, defense=3.5, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=180.0, manpower=500.0, armor=25.0, piercing=35.0,
                hardness=0.5, air_attack=32.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light SP Artillery": Battalion("Light SP Artillery", BaseStatistics(
                soft_attack=46.0, hard_attack=1.5, defense=7.0, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.4,
                ic_cost=360.0, manpower=500.0, armor=25.0, piercing=4.0,
                hardness=0.5, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank": Battalion("Light Tank", BaseStatistics(
                soft_attack=22.0, hard_attack=9.0, defense=6.0, breakthrough=46.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=600.0, manpower=500.0, armor=30.0, piercing=50.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Mountain": TerrainModifier(attack=-0.1, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Light Tank Destroyer": Battalion("Light Tank Destroyer", BaseStatistics(
                soft_attack=8.0, hard_attack=24.0, defense=7.0, breakthrough=1.8,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.2,
                ic_cost=300.0, manpower=500.0, armor=30.0, piercing=99.0,
                hardness=0.8, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1)})),
        "Marine Commandos": Battalion("Marine Commandos", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=64.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Marines": Battalion("Marines", BaseStatistics(
                soft_attack=15.0, hard_attack=3.0, defense=39.8, breakthrough=7.1,
                max_hp=20.0, organization=90.0, combat_width=2.0, supply_use=0.06,
                ic_cost=105.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.3, defense=0.0)})),
        "Mechanized Infantry": Battalion("Mechanized Infantry", BaseStatistics(
                soft_attack=17.4, hard_attack=11.3, defense=81.6, breakthrough=13.2,
                max_hp=30.0, organization=60.0, combat_width=2.0, supply_use=0.18,
                ic_cost=670.0, manpower=1200.0, armor=20.0, piercing=93.0,
                hardness=0.84, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.3, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Forest": TerrainModifier(attack=-0.2, defense=0.0), "Urban": TerrainModifier(attack=0.0, defense=-0.05)})),
        "Medium Amphibious Tank Battalion": Battalion("Medium Amphibious Tank Battalion", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.2,
                ic_cost=0.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Medium SP Anti-Air": Battalion("Medium SP Anti-Air", BaseStatistics(
                soft_attack=11.2, hard_attack=6.0, defense=3.5, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=168.0, manpower=500.0, armor=58.0, piercing=70.0,
                hardness=0.65, air_attack=43.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium SP Artillery": Battalion("Medium SP Artillery", BaseStatistics(
                soft_attack=55.0, hard_attack=2.0, defense=7.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.44,
                ic_cost=504.0, manpower=500.0, armor=58.0, piercing=5.0,
                hardness=0.65, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank": Battalion("Medium Tank", BaseStatistics(
                soft_attack=32.0, hard_attack=24.0, defense=9.0, breakthrough=66.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.22,
                ic_cost=700.0, manpower=500.0, armor=90.0, piercing=91.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Medium Tank Destroyer": Battalion("Medium Tank Destroyer", BaseStatistics(
                soft_attack=8.0, hard_attack=32.0, defense=7.0, breakthrough=1.8,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.22,
                ic_cost=336.0, manpower=500.0, armor=90.0, piercing=120.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.3, defense=0.0), "Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Militia": Battalion("Militia", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=25.0, organization=50.0, combat_width=2.0, supply_use=0.06,
                ic_cost=43.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Modern SP Anti-Air": Battalion("Modern SP Anti-Air", BaseStatistics(
                soft_attack=13.5, hard_attack=7.5, defense=4.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=336.0, manpower=500.0, armor=90.0, piercing=100.0,
                hardness=0.85, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern SP Artillery": Battalion("Modern SP Artillery", BaseStatistics(
                soft_attack=80.0, hard_attack=3.0, defense=8.0, breakthrough=4.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.5,
                ic_cost=1120.0, manpower=500.0, armor=90.0, piercing=10.0,
                hardness=0.85, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank": Battalion("Modern Tank", BaseStatistics(
                soft_attack=40.0, hard_attack=32.0, defense=10.0, breakthrough=84.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.25,
                ic_cost=1400.0, manpower=500.0, armor=130.0, piercing=131.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=-0.1, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Modern Tank Destroyer": Battalion("Modern Tank Destroyer", BaseStatistics(
                soft_attack=10.0, hard_attack=42.0, defense=8.0, breakthrough=2.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=672.0, manpower=500.0, armor=130.0, piercing=165.0,
                hardness=0.98, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=0.0), "Mountain": TerrainModifier(attack=-0.2, defense=0.0), "Forest": TerrainModifier(attack=-0.3, defense=0.0), "Urban": TerrainModifier(attack=-0.4, defense=-0.1), "Hills": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Mot. R. Artillery": Battalion("Mot. R. Artillery", BaseStatistics(
                soft_attack=36.0, hard_attack=1.0, defense=15.0, breakthrough=17.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=277.5, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Air": Battalion("Motorized Anti-Air", BaseStatistics(
                soft_attack=3.0, hard_attack=7.0, defense=4.0, breakthrough=6.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=245.0, manpower=500.0, armor=0.0, piercing=25.0,
                hardness=0.1, air_attack=19.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Anti-Tank": Battalion("Motorized Anti-Tank", BaseStatistics(
                soft_attack=4.0, hard_attack=20.0, defense=4.0, breakthrough=5.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.15,
                ic_cost=269.0, manpower=500.0, armor=0.0, piercing=60.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Artillery": Battalion("Motorized Artillery", BaseStatistics(
                soft_attack=25.0, hard_attack=2.0, defense=10.0, breakthrough=11.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=216.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Motorized Infantry": Battalion("Motorized Infantry", BaseStatistics(
                soft_attack=14.4, hard_attack=3.0, defense=40.8, breakthrough=6.0,
                max_hp=25.0, organization=60.0, combat_width=2.0, supply_use=0.11,
                ic_cost=195.0, manpower=1200.0, armor=0.0, piercing=30.0,
                hardness=0.2, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.1, defense=0.0), "Jungle": TerrainModifier(attack=-0.2, defense=0.0), "Mountain": TerrainModifier(attack=-0.05, defense=0.0), "Marsh": TerrainModifier(attack=-0.1, defense=0.0)})),
        "Motorized Rocket Artillery": Battalion("Motorized Rocket Artillery", BaseStatistics(
                soft_attack=61.2, hard_attack=1.0, defense=15.0, breakthrough=12.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.28,
                ic_cost=277.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Mountain": Battalion("Mountain", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=60.2, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Mountain": TerrainModifier(attack=0.35, defense=0.1), "Hills": TerrainModifier(attack=0.2, defense=0.05)})),
        "Mountaineers": Battalion("Mountaineers", BaseStatistics(
                soft_attack=15.0, hard_attack=3.0, defense=39.8, breakthrough=7.1,
                max_hp=20.0, organization=90.0, combat_width=2.0, supply_use=0.07,
                ic_cost=98.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Paratrooper": Battalion("Paratrooper", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=22.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=55.9, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Paratroopers": Battalion("Paratroopers", BaseStatistics(
                soft_attack=15.0, hard_attack=3.0, defense=39.8, breakthrough=5.6,
                max_hp=22.0, organization=90.0, combat_width=2.0, supply_use=0.06,
                ic_cost=91.0, manpower=1000.0, armor=0.0, piercing=30.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.4
            )),
        "Penal Battalion": Battalion("Penal Battalion", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=15.0, organization=70.0, combat_width=2.0, supply_use=0.05,
                ic_cost=36.55, manpower=850.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Rocket Artillery": Battalion("Rocket Artillery", BaseStatistics(
                soft_attack=53.2, hard_attack=1.0, defense=15.0, breakthrough=12.0,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.2,
                ic_cost=180.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=-0.2, defense=0.0), "Jungle": TerrainModifier(attack=-0.25, defense=0.0), "Marsh": TerrainModifier(attack=-0.2, defense=0.0)})),
        "Super Heavy SP Anti-Air": Battalion("Super Heavy SP Anti-Air", BaseStatistics(
                soft_attack=17.2, hard_attack=9.0, defense=3.5, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=1.0, supply_use=0.1,
                ic_cost=400.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.9, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Super Heavy SP Artillery": Battalion("Super Heavy SP Artillery", BaseStatistics(
                soft_attack=85.0, hard_attack=3.0, defense=7.0, breakthrough=3.5,
                max_hp=0.6, organization=0.0, combat_width=3.0, supply_use=0.8,
                ic_cost=1200.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.9, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Super Heavy Tank Destroyer": Battalion("Super Heavy Tank Destroyer", BaseStatistics(
                soft_attack=12.0, hard_attack=70.0, defense=7.0, breakthrough=1.8,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.4,
                ic_cost=700.0, manpower=500.0, armor=145.0, piercing=170.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Super-Heavy Tank": Battalion("Super-Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=2.0, supply_use=0.4,
                ic_cost=1500.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.99, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Truck-drawn Rocket Artillery": Battalion("Truck-drawn Rocket Artillery", BaseStatistics(
                soft_attack=30.0, hard_attack=1.0, defense=12.0, breakthrough=14.0,
                max_hp=0.6, organization=0.0, combat_width=2.0, supply_use=0.25,
                ic_cost=234.0, manpower=500.0, armor=0.0, piercing=2.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
}

Support_Companies: Dict[str, Dict[str, SupportCompany]] = {
    "1934": {
        "Airborne Light armour": SupportCompany("Airborne Light armour", BaseStatistics(
                soft_attack=6.0, hard_attack=3.0, defense=2.0, breakthrough=13.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=168.0, manpower=500.0, armor=2.5, piercing=15.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=485.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.0, defense=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.1)})),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armoured Car Recon Company": SupportCompany("Armoured Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=96.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=22.0, breakthrough=2.6,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=385.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.05, defense=0.1), "Urban": TerrainModifier(attack=0.2, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.1)})),
        "Cavalry Recon Company": SupportCompany("Cavalry Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=10.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=124.0, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.0, defense=0.25), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25)})),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=6.0, hard_attack=8.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=26.0, breakthrough=10.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=228.6, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.1,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.0
            )),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=21.0, breakthrough=2.6,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=164.3, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=80.0, hard_attack=65.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=300.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=0.0, air_attack=32.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=-0.4), "Urban": TerrainModifier(attack=-0.3, defense=-0.3), "Hills": TerrainModifier(attack=-0.2, defense=-0.2), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3), "Forest": TerrainModifier(attack=-0.3, defense=-0.3)})),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=1.3, hard_attack=0.4, defense=2.0, breakthrough=13.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.1,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.0
            )),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.02,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=50.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=3.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=20.0, breakthrough=3.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=107.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=164.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.1, defense=0.2)})),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=77.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Plains": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.0, defense=0.05), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=5.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=98.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.1,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=104.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Urban": TerrainModifier(attack=0.1, defense=0.0)})),
        "Super Heavy SP Anti-Air": SupportCompany("Super Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=2.275,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.0, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy SP Artillery": SupportCompany("Super Heavy SP Artillery", BaseStatistics(
                soft_attack=85.0, hard_attack=3.0, defense=7.0, breakthrough=2.6,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy Tank": SupportCompany("Super Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.35, defense=-0.35), "Urban": TerrainModifier(attack=-0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "Forest": TerrainModifier(attack=-0.25, defense=0.0)})),
        "Super Heavy Tank Destroyer": SupportCompany("Super Heavy Tank Destroyer", BaseStatistics(
                soft_attack=12.0, hard_attack=70.0, defense=7.0, breakthrough=1.35,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=170.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=1.8, hard_attack=4.2, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=80.0, manpower=300.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=15.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.0, hard_attack=10.0, defense=2.0, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=51.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=15.0, hard_attack=1.2, defense=6.0, breakthrough=3.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=42.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=15.0, hard_attack=0.5, defense=6.0, breakthrough=4.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=20.0, breakthrough=1.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1936": {
        "Airborne Light armour": SupportCompany("Airborne Light armour", BaseStatistics(
                soft_attack=6.0, hard_attack=3.0, defense=2.0, breakthrough=13.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=168.0, manpower=500.0, armor=2.5, piercing=15.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=485.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.0, defense=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.1)})),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armoured Car Recon Company": SupportCompany("Armoured Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=96.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=22.0, breakthrough=2.6,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=385.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.05, defense=0.1), "Urban": TerrainModifier(attack=0.2, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.1)})),
        "Cavalry Recon Company": SupportCompany("Cavalry Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=10.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=24.2, breakthrough=4.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=125.0, manpower=300.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.0, defense=0.25), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25)})),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=6.0, hard_attack=8.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=26.0, breakthrough=10.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=228.6, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.1,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.0
            )),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=21.0, breakthrough=2.6,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=164.3, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=80.0, hard_attack=65.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=300.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=0.0, air_attack=32.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=-0.4), "Urban": TerrainModifier(attack=-0.3, defense=-0.3), "Hills": TerrainModifier(attack=-0.2, defense=-0.2), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3), "Forest": TerrainModifier(attack=-0.3, defense=-0.3)})),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=1.3, hard_attack=0.4, defense=2.0, breakthrough=13.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.02,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=6.0, hard_attack=1.0, defense=22.0, breakthrough=3.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=3.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=20.0, breakthrough=3.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=107.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=164.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.1, defense=0.2)})),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=77.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Plains": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.0, defense=0.05), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.6, hard_attack=0.1, defense=11.0, breakthrough=1.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=60.0, manpower=500.0, armor=0.0, piercing=4.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=104.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Urban": TerrainModifier(attack=0.1, defense=0.0)})),
        "Super Heavy SP Anti-Air": SupportCompany("Super Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=2.275,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.0, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy SP Artillery": SupportCompany("Super Heavy SP Artillery", BaseStatistics(
                soft_attack=85.0, hard_attack=3.0, defense=7.0, breakthrough=2.6,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy Tank": SupportCompany("Super Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.35, defense=-0.35), "Urban": TerrainModifier(attack=-0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "Forest": TerrainModifier(attack=-0.25, defense=0.0)})),
        "Super Heavy Tank Destroyer": SupportCompany("Super Heavy Tank Destroyer", BaseStatistics(
                soft_attack=12.0, hard_attack=70.0, defense=7.0, breakthrough=1.35,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=170.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=1.8, hard_attack=4.2, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=80.0, manpower=300.0, armor=0.0, piercing=25.0,
                hardness=0.0, air_attack=15.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.0, hard_attack=7.5, defense=2.0, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=63.8,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=17.5, hard_attack=1.2, defense=6.0, breakthrough=3.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=42.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=15.0, hard_attack=0.5, defense=6.0, breakthrough=4.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=20.0, breakthrough=1.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1940": {
        "Airborne Light armour": SupportCompany("Airborne Light armour", BaseStatistics(
                soft_attack=6.0, hard_attack=3.0, defense=2.0, breakthrough=13.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=168.0, manpower=500.0, armor=2.5, piercing=15.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=485.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.0, defense=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.1)})),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armoured Car Recon Company": SupportCompany("Armoured Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=96.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=22.0, breakthrough=2.6,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=385.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.05, defense=0.1), "Urban": TerrainModifier(attack=0.2, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.1)})),
        "Cavalry Recon Company": SupportCompany("Cavalry Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=10.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=4.5, hard_attack=1.5, defense=30.8, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=126.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.0, defense=0.25), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25)})),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=6.0, hard_attack=8.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=26.0, breakthrough=10.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=228.6, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.1,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.0
            )),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=21.0, breakthrough=2.6,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=164.3, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=80.0, hard_attack=65.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=300.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=0.0, air_attack=32.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=-0.4), "Urban": TerrainModifier(attack=-0.3, defense=-0.3), "Hills": TerrainModifier(attack=-0.2, defense=-0.2), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3), "Forest": TerrainModifier(attack=-0.3, defense=-0.3)})),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=1.3, hard_attack=0.4, defense=2.0, breakthrough=13.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.02,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=9.0, hard_attack=1.5, defense=28.0, breakthrough=4.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=64.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=3.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=20.0, breakthrough=3.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=107.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=164.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.1, defense=0.2)})),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=77.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Plains": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.0, defense=0.05), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=0.9, hard_attack=0.1, defense=14.0, breakthrough=2.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=64.0, manpower=500.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=104.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Urban": TerrainModifier(attack=0.1, defense=0.0)})),
        "Super Heavy SP Anti-Air": SupportCompany("Super Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=2.275,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.0, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy SP Artillery": SupportCompany("Super Heavy SP Artillery", BaseStatistics(
                soft_attack=85.0, hard_attack=3.0, defense=7.0, breakthrough=2.6,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy Tank": SupportCompany("Super Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.35, defense=-0.35), "Urban": TerrainModifier(attack=-0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "Forest": TerrainModifier(attack=-0.25, defense=0.0)})),
        "Super Heavy Tank Destroyer": SupportCompany("Super Heavy Tank Destroyer", BaseStatistics(
                soft_attack=12.0, hard_attack=70.0, defense=7.0, breakthrough=1.35,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=170.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=2.1, hard_attack=6.6, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=100.0, manpower=300.0, armor=0.0, piercing=60.0,
                hardness=0.0, air_attack=22.5, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.0, hard_attack=13.2, defense=2.0, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=120.0, manpower=300.0, armor=0.0, piercing=92.4,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=24.0, hard_attack=1.2, defense=9.0, breakthrough=4.2,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=48.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=15.0, hard_attack=0.5, defense=6.0, breakthrough=4.5,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=96.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=20.0, breakthrough=1.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
    "1945": {
        "Airborne Light armour": SupportCompany("Airborne Light armour", BaseStatistics(
                soft_attack=6.0, hard_attack=3.0, defense=2.0, breakthrough=13.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=168.0, manpower=500.0, armor=2.5, piercing=15.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Engineer Company": SupportCompany("Armored Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.5, breakthrough=6.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=485.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=3.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.0, defense=0.15), "Marsh": TerrainModifier(attack=0.0, defense=0.15), "Forest": TerrainModifier(attack=0.0, defense=0.25), "Urban": TerrainModifier(attack=0.2, defense=0.1), "Hills": TerrainModifier(attack=0.0, defense=0.1)})),
        "Armored Maintenance Company": SupportCompany("Armored Maintenance Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armored Signal Company": SupportCompany("Armored Signal Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=10.0, breakthrough=3.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.035,
                ic_cost=365.0, manpower=500.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.12,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Armoured Car Recon Company": SupportCompany("Armoured Car Recon Company", BaseStatistics(
                soft_attack=3.0, hard_attack=1.0, defense=1.0, breakthrough=9.6,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=96.0, manpower=500.0, armor=3.0, piercing=6.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Battalion": SupportCompany("Assault Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=22.0, breakthrough=2.6,
                max_hp=40.0, organization=10.0, combat_width=0.0, supply_use=0.06,
                ic_cost=83.0, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Assault Engineer Company": SupportCompany("Assault Engineer Company", BaseStatistics(
                soft_attack=3.0, hard_attack=2.0, defense=11.0, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=385.0, manpower=300.0, armor=12.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.05, defense=0.1), "Urban": TerrainModifier(attack=0.2, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.1), "Marsh": TerrainModifier(attack=0.05, defense=0.1), "Forest": TerrainModifier(attack=0.05, defense=0.1)})),
        "Cavalry Recon Company": SupportCompany("Cavalry Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=10.0, breakthrough=1.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Engineer Company": SupportCompany("Engineer Company", BaseStatistics(
                soft_attack=6.0, hard_attack=2.0, defense=37.4, breakthrough=7.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=127.0, manpower=300.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            ), modifiers=UnitModifiers(terrain_modifiers={"Forest": TerrainModifier(attack=0.0, defense=0.25), "Jungle": TerrainModifier(attack=0.0, defense=0.25), "Marsh": TerrainModifier(attack=0.0, defense=0.25)})),
        "Field Hospital": SupportCompany("Field Hospital", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.05,
                ic_cost=170.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Heavy Flame Tank Company": SupportCompany("Heavy Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Helicopter Brigade": SupportCompany("Helicopter Brigade", BaseStatistics(
                soft_attack=6.0, hard_attack=8.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Med-Evac": SupportCompany("Helicopter Med-Evac", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=292.5, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Recon": SupportCompany("Helicopter Recon", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=26.0, breakthrough=10.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.07,
                ic_cost=228.6, manpower=500.0, armor=4.0, piercing=11.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Helicopter Transports": SupportCompany("Helicopter Transports", BaseStatistics(
                soft_attack=6.0, hard_attack=13.0, defense=4.0, breakthrough=11.0,
                max_hp=1.0, organization=12.0, combat_width=0.0, supply_use=0.1,
                ic_cost=195.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=-0.1, recovery_rate=0.0
            )),
        "Jungle Pioneers": SupportCompany("Jungle Pioneers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=21.0, breakthrough=2.6,
                max_hp=1.0, organization=30.0, combat_width=0.0, supply_use=0.1,
                ic_cost=164.3, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Land Cruiser": SupportCompany("Land Cruiser", BaseStatistics(
                soft_attack=80.0, hard_attack=65.0, defense=35.0, breakthrough=120.0,
                max_hp=15.0, organization=60.0, combat_width=0.0, supply_use=0.6,
                ic_cost=300.0, manpower=1000.0, armor=180.0, piercing=160.0,
                hardness=0.0, air_attack=32.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.4, defense=-0.4), "Urban": TerrainModifier(attack=-0.3, defense=-0.3), "Hills": TerrainModifier(attack=-0.2, defense=-0.2), "Marsh": TerrainModifier(attack=-0.4, defense=-0.4), "Mountain": TerrainModifier(attack=-0.3, defense=-0.3), "Forest": TerrainModifier(attack=-0.3, defense=-0.3)})),
        "Light Flame Tank Company": SupportCompany("Light Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.1, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Urban": TerrainModifier(attack=0.1, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Light Tank Recon Company": SupportCompany("Light Tank Recon Company", BaseStatistics(
                soft_attack=1.3, hard_attack=0.4, defense=2.0, breakthrough=13.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=192.0, manpower=500.0, armor=10.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Logistics Company": SupportCompany("Logistics Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=10.0, combat_width=0.0, supply_use=0.0,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Long Range Patrol Company": SupportCompany("Long Range Patrol Company", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=10.0, organization=60.0, combat_width=0.0, supply_use=0.04,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.02,
                recon=2.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Maintenance Company": SupportCompany("Maintenance Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.03,
                ic_cost=100.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Medium Flame Tank Company": SupportCompany("Medium Flame Tank Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.025,
                ic_cost=0.0, manpower=300.0, armor=0.0, piercing=0.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=0.15, defense=0.0), "Marsh": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.1, defense=0.0), "Urban": TerrainModifier(attack=0.15, defense=0.0), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Military Police": SupportCompany("Military Police", BaseStatistics(
                soft_attack=12.0, hard_attack=2.0, defense=34.0, breakthrough=5.0,
                max_hp=1.0, organization=0.0, combat_width=0.0, supply_use=0.02,
                ic_cost=68.0, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Motorized Military Police": SupportCompany("Motorized Military Police", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=3.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.03,
                ic_cost=51.6, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Motorized Recon Company": SupportCompany("Motorized Recon Company", BaseStatistics(
                soft_attack=0.3, hard_attack=0.05, defense=20.0, breakthrough=3.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=107.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.5, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Pioneers": SupportCompany("Pioneers", BaseStatistics(
                soft_attack=1.5, hard_attack=0.5, defense=22.0, breakthrough=3.0,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=164.3, manpower=300.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=2.5, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Marsh": TerrainModifier(attack=0.1, defense=0.2)})),
        "Rangers": SupportCompany("Rangers", BaseStatistics(
                soft_attack=3.0, hard_attack=0.5, defense=20.0, breakthrough=2.0,
                max_hp=2.0, organization=30.0, combat_width=0.0, supply_use=0.06,
                ic_cost=77.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=1.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Plains": TerrainModifier(attack=0.05, defense=0.0), "Forest": TerrainModifier(attack=0.05, defense=0.0), "Mountain": TerrainModifier(attack=0.0, defense=0.05), "Hills": TerrainModifier(attack=0.05, defense=0.0)})),
        "Recon Company": SupportCompany("Recon Company", BaseStatistics(
                soft_attack=1.2, hard_attack=0.2, defense=17.0, breakthrough=2.5,
                max_hp=2.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=68.0, manpower=500.0, armor=0.0, piercing=10.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Self-Propelled Super-Heavy Artillery": SupportCompany("Self-Propelled Super-Heavy Artillery", BaseStatistics(
                soft_attack=44.0, hard_attack=6.0, defense=14.0, breakthrough=14.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.35,
                ic_cost=195.0, manpower=1000.0, armor=6.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Signal Company": SupportCompany("Signal Company", BaseStatistics(
                soft_attack=0.0, hard_attack=0.0, defense=0.0, breakthrough=0.0,
                max_hp=1.0, organization=20.0, combat_width=0.0, supply_use=0.02,
                ic_cost=105.0, manpower=500.0, armor=0.0, piercing=0.0,
                hardness=0.1, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.3
            )),
        "Sturmtruppe Battalion": SupportCompany("Sturmtruppe Battalion", BaseStatistics(
                soft_attack=3.3, hard_attack=0.5, defense=20.0, breakthrough=2.6,
                max_hp=20.0, organization=70.0, combat_width=0.0, supply_use=0.05,
                ic_cost=104.5, manpower=1000.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Urban": TerrainModifier(attack=0.1, defense=0.0)})),
        "Super Heavy SP Anti-Air": SupportCompany("Super Heavy SP Anti-Air", BaseStatistics(
                soft_attack=11.5, hard_attack=9.0, defense=3.5, breakthrough=2.275,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=98.0,
                hardness=0.0, air_attack=50.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=0.0), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy SP Artillery": SupportCompany("Super Heavy SP Artillery", BaseStatistics(
                soft_attack=85.0, hard_attack=3.0, defense=7.0, breakthrough=2.6,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.8,
                ic_cost=2000.0, manpower=500.0, armor=100.0, piercing=9.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super Heavy Tank": SupportCompany("Super Heavy Tank", BaseStatistics(
                soft_attack=38.0, hard_attack=45.0, defense=10.0, breakthrough=74.0,
                max_hp=2.0, organization=10.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=146.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.35, defense=-0.35), "Urban": TerrainModifier(attack=-0.3, defense=0.0), "Hills": TerrainModifier(attack=-0.15, defense=-0.15), "Marsh": TerrainModifier(attack=-0.3, defense=-0.3), "Mountain": TerrainModifier(attack=-0.2, defense=-0.2), "Forest": TerrainModifier(attack=-0.25, defense=0.0)})),
        "Super Heavy Tank Destroyer": SupportCompany("Super Heavy Tank Destroyer", BaseStatistics(
                soft_attack=12.0, hard_attack=70.0, defense=7.0, breakthrough=1.35,
                max_hp=0.6, organization=0.0, combat_width=0.0, supply_use=0.4,
                ic_cost=2000.0, manpower=500.0, armor=145.0, piercing=170.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            ), modifiers=UnitModifiers(terrain_modifiers={"Jungle": TerrainModifier(attack=-0.7, defense=0.0), "Marsh": TerrainModifier(attack=-0.5, defense=0.0), "Mountain": TerrainModifier(attack=-0.4, defense=0.0), "Forest": TerrainModifier(attack=-0.5, defense=0.0), "Urban": TerrainModifier(attack=-0.6, defense=-0.2), "Hills": TerrainModifier(attack=-0.3, defense=0.0)})),
        "Super-Heavy Artillery": SupportCompany("Super-Heavy Artillery", BaseStatistics(
                soft_attack=35.0, hard_attack=4.0, defense=12.0, breakthrough=12.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.25,
                ic_cost=135.0, manpower=1000.0, armor=0.0, piercing=7.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
        "Support Anti-Air": SupportCompany("Support Anti-Air", BaseStatistics(
                soft_attack=2.4, hard_attack=9.0, defense=2.4, breakthrough=0.6,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.1,
                ic_cost=120.0, manpower=300.0, armor=0.0, piercing=88.0,
                hardness=0.0, air_attack=35.2, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Anti-Tank": SupportCompany("Support Anti-Tank", BaseStatistics(
                soft_attack=2.0, hard_attack=24.0, defense=2.0, breakthrough=0.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.08,
                ic_cost=144.0, manpower=300.0, armor=0.0, piercing=135.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Artillery": SupportCompany("Support Artillery", BaseStatistics(
                soft_attack=34.0, hard_attack=1.2, defense=10.8, breakthrough=4.8,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=54.0, manpower=300.0, armor=0.0, piercing=5.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Support Rocket Artillery": SupportCompany("Support Rocket Artillery", BaseStatistics(
                soft_attack=34.2, hard_attack=0.5, defense=7.5, breakthrough=6.0,
                max_hp=0.2, organization=0.0, combat_width=0.0, supply_use=0.16,
                ic_cost=120.0, manpower=300.0, armor=0.0, piercing=2.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.1
            )),
        "Winter Logistics Company": SupportCompany("Winter Logistics Company", BaseStatistics(
                soft_attack=1.5, hard_attack=0.25, defense=20.0, breakthrough=1.0,
                max_hp=2.0, organization=45.0, combat_width=0.0, supply_use=0.05,
                ic_cost=57.2, manpower=500.0, armor=0.0, piercing=1.0,
                hardness=0.0, air_attack=0.0, entrenchment=0.0, initiative=0.0,
                recon=0.0, supply_consumption_factor=0.0, recovery_rate=0.0
            )),
    },
}
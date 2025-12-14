import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

from division_database import (
    create_cheap_infantry_1934,
    create_standard_infantry_1936,
    create_offensive_infantry_1936,
    create_medium_armor_1940,
    create_heavy_infantry_1940,
    create_light_armor_1940,
    create_motorized_division_1940,
    create_mountaineer_division_1940,
    create_marine_division_1940
)
from terrain import PLAINS, MOUNTAIN, URBAN, MARSH, FOREST, HILLS, JUNGLE, DESERT

def run_battle_scenario(attacker, defender, terrain, scenario_name):
    print(f"\n{'='*60}")
    print(f"SCENARIO: {scenario_name}")
    print(f"{'='*60}")
    print(f"Attacker: {attacker.name}")
    print(f"Defender: {defender.name}")
    print(f"Terrain: {terrain.name}")
    print("-" * 60)
    
    # Print initial stats comparison
    att_stats = attacker.calculate_stats()
    def_stats = defender.calculate_stats()
    
    print(f"{'Stat':<20} {'Attacker':>10} {'Defender':>10}")
    print("-" * 45)
    print(f"{'Soft Attack':<20} {att_stats.soft_attack:>10.1f} {def_stats.soft_attack:>10.1f}")
    print(f"{'Hard Attack':<20} {att_stats.hard_attack:>10.1f} {def_stats.hard_attack:>10.1f}")
    print(f"{'Breakthrough':<20} {att_stats.breakthrough:>10.1f} {def_stats.breakthrough:>10.1f}")
    print(f"{'Defense':<20} {att_stats.defense:>10.1f} {def_stats.defense:>10.1f}")
    print(f"{'Armor':<20} {att_stats.armor:>10.1f} {def_stats.armor:>10.1f}")
    print(f"{'Piercing':<20} {att_stats.piercing:>10.1f} {def_stats.piercing:>10.1f}")
    print(f"{'Hardness':<20} {att_stats.hardness:>10.1%} {def_stats.hardness:>10.1%}")
    print("-" * 60)
    
    # Run Battle
    result = attacker.battle(defender, terrain, verbose=True)
    
    print(f"\n{'='*60}")
    print(f"RESULT: {result['winner']} WON")
    print(f"Duration: {result['duration_hours']} hours ({result['duration_days']:.1f} days)")
    print(f"Attacker Remaining ORG: {result['attacker_final_org']:.1f}")
    print(f"Defender Remaining ORG: {result['defender_final_org']:.1f}")
    print(f"{'='*60}\n")

def scenario_cheap_infantry_1934():
    """
    Cheap 1934 Infantry vs Standard 1936 Infantry on Plains.
    Testing cheap infantry.
    """
    attacker = create_cheap_infantry_1934()
    defender = create_cheap_infantry_1934()
    run_battle_scenario(attacker, defender, PLAINS, "Cheap Infantry (1934 vs 1934)")

def scenario_clash_of_infantry():
    """
    Standard 1936 Infantry vs Standard 1936 Infantry on Plains.
    Baseline test.
    """
    attacker = create_standard_infantry_1936()
    defender = create_standard_infantry_1936()
    run_battle_scenario(attacker, defender, PLAINS, "Clash of Infantry (1936)")

def scenario_blitzkrieg_breakthrough():
    """
    1940 Medium Armor vs 1936 Standard Infantry on Plains.
    Testing armor advantage and breakthrough.
    """
    attacker = create_medium_armor_1940()
    defender = create_standard_infantry_1936()
    run_battle_scenario(attacker, defender, PLAINS, "Blitzkrieg Breakthrough (1940 vs 1936)")

def scenario_mountain_warfare():
    """
    1940 Mountaineers vs 1940 Standard Infantry (upgraded) in Mountains.
    Testing terrain bonuses.
    """
    # Note: We don't have a 1940 Standard Infantry function, so we'll use 1936 for defender
    # or maybe Motorized 1940 as a proxy for "modern" infantry? 
    # Let's use Motorized 1940 for defender to make it a fair 1940 fight.
    attacker = create_mountaineer_division_1940()
    defender = create_motorized_division_1940() 
    run_battle_scenario(attacker, defender, MOUNTAIN, "Mountain Warfare (Mountaineers vs Motorized)")

def scenario_urban_assault():
    """
    1940 Heavy Infantry (Space Marines) vs 1940 Medium Armor in Urban.
    Testing high armor/piercing and urban penalties for tanks.
    """
    attacker = create_heavy_infantry_1940()
    defender = create_medium_armor_1940()
    run_battle_scenario(attacker, defender, URBAN, "Urban Assault (Space Marines vs Medium Armor)")

def scenario_jungle_skirmish():
    """
    1940 Marines vs 1936 Infantry in Jungle.
    Testing Marine bonuses in rough terrain.
    """
    attacker = create_marine_division_1940()
    defender = create_standard_infantry_1936()
    run_battle_scenario(attacker, defender, JUNGLE, "Jungle Skirmish (Marines vs Infantry)")

if __name__ == "__main__":
    # Run all scenarios
    scenario_cheap_infantry_1934()
    # scenario_blitzkrieg_breakthrough()
    # scenario_mountain_warfare()
    # scenario_urban_assault()
    # scenario_jungle_skirmish()

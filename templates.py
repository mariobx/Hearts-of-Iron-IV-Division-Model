from division import Division
from unit_database import All_Battalions, Support_Companies
from terrain import PLAINS, MOUNTAIN, ALL_TERRAINS
from battalion import Battalion
from stats import BaseStatistics

def create_division(name, year="1936", battalions=None, supports=None):
    div = Division(name)
    
    if battalions:
        for bat_name, count in battalions:
            bat = All_Battalions[year][bat_name]
            for _ in range(count):
                div.add_battalion(bat)
                
    if supports:
        for sup_name in supports:
            sup = Support_Companies[year][sup_name]
            div.add_support_company(sup)
            
    return div

def elephant_tank(year="1936"):
    return create_division(
        f"Elephant Tank ({year})",
        year,
        battalions=[("Elephantry", 5), ("Light Tank", 2)],
        supports=["Support Artillery", "Engineer Company", "Signal Company", "Support Anti-Air"]
    )

def inf_7_2(year="1936"):
    return create_division(
        f"7/2 Infantry ({year})", 
        year,
        battalions=[("Infantry", 7), ("Artillery", 2)],
        supports=["Engineer Company", "Support Artillery"] # Assuming names match DB
    )

def space_marines(year="1936"):
    # Note: Using Heavy Tank for Space Marines
    return create_division(
        f"Space Marines ({year})",
        year,
        battalions=[("Infantry", 7), ("Heavy Tank", 2)],
        supports=["Support Artillery", "Engineer Company", "Signal Company", "Support Anti-Air"] # Adjusted names to match likely DB keys
    )

def tank_buster(year="1936"):
    return create_division(
        f"Tank Buster ({year})",
        year,
        battalions=[("Mountain", 7), ("Anti-Tank", 2)],
        supports=["Support Anti-Tank", "Support Artillery", "Support Anti-Air", "Engineer Company"]
    )



def run_battle(attacker, defender, terrain):
    print(f"\n--- {attacker.name} vs {defender.name} ---")
    print(f"Terrain: {terrain.name} (Width: {terrain.combat_width}, Attack Debuff: {terrain.attack_debuff})")
    
    # Re-instantiate for clean state to avoid state carry-over between tests if reusing objects
    # (Though here we pass fresh objects usually)
    
    # Print Stats
    att_stats = attacker.calculate_stats()
    def_stats = defender.calculate_stats()
    
    att_mods = attacker.calculate_terrain_modifiers().get(terrain.name)
    def_mods = defender.calculate_terrain_modifiers().get(terrain.name)
    
    print(f"Attacker ({attacker.name}) Stats:")
    print(f"  Soft Attack: {att_stats.soft_attack:.1f}, Hard Attack: {att_stats.hard_attack:.1f}")
    print(f"  Armor: {att_stats.armor:.1f}, Piercing: {att_stats.piercing:.1f}, Hardness: {att_stats.hardness:.1%}")
    if att_mods:
        print(f"  Terrain Mods: Attack {att_mods.attack:+.2f}, Defense {att_mods.defense:+.2f}")

    print(f"Defender ({defender.name}) Stats:")
    print(f"  Soft Attack: {def_stats.soft_attack:.1f}, Hard Attack: {def_stats.hard_attack:.1f}")
    print(f"  Armor: {def_stats.armor:.1f}, Piercing: {def_stats.piercing:.1f}, Hardness: {def_stats.hardness:.1%}")
    if def_mods:
        print(f"  Terrain Mods: Attack {def_mods.attack:+.2f}, Defense {def_mods.defense:+.2f}")
    
    # Check Armor Advantage
    att_pierced = def_stats.piercing > att_stats.armor
    def_pierced = att_stats.piercing > def_stats.armor
    print(f"  Attacker Pierced? {att_pierced} (Def Piercing {def_stats.piercing:.1f} vs Att Armor {att_stats.armor:.1f})")
    print(f"  Defender Pierced? {def_pierced} (Att Piercing {att_stats.piercing:.1f} vs Def Armor {def_stats.armor:.1f})")
    
    # Run
    result = attacker.battle(defender, terrain)
    
    print(f"Winner: {result['winner']}")
    print(f"Duration: {result['duration_days']:.2f} days")
    print(f"Attacker Final Org: {result['attacker_final_org']:.1f}")
    print(f"Defender Final Org: {result['defender_final_org']:.1f}")

def elephant_tank_vs_inf72():
    for _, terrain in ALL_TERRAINS.items():
        run_battle(elephant_tank("1936"), inf_7_2("1945"), terrain)
    print("attacker elephants, now switching")
    for _, terrain in ALL_TERRAINS.items():
        run_battle(inf_7_2("1945"), elephant_tank("1936"), terrain)
    print("defender elephants")

def test_infantry_evolution():
    print("==================================================")
    print("INFANTRY EVOLUTION TESTS (Plains)")
    print("==================================================")
    
    years = ["1934", "1936", "1940", "1945"]
    
    # Standard 9 Infantry Division Template for comparison
    def create_standard_inf(year):
        return create_division(
            f"Infantry {year}",
            year,
            battalions=[("Infantry", 9)],
            supports=["Engineer Company", "Support Artillery", "Recon Company"] # Basic supports
        )

    # We need to check if "Recon Company" exists in DB, usually it's "Cavalry Recon Company" or similar.
    # Let's check keys in unit_database.py or just use "Engineer Company" and "Support Artillery" to be safe.
    # Looking at previous view_file, "Engineer Company" exists. "Support Artillery" might be named differently?
    # In unit_database.py (lines 1-100 view), I saw "Engineer Company".
    # I didn't see Support Artillery in the snippet, but I saw "Artillery" battalion.
    # Let's use a safer set or check DB keys.
    # Safe bet: Just Infantry battalions for raw comparison if supports are uncertain, 
    # but user asked for "Infantry" which usually implies 9/0 or 9/1.
    # Let's stick to 9 Infantry battalions + Engineer for now to minimize KeyErrors.
    
    matchups = [
        ("1934", "1936"),
        ("1936", "1940"),
        ("1940", "1945"),
        ("1934", "1945")
    ]
    
    for y1, y2 in matchups:
        # Attacker: Older year, Defender: Newer year (and vice versa?)
        # Let's do Older vs Newer
        
        # 1. Older Attacking Newer
        div1 = create_division(f"Infantry {y1}", y1, [("Infantry", 9)], ["Engineer Company"])
        div2 = create_division(f"Infantry {y2}", y2, [("Infantry", 9)], ["Engineer Company"])
        run_battle(div1, div2, PLAINS)
        
        # 2. Newer Attacking Older
        div1 = create_division(f"Infantry {y1}", y1, [("Infantry", 9)], ["Engineer Company"])
        div2 = create_division(f"Infantry {y2}", y2, [("Infantry", 9)], ["Engineer Company"])
        run_battle(div2, div1, PLAINS)

def tester():
    print("==================================================")
    print("TERRAIN BATTLE TESTS")
    print("==================================================")

    # 1. Define Templates (Using 1936 as baseline)
    inf_anti = tank_buster("1936")
    space_marine_div = space_marines("1936")

    # 2. Define Scenarios
    # We need to recreate divisions for each scenario to avoid state persistence
    
    scenarios = [
        ("Infantry vs Infantry (Plains)", tank_buster("1936"), tank_buster("1936"), PLAINS),
        ("Infantry vs Infantry (Mountains)", tank_buster("1936"), tank_buster("1936"), MOUNTAIN),
        ("Space Marines vs Infantry (Plains)", space_marines("1936"), tank_buster("1936"), PLAINS),
        ("Space Marines vs Infantry (Mountains)", space_marines("1936"), tank_buster("1936"), MOUNTAIN),
    ]

    # 3. Run Tests
    for name, attacker, defender, terrain in scenarios:
        run_battle(attacker, defender, terrain)

def test_tank_buster_vs_space_marine_evolution():
    print("==================================================")
    print("TANK BUSTER VS SPACE MARINE EVOLUTION (Plains)")
    print("==================================================")
    
    years = ["1934", "1945"]
    
    for year in years:
        print(f"\n>>> YEAR: {year} <<<")
        
        # Create Divisions
        tb = tank_buster(year)
        sm = space_marines(year)
        
        # Run Battle
        run_battle(tb, sm, PLAINS)

def main():
    # tester() 
    # test_infantry_evolution()
    # test_tank_buster_vs_space_marine_evolution()
    elephant_tank_vs_inf72()

if __name__ == "__main__":
    main()


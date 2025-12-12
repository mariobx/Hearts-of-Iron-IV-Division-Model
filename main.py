from division import Division
import unit_database as db

def print_division_stats(division: Division):
    stats = division.calculate_stats()
    print(f"--- {division.name} ---")
    print(f"Combat Width: {stats.combat_width}")
    print(f"Soft Attack:  {stats.soft_attack:.1f}")
    print(f"Hard Attack:  {stats.hard_attack:.1f}")
    print(f"Defense:      {stats.defense:.1f}")
    print(f"Breakthrough: {stats.breakthrough:.1f}")
    print(f"Organization: {stats.organization:.1f}")
    print(f"HP:           {stats.max_hp:.1f}")
    print(f"Armor:        {stats.armor:.1f}")
    print(f"Piercing:     {stats.piercing:.1f}")
    print(f"Hardness:     {stats.hardness*100:.1f}%")
    print(f"IC Cost:      {stats.ic_cost:.1f}")
    print(f"Manpower:     {stats.manpower:.0f}")
    print("")

def main():
    # 1. Standard "7/2" Infantry Division (20 Width)
    div_7_2 = Division("7/2 Infantry")
    for _ in range(7):
        div_7_2.add_battalion(db.create_infantry())
    for _ in range(2):
        div_7_2.add_battalion(db.create_artillery())
    
    div_7_2.add_support_company(db.create_engineer_company())
    div_7_2.add_support_company(db.create_support_artillery())
    div_7_2.add_support_company(db.create_recon_company())

    print_division_stats(div_7_2)

    # 2. "Space Marine" Division
    div_space_marine = Division("Space Marine")
    for _ in range(8):
        div_space_marine.add_battalion(db.create_infantry())
    div_space_marine.add_battalion(db.create_heavy_tank())
    div_space_marine.add_battalion(db.create_artillery())
    
    div_space_marine.add_support_company(db.create_engineer_company())
    div_space_marine.add_support_company(db.create_support_artillery())

    print_division_stats(div_space_marine)

    # 3. Medium Tank Division
    div_tank = Division("Medium Tank Division")
    for _ in range(8):
        div_tank.add_battalion(db.create_medium_tank())
    for _ in range(7):
        div_tank.add_battalion(db.create_motorized())
    
    div_tank.add_support_company(db.create_engineer_company())
    div_tank.add_support_company(db.create_logistics_company())
    div_tank.add_support_company(db.create_support_artillery())

    print_division_stats(div_tank)

if __name__ == "__main__":
    main()

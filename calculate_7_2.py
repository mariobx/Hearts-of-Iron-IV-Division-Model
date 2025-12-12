from division import Division
from unit_database import All_Battalions, Support_Companies

def main():
    # Create Division
    div = Division("7/2 Infantry Division")
    
    # Add Battalions
    # 7 Infantry
    infantry = All_Battalions["Infantry"]
    for _ in range(7):
        div.add_battalion(infantry)
        
    # 2 Artillery
    artillery = All_Battalions["Artillery"]
    for _ in range(2):
        div.add_battalion(artillery)
        
    # Add Support Companies
    # Engineer
    engineer = Support_Companies["Engineer Company"]
    div.add_support_company(engineer)
    
    # Support Artillery
    # Note: The key in Support_Companies is "Support Artillery"
    support_artillery = Support_Companies["Support Artillery"]
    div.add_support_company(support_artillery)
    
    # Print Stats
    div.print_stats_table()

if __name__ == "__main__":
    main()

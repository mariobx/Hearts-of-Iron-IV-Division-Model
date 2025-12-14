from division import Division
from unit_database import All_Battalions, Support_Companies
from support_company import SupportCompany
from battalion import Battalion


def create_cheap_infantry_1934() -> Division:
    """
    Creates a Cheap 1934 Infantry Division (18 Width).
    
    Composition:
    - 9 Infantry Battalions
    """
    div = Division("Cheap Infantry Division")
    
    # Line Battalions
    infantry = All_Battalions["1934"]["Infantry"]
    for _ in range(9):
        div.add_battalion(infantry)
        
    return div

def create_standard_infantry_1936() -> Division:
    """
    Creates a Standard 1936 Infantry Division (18 Width).
    
    Composition:
    - 9 Infantry Battalions
    - Support: Engineer Company, Support Artillery
    
    Role: Standard defensive line infantry. Cost-effective and reliable.
    """
    div = Division("Standard Infantry Division")
    
    # Line Battalions
    infantry = All_Battalions["1936"]["Infantry"]
    for _ in range(9):
        div.add_battalion(infantry)
        
    # Support Companies
    engineer = Support_Companies["1936"]["Engineer Company"]
    support_arty = Support_Companies["1936"]["Support Artillery"]
    
    if isinstance(engineer, SupportCompany):
        div.add_support_company(engineer)
    if isinstance(support_arty, SupportCompany):
        div.add_support_company(support_arty)
        
    return div

def create_offensive_infantry_1936() -> Division:
    """
    Creates a 1936 Offensive Infantry Division (7/2 Template).
    
    Composition:
    - 7 Infantry Battalions
    - 2 Artillery Battalions
    - Support: Engineer Company, Support Artillery, Cavalry Recon
    
    Role: Offensive infantry with increased soft attack for pushing enemy lines.
    """
    div = Division("7/2 Infantry Division")
    
    # Line Battalions
    infantry = All_Battalions["1936"]["Infantry"]
    artillery = All_Battalions["1936"]["Artillery"]
    
    for _ in range(7):
        div.add_battalion(infantry)
    for _ in range(2):
        div.add_battalion(artillery)
        
    # Support Companies
    engineer = Support_Companies["1936"]["Engineer Company"]
    support_arty = Support_Companies["1936"]["Support Artillery"]
    recon = Support_Companies["1936"]["Cavalry Recon Company"]
    
    for comp in [engineer, support_arty, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_medium_armor_1940() -> Division:
    """
    Creates a 1940 Medium Armor Division (30 Width).
    
    Composition:
    - 6 Medium Tank Battalions
    - 4 Motorized Infantry Battalions
    - Support: Engineer, Motorized Recon, Support AA, Support Artillery
    
    Role: Primary breakthrough unit. Balances speed, armor, and firepower.
    """
    div = Division("Medium Armor Division")
    
    # Line Battalions
    medium_tank = All_Battalions["1940"]["Medium Tank"]
    motorized = All_Battalions["1940"]["Motorized Infantry"]
    
    for _ in range(6):
        div.add_battalion(medium_tank)
    for _ in range(4):
        div.add_battalion(motorized)
        
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    recon = Support_Companies["1940"]["Motorized Recon Company"]
    support_aa = Support_Companies["1940"]["Support Anti-Air"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    
    for comp in [engineer, recon, support_aa, support_arty]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_heavy_infantry_1940() -> Division:
    """
    Creates a 1940 Heavy Infantry Division ("Space Marines").
    
    Composition:
    - 8 Infantry Battalions
    - 1 Heavy Tank Battalion
    - Support: Engineer, Support AA, Support AT
    
    Role: High-armor infantry designed to be unpiercable by standard enemy infantry.
    """
    div = Division("Heavy Infantry Division")
    
    # Line Battalions
    infantry = All_Battalions["1940"]["Infantry"]
    heavy_tank = All_Battalions["1940"]["Heavy Tank"]
    
    for _ in range(8):
        div.add_battalion(infantry)
    div.add_battalion(heavy_tank)
    
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    support_aa = Support_Companies["1940"]["Support Anti-Air"]
    support_at = Support_Companies["1940"]["Support Anti-Tank"]
    
    for comp in [engineer, support_aa, support_at]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_light_armor_1940() -> Division:
    """
    Creates a 1940 Light Armor Division.
    
    Composition:
    - 5 Light Tank Battalions
    - 5 Motorized Infantry Battalions
    - Support: Engineer, Motorized Recon
    
    Role: Fast exploitation unit for encircling enemies and overrunning rear areas.
    """
    div = Division("Light Armor Division")
    
    # Line Battalions
    light_tank = All_Battalions["1940"]["Light Tank"]
    motorized = All_Battalions["1940"]["Motorized Infantry"]
    
    for _ in range(5):
        div.add_battalion(light_tank)
    for _ in range(5):
        div.add_battalion(motorized)
        
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    recon = Support_Companies["1940"]["Motorized Recon Company"]
    
    for comp in [engineer, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_motorized_division_1940() -> Division:
    """
    Creates a 1940 Motorized Infantry Division.
    
    Composition:
    - 9 Motorized Infantry Battalions
    - Support: Engineer, Motorized Recon, Support Artillery
    
    Role: Fast infantry to follow tanks and hold breakthroughs.
    """
    div = Division("Motorized Infantry Division")
    
    # Line Battalions
    motorized = All_Battalions["1940"]["Motorized Infantry"]
    for _ in range(9):
        div.add_battalion(motorized)
        
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    recon = Support_Companies["1940"]["Motorized Recon Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    
    for comp in [engineer, recon, support_arty]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_mountaineer_division_1940() -> Division:
    """
    Creates a 1940 Mountaineer Division.
    
    Composition:
    - 9 Mountaineer Battalions
    - Support: Engineer, Support Artillery, Cavalry Recon
    
    Role: Specialized infantry for fighting in mountains and hills.
    """
    div = Division("Mountaineer Division")
    
    # Line Battalions
    mountaineer = All_Battalions["1940"]["Mountaineers"]
    for _ in range(9):
        div.add_battalion(mountaineer)
        
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    recon = Support_Companies["1940"]["Cavalry Recon Company"]
    
    for comp in [engineer, support_arty, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

def create_marine_division_1940() -> Division:
    """
    Creates a 1940 Marine Division.
    
    Composition:
    - 9 Marine Battalions
    - Support: Engineer, Support Artillery, Support AA
    
    Role: Specialized infantry for naval invasions and river crossings.
    """
    div = Division("Marine Division")
    
    # Line Battalions
    marine = All_Battalions["1940"]["Marines"]
    for _ in range(9):
        div.add_battalion(marine)
        
    # Support Companies
    engineer = Support_Companies["1940"]["Engineer Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    support_aa = Support_Companies["1940"]["Support Anti-Air"]
    
    for comp in [engineer, support_arty, support_aa]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)
            
    return div

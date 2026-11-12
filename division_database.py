"""
Historical & Benchmark Division Templates Database for Hearts of Iron IV (v1.19.4.2).

Provides factory functions for standard historical and competitive HOI4 division templates
across all 5 benchmark technology years (`1934`, `1936`, `1939`, `1940`, `1945`), including
Divisional Support Companies and v1.19 (`Operation Postern`) Regimental Support Companies.
"""

from typing import List
from division import Division
from unit_database import (
    All_Battalions,
    Support_Companies,
    Regimental_Support_Companies,
    SUPPORTED_YEARS,
)
from support_company import SupportCompany
from battalion import Battalion


def create_cheap_infantry_1934() -> Division:
    """
    Creates a Cheap 1934 Infantry Division (18 Width).

    Composition:
    - 9 Infantry Battalions (2 brigade columns: 5 + 4)
    """
    div = Division("Cheap Infantry Division")
    infantry = All_Battalions["1934"]["Infantry"]
    for _ in range(9):
        div.add_battalion(infantry)
    return div


def create_standard_infantry_1936() -> Division:
    """
    Creates a Standard 1936 Infantry Division (18 Width).

    Composition:
    - 9 Infantry Battalions
    - Divisional Support: Engineer Company, Support Artillery

    Role: Standard defensive line infantry. Cost-effective and reliable.
    """
    div = Division("Standard Infantry Division")
    infantry = All_Battalions["1936"]["Infantry"]
    for _ in range(9):
        div.add_battalion(infantry)

    engineer = Support_Companies["1936"]["Engineer Company"]
    support_arty = Support_Companies["1936"]["Support Artillery"]

    if isinstance(engineer, SupportCompany):
        div.add_support_company(engineer)
    if isinstance(support_arty, SupportCompany):
        div.add_support_company(support_arty)

    return div


def create_offensive_infantry_1936() -> Division:
    """
    Creates a 1936 Offensive Infantry Division (7/2 Template, 20 Width).

    Composition:
    - 7 Infantry Battalions
    - 2 Artillery Battalions
    - Divisional Support: Engineer Company, Support Artillery, Recon Company

    Role: Offensive infantry with increased soft attack for pushing enemy lines.
    """
    div = Division("7/2 Infantry Division")
    infantry = All_Battalions["1936"]["Infantry"]
    artillery = All_Battalions["1936"]["Artillery"]

    for _ in range(7):
        div.add_battalion(infantry)
    for _ in range(2):
        div.add_battalion(artillery)

    engineer = Support_Companies["1936"]["Engineer Company"]
    support_arty = Support_Companies["1936"]["Support Artillery"]
    recon = Support_Companies["1936"]["Cavalry Recon Company"]

    for comp in [engineer, support_arty, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_standard_infantry_1939() -> Division:
    """
    Creates a 1939 Wartime Infantry Division (21 Width, 9/1 Template) with v1.19 Regimental Support.

    Composition:
    - 9 Infantry Battalions + 1 Artillery Battalion
    - Divisional Support: Engineer Company, Support Artillery, Support Anti-Air, Recon Company
    - Regimental Support (v1.19): Field Gun Battery, Fire Support Team
    """
    div = Division("1939 9/1 Infantry Division")
    infantry = All_Battalions["1939"]["Infantry"]
    artillery = All_Battalions["1939"]["Artillery"]

    for _ in range(9):
        div.add_battalion(infantry)
    div.add_battalion(artillery)

    for s_name in ["Engineer Company", "Support Artillery", "Support Anti-Air", "Recon Company"]:
        div.add_support_company(Support_Companies["1939"][s_name])

    div.add_regimental_support(Regimental_Support_Companies["1939"]["Field Gun Battery"])
    div.add_regimental_support(Regimental_Support_Companies["1939"]["Fire Support Team"])
    return div


def create_medium_armor_1939() -> Division:
    """
    Creates a 1939 Early Blitzkrieg Medium Armor Division (20 Width).

    Composition:
    - 5 Medium Tank Battalions
    - 5 Motorized Infantry Battalions
    - Divisional Support: Engineer Company, Motorized Recon Company, Support Artillery, Support Anti-Air
    - Regimental Support (v1.19): Medium Tank Destroyer Support, Motorized Fire Support Team
    """
    div = Division("1939 Medium Armor Division")
    medium_tank = All_Battalions["1939"]["Medium Tank"]
    motorized = All_Battalions["1939"]["Motorized Infantry"]

    for _ in range(5):
        div.add_battalion(medium_tank)
    for _ in range(5):
        div.add_battalion(motorized)

    for s_name in ["Engineer Company", "Motorized Recon Company", "Support Artillery", "Support Anti-Air"]:
        div.add_support_company(Support_Companies["1939"][s_name])

    div.add_regimental_support(Regimental_Support_Companies["1939"]["Medium Tank Destroyer Support"])
    div.add_regimental_support(Regimental_Support_Companies["1939"]["Motorized Fire Support Team"])
    return div


def create_medium_armor_1940() -> Division:
    """
    Creates a 1940 Medium Armor Division (20 Width).

    Composition:
    - 6 Medium Tank Battalions
    - 4 Motorized Infantry Battalions
    - Divisional Support: Engineer, Motorized Recon, Support AA, Support Artillery

    Role: Primary breakthrough unit. Balances speed, armor, and firepower.
    """
    div = Division("Medium Armor Division")
    medium_tank = All_Battalions["1940"]["Medium Tank"]
    motorized = All_Battalions["1940"]["Motorized Infantry"]

    for _ in range(6):
        div.add_battalion(medium_tank)
    for _ in range(4):
        div.add_battalion(motorized)

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
    Creates a 1940 Heavy Infantry Division ("Space Marines", 18 Width).

    Composition:
    - 8 Infantry Battalions
    - 1 Heavy Tank Battalion
    - Divisional Support: Engineer, Support AA, Support AT

    Role: High-armor infantry designed to be unpiercable by standard enemy infantry.
    """
    div = Division("Heavy Infantry Division")
    infantry = All_Battalions["1940"]["Infantry"]
    heavy_tank = All_Battalions["1940"]["Heavy Tank"]

    for _ in range(8):
        div.add_battalion(infantry)
    div.add_battalion(heavy_tank)

    engineer = Support_Companies["1940"]["Engineer Company"]
    support_aa = Support_Companies["1940"]["Support Anti-Air"]
    support_at = Support_Companies["1940"]["Support Anti-Tank"]

    for comp in [engineer, support_aa, support_at]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_light_armor_1940() -> Division:
    """
    Creates a 1940 Light Armor Division (20 Width).

    Composition:
    - 5 Light Tank Battalions
    - 5 Motorized Infantry Battalions
    - Divisional Support: Engineer, Motorized Recon

    Role: Fast exploitation unit for encircling enemies and overrunning rear areas.
    """
    div = Division("Light Armor Division")
    light_tank = All_Battalions["1940"]["Light Tank"]
    motorized = All_Battalions["1940"]["Motorized Infantry"]

    for _ in range(5):
        div.add_battalion(light_tank)
    for _ in range(5):
        div.add_battalion(motorized)

    engineer = Support_Companies["1940"]["Engineer Company"]
    recon = Support_Companies["1940"]["Motorized Recon Company"]

    for comp in [engineer, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_motorized_division_1940() -> Division:
    """
    Creates a 1940 Motorized Infantry Division (18 Width).

    Composition:
    - 9 Motorized Infantry Battalions
    - Divisional Support: Engineer, Motorized Recon, Support Artillery

    Role: Fast infantry to follow tanks and hold breakthroughs.
    """
    div = Division("Motorized Infantry Division")
    motorized = All_Battalions["1940"]["Motorized Infantry"]
    for _ in range(9):
        div.add_battalion(motorized)

    engineer = Support_Companies["1940"]["Engineer Company"]
    recon = Support_Companies["1940"]["Motorized Recon Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]

    for comp in [engineer, recon, support_arty]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_mountaineer_division_1940() -> Division:
    """
    Creates a 1940 Mountaineer Division (18 Width).

    Composition:
    - 9 Mountaineer Battalions
    - Divisional Support: Engineer, Support Artillery, Recon Company

    Role: Specialized infantry for fighting in mountains and hills.
    """
    div = Division("Mountaineer Division")
    mountaineer = All_Battalions["1940"]["Mountaineers"]
    for _ in range(9):
        div.add_battalion(mountaineer)

    engineer = Support_Companies["1940"]["Engineer Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    recon = Support_Companies["1940"]["Cavalry Recon Company"]

    for comp in [engineer, support_arty, recon]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_marine_division_1940() -> Division:
    """
    Creates a 1940 Marine Division (18 Width).

    Composition:
    - 9 Marine Battalions
    - Divisional Support: Engineer, Support Artillery, Support AA

    Role: Specialized infantry for naval invasions and river crossings.
    """
    div = Division("Marine Division")
    marine = All_Battalions["1940"]["Marines"]
    for _ in range(9):
        div.add_battalion(marine)

    engineer = Support_Companies["1940"]["Engineer Company"]
    support_arty = Support_Companies["1940"]["Support Artillery"]
    support_aa = Support_Companies["1940"]["Support Anti-Air"]

    for comp in [engineer, support_arty, support_aa]:
        if isinstance(comp, SupportCompany):
            div.add_support_company(comp)

    return div


def create_modern_armor_1945() -> Division:
    """
    Creates a 1945 Late-War Modern Armor & Mechanized Division (30 Width) with v1.19 Regimental Support.

    Composition:
    - 8 Modern Tank Battalions
    - 7 Mechanized Infantry Battalions
    - Divisional Support: Armored Engineer Company, Medium Flame Tank Company, Logistics Company,
      Armored Signal Company, Support Anti-Air
    - Regimental Support (v1.19): Modern Tank Destroyer Support, Modern SP Anti-Air Battery,
      Motorized Fire Support Team, Rocket Artillery Battery
    """
    div = Division("1945 Modern Armor Division")
    modern_tank = All_Battalions["1945"]["Modern Tank"]
    mechanized = All_Battalions["1945"]["Mechanized Infantry"]

    for _ in range(8):
        div.add_battalion(modern_tank)
    for _ in range(7):
        div.add_battalion(mechanized)

    for s_name in [
        "Armored Engineer Company",
        "Medium Flame Tank Company",
        "Logistics Company",
        "Armored Signal Company",
        "Support Anti-Air",
    ]:
        div.add_support_company(Support_Companies["1945"][s_name])

    div.add_regimental_support(Regimental_Support_Companies["1945"]["Modern Tank Destroyer Support"])
    div.add_regimental_support(Regimental_Support_Companies["1945"]["Modern SP Anti-Air Battery"])
    div.add_regimental_support(Regimental_Support_Companies["1945"]["Motorized Fire Support Team"])
    div.add_regimental_support(Regimental_Support_Companies["1945"]["Rocket Artillery Battery"])
    return div


def get_benchmark_divisions(year: str) -> List[Division]:
    """
    Returns a list of representative benchmark divisions for the specified ``year``
    (``"1934"``, ``"1936"``, ``"1939"``, ``"1940"``, or ``"1945"``).
    """
    if year not in SUPPORTED_YEARS:
        raise ValueError(f"Unsupported year {year!r}. Choose from {SUPPORTED_YEARS}.")
    if year == "1934":
        return [create_cheap_infantry_1934()]
    if year == "1936":
        return [create_standard_infantry_1936(), create_offensive_infantry_1936()]
    if year == "1939":
        return [create_standard_infantry_1939(), create_medium_armor_1939()]
    if year == "1940":
        return [
            create_medium_armor_1940(),
            create_heavy_infantry_1940(),
            create_light_armor_1940(),
            create_motorized_division_1940(),
            create_mountaineer_division_1940(),
            create_marine_division_1940(),
        ]
    return [create_modern_armor_1945()]

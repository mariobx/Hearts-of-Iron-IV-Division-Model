"""
Terrain Definitions Module for HOI4 Land Combat Simulation.

Defines the ``Terrain`` dataclass and the official HOI4 map terrain presets:
- ``ALL_TERRAINS``: The 8 primary land map terrains used in standard combat simulation
  and multi-terrain optimization (Plains, Forest, Hills, Jungle, Mountain, Marsh, Desert, Urban).
- ``EXTENDED_TERRAINS``: Includes the 8 primary map terrains plus special tactical combat
  conditions/features (Fort, River, Amphibious, Snow) that units such as Engineers, Pioneers,
  Marines, and Winter Logistics Companies modify in HOI4 v1.19.4.2.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Terrain:
    """
    Represents a land combat terrain or tactical feature in Hearts of Iron IV.

    Attributes:
        name (str): Display name of the terrain (e.g., ``"Plains"``, ``"Mountain"``).
        combat_width (int): Base combat width for a single-direction attack into this terrain.
        attack_debuff (float): Base terrain attack penalty applied to the attacker
            (expressed as a negative fraction, e.g., ``-0.50`` for -50% attack in Mountain).
        reinforce_width (int): Additional combat width added per extra attack direction.
    """
    name: str
    combat_width: int
    attack_debuff: float
    reinforce_width: int = 35


# Primary HOI4 Land Map Terrains
PLAINS = Terrain("Plains", 70, 0.0, reinforce_width=35)
FOREST = Terrain("Forest", 60, -0.15, reinforce_width=30)
HILLS = Terrain("Hills", 70, -0.25, reinforce_width=35)
JUNGLE = Terrain("Jungle", 60, -0.30, reinforce_width=30)
MOUNTAIN = Terrain("Mountain", 50, -0.50, reinforce_width=25)
MARSH = Terrain("Marsh", 50, -0.40, reinforce_width=25)
DESERT = Terrain("Desert", 70, 0.0, reinforce_width=35)
URBAN = Terrain("Urban", 80, -0.30, reinforce_width=40)

# Extended Tactical Combat Features / Modifiers
FORT = Terrain("Fort", 70, -0.15, reinforce_width=35)
RIVER = Terrain("River", 70, -0.30, reinforce_width=35)
AMPHIBIOUS = Terrain("Amphibious", 70, -0.70, reinforce_width=35)
SNOW = Terrain("Snow", 70, -0.10, reinforce_width=35)

# Standard 8 map terrains used in division battle loops and terrain-weighted evaluation
ALL_TERRAINS: Dict[str, Terrain] = {
    "Plains": PLAINS,
    "Forest": FOREST,
    "Hills": HILLS,
    "Jungle": JUNGLE,
    "Mountain": MOUNTAIN,
    "Marsh": MARSH,
    "Desert": DESERT,
    "Urban": URBAN,
}

# Full dictionary including tactical combat features (Fort, River, Amphibious, Snow)
EXTENDED_TERRAINS: Dict[str, Terrain] = {
    **ALL_TERRAINS,
    "Fort": FORT,
    "River": RIVER,
    "Amphibious": AMPHIBIOUS,
    "Snow": SNOW,
}

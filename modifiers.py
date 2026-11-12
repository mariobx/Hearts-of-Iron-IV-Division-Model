"""
Terrain and Battalion Multiplier Modifiers Module for HOI4 Division Simulation.

Models the two primary modifier systems attached to HOI4 sub-units and support companies:
1. ``TerrainModifier``: Per-unit percentage combat/movement adjustments in specific terrains
   (e.g., Mountaineers gaining +35% attack and +10% defense in Mountain terrain, or Heavy Tanks
   suffering -40% attack in Forest).
2. ``BattalionMultiplier`` (Clausewitz ``battalion_mult``): Divisional support company scaling
   modifiers introduced/expanded in HOI4 that buff all line battalions matching a specific
   unit category (e.g., Recon Companies granting +10% Soft Attack to ``category_artillery``,
   Field Hospitals granting +10% Max HP to ``category_all_infantry``, or Engineer Companies
   adding +0.20 Entrenchment to ``category_light_infantry`` when ``add = yes``).
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class TerrainModifier:
    """
    Represents a unit's specific combat and movement bonus or penalty in a terrain type.

    Attributes:
        attack (float): Fractional attack/breakthrough modifier (e.g., 0.35 for +35%, -0.40 for -40%).
        defense (float): Fractional defense modifier (e.g., 0.10 for +10%, -0.20 for -20%).
        movement (float): Fractional movement speed modifier in this terrain (e.g., 0.20 for +20%).
    """
    attack: float = 0.0
    defense: float = 0.0
    movement: float = 0.0


@dataclass
class BattalionMultiplier:
    """
    Represents a Clausewitz ``battalion_mult`` modifier granted by a support company to all
    line battalions in the division belonging to ``category``.

    In HOI4 v1.19.4.2:
    - When ``additive`` is False (default), each non-zero stat acts as a percentage multiplier
      on matching line battalions: ``stat = stat * (1.0 + mult)``.
    - When ``additive`` is True (Clausewitz ``add = yes``), each non-zero stat is added flatly
      to every matching line battalion: ``stat = stat + bonus``.

    Attributes:
        category (str): Target Clausewitz unit category (e.g., ``"category_artillery"``,
            ``"category_all_infantry"``, ``"category_light_infantry"``, ``"category_all_armor"``).
        soft_attack (float): Soft attack modifier for matching battalions.
        hard_attack (float): Hard attack modifier for matching battalions.
        defense (float): Defense modifier for matching battalions.
        breakthrough (float): Breakthrough modifier for matching battalions.
        max_hp (float): Max HP (``max_strength``) modifier for matching battalions.
        organization (float): Max Organization modifier for matching battalions.
        recovery_rate (float): Recovery rate (``default_morale``) modifier for matching battalions.
        air_attack (float): Air attack modifier for matching battalions.
        armor (float): Armor modifier for matching battalions.
        piercing (float): Piercing (``ap_attack``) modifier for matching battalions.
        additive (bool): If True (``add = yes``), applies flatly instead of multiplicatively.
        entrenchment (float): Entrenchment modifier for matching battalions.
        initiative (float): Initiative modifier for matching battalions.
        supply_use (float): Supply consumption modifier for matching battalions.
    """
    category: str
    soft_attack: float = 0.0
    hard_attack: float = 0.0
    defense: float = 0.0
    breakthrough: float = 0.0
    max_hp: float = 0.0
    organization: float = 0.0
    recovery_rate: float = 0.0
    air_attack: float = 0.0
    armor: float = 0.0
    piercing: float = 0.0
    additive: bool = False
    entrenchment: float = 0.0
    initiative: float = 0.0
    supply_use: float = 0.0


@dataclass
class UnitModifiers:
    """
    Container holding all terrain modifiers and ``battalion_mult`` multipliers for a unit.

    Attributes:
        terrain_modifiers (Dict[str, TerrainModifier]): Mapping from terrain name (e.g., ``"Forest"``)
            to the unit's ``TerrainModifier`` in that terrain.
        battalion_multipliers (List[BattalionMultiplier]): List of ``BattalionMultiplier`` rules
            that this unit (typically a support company) applies to matching line battalions.
    """
    terrain_modifiers: Dict[str, TerrainModifier] = field(default_factory=dict)
    battalion_multipliers: List[BattalionMultiplier] = field(default_factory=list)

    def get_modifier(self, terrain_name: str) -> TerrainModifier:
        """
        Returns the ``TerrainModifier`` for ``terrain_name``, or a zero-modifier default
        if the unit has no special adjustment for that terrain.
        """
        return self.terrain_modifiers.get(terrain_name, TerrainModifier())

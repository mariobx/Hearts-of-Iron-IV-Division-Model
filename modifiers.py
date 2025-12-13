from dataclasses import dataclass, field
from typing import Dict

@dataclass
class TerrainModifier:
    """
    Represents a unit's specific bonus/penalty in a terrain.
    """
    attack: float = 0.0  # e.g., 0.35 for +35%
    defense: float = 0.0 # e.g., 0.10 for +10%

@dataclass
class UnitModifiers:
    """
    Holds all terrain modifiers for a specific unit type.
    """
    terrain_modifiers: Dict[str, TerrainModifier] = field(default_factory=dict)

    def get_modifier(self, terrain_name: str) -> TerrainModifier:
        return self.terrain_modifiers.get(terrain_name, TerrainModifier())

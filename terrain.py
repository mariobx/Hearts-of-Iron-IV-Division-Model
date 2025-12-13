from dataclasses import dataclass

@dataclass
class Terrain:
    name: str
    combat_width: int
    attack_debuff: float  # Base penalty for attacker (e.g., 0.5 for -50%)

# Hardcoded Terrain Types
PLAINS = Terrain("Plains", 70, 0.0)
FOREST = Terrain("Forest", 60, -0.15)
HILLS = Terrain("Hills", 70, -0.25)
JUNGLE = Terrain("Jungle", 60, -0.30)
MOUNTAIN = Terrain("Mountain", 50, -0.50)
MARSH = Terrain("Marsh", 50, -0.40)
DESERT = Terrain("Desert", 70, 0.0)
URBAN = Terrain("Urban", 80, -0.30)

ALL_TERRAINS = {
    "Plains": PLAINS,
    "Forest": FOREST,
    "Hills": HILLS,
    "Jungle": JUNGLE,
    "Mountain": MOUNTAIN,
    "Marsh": MARSH,
    "Desert": DESERT,
    "Urban": URBAN,
}

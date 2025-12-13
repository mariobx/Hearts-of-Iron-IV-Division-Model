from typing import Dict, Any
from stats import BaseStatistics
from modifiers import UnitModifiers

class Battalion:
    """
    Represents a single battalion (e.g., Infantry, Artillery, Light Tank).
    """
    def __init__(self, name: str, base_stats: BaseStatistics, modifiers: UnitModifiers = None):
        self.name = name
        self.base_stats = base_stats
        self.modifiers = modifiers or UnitModifiers()

    def get_stats(self) -> BaseStatistics:
        """
        Calculates the total stats for this battalion.
        """
        return self.base_stats

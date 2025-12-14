from stats import BaseStatistics
from modifiers import UnitModifiers

class SupportCompany:
    """
    Represents a support company (e.g., Engineer, Recon, Support Artillery).
    """
    def __init__(self, name: str, base_stats: BaseStatistics, modifiers: UnitModifiers = None):
        self.name = name
        self.base_stats = base_stats
        self.modifiers = modifiers or UnitModifiers()

    def get_stats(self) -> BaseStatistics:
        """
        Returns the stats of the support company.
        """
        return self.base_stats

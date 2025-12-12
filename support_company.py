from stats import BaseStatistics

class SupportCompany:
    """
    Represents a support company (e.g., Engineer, Recon, Support Artillery).
    """
    def __init__(self, name: str, stats: BaseStatistics):
        self.name = name
        self.stats = stats

    def get_stats(self) -> BaseStatistics:
        """
        Returns the stats of the support company.
        """
        return self.stats

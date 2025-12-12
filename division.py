from typing import List
from battalion import Battalion
from support_company import SupportCompany
from stats import BaseStatistics

class Division:
    """
    Represents a division template, consisting of battalions and support companies.
    """
    def __init__(self, name: str):
        self.name = name
        self.battalions: List[Battalion] = []
        self.support_companies: List[SupportCompany] = []
        

    def add_battalion(self, battalion: Battalion):
        if len(self.battalions) >= 25:
            raise ValueError("Division cannot have more than 25 battalions.")
        self.battalions.append(battalion)

    def add_support_company(self, company: SupportCompany):
        if len(self.support_companies) >= 5:
            raise ValueError("Division cannot have more than 5 support companies.")
        self.support_companies.append(company)

    def calculate_stats(self) -> BaseStatistics:
        """
        Calculates the aggregate statistics for the division.
        """
        from stats import calculate_division_stats
        
        battalion_stats = [b.get_stats() for b in self.battalions]
        support_stats = [c.get_stats() for c in self.support_companies]
        
        return calculate_division_stats(battalion_stats, support_stats)

    def print_stats_table(self):
        """
        Prints the division statistics in a formatted table.
        """
        stats = self.calculate_stats()
        print(f"Division Stats: {self.name}")
        print("-" * 40)
        print(f"{'Stat':<25} {'Value':>10}")
        print("-" * 40)
        
        # List of stats to display
        display_stats = [
            ("Soft Attack", stats.soft_attack),
            ("Hard Attack", stats.hard_attack),
            ("Defense", stats.defense),
            ("Breakthrough", stats.breakthrough),
            ("Max HP", stats.max_hp),
            ("Organization", stats.organization),
            ("Combat Width", stats.combat_width),
            ("Supply Use", stats.supply_use),
            ("IC Cost", stats.ic_cost),
            ("Manpower", stats.manpower),
            ("Armor", stats.armor),
            ("Piercing", stats.piercing),
            ("Hardness", stats.hardness),
            ("Air Attack", stats.air_attack),
            ("Entrenchment", stats.entrenchment),
            ("Initiative", stats.initiative),
            ("Recon", stats.recon),
            ("Supply Cons. Factor", stats.supply_consumption_factor),
        ]
        
        for name, value in display_stats:
            print(f"{name:<25} {value:>10.2f}")
        print("-" * 40)

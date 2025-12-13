from dataclasses import dataclass
from statistics import fmean

@dataclass
class BaseStatistics:
    """
    Holds all statistics for a unit or division.
    Using a dataclass for readability and type safety.
    """
    soft_attack: float = 0.0
    hard_attack: float = 0.0
    defense: float = 0.0
    breakthrough: float = 0.0
    max_hp: float = 0.0
    organization: float = 0.0
    combat_width: float = 0.0
    supply_use: float = 0.0
    ic_cost: float = 0.0
    manpower: float = 0.0
    armor: float = 0.0
    piercing: float = 0.0
    hardness: float = 0.0
    air_attack: float = 0.0
    entrenchment: float = 0.0
    initiative: float = 0.0
    recon: float = 0.0
    supply_consumption_factor: float = 0.0
    recovery_rate: float = 0.0

    def get_effective_attacks(self, target_hardness: float) -> float:
        """
        Calculates the number of attacks against a specific target.
        Formula: Soft Attack * (1 - Hardness) + Hard Attack * Hardness
        """
        return (self.soft_attack * (1.0 - target_hardness)) + (self.hard_attack * target_hardness)

    def get_battle_defense(self, is_attacker: bool) -> float:
        """
        Returns the relevant defense stat for the battle phase.
        Attacker uses Breakthrough. Defender uses Defense.
        """
        return self.breakthrough if is_attacker else self.defense

    def get_damage_dice_size(self, has_armor_advantage: bool) -> int:
        """
        Returns the size of the Organization damage die.
        Standard is 1d4. If Armor > Piercing, it becomes 1d6.
        """
        return 6 if has_armor_advantage else 4

def calculate_division_stats(battalion_stats: list[BaseStatistics], support_stats: list[BaseStatistics]) -> BaseStatistics:
    """
    Calculates the final statistics for a division based on its battalions and support companies.
    """
    all_stats = battalion_stats + support_stats
    if not all_stats:
        return BaseStatistics()

    # Initialize with 0
    final_stats = BaseStatistics()

    # 1. Sum Additive Stats
    for s in all_stats:
        final_stats.soft_attack += s.soft_attack
        final_stats.hard_attack += s.hard_attack
        final_stats.defense += s.defense
        final_stats.breakthrough += s.breakthrough
        final_stats.max_hp += s.max_hp
        final_stats.combat_width += s.combat_width
        final_stats.supply_use += s.supply_use
        final_stats.ic_cost += s.ic_cost
        final_stats.manpower += s.manpower
        final_stats.air_attack += s.air_attack
        final_stats.entrenchment += s.entrenchment
        final_stats.initiative += s.initiative
        final_stats.recon += s.recon
        final_stats.supply_consumption_factor += s.supply_consumption_factor

    # 2. Averages (Organization)
    # Organization is the average of ALL units
    if all_stats:
        final_stats.organization = fmean(s.organization for s in all_stats)
        final_stats.recovery_rate = fmean(s.recovery_rate for s in all_stats)

    # 3. Special Formulas
    
    # Hardness: Average of Line Battalions ONLY (exclude support companies)
    if battalion_stats:
        final_stats.hardness = fmean(b.hardness for b in battalion_stats)
    else:
        final_stats.hardness = 0.0

    # Armor: 40% of max + 60% of average (of ALL units)
    armor_values = [s.armor for s in all_stats]
    if armor_values:
        max_armor = max(armor_values)
        avg_armor = fmean(armor_values)
        final_stats.armor = (0.4 * max_armor) + (0.6 * avg_armor)

    # Piercing: 40% of max + 60% of average (of ALL units)
    piercing_values = [s.piercing for s in all_stats]
    if piercing_values:
        max_piercing = max(piercing_values)
        avg_piercing = fmean(piercing_values)
        final_stats.piercing = (0.4 * max_piercing) + (0.6 * avg_piercing)

    return final_stats


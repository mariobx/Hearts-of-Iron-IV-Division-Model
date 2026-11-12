"""
Core Statistics Module for Hearts of Iron IV Units and Divisions.

Defines ``BaseStatistics``, the central dataclass storing all combat, logistical, and economic
attributes for a single battalion, support company, or complete division, and
``calculate_division_stats`` for aggregating unit statistics using official HOI4 formulas.
"""

from dataclasses import dataclass
from statistics import fmean
from typing import List


@dataclass
class BaseStatistics:
    """
    Holds all combat, logistical, and economic statistics for a unit or division in HOI4.

    Attributes:
        soft_attack (float): Number of attacks directed at soft (unarmored) components.
        hard_attack (float): Number of attacks directed at hard (armored) components.
        defense (float): Number of defensive points available when defending in battle.
        breakthrough (float): Number of defensive points available when attacking in battle.
        max_hp (float): Total strength / hit points (``max_strength``) representing manpower/equipment pool.
        organization (float): Combat readiness and staying power (``max_organisation``).
        combat_width (float): Frontage occupied in battle (0.0 for divisional/regimental support companies).
        supply_use (float): Base supply consumption per unit time (``supply_consumption``).
        ic_cost (float): Total industrial production cost (sum of required equipment quantities * build_cost_ic).
        manpower (float): Total personnel required by the unit or division.
        armor (float): Armor rating determining whether enemy units can pierce the formation.
        piercing (float): Armor-piercing capability (``ap_attack``) against enemy armor.
        hardness (float): Fraction of the unit that is armored (0.0 to 1.0), weighting soft vs hard attacks received.
        air_attack (float): Anti-air firepower reducing enemy CAS damage and shooting down attacking aircraft.
        entrenchment (float): Flat entrenchment cap bonus contributed by the unit (e.g., Engineers).
        initiative (float): Reinforce rate and combat planning speed bonus (e.g., Signal Companies).
        recon (float): Reconnaissance value giving tactical advantage in combat tactic selection.
        supply_consumption_factor (float): Percentage modifier to total division supply use (e.g., -0.20 for -20%).
        recovery_rate (float): Organization regain rate per hour out of combat (``default_morale``).
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
        Calculates the effective number of attacks directed against a target with ``target_hardness``.

        Official HOI4 Formula:
            Effective Attacks = Soft Attack * (1 - Target Hardness) + Hard Attack * Target Hardness
        """
        return (self.soft_attack * (1.0 - target_hardness)) + (self.hard_attack * target_hardness)

    def get_battle_defense(self, is_attacker: bool) -> float:
        """
        Returns the relevant defense stat for the unit's role in the battle phase.
        Attackers use ``breakthrough``; defenders use ``defense``.
        """
        return self.breakthrough if is_attacker else self.defense

    def get_damage_dice_size(self, has_armor_advantage: bool) -> int:
        """
        Returns the size of the Organization damage die in land combat.
        Standard is 1d4 (mean 2.5). If the unit is unpierced (Armor > Enemy Piercing),
        it becomes 1d6 (mean 3.5, +40% expected organization damage).
        """
        return 6 if has_armor_advantage else 4


def calculate_division_stats(
    battalion_stats: List[BaseStatistics],
    support_stats: List[BaseStatistics],
) -> BaseStatistics:
    """
    Calculates the aggregate statistics for a division from its (already multiplier-adjusted)
    line battalion statistics and support company (divisional + regimental) statistics.

    Official HOI4 Aggregation Rules:
    1. Additive Stats (summed across all line battalions and support companies):
       - ``soft_attack``, ``hard_attack``, ``defense``, ``breakthrough``, ``max_hp``,
         ``combat_width``, ``supply_use``, ``ic_cost``, ``manpower``, ``air_attack``,
         ``entrenchment``, ``initiative``, ``recon``, ``supply_consumption_factor``.
    2. Averaged Stats (arithmetic mean across all line battalions AND support companies):
       - ``organization``, ``recovery_rate``.
    3. Line-Battalion-Only Averaged Stats (support companies excluded):
       - ``hardness``: Arithmetic mean of ``hardness`` across line battalions ONLY.
    4. Weighted Max/Average Stats (across all line battalions and support companies):
       - ``armor`` = 0.40 * max(armor) + 0.60 * mean(armor)
       - ``piercing`` = 0.40 * max(piercing) + 0.60 * mean(piercing)
    5. Net Supply Use:
       - ``supply_use = max(0.0, supply_use * (1.0 + supply_consumption_factor))``
    """
    all_stats = battalion_stats + support_stats
    if not all_stats:
        return BaseStatistics()

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

    # Apply supply_consumption_factor (e.g., from Logistics Company or Helicopter Transports)
    final_stats.supply_use = max(
        0.0, final_stats.supply_use * (1.0 + final_stats.supply_consumption_factor)
    )

    # 2. Averages (Organization & Recovery Rate across ALL units)
    final_stats.organization = fmean(s.organization for s in all_stats)
    final_stats.recovery_rate = fmean(s.recovery_rate for s in all_stats)

    # 3. Hardness: Average of Line Battalions ONLY (exclude support companies)
    if battalion_stats:
        final_stats.hardness = fmean(b.hardness for b in battalion_stats)
    else:
        final_stats.hardness = 0.0

    # 4. Armor: 40% of max + 60% of average (across ALL units)
    armor_values = [s.armor for s in all_stats]
    max_armor = max(armor_values)
    avg_armor = fmean(armor_values)
    final_stats.armor = (0.4 * max_armor) + (0.6 * avg_armor)

    # 5. Piercing: 40% of max + 60% of average (across ALL units)
    piercing_values = [s.piercing for s in all_stats]
    max_piercing = max(piercing_values)
    avg_piercing = fmean(piercing_values)
    final_stats.piercing = (0.4 * max_piercing) + (0.6 * avg_piercing)

    return final_stats

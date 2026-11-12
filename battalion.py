"""
Line Battalion Module for Hearts of Iron IV Division Simulation.

Defines the ``Battalion`` class representing a combat regiment/battalion placed in one of the
5 brigade columns of the HOI4 Division Designer (e.g., Infantry, Medium Tank, Artillery).
"""

from typing import List, Optional
from stats import BaseStatistics
from modifiers import UnitModifiers


class Battalion:
    """
    Represents a single line battalion in a Hearts of Iron IV division template.

    In HOI4 v1.19.4.2, each line battalion belongs to a specific brigade column ``group``
    (``"infantry"``, ``"combat_support"``, ``"mobile"``, ``"mobile_combat_support"``,
    ``"armor"``, or ``"armor_combat_support"``). All battalions within the same brigade column
    must share the same ``group``. Each battalion also carries a list of Clausewitz
    ``categories`` (e.g., ``"category_all_infantry"``, ``"category_artillery"``) used by
    support companies to apply ``battalion_mult`` modifiers.

    Attributes:
        name (str): Display name of the battalion (e.g., ``"Infantry"``, ``"Medium Tank"``).
        base_stats (BaseStatistics): Year-adjusted base statistics of the battalion.
        modifiers (UnitModifiers): Terrain modifiers and battalion multipliers attached to the unit.
        unit_id (str): Internal Clausewitz sub-unit key (e.g., ``"infantry"``, ``"medium_armor"``).
        group (str): Brigade column group in the HOI4 Division Designer.
        categories (List[str]): Clausewitz unit categories (e.g., ``["category_front_line", ...]``).
        year_unlocked (int): Historical year the sub-unit is unlocked via technology.
        is_special_project (bool): True if unlocked via a Special Project facility.
        is_country_locked (bool): True if locked behind a specific country focus/decision.
    """

    def __init__(
        self,
        name: str,
        base_stats: BaseStatistics,
        modifiers: Optional[UnitModifiers] = None,
        unit_id: str = "",
        group: str = "infantry",
        categories: Optional[List[str]] = None,
        year_unlocked: int = 1918,
        is_special_project: bool = False,
        is_country_locked: bool = False,
    ):
        self.name = name
        self.base_stats = base_stats
        self.modifiers = modifiers or UnitModifiers()
        self.unit_id = unit_id or name.lower().replace(" ", "_")
        self.group = group
        self.categories: List[str] = list(categories) if categories else []
        self.year_unlocked = year_unlocked
        self.is_special_project = is_special_project
        self.is_country_locked = is_country_locked

    def get_stats(self) -> BaseStatistics:
        """
        Returns the base statistics for this battalion.
        """
        return self.base_stats

    def has_category(self, category: str) -> bool:
        """
        Returns True if this battalion belongs to the specified Clausewitz ``category``
        or if ``category`` matches its ``unit_id``.
        """
        return category in self.categories or category == self.unit_id

    def __repr__(self) -> str:
        return f"Battalion({self.name!r}, group={self.group!r}, width={self.base_stats.combat_width})"

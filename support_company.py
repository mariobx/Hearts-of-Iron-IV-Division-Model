"""
Support Company Module for Hearts of Iron IV Division Simulation (v1.19.4.2).

Models both types of support units in HOI4 v1.19 (`Operation Postern`):
1. **Divisional Support Companies** (``is_divisional=True, is_regimental=False``):
   Placed in the 5 support slots on the left side of the Division Designer (e.g., Engineer
   Company, Recon Company, Support Artillery, Field Hospital, Logistics Company, Flame Tanks,
   Helicopters, Land Cruiser, Super-Heavy Tank/Artillery). Subject to ``same_support_type``
   mutual exclusivity rules.
2. **Regimental Support Companies** (``is_divisional=False, is_regimental=True``):
   Introduced in HOI4 v1.19 (`Operation Postern`). Placed in the dedicated Regimental Support
   slot at the bottom of each of the 5 brigade columns. Requires at least 3 line battalions
   in that brigade column and requires the column's ``group`` to be in the company's
   ``allowed_battalion_groups`` (e.g., Fire Support Team, Field Gun Battery, Anti-Air Battery,
   Anti-Tank Battery, SP Anti-Air Battery, Tank Destroyer Support).
"""

from typing import List, Optional
from stats import BaseStatistics
from modifiers import UnitModifiers


class SupportCompany:
    """
    Represents a Divisional or Regimental Support Company in HOI4 v1.19.4.2.

    Attributes:
        name (str): Display name of the support company.
        base_stats (BaseStatistics): Year-adjusted base statistics (``combat_width = 0.0``).
        modifiers (UnitModifiers): Terrain modifiers and ``battalion_mult`` multipliers.
        unit_id (str): Internal Clausewitz sub-unit key (e.g., ``"engineer"``, ``"field_guns"``).
        is_divisional (bool): True if this company can be placed in the 5 left-hand divisional support slots.
        is_regimental (bool): True if this company can be placed in the 5 bottom regimental support slots.
        allowed_battalion_groups (List[str]): For regimental support companies, the brigade column
            groups (e.g., ``["infantry", "mobile", "combat_support"]``) that may host this company.
        same_support_type (List[str]): Mutual exclusivity tags (e.g., ``["engineer"]``, ``["recon"]``).
            Two divisional support companies sharing any tag in ``same_support_type`` cannot coexist.
        categories (List[str]): Clausewitz unit categories.
        year_unlocked (int): Historical year the company is unlocked via technology.
        is_special_project (bool): True if unlocked via a Special Project facility.
        is_country_locked (bool): True if locked behind a specific country focus/decision.
    """

    def __init__(
        self,
        name: str,
        base_stats: BaseStatistics,
        modifiers: Optional[UnitModifiers] = None,
        unit_id: str = "",
        is_divisional: bool = True,
        is_regimental: bool = False,
        allowed_battalion_groups: Optional[List[str]] = None,
        same_support_type: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        year_unlocked: int = 1918,
        is_special_project: bool = False,
        is_country_locked: bool = False,
    ):
        self.name = name
        self.base_stats = base_stats
        self.modifiers = modifiers or UnitModifiers()
        self.unit_id = unit_id or name.lower().replace(" ", "_")
        self.is_divisional = is_divisional
        self.is_regimental = is_regimental
        self.allowed_battalion_groups: List[str] = (
            list(allowed_battalion_groups) if allowed_battalion_groups else []
        )
        if isinstance(same_support_type, str):
            self.same_support_type: List[str] = [same_support_type]
        elif same_support_type:
            self.same_support_type = list(same_support_type)
        else:
            self.same_support_type = []
        self.categories: List[str] = list(categories) if categories else []
        self.year_unlocked = year_unlocked
        self.is_special_project = is_special_project
        self.is_country_locked = is_country_locked

    def get_stats(self) -> BaseStatistics:
        """
        Returns the base statistics of the support company.
        """
        return self.base_stats

    def __repr__(self) -> str:
        kind = "Regimental" if self.is_regimental and not self.is_divisional else "Divisional"
        return f"SupportCompany({self.name!r}, type={kind})"

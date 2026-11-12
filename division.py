"""
Division Template & Combat Simulation Engine for Hearts of Iron IV (v1.19.4.2 `Operation Postern`).

Implements the ``Division`` class modeling:
1. **Official HOI4 v1.19.4.2 Division Designer Rules**:
   - Up to 5 brigade columns (``regiments``), each containing up to 5 line battalions (max 25 total).
   - Brigade column group locking: all battalions within a single column must belong to the same
     brigade group (``infantry``, ``combat_support``, ``mobile``, ``mobile_combat_support``,
     ``armor``, ``armor_combat_support``).
   - Up to 5 Divisional Support Companies in the left-hand support column, enforcing mutual
     exclusivity via ``same_support_type`` and ``SUPPORT_TYPES``.
   - Up to 5 Regimental Support Companies (new in v1.19 ``Operation Postern``), placed in the
     dedicated slot at the bottom of each brigade column. Requires at least 3 line battalions
     in that column (``REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS = 3``) and requires the column's
     group to be in the regimental support company's ``allowed_battalion_groups``.
2. **Division Stat Aggregation & ``battalion_mult`` Scaling**:
   - Applies all ``BattalionMultiplier`` (Clausewitz ``battalion_mult``) bonuses from divisional
     and regimental support companies to matching line battalions by Clausewitz category.
   - Aggregates additive, averaged, line-only hardness, 40%-max/60%-mean armor & piercing, and
     net supply consumption factor via ``calculate_division_stats``.
3. **Hourly Land Combat Simulation (``battle``)**:
   - Simulates simultaneous hourly strike rounds between an attacking division and a defending
     division on a given ``Terrain``, incorporating hardness-weighted effective attacks,
     terrain modifiers, breakthrough vs. defense hit probabilities (10% guarded vs. 40% unguarded),
     piercing/armor damage reduction tiers, unpierced 1d6 organization dice advantage, and
     10%-stepped HP strength damage scaling.
"""

from __future__ import annotations
from collections import Counter, defaultdict
from dataclasses import asdict
import math
import random
import statistics
import sys
from typing import Dict, List, Optional, Tuple, Any

from battalion import Battalion
from support_company import SupportCompany
from stats import BaseStatistics, calculate_division_stats
from terrain import Terrain, ALL_TERRAINS
from modifiers import TerrainModifier, BattalionMultiplier


class Division:
    """
    Represents a Hearts of Iron IV division template consisting of up to 5 brigade columns
    of line battalions, up to 5 divisional support companies, and up to 5 v1.19 regimental
    support companies.
    """

    MAX_REGIMENTS: int = 5
    MAX_BATTALIONS_PER_REGIMENT: int = 5
    MAX_BATTALIONS: int = 25
    MAX_SUPPORT_COMPANIES: int = 5
    REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS: int = 3

    VALID_BRIGADE_GROUPS = {
        "infantry",
        "combat_support",
        "mobile",
        "mobile_combat_support",
        "armor",
        "armor_combat_support",
    }

    # Mutually Exclusive Divisional Support Company Types (fallback/display mapping)
    SUPPORT_TYPES: Dict[str, List[str]] = {
        "Engineer": [
            "Engineer Company", "Pioneers", "Jungle Pioneers",
            "Assault Engineer Company", "Armored Engineer Company",
            "Amphibious Tank Engineer Company", "Light Tank Engineer Company",
            "Medium Tank Engineer Company", "Heavy Tank Engineer Company",
            "Super Heavy Tank Engineer Company", "Modern Tank Engineer Company",
        ],
        "Recon": [
            "Recon Company", "Cavalry Recon Company", "Motorized Recon Company",
            "Armored Car Recon Company", "Armoured Car Recon Company",
            "Light Tank Recon Company", "Airborne Light Armor", "Airborne Light armour",
            "Rangers", "Long Range Patrol Company", "Northern Territory Recon",
            "Elephantry Recon", "Elephantry", "Helicopter Recon",
            "Medium Tank Recon Company", "Heavy Tank Recon Company",
            "Super Heavy Tank Recon Company", "Modern Tank Recon Company",
            "Camel Recon Company", "Bicycle Recon Company", "Motorcycle Recon Company",
        ],
        "Military Police": ["Military Police", "Motorized Military Police"],
        "Logistics": ["Logistics Company", "Winter Logistics Company", "Helicopter Transports", "Airborne Logistics Company"],
        "Flame Tank": ["Light Flame Tank Company", "Medium Flame Tank Company", "Heavy Flame Tank Company"],
        "Maintenance": ["Maintenance Company", "Armored Maintenance Company"],
        "Field Hospital": ["Field Hospital", "Helicopter Med-Evac"],
        "Signal": ["Signal Company", "Armored Signal Company"],
        "Super-Heavy Artillery": ["Super-Heavy Artillery", "Self-Propelled Super-Heavy Artillery"],
    }

    def __init__(self, name: str):
        self.name: str = name
        self.regiments: List[List[Battalion]] = []
        self.battalions: List[Battalion] = []
        self.support_companies: List[SupportCompany] = []
        self.regimental_support_companies: List[Optional[SupportCompany]] = [
            None
        ] * self.MAX_REGIMENTS

    def _sync_battalions(self) -> None:
        """
        Synchronizes the flat ``self.battalions`` list from the 5x5 ``self.regiments`` grid.
        """
        self.battalions = [b for reg in self.regiments for b in reg]

    def add_battalion(
        self,
        battalion: Battalion,
        column: Optional[int] = None,
        strict: bool = False,
    ) -> bool:
        """
        Places ``battalion`` into the division's 5x5 brigade grid following official HOI4
        Division Designer rules:
        - Each brigade column (0..4) can hold at most 5 battalions.
        - All battalions in a column must share the same ``battalion.group``.
        - If ``column`` is None, automatically places the battalion into the first existing
          column of matching ``group`` with fewer than 5 battalions, or opens a new column
          if fewer than 5 columns exist.

        Args:
            battalion (Battalion): Line battalion to add.
            column (Optional[int]): Specific brigade column index (0..4) if desired.
            strict (bool): If True, raises ``ValueError`` when placement violates designer rules.

        Returns:
            bool: True if the battalion was added, False if rejected (when ``strict=False``).
        """
        if len(self.battalions) >= self.MAX_BATTALIONS:
            if strict:
                raise ValueError(
                    f"Division cannot have more than {self.MAX_BATTALIONS} battalions."
                )
            return False

        b_group = getattr(battalion, "group", "infantry") or "infantry"

        if column is not None:
            if column < 0 or column >= self.MAX_REGIMENTS:
                if strict:
                    raise ValueError(
                        f"Column index {column} out of range (0..{self.MAX_REGIMENTS - 1})."
                    )
                return False
            while len(self.regiments) <= column:
                self.regiments.append([])
            reg = self.regiments[column]
            if len(reg) >= self.MAX_BATTALIONS_PER_REGIMENT:
                if strict:
                    raise ValueError(
                        f"Regiment column {column + 1} already has {self.MAX_BATTALIONS_PER_REGIMENT} battalions."
                    )
                return False
            if reg and reg[0].group != b_group:
                if strict:
                    raise ValueError(
                        f"Cannot place {battalion.name} (group={b_group!r}) into column {column + 1} "
                        f"locked to group={reg[0].group!r}."
                    )
                return False
            reg.append(battalion)
            self._sync_battalions()
            return True

        # Auto-placement: 1) existing non-empty column of matching group with < 5 battalions
        for reg in self.regiments:
            if reg and reg[0].group == b_group and len(reg) < self.MAX_BATTALIONS_PER_REGIMENT:
                reg.append(battalion)
                self._sync_battalions()
                return True

        # 2) existing empty column
        for reg in self.regiments:
            if not reg:
                reg.append(battalion)
                self._sync_battalions()
                return True

        # 3) open a new column if fewer than 5 columns exist
        if len(self.regiments) < self.MAX_REGIMENTS:
            self.regiments.append([battalion])
            self._sync_battalions()
            return True

        if strict:
            raise ValueError(
                f"No valid brigade column available for {battalion.name} (group={b_group!r}); "
                f"all {self.MAX_REGIMENTS} columns are full or locked to other brigade groups."
            )
        return False

    def _has_support_type_conflict(
        self, company: SupportCompany
    ) -> Optional[Tuple[SupportCompany, str]]:
        """
        Checks if ``company`` conflicts with any existing divisional support company via
        Clausewitz ``same_support_type`` tags or ``SUPPORT_TYPES``.
        """
        new_tags = set(getattr(company, "same_support_type", []) or [])
        for existing in self.support_companies:
            if existing.name == company.name or (
                existing.unit_id and existing.unit_id == company.unit_id
            ):
                return existing, "duplicate"
            existing_tags = set(getattr(existing, "same_support_type", []) or [])
            overlap = new_tags & existing_tags
            if overlap:
                return existing, sorted(overlap)[0]

        for type_name, unit_names in self.SUPPORT_TYPES.items():
            if company.name in unit_names:
                for existing in self.support_companies:
                    if existing.name in unit_names:
                        return existing, type_name
        return None

    def add_support_company(
        self, company: SupportCompany, strict: bool = False
    ) -> bool:
        """
        Adds a support company to the division.
        - If ``company`` is a v1.19 Regimental Support Company (``is_regimental=True`` and
          ``is_divisional=False``), delegates automatically to ``add_regimental_support``.
        - Otherwise places ``company`` in one of the 5 Divisional Support slots, enforcing
          the 5-company limit and ``same_support_type`` mutual exclusivity.

        Args:
            company (SupportCompany): Support company to add.
            strict (bool): If True, raises ``ValueError`` when placement is invalid.

        Returns:
            bool: True if added, False otherwise.
        """
        if getattr(company, "is_regimental", False) and not getattr(
            company, "is_divisional", True
        ):
            return self.add_regimental_support(company, strict=strict)

        if not getattr(company, "is_divisional", True):
            if strict:
                raise ValueError(f"{company.name} is not a divisional support company.")
            return False

        if len(self.support_companies) >= self.MAX_SUPPORT_COMPANIES:
            if strict:
                raise ValueError(
                    f"Division cannot have more than {self.MAX_SUPPORT_COMPANIES} divisional support companies."
                )
            return False

        conflict = self._has_support_type_conflict(company)
        if conflict is not None:
            existing, reason = conflict
            if strict:
                raise ValueError(
                    f"Cannot add {company.name}: conflicts with existing {existing.name} ({reason})."
                )
            return False

        self.support_companies.append(company)
        return True

    def add_regimental_support(
        self,
        company: SupportCompany,
        column: Optional[int] = None,
        strict: bool = False,
    ) -> bool:
        """
        Places a v1.19 Regimental Support Company at the bottom of a brigade column.

        Official HOI4 v1.19 Rules:
        - ``company.is_regimental`` must be True.
        - The target brigade column must contain at least ``REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS``
          (3) line battalions.
        - The brigade column's ``group`` must be in ``company.allowed_battalion_groups``.
        - At most 1 Regimental Support Company per brigade column (max 5 total).

        Args:
            company (SupportCompany): Regimental support company to add.
            column (Optional[int]): Specific brigade column index (0..4), or None for auto-fit.
            strict (bool): If True, raises ``ValueError`` if placement is invalid.

        Returns:
            bool: True if added, False otherwise.
        """
        if not getattr(company, "is_regimental", False):
            if strict:
                raise ValueError(
                    f"{company.name} is not a regimental support company."
                )
            return False

        allowed_groups = getattr(company, "allowed_battalion_groups", []) or []

        def is_col_eligible(col_idx: int) -> Tuple[bool, str]:
            if col_idx < 0 or col_idx >= len(self.regiments):
                return False, f"Column {col_idx + 1} does not exist."
            reg = self.regiments[col_idx]
            if len(reg) < self.REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS:
                return (
                    False,
                    f"Column {col_idx + 1} has {len(reg)} battalions (requires >= {self.REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS}).",
                )
            if self.regimental_support_companies[col_idx] is not None:
                return (
                    False,
                    f"Column {col_idx + 1} already has regimental support {self.regimental_support_companies[col_idx].name}.",
                )
            col_group = reg[0].group
            if allowed_groups and col_group not in allowed_groups:
                return (
                    False,
                    f"{company.name} allowed groups {allowed_groups} do not include column {col_idx + 1} group {col_group!r}.",
                )
            return True, ""

        if column is not None:
            ok, reason = is_col_eligible(column)
            if not ok:
                if strict:
                    raise ValueError(f"Cannot add {company.name}: {reason}")
                return False
            self.regimental_support_companies[column] = company
            return True

        for col_idx in range(len(self.regiments)):
            ok, _ = is_col_eligible(col_idx)
            if ok:
                self.regimental_support_companies[col_idx] = company
                return True

        if strict:
            raise ValueError(
                f"No eligible brigade column with >= {self.REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS} "
                f"battalions in {allowed_groups} found for regimental support {company.name}."
            )
        return False

    def validate_division_rules(self) -> Tuple[bool, List[str]]:
        """
        Validates the division against all official HOI4 v1.19.4.2 Division Designer rules.

        Returns:
            Tuple[bool, List[str]]: ``(is_valid, list_of_violation_messages)``
        """
        violations: List[str] = []

        if not self.battalions:
            violations.append("Division must contain at least 1 line battalion.")
        if len(self.battalions) > self.MAX_BATTALIONS:
            violations.append(
                f"Division has {len(self.battalions)} line battalions (max {self.MAX_BATTALIONS})."
            )
        if len(self.regiments) > self.MAX_REGIMENTS:
            violations.append(
                f"Division has {len(self.regiments)} brigade columns (max {self.MAX_REGIMENTS})."
            )

        for idx, reg in enumerate(self.regiments):
            if len(reg) > self.MAX_BATTALIONS_PER_REGIMENT:
                violations.append(
                    f"Brigade column {idx + 1} has {len(reg)} battalions (max {self.MAX_BATTALIONS_PER_REGIMENT})."
                )
            groups = {b.group for b in reg}
            if len(groups) > 1:
                violations.append(
                    f"Brigade column {idx + 1} mixes incompatible battalion groups: {sorted(groups)}."
                )

        if len(self.support_companies) > self.MAX_SUPPORT_COMPANIES:
            violations.append(
                f"Division has {len(self.support_companies)} divisional support companies (max {self.MAX_SUPPORT_COMPANIES})."
            )

        seen_tags: Dict[str, str] = {}
        seen_names: set[str] = set()
        for comp in self.support_companies:
            if not getattr(comp, "is_divisional", True):
                violations.append(
                    f"{comp.name} in divisional support slot is not a divisional support company."
                )
            if comp.name in seen_names:
                violations.append(f"Duplicate divisional support company: {comp.name}.")
            seen_names.add(comp.name)
            for tag in getattr(comp, "same_support_type", []) or []:
                if tag in seen_tags:
                    violations.append(
                        f"Mutually exclusive support companies {seen_tags[tag]} and {comp.name} share type {tag!r}."
                    )
                else:
                    seen_tags[tag] = comp.name

        for col_idx, reg_comp in enumerate(self.regimental_support_companies):
            if reg_comp is None:
                continue
            if not getattr(reg_comp, "is_regimental", False):
                violations.append(
                    f"{reg_comp.name} in column {col_idx + 1} regimental slot is not a regimental support company."
                )
            if col_idx >= len(self.regiments) or not self.regiments[col_idx]:
                violations.append(
                    f"Regimental support {reg_comp.name} is placed in empty brigade column {col_idx + 1}."
                )
                continue
            reg = self.regiments[col_idx]
            if len(reg) < self.REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS:
                violations.append(
                    f"Regimental support {reg_comp.name} in column {col_idx + 1} requires at least "
                    f"{self.REGIMENTAL_SUPPORT_REQUIRED_BATTALIONS} battalions (found {len(reg)})."
                )
            col_group = reg[0].group
            allowed = getattr(reg_comp, "allowed_battalion_groups", []) or []
            if allowed and col_group not in allowed:
                violations.append(
                    f"Regimental support {reg_comp.name} in column {col_idx + 1} is incompatible with "
                    f"column group {col_group!r} (allowed: {allowed})."
                )

        return len(violations) == 0, violations

    def get_all_support_companies(self) -> List[SupportCompany]:
        """
        Returns all active support companies in the division (divisional + non-None regimental).
        """
        return list(self.support_companies) + [
            c for c in self.regimental_support_companies if c is not None
        ]

    def calculate_stats(self) -> BaseStatistics:
        """
        Calculates the aggregate statistics for the division, including:
        1. All line battalions (``self.battalions``).
        2. All divisional support companies (``self.support_companies``).
        3. All active v1.19 regimental support companies (``self.regimental_support_companies``).
        4. All ``BattalionMultiplier`` (``battalion_mult``) scaling/additive bonuses granted by
           support companies to line battalions matching each multiplier's ``category``.
        5. Net supply consumption adjustment via ``supply_consumption_factor``.
        """
        all_supports = self.get_all_support_companies()

        # Collect all active battalion_mult modifiers from support companies
        active_multipliers: List[BattalionMultiplier] = []
        for comp in all_supports:
            if comp.modifiers and comp.modifiers.battalion_multipliers:
                active_multipliers.extend(comp.modifiers.battalion_multipliers)

        adjusted_battalion_stats: List[BaseStatistics] = []
        for bat in self.battalions:
            raw = bat.get_stats()
            if not active_multipliers:
                adjusted_battalion_stats.append(raw)
                continue

            mult_bonuses: Dict[str, float] = defaultdict(float)
            add_bonuses: Dict[str, float] = defaultdict(float)

            for bm in active_multipliers:
                if bat.has_category(bm.category):
                    target = add_bonuses if bm.additive else mult_bonuses
                    for field_name in (
                        "soft_attack",
                        "hard_attack",
                        "defense",
                        "breakthrough",
                        "max_hp",
                        "organization",
                        "recovery_rate",
                        "air_attack",
                        "armor",
                        "piercing",
                        "entrenchment",
                        "initiative",
                        "supply_use",
                    ):
                        val = getattr(bm, field_name, 0.0)
                        if val != 0.0:
                            target[field_name] += val

            if not mult_bonuses and not add_bonuses:
                adjusted_battalion_stats.append(raw)
                continue

            def adj(field_name: str) -> float:
                base_v = getattr(raw, field_name)
                m = mult_bonuses.get(field_name, 0.0)
                a = add_bonuses.get(field_name, 0.0)
                return max(0.0, base_v * (1.0 + m) + a)

            adjusted_battalion_stats.append(
                BaseStatistics(
                    soft_attack=adj("soft_attack"),
                    hard_attack=adj("hard_attack"),
                    defense=adj("defense"),
                    breakthrough=adj("breakthrough"),
                    max_hp=adj("max_hp"),
                    organization=adj("organization"),
                    combat_width=raw.combat_width,
                    supply_use=adj("supply_use"),
                    ic_cost=raw.ic_cost,
                    manpower=raw.manpower,
                    armor=adj("armor"),
                    piercing=adj("piercing"),
                    hardness=raw.hardness,
                    air_attack=adj("air_attack"),
                    entrenchment=adj("entrenchment"),
                    initiative=adj("initiative"),
                    recon=raw.recon,
                    supply_consumption_factor=raw.supply_consumption_factor,
                    recovery_rate=adj("recovery_rate"),
                )
            )

        support_stats = [c.get_stats() for c in all_supports]
        return calculate_division_stats(adjusted_battalion_stats, support_stats)

    def print_stats_table(self) -> None:
        """
        Prints the division statistics in a formatted table.
        """
        stats = self.calculate_stats()
        print(f"Division Stats: {self.name}")
        print("-" * 40)
        print(f"{'Stat':<25} {'Value':>10}")
        print("-" * 40)

        display_stats = [
            ("Soft Attack", stats.soft_attack),
            ("Hard Attack", stats.hard_attack),
            ("Defense", stats.defense),
            ("Breakthrough", stats.breakthrough),
            ("Max HP", stats.max_hp),
            ("Organization", stats.organization),
            ("Recovery Rate", stats.recovery_rate),
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

        for label, value in display_stats:
            print(f"{label:<25} {value:>10.2f}")
        print("-" * 40)

    def calculate_terrain_modifiers(self) -> Dict[str, TerrainModifier]:
        """
        Calculates the average terrain modifiers for the division across all 8 primary terrains.
        """
        units = self.battalions + self.get_all_support_companies()
        if not units:
            return {}

        final_modifiers: Dict[str, TerrainModifier] = {}
        for terrain_name in ALL_TERRAINS.keys():
            unit_mods = [u.modifiers.get_modifier(terrain_name) for u in units]
            avg_attack = statistics.fmean(m.attack for m in unit_mods)
            avg_defense = statistics.fmean(m.defense for m in unit_mods)
            avg_movement = statistics.fmean(m.movement for m in unit_mods)
            final_modifiers[terrain_name] = TerrainModifier(
                attack=avg_attack, defense=avg_defense, movement=avg_movement
            )

        return final_modifiers

    def battle(
        self, other: Division, terrain: Terrain, verbose: bool = False
    ) -> Dict[str, Any]:
        """
        Simulates a land battle between this division (attacker) and ``other`` (defender)
        on ``terrain``.

        Returns:
            dict: Winner name, remaining organization/HP for both sides, and battle duration.
        """
        attacker_stats = self.calculate_stats()
        defender_stats = other.calculate_stats()

        att_terrain_mods = self.calculate_terrain_modifiers().get(
            terrain.name, TerrainModifier()
        )
        def_terrain_mods = other.calculate_terrain_modifiers().get(
            terrain.name, TerrainModifier()
        )

        attacker_org = attacker_stats.organization
        attacker_hp = attacker_stats.max_hp
        defender_org = defender_stats.organization
        defender_hp = defender_stats.max_hp

        hours_passed = 0

        def get_count(value: float) -> int:
            if value <= 0.0:
                return 0
            base = int(value)
            fraction = value - base
            return base + (1 if random.random() < fraction else 0)

        def get_damage_modifier(piercing: float, armor: float) -> float:
            if armor <= 0.0:
                return 1.0
            ratio = piercing / armor
            if ratio >= 1.0:
                return 1.0
            elif ratio >= 0.75:
                return 0.80
            elif ratio >= 0.50:
                return 0.65
            else:
                return 0.50

        ORG_FACTOR = 0.053
        HP_FACTOR = 0.06

        while (
            attacker_org > 0
            and defender_org > 0
            and attacker_hp > 0
            and defender_hp > 0
        ):
            hours_passed += 1
            half_weeks_passed = hours_passed / 84

            if verbose and half_weeks_passed % 0.5 == 0:
                print(f"\n--- Weeks passed: {half_weeks_passed:.1f} ---")
                print(
                    f"{self.name} (ORG: {attacker_org:.1f}, HP: {attacker_hp:.1f}) vs "
                    f"{other.name} (ORG: {defender_org:.1f}, HP: {defender_hp:.1f})"
                )

            att_hp_ratio = (
                attacker_hp / attacker_stats.max_hp
                if attacker_stats.max_hp > 0
                else 0.0
            )
            def_hp_ratio = (
                defender_hp / defender_stats.max_hp
                if defender_stats.max_hp > 0
                else 0.0
            )

            att_dmg_scale = max(0.1, math.floor(att_hp_ratio * 10) / 10.0)
            def_dmg_scale = max(0.1, math.floor(def_hp_ratio * 10) / 10.0)

            att_base_attacks = attacker_stats.get_effective_attacks(
                defender_stats.hardness
            )
            def_base_attacks = defender_stats.get_effective_attacks(
                attacker_stats.hardness
            )

            att_multiplier = 1.0 + terrain.attack_debuff + att_terrain_mods.attack
            att_total_attacks = (att_base_attacks * max(0.0, att_multiplier)) / 10.0

            def_multiplier = 1.0 + def_terrain_mods.attack
            def_total_attacks = (def_base_attacks * max(0.0, def_multiplier)) / 10.0

            att_base_defenses = attacker_stats.get_battle_defense(is_attacker=True)
            att_def_multiplier = 1.0 + terrain.attack_debuff + att_terrain_mods.attack
            att_defenses = (att_base_defenses * max(0.0, att_def_multiplier)) / 10.0

            def_base_defenses = defender_stats.get_battle_defense(is_attacker=False)
            def_def_multiplier = 1.0 + def_terrain_mods.defense
            def_defenses = (def_base_defenses * max(0.0, def_def_multiplier)) / 10.0

            att_armor_advantage = attacker_stats.armor > defender_stats.piercing
            def_armor_advantage = defender_stats.armor > attacker_stats.piercing

            att_dmg_mod = get_damage_modifier(
                attacker_stats.piercing, defender_stats.armor
            )
            def_dmg_mod = get_damage_modifier(
                defender_stats.piercing, attacker_stats.armor
            )

            # 1. Attacker Strikes Defender
            num_attacks_vs_def = get_count(att_total_attacks)
            num_defenses_def = get_count(def_defenses)
            att_org_dice = attacker_stats.get_damage_dice_size(att_armor_advantage)

            for _ in range(num_attacks_vs_def):
                hit_chance = 0.10 if num_defenses_def > 0 else 0.40
                if num_defenses_def > 0:
                    num_defenses_def -= 1
                if random.random() < hit_chance:
                    org_dmg = (
                        random.randint(1, att_org_dice)
                        * ORG_FACTOR
                        * att_dmg_mod
                        * att_dmg_scale
                    )
                    hp_dmg = (
                        random.randint(1, 2)
                        * HP_FACTOR
                        * att_dmg_mod
                        * att_dmg_scale
                    )
                    defender_org -= org_dmg
                    defender_hp -= hp_dmg

            # 2. Defender Strikes Attacker
            num_attacks_vs_att = get_count(def_total_attacks)
            num_defenses_att = get_count(att_defenses)
            def_org_dice = defender_stats.get_damage_dice_size(def_armor_advantage)

            for _ in range(num_attacks_vs_att):
                hit_chance = 0.10 if num_defenses_att > 0 else 0.40
                if num_defenses_att > 0:
                    num_defenses_att -= 1
                if random.random() < hit_chance:
                    org_dmg = (
                        random.randint(1, def_org_dice)
                        * ORG_FACTOR
                        * def_dmg_mod
                        * def_dmg_scale
                    )
                    hp_dmg = (
                        random.randint(1, 2)
                        * HP_FACTOR
                        * def_dmg_mod
                        * def_dmg_scale
                    )
                    attacker_org -= org_dmg
                    attacker_hp -= hp_dmg

        winner = other if (attacker_org <= 0 or attacker_hp <= 0) else self

        return {
            "winner": winner.name,
            "attacker_final_org": max(0.0, attacker_org),
            "attacker_final_hp": max(0.0, attacker_hp),
            "defender_final_org": max(0.0, defender_org),
            "defender_final_hp": max(0.0, defender_hp),
            "duration_hours": hours_passed,
            "duration_days": hours_passed / 24.0,
        }

    def get_composition_grid(self) -> Dict[str, Any]:
        """
        Returns a dictionary representing the official HOI4 v1.19 Division Designer layout:
        - ``"support"``: Up to 5 Divisional Support Companies.
        - ``"regiments"``: Up to 5 brigade columns, each containing up to 5 line battalions.
        - ``"regimental_support"``: 5-element list of Regimental Support Companies (or None)
          at the bottom of each brigade column.
        """
        if not self.regiments and self.battalions:
            # Fallback if self.battalions was populated directly without add_battalion
            for b in list(self.battalions):
                self.battalions.clear()
                self.add_battalion(b)

        return {
            "support": list(self.support_companies[: self.MAX_SUPPORT_COMPANIES]),
            "regiments": [
                list(reg[: self.MAX_BATTALIONS_PER_REGIMENT])
                for reg in self.regiments[: self.MAX_REGIMENTS]
            ],
            "regimental_support": list(
                self.regimental_support_companies[: self.MAX_REGIMENTS]
            ),
        }

    def print_composition_grid(self) -> None:
        """
        Prints the division composition in the HOI4 5x5 brigade grid format with Divisional
        Support Companies on the left and the v1.19 Regimental Support row at the bottom.
        """
        grid = self.get_composition_grid()

        print(f"\nDivision Template: {self.name}")
        print("=" * 125)

        col_headers = []
        for col_idx in range(self.MAX_REGIMENTS):
            if col_idx < len(grid["regiments"]) and grid["regiments"][col_idx]:
                grp = grid["regiments"][col_idx][0].group
                col_headers.append(f"Reg {col_idx + 1} ({grp[:7]})")
            else:
                col_headers.append(f"Regiment {col_idx + 1}")

        print(
            f"{'Divisional Support':<26} | "
            + " ".join([f"{h:<18}" for h in col_headers])
        )
        print("-" * 125)

        for row_idx in range(self.MAX_BATTALIONS_PER_REGIMENT):
            if row_idx < len(grid["support"]):
                support_str = grid["support"][row_idx].name[:25]
            else:
                support_str = "-"

            regiment_strs = []
            for col_idx in range(self.MAX_REGIMENTS):
                if col_idx < len(grid["regiments"]):
                    regiment = grid["regiments"][col_idx]
                    if row_idx < len(regiment):
                        regiment_strs.append(regiment[row_idx].name[:17])
                    else:
                        regiment_strs.append("-")
                else:
                    regiment_strs.append("-")

            row_str = f"{support_str:<26} | " + " ".join(
                [f"{s:<18}" for s in regiment_strs]
            )
            print(row_str)

        print("-" * 125)
        reg_sup_strs = []
        for col_idx in range(self.MAX_REGIMENTS):
            rc = grid["regimental_support"][col_idx]
            reg_sup_strs.append(rc.name[:17] if rc is not None else "-")
        print(
            f"{'Regimental Support (v1.19)':<26} | "
            + " ".join([f"{s:<18}" for s in reg_sup_strs])
        )
        print("=" * 125)

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the division template, aggregated statistics, terrain modifiers, and
        5x5 grid layout into a JSON-serializable dictionary.
        """
        stats = self.calculate_stats()
        t_mods = self.calculate_terrain_modifiers()
        grid = self.get_composition_grid()
        is_valid, errors = self.validate_division_rules()

        return {
            "name": self.name,
            "is_valid": is_valid,
            "validation_errors": errors,
            "battalion_counts": dict(Counter(b.name for b in self.battalions)),
            "support_names": [c.name for c in self.support_companies],
            "regimental_support_names": [
                c.name if c is not None else None
                for c in self.regimental_support_companies
            ],
            "grid": {
                "support": [c.name for c in grid["support"]],
                "regiments": [
                    {
                        "column": idx + 1,
                        "group": reg[0].group if reg else None,
                        "battalions": [b.name for b in reg],
                        "regimental_support": (
                            grid["regimental_support"][idx].name
                            if grid["regimental_support"][idx] is not None
                            else None
                        ),
                    }
                    for idx, reg in enumerate(grid["regiments"])
                ],
            },
            "stats": asdict(stats),
            "terrain_modifiers": {
                k: asdict(v) for k, v in t_mods.items()
            },
        }

    def save_template(self, filename: str) -> None:
        """
        Saves the division template grid and statistics table to a text file.
        """
        with open(filename, "w", encoding="utf-8") as f:
            original_stdout = sys.stdout
            sys.stdout = f
            try:
                self.print_composition_grid()
                print("\n")
                self.print_stats_table()
            finally:
                sys.stdout = original_stdout
        print(f"Template saved to {filename}")

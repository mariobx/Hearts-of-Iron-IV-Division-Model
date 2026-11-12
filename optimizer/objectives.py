"""
optimizer/objectives.py
=======================
Multi-Terrain Battle Simulator & Algorithm-Agnostic Objective Evaluator.

This module evaluates candidate Hearts of Iron IV (v1.19.4.2) ``Division``
templates across configurable terrains (Plains, Forest, Hills, Jungle,
Mountain, Marsh, Desert, Urban) as both **Attacker** and **Defender** against
an era-scaled benchmark opponent pool.

Supported Objective Modes
-------------------------
1. ``"best_overall"``:
   Maximizes all-around combat dominance (Attacker & Defender win rate,
   remaining Organization fraction, remaining HP fraction, speed of victory,
   and terrain combat-width fit efficiency) across all configured terrains.
2. ``"bang_for_buck"``:
   Maximizes combat effectiveness per unit of Industrial Capacity (IC) cost:
   ``CombatScore / (IC_Cost / 600)^0.65``, rewarding cost-effective templates
   that defeat expensive divisions at a fraction of the industrial price tag.
3. ``"offensive_breakthrough"``:
   Heavily weights Attacker win rate (75%), rapid breakthrough duration,
   Breakthrough stat, Soft/Hard Attack density, Armor advantage, and Initiative.
4. ``"defensive_wall"``:
   Heavily weights Defender win rate (75%), Organization & HP preservation,
   Defense stat, Entrenchment, Piercing against enemy armor, and low IC cost.
5. ``"terrain_specialist"``:
   Maximizes combat dominance and terrain-specific attack/defense modifiers on
   the user-selected target terrains (e.g., Mountain, Jungle, Marsh, Urban).
"""

from __future__ import annotations

import copy
import hashlib
import math
import random
import statistics
from typing import Dict, List, Optional, Tuple

from division import Division
from modifiers import TerrainModifier
from terrain import ALL_TERRAINS, Terrain
from optimizer.base import (
    FitnessMetrics,
    OptimizationConfig,
    UnitPool,
)


OBJECTIVE_DESCRIPTIONS: Dict[str, str] = {
    "best_overall": "Balanced Attacker & Defender dominance across all selected terrains",
    "bang_for_buck": "Maximum combat performance per unit of Industrial Capacity (IC) cost",
    "offensive_breakthrough": "High-tempo offensive breakthrough, armor advantage, and rapid victory",
    "defensive_wall": "Maximum defensive hold, entrenchment, ORG/HP retention, and anti-tank piercing",
    "terrain_specialist": "Specialized combat superiority and terrain bonuses on target terrains",
}


def build_benchmark_opponents(year: str, unit_pool: UnitPool) -> List[Division]:
    """
    Constructs a diverse, era-appropriate pool of benchmark opponent divisions
    for the target ``year`` (e.g., ``"1934"``, ``"1936"``, ``"1939"``, ``"1940"``, ``"1945"``).

    Includes:
    1. Standard Line Infantry Division (9 INF + Eng + Sup Arty, 18w)
    2. Shock Artillery Infantry Division (7 INF + 2 ART + Eng + Sup Arty + Recon, 20w)
    3. Mobile / Motorized Division (9 MOT/CAV + Eng + Sup Arty + Recon, 18w)
    4. Armored Breakthrough Division (6 Med/Light Tank + 4 MOT/MECH + Supports, 20w)
    5. Heavy Anti-Tank / Space Marine Infantry (8 INF + 1 Heavy Tank/AT + Eng + Sup AT + Sup AA)
    """
    bats = unit_pool.battalions_by_name
    sups = unit_pool.divisional_supports_by_name

    def _get_bat(*names: str):
        for n in names:
            if n in bats:
                return bats[n]
        return next(iter(bats.values())) if bats else None

    def _add_sups(div: Division, *sup_names: str) -> None:
        for s_name in sup_names:
            if s_name in sups:
                try:
                    div.add_support_company(sups[s_name])
                except Exception:
                    pass

    opponents: List[Division] = []

    inf = _get_bat("Infantry", "Militia", "Cavalry")
    art = _get_bat("Artillery", "Rocket Artillery", "Infantry")
    at = _get_bat("Anti-Tank", "Anti-Air", "Artillery")
    mot = _get_bat("Motorized Infantry", "Mechanized Infantry", "Cavalry", "Infantry")
    mech = _get_bat("Mechanized Infantry", "Motorized Infantry", "Cavalry", "Infantry")
    tank = _get_bat("Medium Tank", "Light Tank", "Modern Tank", "Heavy Tank", "Cavalry")
    htank = _get_bat("Heavy Tank", "Medium Tank", "Light Tank", "Anti-Tank")
    spec = _get_bat("Mountaineers", "Mountain", "Marines", "Infantry")

    if inf is None:
        return opponents

    # 1. Standard 18w Line Infantry
    div_inf = Division(f"Benchmark {year} Line Infantry (9/0)")
    for _ in range(9):
        div_inf.add_battalion(inf)
    _add_sups(div_inf, "Engineer Company", "Support Artillery", "Support Anti-Air")
    opponents.append(div_inf)

    # 2. Offensive 7/2 Infantry-Artillery
    div_art = Division(f"Benchmark {year} Shock Infantry (7/2)")
    for _ in range(7):
        div_art.add_battalion(inf)
    if art is not None:
        for _ in range(2):
            div_art.add_battalion(art)
    _add_sups(
        div_art,
        "Engineer Company",
        "Support Artillery",
        "Recon Company",
        "Support Anti-Tank",
    )
    opponents.append(div_art)

    # 3. Mobile / Motorized Division
    if mot is not None:
        div_mot = Division(f"Benchmark {year} Mobile Division (9 MOT)")
        for _ in range(9):
            div_mot.add_battalion(mot)
        _add_sups(
            div_mot,
            "Engineer Company",
            "Motorized Recon Company",
            "Support Artillery",
            "Support Anti-Air",
        )
        opponents.append(div_mot)

    # 4. Armored Breakthrough Division (6 Tank / 4 Mobile)
    if tank is not None and mech is not None:
        div_armor = Division(f"Benchmark {year} Panzer Division (6/4)")
        for _ in range(6):
            div_armor.add_battalion(tank)
        for _ in range(4):
            div_armor.add_battalion(mech)
        _add_sups(
            div_armor,
            "Engineer Company",
            "Motorized Recon Company",
            "Support Artillery",
            "Support Anti-Air",
            "Maintenance Company",
        )
        opponents.append(div_armor)

    # 5. Reinforced Anti-Tank / Heavy Infantry Division
    div_heavy = Division(f"Benchmark {year} Reinforced Infantry")
    for _ in range(8):
        div_heavy.add_battalion(inf)
    if htank is not None:
        div_heavy.add_battalion(htank)
    elif at is not None:
        div_heavy.add_battalion(at)
    _add_sups(
        div_heavy,
        "Engineer Company",
        "Support Anti-Tank",
        "Support Anti-Air",
        "Support Artillery",
    )
    opponents.append(div_heavy)

    # 6. Special Forces Terrain Division
    if spec is not None and spec.name != inf.name:
        div_spec = Division(f"Benchmark {year} Special Forces (9 SF)")
        for _ in range(9):
            div_spec.add_battalion(spec)
        _add_sups(div_spec, "Engineer Company", "Support Artillery", "Rangers")
        opponents.append(div_spec)

    return opponents


def compute_terrain_width_efficiency(combat_width: float, terrain: Terrain) -> float:
    """
    Calculates how efficiently a division of ``combat_width`` fits into a
    terrain's front width ``terrain.combat_width`` under HOI4 v1.19.4.2 mechanics.

    In HOI4, each terrain has a base combat width W_T (e.g., 50 in Mountain/Marsh,
    60 in Forest/Jungle, 70 in Plains/Hills/Desert, 80 in Urban).
    """
    if combat_width <= 0:
        return 0.0
    w_t = float(terrain.combat_width)
    # Optimal number of divisions that fit into W_T
    num_divs = max(1, round(w_t / combat_width))
    total_used = num_divs * combat_width
    if total_used <= w_t:
        # Unused width fraction
        underfill = (w_t - total_used) / w_t
        penalty = 0.65 * underfill
    else:
        # Overwidth penalty in HOI4 is 1.5% per 1% over combat width
        overfill = (total_used - w_t) / w_t
        penalty = 1.50 * overfill
    return max(0.35, min(1.0, 1.0 - penalty))


class DivisionEvaluator:
    """
    Evaluates candidate ``Division`` templates across multiple terrains and
    benchmark opponents, supporting 5 distinct objective functions and
    deterministic composition-signature caching.
    """

    def __init__(
        self,
        config: OptimizationConfig,
        unit_pool: Optional[UnitPool] = None,
    ) -> None:
        self.config = config
        self.unit_pool = unit_pool or UnitPool(config)
        self.opponents: List[Division] = build_benchmark_opponents(
            self.config.year, self.unit_pool
        )
        self.terrains: List[Terrain] = [
            ALL_TERRAINS[t] for t in self.config.terrains if t in ALL_TERRAINS
        ] or list(ALL_TERRAINS.values())

        # Normalize terrain weights
        raw_weights = {
            t.name: float(self.config.terrain_weights.get(t.name, 1.0))
            for t in self.terrains
        }
        total_w = sum(raw_weights.values()) or 1.0
        self.terrain_weights: Dict[str, float] = {
            k: v / total_w for k, v in raw_weights.items()
        }

        self._cache: Dict[str, FitnessMetrics] = {}
        self.total_evaluations: int = 0
        self.cache_hits: int = 0

    def clear_cache(self) -> None:
        self._cache.clear()
        self.total_evaluations = 0
        self.cache_hits = 0

    def evaluate(
        self,
        division: Division,
        signature: Optional[str] = None,
    ) -> FitnessMetrics:
        """
        Evaluates ``division`` across all configured terrains and opponents,
        returning a populated ``FitnessMetrics`` object.
        """
        sig = signature or getattr(division, "_genome_metadata", {}).get("signature")
        if not sig:
            bats = sorted(b.name for b in getattr(division, "battalions", []))
            sups = sorted(c.name for c in getattr(division, "support_companies", []))
            sig = f"B({','.join(bats)})_S({','.join(sups)})"

        if sig in self._cache:
            self.cache_hits += 1
            return copy.deepcopy(self._cache[sig])

        self.total_evaluations += 1
        stats = division.calculate_stats()

        # Handle empty or zero-organization invalid divisions gracefully
        if not division.battalions or stats.combat_width <= 0 or stats.organization <= 0:
            empty_metrics = FitnessMetrics(total_fitness=0.01)
            self._cache[sig] = empty_metrics
            return copy.deepcopy(empty_metrics)

        terrain_mods = division.calculate_terrain_modifiers()

        # Deterministic seed from signature so identical templates get identical Monte Carlo rolls
        sig_hash = int(hashlib.md5(sig.encode("utf-8")).hexdigest()[:8], 16)
        base_seed = (self.config.random_seed or 42) ^ sig_hash

        trials = max(1, int(self.config.battles_per_evaluation))

        terrain_win_rates: Dict[str, float] = {}
        terrain_scores: Dict[str, float] = {}

        total_att_wins = 0.0
        total_def_wins = 0.0
        total_att_battles = 0
        total_def_battles = 0
        org_ratios: List[float] = []
        hp_ratios: List[float] = []
        durations: List[float] = []

        # Save global random state and use deterministic per-signature sequence
        rng_state = random.getstate()
        try:
            random.seed(base_seed)

            for terrain in self.terrains:
                t_wins = 0.0
                t_battles = 0
                t_score_accum = 0.0
                width_eff = compute_terrain_width_efficiency(stats.combat_width, terrain)

                for opp in self.opponents:
                    opp_stats = opp.calculate_stats()
                    # Combat width normalization factor: prevents 42w templates from winning purely
                    # by having 2.3x as many battalions in a raw 1v1 simulation against an 18w template
                    width_ratio = max(10.0, opp_stats.combat_width) / max(10.0, stats.combat_width)
                    width_norm_factor = min(1.30, max(0.70, width_ratio ** 0.38))

                    for _ in range(trials):
                        # --- 1. Candidate as ATTACKER vs Benchmark Opponent as DEFENDER ---
                        res_att = division.battle(opp, terrain, verbose=False)
                        att_won = 1.0 if res_att["winner"] == division.name else 0.0
                        att_org_rem = res_att["attacker_final_org"] / max(1.0, stats.organization)
                        att_hp_rem = res_att["attacker_final_hp"] / max(1.0, stats.max_hp)
                        def_org_rem = res_att["defender_final_org"] / max(1.0, opp_stats.organization)
                        dur_hours = float(res_att["duration_hours"])

                        # Speed bonus when winning as attacker (faster breakthrough is better)
                        speed_factor = max(0.0, min(1.0, 168.0 / max(24.0, dur_hours))) if att_won else 0.0
                        att_trial_score = (
                            0.50 * att_won
                            + 0.22 * att_org_rem
                            + 0.13 * att_hp_rem
                            + 0.10 * (1.0 - def_org_rem)
                            + 0.05 * speed_factor
                        ) * width_eff * width_norm_factor

                        total_att_wins += att_won
                        total_att_battles += 1
                        t_wins += att_won
                        t_battles += 1
                        org_ratios.append(att_org_rem)
                        hp_ratios.append(att_hp_rem)
                        durations.append(dur_hours)

                        # --- 2. Candidate as DEFENDER vs Benchmark Opponent as ATTACKER ---
                        res_def = opp.battle(division, terrain, verbose=False)
                        def_won = 1.0 if res_def["winner"] == division.name else 0.0
                        cand_def_org_rem = res_def["defender_final_org"] / max(1.0, stats.organization)
                        cand_def_hp_rem = res_def["defender_final_hp"] / max(1.0, stats.max_hp)
                        opp_att_org_rem = res_def["attacker_final_org"] / max(1.0, opp_stats.organization)
                        dur_def_hours = float(res_def["duration_hours"])

                        # Endurance bonus for defenders (holding the line longer or winning outright)
                        endurance_factor = min(1.0, dur_def_hours / 120.0)
                        def_trial_score = (
                            0.50 * def_won
                            + 0.24 * cand_def_org_rem
                            + 0.16 * cand_def_hp_rem
                            + 0.05 * (1.0 - opp_att_org_rem)
                            + 0.05 * endurance_factor
                        ) * width_eff * width_norm_factor

                        total_def_wins += def_won
                        total_def_battles += 1
                        t_wins += def_won
                        t_battles += 1
                        org_ratios.append(cand_def_org_rem)
                        hp_ratios.append(cand_def_hp_rem)
                        durations.append(dur_def_hours)

                        # Blend Attacker and Defender trial scores according to objective
                        if self.config.objective == "offensive_breakthrough":
                            t_score_accum += 0.78 * att_trial_score + 0.22 * def_trial_score
                        elif self.config.objective == "defensive_wall":
                            t_score_accum += 0.22 * att_trial_score + 0.78 * def_trial_score
                        else:
                            t_score_accum += 0.50 * att_trial_score + 0.50 * def_trial_score

                num_pairs = max(1, len(self.opponents) * trials)
                terrain_win_rates[terrain.name] = t_wins / max(1, t_battles)
                terrain_scores[terrain.name] = (t_score_accum / num_pairs) * 100.0
        finally:
            random.setstate(rng_state)

        attacker_win_rate = total_att_wins / max(1, total_att_battles)
        defender_win_rate = total_def_wins / max(1, total_def_battles)
        overall_win_rate = (total_att_wins + total_def_wins) / max(1, total_att_battles + total_def_battles)
        avg_org_ratio = statistics.fmean(org_ratios) if org_ratios else 0.0
        avg_hp_ratio = statistics.fmean(hp_ratios) if hp_ratios else 0.0
        avg_duration = statistics.fmean(durations) if durations else 0.0

        # Weighted multi-terrain combat score (0..100 scale)
        weighted_combat_score = sum(
            terrain_scores[t.name] * self.terrain_weights.get(t.name, 1.0 / len(self.terrains))
            for t in self.terrains
        )

        # Analytical stat synergy bonuses per objective
        width = max(2.0, stats.combat_width)
        sa_per_w = stats.soft_attack / width
        ha_per_w = stats.hard_attack / width
        brk_per_w = stats.breakthrough / width
        def_per_w = stats.defense / width

        # Bang-for-buck / IC efficiency calculation
        # Standard 18w infantry costs ~550-750 IC; medium tank division costs ~3500-5500 IC.
        ic_norm = max(250.0, stats.ic_cost) / 650.0
        ic_efficiency_score = weighted_combat_score / (ic_norm ** 0.55)
        bang_for_buck_score = (
            weighted_combat_score
            * (1.0 + 0.15 * overall_win_rate + 0.10 * avg_org_ratio)
            / (ic_norm ** 0.65)
        )

        # Select final objective score before constraint penalties
        obj = self.config.objective.lower().strip()
        if obj == "bang_for_buck":
            raw_fitness = bang_for_buck_score
        elif obj == "offensive_breakthrough":
            off_stat_bonus = (
                1.8 * sa_per_w
                + 1.4 * ha_per_w
                + 2.2 * brk_per_w
                + 0.18 * stats.armor
                + 12.0 * stats.hardness
                + 25.0 * stats.initiative
                + 2.5 * stats.recon
            )
            raw_fitness = 0.72 * weighted_combat_score + 0.28 * min(120.0, off_stat_bonus)
        elif obj == "defensive_wall":
            def_stat_bonus = (
                2.2 * def_per_w
                + 1.2 * sa_per_w
                + 2.8 * stats.entrenchment
                + 0.22 * stats.piercing
                + 0.35 * stats.organization
                + 0.12 * stats.max_hp
            )
            ic_mod = 1.0 / (max(1.0, stats.ic_cost / 1200.0) ** 0.20)
            raw_fitness = (0.72 * weighted_combat_score + 0.28 * min(120.0, def_stat_bonus)) * ic_mod
        elif obj == "terrain_specialist":
            # Reward positive terrain modifiers on the configured terrains
            t_mod_bonus = 0.0
            for t in self.terrains:
                w_t = self.terrain_weights.get(t.name, 1.0 / len(self.terrains))
                mod = terrain_mods.get(t.name, TerrainModifier())
                t_mod_bonus += w_t * (65.0 * mod.attack + 55.0 * mod.defense)
            raw_fitness = weighted_combat_score + t_mod_bonus
        else:
            # "best_overall"
            synergy_bonus = (
                1.1 * sa_per_w
                + 0.8 * ha_per_w
                + 0.9 * brk_per_w
                + 0.9 * def_per_w
                + 0.10 * stats.armor
                + 0.10 * stats.piercing
                + 1.2 * stats.entrenchment
                + 1.5 * stats.recon
            )
            raw_fitness = 0.80 * weighted_combat_score + 0.20 * min(110.0, synergy_bonus)

        # Constraint penalty evaluation (soft + hard boundaries)
        penalty = 0.0
        if self.config.target_combat_width is not None and self.config.target_combat_width > 0:
            width_diff = abs(stats.combat_width - self.config.target_combat_width)
            if width_diff > 0:
                penalty += 6.5 * width_diff
        else:
            if stats.combat_width < self.config.min_combat_width:
                penalty += 8.0 * (self.config.min_combat_width - stats.combat_width)
            elif stats.combat_width > self.config.max_combat_width:
                penalty += 8.0 * (stats.combat_width - self.config.max_combat_width)

        if self.config.max_ic_cost is not None and stats.ic_cost > self.config.max_ic_cost:
            excess_ic_ratio = (stats.ic_cost - self.config.max_ic_cost) / max(100.0, self.config.max_ic_cost)
            penalty += 60.0 * excess_ic_ratio

        if self.config.max_manpower is not None and stats.manpower > self.config.max_manpower:
            excess_mp_ratio = (stats.manpower - self.config.max_manpower) / max(1000.0, self.config.max_manpower)
            penalty += 60.0 * excess_mp_ratio

        # Organization sanity check (divisions with < 20 ORG shatter rapidly in sustained fronts)
        if stats.organization < 20.0:
            penalty += 2.5 * (20.0 - stats.organization)

        total_fitness = max(0.01, raw_fitness - penalty)

        combat_stats_summary = {
            "soft_attack": round(stats.soft_attack, 2),
            "hard_attack": round(stats.hard_attack, 2),
            "defense": round(stats.defense, 2),
            "breakthrough": round(stats.breakthrough, 2),
            "organization": round(stats.organization, 2),
            "max_hp": round(stats.max_hp, 2),
            "combat_width": round(stats.combat_width, 2),
            "ic_cost": round(stats.ic_cost, 2),
            "manpower": round(stats.manpower, 0),
            "supply_use": round(stats.supply_use, 3),
            "armor": round(stats.armor, 2),
            "piercing": round(stats.piercing, 2),
            "hardness": round(stats.hardness, 3),
            "entrenchment": round(stats.entrenchment, 2),
            "recon": round(stats.recon, 2),
            "initiative": round(stats.initiative, 3),
            "soft_attack_per_width": round(sa_per_w, 2),
            "ic_per_width": round(stats.ic_cost / width, 2),
        }

        metrics = FitnessMetrics(
            total_fitness=total_fitness,
            win_rate=overall_win_rate,
            attacker_win_rate=attacker_win_rate,
            defender_win_rate=defender_win_rate,
            avg_org_remaining_ratio=avg_org_ratio,
            avg_hp_remaining_ratio=avg_hp_ratio,
            avg_battle_duration_hours=avg_duration,
            ic_efficiency_score=ic_efficiency_score,
            bang_for_buck_score=bang_for_buck_score,
            terrain_win_rates=terrain_win_rates,
            terrain_scores=terrain_scores,
            combat_stats_summary=combat_stats_summary,
            constraint_penalty=penalty,
        )

        self._cache[sig] = copy.deepcopy(metrics)
        return metrics

from typing import List, Dict
from battalion import Battalion
from support_company import SupportCompany
from stats import BaseStatistics
from terrain import Terrain
from modifiers import TerrainModifier
import random
import math
import statistics


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


    def calculate_terrain_modifiers(self) -> Dict[str, TerrainModifier]:
        """
        Calculates the average terrain modifiers for the division.
        """
        from terrain import ALL_TERRAINS
        
        # Collect all units
        units = self.battalions + self.support_companies
        if not units:
            return {}

        final_modifiers = {}
        
        for terrain_name in ALL_TERRAINS.keys():
            # Get modifiers for this terrain from all units
            # If a unit has no modifier for this terrain, it defaults to 0.0 (via get_modifier)
            unit_mods = [u.modifiers.get_modifier(terrain_name) for u in units]
            
            avg_attack = statistics.fmean(m.attack for m in unit_mods)
            avg_defense = statistics.fmean(m.defense for m in unit_mods)
            
            final_modifiers[terrain_name] = TerrainModifier(attack=avg_attack, defense=avg_defense)
            
        return final_modifiers

    def battle(self, other: 'Division', terrain: Terrain) -> dict:
        """
        Simulates a land battle between this division (attacker) and another (defender).
        Returns a dictionary with the winner, final stats, and battle duration.
        """
 
        # 1. Calculate Stats
        attacker_stats = self.calculate_stats()
        defender_stats = other.calculate_stats()
        
        # 2. Calculate Terrain Modifiers
        att_terrain_mods = self.calculate_terrain_modifiers().get(terrain.name, TerrainModifier())
        def_terrain_mods = other.calculate_terrain_modifiers().get(terrain.name, TerrainModifier())

        # 3. Initialize State
        attacker_org = attacker_stats.organization
        attacker_hp = attacker_stats.max_hp
        defender_org = defender_stats.organization
        defender_hp = defender_stats.max_hp

        hours_passed = 0

        # Helper for Bernoulli rounding
        def get_count(value):
            base = int(value)
            fraction = value - base
            return base + (1 if random.random() < fraction else 0)


        # Battle Loop
        while attacker_org > 0 and defender_org > 0:
            hours_passed += 1

            # --- Determine Effective Attacks & Defenses ---
            # Base Attacks
            att_base_attacks = attacker_stats.get_effective_attacks(defender_stats.hardness)
            def_base_attacks = defender_stats.get_effective_attacks(attacker_stats.hardness)
            
            # Apply Modifiers
            # Attacker: Base * (1 + TerrainDebuff + UnitAttackMod)
            # Note: Terrain.attack_debuff is usually positive in our file (e.g. 0.5), representing a penalty?
            # Wait, in terrain.py we wrote: attack_debuff: float # Base penalty for attacker (e.g., 0.5 for -50%)
            # And user changed it to negative: -0.50.
            # So we should ADD it. 1 + (-0.50) = 0.5 (50% stats).
            
            att_multiplier = 1.0 + terrain.attack_debuff + att_terrain_mods.attack
            att_total_attacks = (att_base_attacks * max(0.0, att_multiplier)) / 10.0
            
            # Defender: Base * (1 + UnitAttackMod) [For return strikes]
            # Defender does NOT suffer terrain attack debuff when striking back (standard HOI4 logic)
            def_multiplier = 1.0 + def_terrain_mods.attack
            def_total_attacks = (def_base_attacks * max(0.0, def_multiplier)) / 10.0

            # Defenses
            # Attacker uses Breakthrough. Does terrain affect this?
            # Wiki: "Terrain modifiers... apply to... breakthrough".
            # So Attacker Breakthrough gets the same penalty.
            att_base_defenses = attacker_stats.get_battle_defense(is_attacker=True)
            att_def_multiplier = 1.0 + terrain.attack_debuff + att_terrain_mods.attack # Breakthrough uses Attack modifiers in terrain?
            # Actually Wiki says "Attack" modifiers usually apply to Breakthrough too for Attacker.
            # Let's assume UnitAttackMod applies to Breakthrough.
            att_defenses = (att_base_defenses * max(0.0, att_def_multiplier)) / 10.0
            
            # Defender uses Defense.
            # Defender Defense: Base * (1 + UnitDefenseMod)
            def_base_defenses = defender_stats.get_battle_defense(is_attacker=False)
            def_def_multiplier = 1.0 + def_terrain_mods.defense
            def_defenses = (def_base_defenses * max(0.0, def_def_multiplier)) / 10.0

            # --- Armor Checks ---
            # Advantage = My Armor > Enemy Piercing
            att_armor_advantage = attacker_stats.armor > defender_stats.piercing
            def_armor_advantage = defender_stats.armor > attacker_stats.piercing

            # --- Constants ---
            ORG_FACTOR = 0.053
            HP_FACTOR = 0.06

            # --- Resolve Round (Simultaneous) ---
            
            # Helper to calculate damage modifier based on Piercing vs Armor
            def get_damage_modifier(piercing, armor):
                if armor <= 0: return 1.0
                ratio = piercing / armor
                if ratio >= 1.0:
                    return 1.0
                elif ratio >= 0.75:
                    return 0.80 # -20% damage
                elif ratio >= 0.50:
                    return 0.65 # -35% damage
                else:
                    return 0.50 # -50% damage

            att_dmg_mod = get_damage_modifier(attacker_stats.piercing, defender_stats.armor)
            def_dmg_mod = get_damage_modifier(defender_stats.piercing, attacker_stats.armor)

            # 1. Attacker Strikes Defender
            num_attacks_vs_def = get_count(att_total_attacks)
            num_defenses_def = get_count(def_defenses)
            
            # Dice size depends on ATTACKER'S armor advantage (Wiki: "If armor is not pierced... deals 40% more org damage" -> 1d6)
            att_org_dice = attacker_stats.get_damage_dice_size(att_armor_advantage)

            for _ in range(num_attacks_vs_def):
                hit_chance = 0.10 if num_defenses_def > 0 else 0.40
                if num_defenses_def > 0:
                    num_defenses_def -= 1
                
                if random.random() < hit_chance:
                    # Hit!
                    org_dmg = random.randint(1, att_org_dice) * ORG_FACTOR
                    hp_dmg = random.randint(1, 2) * HP_FACTOR
                    
                    # Apply Damage Reduction
                    org_dmg *= att_dmg_mod
                    hp_dmg *= att_dmg_mod
                    
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
                    # Hit!
                    org_dmg = random.randint(1, def_org_dice) * ORG_FACTOR
                    hp_dmg = random.randint(1, 2) * HP_FACTOR
                    
                    # Apply Damage Reduction
                    org_dmg *= def_dmg_mod
                    hp_dmg *= def_dmg_mod
                    
                    attacker_org -= org_dmg
                    attacker_hp -= hp_dmg

        # Determine Winner
        if attacker_org <= 0:
            winner = other
        else:
            winner = self

        return {
            "winner": winner.name,
            "attacker_final_org": max(0, attacker_org),
            "attacker_final_hp": max(0, attacker_hp),
            "defender_final_org": max(0, defender_org),
            "defender_final_hp": max(0, defender_hp),
            "duration_hours": hours_passed,
            "duration_days": hours_passed / 24.0
        }

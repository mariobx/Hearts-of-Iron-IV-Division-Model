"""
Official Hearts of Iron IV v1.19.4.2 (`Operation Postern`) Land Doctrines Engine.

This module extracts and models the complete Hearts of Iron IV v1.19.4.2 Land Doctrine
architecture directly from the official Clausewitz script files in:
- ``common/doctrines/grand_doctrines/land_grand_doctrines.txt``
- ``common/doctrines/tracks/land_doctrine_tracks.txt``
- ``common/doctrines/subdoctrines/land/infantry_subdoctrines.txt``
- ``common/doctrines/subdoctrines/land/armor_subdoctrines.txt``
- ``common/doctrines/subdoctrines/land/combat_support_subdoctrines.txt``
- ``common/doctrines/subdoctrines/land/operations_subdoctrines.txt``
- ``localisation/english/doctrines_l_english.yml``

Architecture of the HOI4 v1.19 (`Operation Postern`) Land Doctrine System
=========================================================================
In HOI4 v1.19, Paradox replaced the legacy static 10-row technology tree with a modular
two-tier **Grand Doctrine + 4 Track Sub-Doctrine Mastery** system:

1. **Grand Doctrine Root** (``GRAND_DOCTRINES``):
   The player selects one of four mutually exclusive Land Grand Doctrines for 100 Army XP:
   - ``new_mobile_warfare`` ("Mobile Warfare"): Immediate +20% Planning Speed, +10% Army Speed,
     and *Unexpected Thrust* combat tactic.
   - ``superior_firepower`` ("Superior Firepower"): Immediate +10% Line Artillery Soft Attack,
     +5% Support Artillery Soft Attack, and *Overwhelming Fire* combat tactic.
   - ``grand_battleplan`` ("Grand Battleplan"): Immediate +10% Max Planning, +25% Command Power
     Gain, and *Planned Attack* combat tactic.
   - ``mass_assault`` ("Mass Assault"): Immediate +48h Out-of-Supply Grace, -15% Out-of-Supply
     Penalty, and *Relentless Assault* combat tactic.

2. **Four Doctrine Tracks & Track Completion Milestones** (``DOCTRINE_TRACKS``):
   Every Land Grand Doctrine unlocks four specialized Sub-Doctrine Tracks:
   - Track 1 — ``infantry`` (*Infantry*): Driven by ``category_all_infantry`` & ``category_cavalry``.
   - Track 2 — ``combat_support`` (*Artillery & Combat Support*): Driven by ``category_line_artillery``,
     ``category_artillery``, and ``category_support_battalions``.
   - Track 3 — ``armor`` (*Armor*): Driven by ``category_tanks``, ``category_all_armor``, and ``armored_car``.
   - Track 4 — ``operations`` (*Operations*): Driven by ``category_army``.
   When a track reaches 100% Mastery (all rewards unlocked), the active Grand Doctrine grants
   its corresponding **Track Milestone** (e.g., Mass Assault's Infantry Milestone grants
   ``infantry = { combat_width = -0.2 }`` and ``category_regimental_support_battalions = { supply_consumption = -0.02, default_morale = 0.1 }``).

3. **34 Specialized Land Sub-Doctrines & 5-Tier Mastery Rewards** (``LAND_SUBDOCTRINES``):
   Into each of the 4 tracks, the player slots a specialized Sub-Doctrine (9 Infantry,
   9 Artillery/Combat Support, 8 Armor, and 10 Operations sub-doctrines). Slotting a
   Sub-Doctrine grants immediate **Base Activation Effects** and progressively unlocks
   5 sequential **Mastery Rewards** as units fight and train in the field.

4. **Canonical Preset Paths & Custom Doctrine Composition**:
   This module supports both:
   - **9 Canonical Preset Doctrine Paths** (``CANONICAL_DOCTRINE_PRESETS``):
     * ``"none"``: Baseline (No Doctrine).
     * ``"mobile_warfare"`` / ``"mobile_warfare_blitzkrieg"``: Mobile Warfare + Mobile Infantry +
       Mobile Recon & Assault + Armored Spearhead + Mission-Type Tactics.
     * ``"mobile_warfare_desperate_defense"``: Mobile Warfare + Mobile Infantry +
       Self-propelled Support + Streamlined Deployment (Mechanized Wave) + Desperate Defense.
     * ``"superior_firepower"`` / ``"superior_firepower_integrated_support"``: Superior Firepower +
       Assault Infantry (Integrated Support) + Mobile Recon & Assault + Mobile Defense +
       Rapid Domination (Regimental Combat Teams / Shock & Awe).
     * ``"superior_firepower_dispersed_support"``: Superior Firepower + Assault Infantry +
       Fire Concentration (-0.8 Line/Rocket Artillery Combat Width) + Mobile Defense +
       Rapid Domination (Shock & Awe).
     * ``"grand_battleplan"`` / ``"grand_battleplan_assault"``: Grand Battleplan +
       Defensive Postures + Fire Concentration + Armored Infantry Support + Grand Assault.
     * ``"grand_battleplan_infiltration"``: Grand Battleplan + Individual Excellence (Commandos) +
       Field Engineering + Armored Cavalry + Infiltration Tactics.
     * ``"mass_assault"`` / ``"mass_assault_deep_battle"``: Mass Assault + Large Unit Tactics
       (combined -0.4 Infantry Combat Width) + Fire Concentration + Streamlined Deployment +
       Deep Battle.
     * ``"mass_assault_mass_mobilization"``: Mass Assault + Large Unit Tactics (combined -0.4
       Infantry Combat Width) + Field Engineering + Streamlined Deployment + Guerilla War /
       Mass Mobilization (+0.30 Infantry Recovery Rate, +15 Infantry Organization, +20% Defense).
   - **All 34 Individual v1.19 Sub-Doctrines**: Any individual sub-doctrine key (e.g.,
     ``"assault_infantry"``, ``"fire_concentration"``, ``"armored_spearhead"``, ``"deep_battle"``,
     ``"siege_artillery"``, ``"air_cavalry"``) can be queried or applied directly.
   - **Custom v1.19 Doctrine Composition** via ``compose_custom_doctrine(...)`` or composite
     string keys ``"<grand_doctrine>:<infantry>,<combat_support>,<armor>,<operations>"``.

5. **Clausewitz Stat Application Rules**:
   - **Additive Unit Stats** (``base + sum(bonus * mastery_scale)``):
     ``max_organisation`` (``organization``), ``default_morale`` / ``army_morale`` (``recovery_rate``),
     ``entrenchment``, ``initiative``, ``recon``, ``supply_consumption`` (``supply_use``),
     ``supply_consumption_factor``, and discrete ``combat_width`` (applied in full when
     ``mastery_level >= 0.60``).
   - **Multiplicative Unit Stats** (``base * (1.0 + sum(pct * mastery_scale))``):
     ``soft_attack``, ``hard_attack``, ``defense``, ``breakthrough``, ``ap_attack`` (``piercing``),
     ``armor_value`` (``armor``), ``air_attack``, and ``max_strength`` (``max_hp``).
   - **Support Company ``battalion_mult`` & Terrain Modifiers**:
     Doctrine-granted ``battalion_mult`` blocks (e.g., Assault Infantry granting +20% Soft Attack
     on ``category_light_infantry`` to Support Artillery, or Rapid Domination granting +0.10
     additive Recovery Rate on ``category_army`` to ``category_support_artillery``) and per-unit
     terrain modifiers (e.g., Siege Artillery granting +25% Fort attack to Super-Heavy Artillery)
     are cloned and merged onto the unit's ``UnitModifiers``.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
import os
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from battalion import Battalion
from modifiers import BattalionMultiplier, TerrainModifier, UnitModifiers
from stats import BaseStatistics
from support_company import SupportCompany


# =============================================================================
# 1. Year-Based Mastery Progression & Constants
# =============================================================================

#: Default historical doctrine mastery progression by benchmark technology year.
#: - 1934 (Interwar): 0.00 (Doctrines not yet unlocked / interwar baseline)
#: - 1936 (Pre-War):  0.20 (Grand Doctrine + initial Sub-Doctrine activation)
#: - 1939 (Outbreak): 0.50 (Halfway through Sub-Doctrine Mastery tracks)
#: - 1940 (Blitz):    0.70 (Operational nodes & combat width reductions unlocked)
#: - 1945 (Late War): 1.00 (Full Grand Doctrine + 4 Sub-Doctrines + 4 Milestones)
DEFAULT_MASTERY_BY_YEAR: Dict[str, float] = {
    "1934": 0.00,
    "1936": 0.20,
    "1939": 0.50,
    "1940": 0.70,
    "1945": 1.00,
}

#: Mastery threshold at which discrete structural combat width reductions
#: (such as Mass Assault's -0.4 Infantry combat width or Fire Concentration's
#: -0.8 Line Artillery / Rocket Artillery combat width) take effect.
DISCRETE_COMBAT_WIDTH_MASTERY_THRESHOLD: float = 0.60

#: Official HOI4 v1.19.4.2 Land Doctrine Track definitions from
#: ``common/doctrines/tracks/land_doctrine_tracks.txt``.
DOCTRINE_TRACKS: Dict[str, Dict[str, Any]] = {
    "infantry": {
        "key": "infantry",
        "name": "Infantry",
        "mastery_multiplier": 1.0,
        "categories": ["category_all_infantry", "category_cavalry"],
        "sub_units": [],
    },
    "combat_support": {
        "key": "combat_support",
        "name": "Artillery & Combat Support",
        "mastery_multiplier": 8.0,
        "categories": [
            "category_line_artillery",
            "category_artillery",
            "category_support_battalions",
        ],
        "sub_units": [],
    },
    "armor": {
        "key": "armor",
        "name": "Armor",
        "mastery_multiplier": 10.0,
        "categories": ["category_tanks", "category_all_armor"],
        "sub_units": ["armored_car"],
    },
    "operations": {
        "key": "operations",
        "name": "Operations",
        "mastery_multiplier": 0.7,
        "categories": ["category_army"],
        "sub_units": [],
    },
}

GRAND_DOCTRINES: Dict[str, Dict[str, Any]] = {'new_mobile_warfare': {'key': 'new_mobile_warfare',
                        'name': 'Mobile Warfare',
                        'description': "Hit them where they don't expect - mobile warfare doctrine "
                                       'seeks to break the trench deadlock of the First World War '
                                       'via aggressive maneuvers to pre-empt and disrupt the '
                                       'enemy.',
                        'tracks': ['infantry', 'combat_support', 'armor', 'operations'],
                        'base_effects': {'unit_mods': {},
                                         'army_mods': {'planning_speed': 0.2,
                                                       'army_speed_factor': 0.1},
                                         'tactics': ['tactic_unexpected_thrust']},
                        'milestones': [{'unit_mods': {},
                                        'army_mods': {'org_loss_when_moving': -0.15,
                                                      'land_reinforce_rate': 0.02},
                                        'tactics': ['tactic_delay']},
                                       {'unit_mods': {},
                                        'army_mods': {'planning_speed': 0.1,
                                                      'org_loss_at_low_org_factor': -0.1},
                                        'tactics': ['tactic_overwhelming_fire']},
                                       {'unit_mods': {'category_army': {'stats': {'breakthrough': 0.15},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []}},
                                        'army_mods': {'additional_brigade_column_size': 1.0},
                                        'tactics': ['tactic_blitz']},
                                       {'unit_mods': {'category_regimental_support_battalions': {'stats': {'max_organisation': 10.0,
                                                                                                           'breakthrough': 0.1},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': []}},
                                        'army_mods': {'planning_speed': 0.2},
                                        'tactics': ['tactic_backhand_blow']}]},
 'superior_firepower': {'key': 'superior_firepower',
                        'name': 'Superior Firepower',
                        'description': 'Send shells, not men - Superior Firepower emphasizes '
                                       'employing crushing masses of fire to pave the way for '
                                       'maneuver units to advance and capture territory.',
                        'tracks': ['infantry', 'combat_support', 'armor', 'operations'],
                        'base_effects': {'unit_mods': {'category_line_artillery': {'stats': {'soft_attack': 0.1},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                       'category_support_artillery': {'stats': {'soft_attack': 0.05},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': ['tactic_overwhelming_fire']},
                        'milestones': [{'unit_mods': {},
                                        'army_mods': {'supply_consumption_factor': -0.1},
                                        'tactics': ['tactic_elastic_defense']},
                                       {'unit_mods': {'category_support_battalions': {'stats': {'max_organisation': 10.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                        'army_mods': {'additional_brigade_column_size': 1.0,
                                                      'planning_decay_rate_factor': -0.1},
                                        'tactics': ['tactic_barrage']},
                                       {'unit_mods': {'category_army': {'stats': {'default_morale': 0.1},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []},
                                                      'category_regimental_support_battalions': {'stats': {'soft_attack': 0.05,
                                                                                                           'hard_attack': 0.05},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': ['tactic_delay']},
                                       {'unit_mods': {'category_army': {'stats': {'default_morale': 0.2},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []}},
                                        'army_mods': {'planning_decay_rate_factor': -0.1},
                                        'tactics': ['tactic_tactical_withdrawal']}]},
 'grand_battleplan': {'key': 'grand_battleplan',
                      'name': 'Grand Battleplan',
                      'description': 'With sufficient preparation, no obstacle is insurmountable - '
                                     'Grand Battleplan is characterized by patient, meticulous '
                                     'preparation of all arms, in both attack and defense.',
                      'tracks': ['infantry', 'combat_support', 'armor', 'operations'],
                      'base_effects': {'unit_mods': {},
                                       'army_mods': {'max_planning': 0.1,
                                                     'command_power_gain': 0.25},
                                       'tactics': ['tactic_planned_attack']},
                      'milestones': [{'unit_mods': {},
                                      'army_mods': {'additional_brigade_column_size': 1.0,
                                                    'max_dig_in_factor': 0.05},
                                      'tactics': ['tactic_elastic_defense']},
                                     {'unit_mods': {'category_regimental_support_battalions': {'stats': {'defense': 0.1,
                                                                                                         'entrenchment': 0.2},
                                                                                               'terrain_modifiers': {},
                                                                                               'battalion_multipliers': []}},
                                      'army_mods': {'coordination_bonus': 0.1},
                                      'tactics': ['tactic_overwhelming_fire']},
                                     {'unit_mods': {},
                                      'army_mods': {'land_reinforce_rate': 0.02},
                                      'tactics': ['tactic_breakthrough']},
                                     {'unit_mods': {},
                                      'army_mods': {'coordination_bonus': 0.1,
                                                    'max_command_power': 30.0},
                                      'tactics': []}]},
 'mass_assault': {'key': 'mass_assault',
                  'name': 'Mass Assault',
                  'description': 'Our willingness to sacrifice guarantees our victory - Mass '
                                 'Assault focuses on concentrating numerical superiority to force '
                                 'a breakthrough at the chosen time and place.',
                  'tracks': ['infantry', 'combat_support', 'armor', 'operations'],
                  'base_effects': {'unit_mods': {},
                                   'army_mods': {'no_supply_grace': 48.0,
                                                 'out_of_supply_factor': -0.15},
                                   'tactics': ['tactic_relentless_assault']},
                  'milestones': [{'unit_mods': {'infantry': {'stats': {'combat_width': -0.2},
                                                             'terrain_modifiers': {},
                                                             'battalion_multipliers': []},
                                                'category_regimental_support_battalions': {'stats': {'supply_consumption': -0.02,
                                                                                                     'default_morale': 0.1},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                  'army_mods': {},
                                  'tactics': ['tactic_human_wave_tactics']},
                                 {'unit_mods': {},
                                  'army_mods': {'additional_brigade_column_size': 1.0,
                                                'land_reinforce_rate': 0.02},
                                  'tactics': ['tactic_elastic_defense']},
                                 {'unit_mods': {},
                                  'army_mods': {'land_reinforce_rate': 0.02},
                                  'tactics': ['tactic_overwhelming_fire']},
                                 {'unit_mods': {},
                                  'army_mods': {'weekly_casualties_war_support': 0.001,
                                                'minimum_training_level': -0.1,
                                                'supply_consumption_factor': -0.15},
                                  'tactics': ['tactic_backhand_blow']}]}}

LAND_SUBDOCTRINES: Dict[str, Dict[str, Any]] = {'mobile_infantry': {'key': 'mobile_infantry',
                     'track': 'infantry',
                     'name': 'Mobile Infantry',
                     'description': 'Focus our infantry on mobility to keep up the pace of '
                                    'advances and avoid getting bogged down in costly positional '
                                    'fighting.',
                     'base_effects': {'unit_mods': {'category_all_infantry': {'stats': {'breakthrough': 0.1},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []}},
                                      'army_mods': {},
                                      'tactics': ['tactic_overwhelming_fire']},
                     'rewards': [{'key': 'cavalry_charge',
                                  'name': 'Modernized Cavalry',
                                  'effects': {'unit_mods': {'category_cavalry': {'stats': {'breakthrough': 0.2},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []},
                                                            'recon': {'stats': {'breakthrough': 0.1,
                                                                                'defense': 0.1},
                                                                      'terrain_modifiers': {},
                                                                      'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'combined_arms_planning',
                                  'name': 'Infiltration',
                                  'effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                'maximum_speed': 0.05},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'decisive_operations',
                                  'name': 'First Strike Operations',
                                  'effects': {'unit_mods': {'category_vehicle_infantry': {'stats': {'max_organisation': 20.0},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []},
                                                            'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1,
                                                                                                                'breakthrough': 0.05,
                                                                                                                'defense': 0.05},
                                                                                                      'terrain_modifiers': {},
                                                                                                      'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'delegated_authority',
                                  'name': 'Delegated Authority',
                                  'effects': {'unit_mods': {'category_vehicle_infantry': {'stats': {'default_morale': 0.1,
                                                                                                    'soft_attack': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'maneuver_warfare',
                                  'name': 'Maneuver Warfare',
                                  'effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                'maximum_speed': 0.2},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                            'mot_fire_support': {'stats': {'max_organisation': 10.0,
                                                                                           'soft_attack': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}}]},
 'defensive_postures': {'key': 'defensive_postures',
                        'track': 'infantry',
                        'name': 'Defensive Postures',
                        'description': 'A training and doctrinal emphasis on defensive tactics '
                                       'designed to stubbornly hold ground, inflicting casualties '
                                       'and delay upon the attacker.',
                        'base_effects': {'unit_mods': {'category_cavalry': {'stats': {'supply_consumption': -0.01},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                       'category_all_infantry': {'stats': {'entrenchment': 0.2},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []},
                        'rewards': [{'key': 'improvised_fighting_position',
                                     'name': 'Improvised Fighting Positions',
                                     'effects': {'unit_mods': {'fire_support': {'stats': {'supply_consumption': -0.01,
                                                                                          'soft_attack': 0.2,
                                                                                          'entrenchment': 0.2},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []}},
                                                 'army_mods': {'dig_in_speed_factor': 0.05},
                                                 'tactics': []}},
                                    {'key': 'elastic_operations',
                                     'name': 'Outpost Line',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                   'defense': 0.1},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'developed_trench_networking',
                                     'name': 'Strongpoint Network',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'entrenchment': 0.2},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'field_emplacements',
                                     'name': 'Interlocking Fields of Fire',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'soft_attack': 0.1},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []},
                                                               'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'field_construction_training',
                                     'name': 'Infantry Engineer Training',
                                     'effects': {'unit_mods': {},
                                                 'army_mods': {'dig_in_speed_factor': 0.2},
                                                 'tactics': []}}]},
 'large_unit_tactics': {'key': 'large_unit_tactics',
                        'track': 'infantry',
                        'name': 'Large Unit Tactics',
                        'description': 'If we can master concentrated operations on a narrow '
                                       'front, we can create local superiority to overwhelm the '
                                       'enemy at the point of main effort and create a '
                                       'breakthrough.',
                        'base_effects': {'unit_mods': {'category_all_infantry': {'stats': {'supply_consumption': -0.01},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []},
                        'rewards': [{'key': 'wide_trench_networks',
                                     'name': 'Overnight Entrenchment',
                                     'effects': {'unit_mods': {},
                                                 'army_mods': {'dig_in_speed_factor': 0.15},
                                                 'tactics': []}},
                                    {'key': 'flexible_division_structures',
                                     'name': 'Flexible Division Structures',
                                     'effects': {'unit_mods': {'infantry': {'stats': {'combat_width': -0.2},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []}},
                                                 'army_mods': {'unit_infantry_design_cost_factor': -1.0},
                                                 'tactics': []}},
                                    {'key': 'unit_knowledge_sharing',
                                     'name': 'Unit Knowledge Sharing',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'experience_loss_factor': -0.01},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'large_front_offensive',
                                     'name': 'Large Front Offensive',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                   'soft_attack': 0.1},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []},
                                                               'fire_support': {'stats': {'breakthrough': 0.1},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                               'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {'army_morale': 0.1},
                                                 'tactics': []}},
                                    {'key': 'motorization_initiative',
                                     'name': 'Motorization Initiative',
                                     'effects': {'unit_mods': {'category_all_infantry': {'stats': {'breakthrough': 0.1,
                                                                                                   'soft_attack': 0.1},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []},
                                                               'category_vehicle_infantry': {'stats': {'supply_consumption': -0.02,
                                                                                                       'reliability': 0.1},
                                                                                             'terrain_modifiers': {},
                                                                                             'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}}]},
 'assault_infantry': {'key': 'assault_infantry',
                      'track': 'infantry',
                      'name': 'Assault Infantry',
                      'description': 'Organize the army with a combined arms approach to battle, '
                                     'with organic fire support assets integrated down to the '
                                     'smallest tactical unit.',
                      'base_effects': {'unit_mods': {'artillery': {'stats': {'soft_attack': 0.2},
                                                                   'terrain_modifiers': {},
                                                                   'battalion_multipliers': []}},
                                       'army_mods': {},
                                       'tactics': []},
                      'rewards': [{'key': 'low_echelon_fire_support',
                                   'name': 'Low Echelon Fire Support',
                                   'effects': {'unit_mods': {'artillery': {'stats': {},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_light_infantry',
                                                                                                      'soft_attack': 0.2}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'organic_battalion_fire_support',
                                   'name': 'Organic Battalion Fire Support',
                                   'effects': {'unit_mods': {'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                       'terrain_modifiers': {},
                                                                                                       'battalion_multipliers': []},
                                                             'anti_tank_battery': {'stats': {'ap_attack': 0.05,
                                                                                             'hard_attack': 0.05},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                             'anti_air_battery': {'stats': {'air_attack': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'integrated_support_batteries',
                                   'name': 'Infantry Forward Observer Training',
                                   'effects': {'unit_mods': {'category_support_artillery': {'stats': {'max_organisation': 20.0,
                                                                                                      'soft_attack': 0.05},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []},
                                                             'anti_tank': {'stats': {'max_organisation': 20.0,
                                                                                     'ap_attack': 0.05,
                                                                                     'hard_attack': 0.05},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                             'anti_air': {'stats': {'max_organisation': 20.0,
                                                                                    'air_attack': 0.05},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'breakthrough_fireteams',
                                   'name': 'Recon Pull',
                                   'effects': {'unit_mods': {'light_tank_recon': {'stats': {'max_organisation': 20.0},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': [{'additive': False,
                                                                                                             'category': 'category_all_infantry',
                                                                                                             'breakthrough': 0.2},
                                                                                                            {'additive': True,
                                                                                                             'category': 'category_all_infantry',
                                                                                                             'max_organisation': 5.0}]},
                                                             'mot_recon': {'stats': {'max_organisation': 20.0},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_all_infantry',
                                                                                                      'breakthrough': 0.1},
                                                                                                     {'additive': True,
                                                                                                      'category': 'category_all_infantry',
                                                                                                      'max_organisation': 5.0}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'assault_detachments',
                                   'name': 'Assault Detachments',
                                   'effects': {'unit_mods': {'category_support_artillery': {'stats': {'supply_consumption': -0.02},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []},
                                                             'category_regimental_support_artillery': {'stats': {'supply_consumption': -0.01},
                                                                                                       'terrain_modifiers': {},
                                                                                                       'battalion_multipliers': []},
                                                             'light_flame_tank': {'stats': {},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': [{'additive': False,
                                                                                                             'category': 'category_all_infantry',
                                                                                                             'breakthrough': 0.1,
                                                                                                             'soft_attack': 0.1}]},
                                                             'medium_flame_tank': {'stats': {},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': [{'additive': False,
                                                                                                              'category': 'category_all_infantry',
                                                                                                              'breakthrough': 0.1,
                                                                                                              'soft_attack': 0.1}]},
                                                             'heavy_flame_tank': {'stats': {},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': [{'additive': False,
                                                                                                             'category': 'category_all_infantry',
                                                                                                             'breakthrough': 0.1,
                                                                                                             'soft_attack': 0.1}]}},
                                               'army_mods': {},
                                               'tactics': []}}]},
 'mounted_infantry': {'key': 'mounted_infantry',
                      'track': 'infantry',
                      'name': 'Mounted Infantry',
                      'description': 'To update our cavalry for the 20th century, we need '
                                     'cross-country operational mobility while mounted, and to '
                                     'fight dismounted with fast, modern heavy weapons in support.',
                      'base_effects': {'unit_mods': {'category_cavalry': {'stats': {'soft_attack': 0.1,
                                                                                    'breakthrough': 0.1},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                       'army_mods': {'unit_cavalry_design_cost_factor': -1.0},
                                       'tactics': []},
                      'rewards': [{'key': 'dragoon_traditions',
                                   'name': 'Dragoon Traditions',
                                   'effects': {'unit_mods': {'category_cavalry': {'stats': {'breakthrough': 0.2,
                                                                                            'defense': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'mounted_skirmish_groups',
                                   'name': 'Regimental Scout Troop',
                                   'effects': {'unit_mods': {'recon': {'stats': {'max_organisation': 10.0,
                                                                                 'soft_attack': 0.2},
                                                                       'terrain_modifiers': {},
                                                                       'battalion_multipliers': [{'additive': False,
                                                                                                  'category': 'category_light_infantry',
                                                                                                  'soft_attack': 0.1,
                                                                                                  'defense': 0.1},
                                                                                                 {'additive': True,
                                                                                                  'category': 'category_light_infantry',
                                                                                                  'max_organisation': 5.0}]},
                                                             'category_cavalry': {'stats': {'max_organisation': 5.0},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'anti_mechanized_cavalry_groups',
                                   'name': 'Anti-Mechanized Cavalry Groups',
                                   'effects': {'unit_mods': {'category_cavalry': {'stats': {'hard_attack': 0.2,
                                                                                            'ap_attack': 0.2},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'beasts_of_war',
                                   'name': 'Beasts of War',
                                   'effects': {'unit_mods': {'category_cavalry': {'stats': {'maximum_speed': 0.4,
                                                                                            'max_strength': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                             'recon': {'stats': {'maximum_speed': 0.4},
                                                                       'terrain_modifiers': {},
                                                                       'battalion_multipliers': [{'additive': True,
                                                                                                  'category': 'category_cavalry',
                                                                                                  'max_strength': 5.0}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'limbered_combat_support',
                                   'name': 'Limbered Combat Support',
                                   'effects': {'unit_mods': {'artillery_brigade': {'stats': {'maximum_speed': 1.0},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                             'anti_tank_brigade': {'stats': {'maximum_speed': 1.0},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                             'anti_air_brigade': {'stats': {'maximum_speed': 1.0},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                             'rocket_artillery_brigade': {'stats': {'maximum_speed': 1.0},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}}]},
 'commandos': {'key': 'commandos',
               'track': 'infantry',
               'name': 'Individual Excellence',
               'description': 'Every Man An Emperor: Our troops need to be able to individually '
                              'undertake difficult and demanding tasks, and carry their weight at '
                              'all times. How we train them is vital for our success on the front.',
               'base_effects': {'unit_mods': {'logistics_company': {'stats': {},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': [{'additive': True,
                                                                                               'category': 'category_light_infantry',
                                                                                               'max_strength': 5.0}]}},
                                'army_mods': {},
                                'tactics': ['tactic_infantry_charge']},
               'rewards': [{'key': 'isolated_combat_elements',
                            'name': 'Isolated Combat Elements',
                            'effects': {'unit_mods': {'category_light_infantry': {'stats': {'supply_consumption': -0.01,
                                                                                            'reliability': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                      'field_hospital': {'stats': {'casualty_trickleback': 0.05},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': []},
                                                      'helicopter_brigade': {'stats': {'casualty_trickleback': 0.05},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []},
                                                      'helicopter_field_hospital': {'stats': {'casualty_trickleback': 0.05},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []},
                                                      'category_regimental_support_artillery': {'stats': {'supply_consumption': -0.01,
                                                                                                          'soft_attack': 0.05},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': []}},
                           {'key': 'security_zone_operations',
                            'name': 'Dispersed Element Coordination',
                            'effects': {'unit_mods': {'signal_company': {'stats': {},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': [{'additive': False,
                                                                                                    'category': 'category_all_infantry',
                                                                                                    'defense': 0.1}]},
                                                      'logistics_company': {'stats': {},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': [{'additive': True,
                                                                                                       'category': 'category_vehicle_infantry',
                                                                                                       'max_strength': 2.5}]},
                                                      'category_vehicle_infantry': {'stats': {'reliability': 0.05,
                                                                                              'breakthrough': 0.1},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': []}},
                           {'key': 'rigorous_training_regimen',
                            'name': 'Rigorous Training Regime',
                            'effects': {'unit_mods': {'recon': {'stats': {},
                                                                'terrain_modifiers': {},
                                                                'battalion_multipliers': [{'additive': False,
                                                                                           'category': 'category_all_infantry',
                                                                                           'soft_attack': 0.1}]},
                                                      'mot_recon': {'stats': {},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': [{'additive': False,
                                                                                               'category': 'category_all_infantry',
                                                                                               'soft_attack': 0.1}]},
                                                      'light_tank_recon': {'stats': {},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_all_infantry',
                                                                                                      'soft_attack': 0.1}]},
                                                      'anti_tank_battery': {'stats': {},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': [{'additive': False,
                                                                                                       'category': 'category_light_infantry',
                                                                                                       'hard_attack': 0.1}]},
                                                      'infantry': {'stats': {},
                                                                   'terrain_modifiers': {'Desert': {'attack': 0.05,
                                                                                                    'movement': 0.1},
                                                                                         'Jungle': {'attack': 0.05,
                                                                                                    'movement': 0.1},
                                                                                         'Hills': {'attack': 0.05,
                                                                                                   'movement': 0.1}},
                                                                   'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': []}},
                           {'key': 'field_intel_retrieval',
                            'name': 'Field Intelligence Gathering',
                            'effects': {'unit_mods': {},
                                        'army_mods': {'intel_from_combat_factor': 0.15},
                                        'tactics': []}},
                           {'key': 'integrated_assaults',
                            'name': 'Integrated Assaults',
                            'effects': {'unit_mods': {'category_all_infantry': {'stats': {'soft_attack': 0.1,
                                                                                          'breakthrough': 0.1},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                      'category_regimental_support_artillery': {'stats': {'breakthrough': 0.15},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []},
                                                      'fire_support': {'stats': {'breakthrough': 0.15},
                                                                       'terrain_modifiers': {},
                                                                       'battalion_multipliers': []},
                                                      'mot_fire_support': {'stats': {'breakthrough': 0.15},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': []}}]},
 'irregulars': {'key': 'irregulars',
                'track': 'infantry',
                'name': 'Irregulars',
                'description': 'An asymmetric approach to infantry warfare in which direct combat '
                               'with superior forces is avoided, using the guerilla tactics of '
                               'ambush, misdirection, and harassment to wear down enemy resolve.',
                'base_effects': {'unit_mods': {'irregular_infantry': {'stats': {'defense': 0.1,
                                                                                'supply_consumption': -0.05},
                                                                      'terrain_modifiers': {},
                                                                      'battalion_multipliers': []},
                                               'militia': {'stats': {'defense': 0.1,
                                                                     'supply_consumption': -0.01},
                                                           'terrain_modifiers': {},
                                                           'battalion_multipliers': []}},
                                 'army_mods': {},
                                 'tactics': []},
                'rewards': [{'key': 'service_by_lot',
                             'name': 'Service By Lot',
                             'effects': {'unit_mods': {},
                                         'army_mods': {'mobilization_speed': 0.05},
                                         'tactics': []}},
                            {'key': 'partisan_regiments',
                             'name': 'Partisan Regiments',
                             'effects': {'unit_mods': {'irregular_infantry': {'stats': {'combat_width': -0.4},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                       'militia': {'stats': {'combat_width': -0.4},
                                                                   'terrain_modifiers': {},
                                                                   'battalion_multipliers': []},
                                                       'category_light_infantry': {'stats': {'defense': 0.1},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []}},
                            {'key': 'improvised_officer_groups',
                             'name': 'Improvised Officer Groups',
                             'effects': {'unit_mods': {'category_light_infantry': {'stats': {'max_organisation': 10.0,
                                                                                             'soft_attack': 0.1,
                                                                                             'breakthrough': 0.1},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []}},
                            {'key': 'levee_en_masse',
                             'name': 'Levée En Masse',
                             'effects': {'unit_mods': {},
                                         'army_mods': {'conscription': 0.02,
                                                       'mobilization_speed': 0.05},
                                         'tactics': []}},
                            {'key': 'standardization_efforts',
                             'name': 'Standardization Efforts',
                             'effects': {'unit_mods': {'category_light_infantry': {'stats': {'max_organisation': 10.0,
                                                                                             'soft_attack': 0.1},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []}}]},
 'peoples_war': {'key': 'peoples_war',
                 'track': 'infantry',
                 'name': "People's Militia",
                 'description': 'The will of the people to resist, mobilized and guided by the '
                                'state, guarantees our eventual victory over imperialism and '
                                'counter-revolution.',
                 'base_effects': {'unit_mods': {'militia': {'stats': {'soft_attack': 0.1,
                                                                      'defense': 0.2},
                                                            'terrain_modifiers': {},
                                                            'battalion_multipliers': []}},
                                  'army_mods': {},
                                  'tactics': ['tactic_guerrilla_tactics']},
                 'rewards': [{'key': 'revolutionary_base_area',
                              'name': 'Revolutionary Base Area',
                              'effects': {'unit_mods': {'militia': {'stats': {'defense': 0.1,
                                                                              'supply_consumption': -0.02},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': []},
                                                        'category_light_infantry': {'stats': {'max_organisation': 5.0},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'destruction_over_land_gains',
                              'name': 'Destruction over Land Gains',
                              'effects': {'unit_mods': {'category_light_infantry': {'stats': {'default_morale': 0.1},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []},
                                                        'militia': {'stats': {'equipment_capture_factor': 0.01},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': []},
                                                        'field_guns': {'stats': {'soft_attack': 0.1,
                                                                                 'breakthrough': 0.1},
                                                                       'terrain_modifiers': {},
                                                                       'battalion_multipliers': []}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'quick_decision_offensive_warfare',
                              'name': 'Quick Decision Offensive Warfare',
                              'effects': {'unit_mods': {'militia': {'stats': {'initiative': 0.015,
                                                                              'max_organisation': 10.0,
                                                                              'breakthrough': 0.2},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': []}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'people_not_things',
                              'name': 'People, not Things',
                              'effects': {'unit_mods': {'category_light_infantry': {'stats': {'soft_attack': 0.1,
                                                                                              'max_strength': 0.15},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                          'army_mods': {},
                                          'tactics': []}}]},
 'great_war_infantry': {'key': 'great_war_infantry',
                        'track': 'infantry',
                        'name': 'Great War Infantry',
                        'description': 'A methodical approach to infantry fighting, featuring '
                                       'attacks with limited objectives followed by rapid '
                                       'entrenchment to tenaciously hold the won ground.',
                        'base_effects': {'unit_mods': {'category_cavalry': {'stats': {'supply_consumption': -0.02},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                       'category_light_infantry': {'stats': {'defense': 0.1},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                         'army_mods': {'production_speed_bunker_factor': 0.25},
                                         'tactics': []},
                        'rewards': [{'key': 'traverse_digging',
                                     'name': 'Zig-zag Trenches',
                                     'effects': {'unit_mods': {'fire_support': {'stats': {'soft_attack': 0.1,
                                                                                          'defense': 0.1},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                               'engineer': {'stats': {},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': [{'additive': True,
                                                                                                       'category': 'category_light_infantry',
                                                                                                       'entrenchment': 0.05}]}},
                                                 'army_mods': {'dig_in_speed_factor': 0.05},
                                                 'tactics': []}},
                                    {'key': 'sapping_operations',
                                     'name': 'Communication Trenches',
                                     'effects': {'unit_mods': {'category_light_infantry': {'stats': {'defense': 0.1},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []},
                                                               'field_hospital': {'stats': {'casualty_trickleback': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'centralized_artillery_control',
                                     'name': 'Creeping Barrages',
                                     'effects': {'unit_mods': {'artillery': {'stats': {'soft_attack': 0.1},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': False,
                                                                                                        'category': 'category_light_infantry',
                                                                                                        'soft_attack': 0.1,
                                                                                                        'breakthrough': 0.1}]},
                                                               'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'field_fortification_emphasis',
                                     'name': 'Overhead Cover',
                                     'effects': {'unit_mods': {'category_light_infantry': {'stats': {'reliability': 0.05,
                                                                                                     'defense': 0.05,
                                                                                                     'max_organisation': 5.0},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'redoubt_networks',
                                     'name': 'Redoubt Networks',
                                     'effects': {'unit_mods': {},
                                                 'army_mods': {'dig_in_speed_factor': 0.1,
                                                               'max_dig_in': 5.0},
                                                 'tactics': []}}]},
 'armored_spearhead': {'key': 'armored_spearhead',
                       'track': 'armor',
                       'name': 'Armored Spearhead',
                       'description': 'The tank offers the opportunity to create a war of movement '
                                      'rather than mere attrition. Our doctrine should emphasize '
                                      'rapid exploitation of breakthroughs to surround and destroy '
                                      'the enemy.',
                       'base_effects': {'unit_mods': {},
                                        'army_mods': {},
                                        'tactics': ['tactic_breakthrough']},
                       'rewards': [{'key': 'force_concentration',
                                    'name': 'Point of Main Effort',
                                    'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 2.0,
                                                                                           'default_morale': 0.05},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'armored_breakthrough_exploits',
                                    'name': 'Breakthrough Exploitation',
                                    'effects': {'unit_mods': {'category_all_armor': {'stats': {'breakthrough': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'local_reserves',
                                    'name': 'Local Reserves',
                                    'effects': {'unit_mods': {'armored_car': {'stats': {'default_morale': 0.1,
                                                                                        'max_organisation': 7.0},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                              'light_armor': {'stats': {'default_morale': 0.1,
                                                                                        'max_organisation': 3.0},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                              'category_self_propelled_anti_air_regimental_support': {'stats': {'max_organisation': 5.0,
                                                                                                                                'air_attack': 0.05},
                                                                                                                      'terrain_modifiers': {},
                                                                                                                      'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'tactical_reconnaissance',
                                    'name': 'Strong Point Bypassing',
                                    'effects': {'unit_mods': {'category_all_armor': {'stats': {'breakthrough': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'assault_detachments',
                                    'name': 'Flank Protection',
                                    'effects': {'unit_mods': {'armored_car': {'stats': {'default_morale': 0.2,
                                                                                        'max_organisation': 3.0,
                                                                                        'breakthrough': 0.2},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                              'category_tanks': {'stats': {'max_organisation': 3.0,
                                                                                           'breakthrough': 0.2},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}}]},
 'armored_spearhead_no_lar': {'key': 'armored_spearhead_no_lar',
                              'track': 'armor',
                              'name': 'Armored Spearhead',
                              'description': 'The tank offers the opportunity to create a war of '
                                             'movement rather than mere attrition. Our doctrine '
                                             'should emphasize rapid exploitation of breakthroughs '
                                             'to surround and destroy the enemy.',
                              'base_effects': {'unit_mods': {},
                                               'army_mods': {},
                                               'tactics': ['tactic_breakthrough']},
                              'rewards': [{'key': 'force_concentration',
                                           'name': '$armored_spearhead_force_concentration$',
                                           'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 2.0,
                                                                                                  'default_morale': 0.05},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'armored_breakthrough_exploits',
                                           'name': '$armored_spearhead_armored_breakthrough_exploits$',
                                           'effects': {'unit_mods': {'category_all_armor': {'stats': {'breakthrough': 0.1},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'local_reserves',
                                           'name': '$armored_spearhead_local_reserves$',
                                           'effects': {'unit_mods': {'recon': {'stats': {'max_organisation': 10.0},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []},
                                                                     'light_armor': {'stats': {'default_morale': 0.1,
                                                                                               'max_organisation': 3.0},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'tactical_reconnaissance',
                                           'name': '$armored_spearhead_tactical_reconnaissance$',
                                           'effects': {'unit_mods': {'category_all_armor': {'stats': {'breakthrough': 0.1},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'assault_detachments',
                                           'name': '$armored_spearhead_assault_detachments$',
                                           'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 3.0,
                                                                                                  'breakthrough': 0.2},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}}]},
 'armored_infantry_support': {'key': 'armored_infantry_support',
                              'track': 'armor',
                              'name': 'Armored Infantry Support',
                              'description': 'With their firepower and protection, tanks can '
                                             'rapidly knock out machine guns and other weapons '
                                             'that hinder the advance of the infantry. '
                                             'Tank-Infantry cooperation must be seamless.',
                              'base_effects': {'unit_mods': {},
                                               'army_mods': {},
                                               'tactics': ['tactic_blitz']},
                              'rewards': [{'key': 'mobile_reserves',
                                           'name': 'Assault Overrun',
                                           'effects': {'unit_mods': {'medium_armor': {'stats': {'breakthrough': 0.05,
                                                                                                'soft_attack': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                                     'heavy_armor': {'stats': {'breakthrough': 0.05,
                                                                                               'soft_attack': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'armored_cohorts',
                                           'name': 'Armored Cohorts',
                                           'effects': {'unit_mods': {'medium_armor': {'stats': {'max_organisation': 5.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                                     'heavy_armor': {'stats': {'max_organisation': 5.0},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []},
                                                                     'category_tank_destroyer_regimental_support': {'stats': {'max_organisation': 5.0},
                                                                                                                    'terrain_modifiers': {},
                                                                                                                    'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'maintenance_routines',
                                           'name': 'Maintenance Routines',
                                           'effects': {'unit_mods': {'armored_maintenance': {'stats': {},
                                                                                             'terrain_modifiers': {},
                                                                                             'battalion_multipliers': [{'additive': True,
                                                                                                                        'category': 'category_all_armor',
                                                                                                                        'max_strength': 0.15}]}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'fuel_rationing',
                                           'name': 'Fuel Rationing',
                                           'effects': {'unit_mods': {'heavy_armor': {'stats': {'supply_consumption': -0.08},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'mobile_armored_strongpoints',
                                           'name': 'Mobile Armored Strongpoints',
                                           'effects': {'unit_mods': {'category_all_infantry': {'stats': {'breakthrough': 0.05},
                                                                                               'terrain_modifiers': {},
                                                                                               'battalion_multipliers': []},
                                                                     'heavy_armor': {'stats': {'breakthrough': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []},
                                                                     'heavy_sp_anti_air_support': {'stats': {'air_attack': 0.05},
                                                                                                   'terrain_modifiers': {},
                                                                                                   'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}}]},
 'streamlined_deployment': {'key': 'streamlined_deployment',
                            'track': 'armor',
                            'name': 'Streamlined Deployment',
                            'description': 'Offensive results on the strategic scale can only be '
                                           'achieved when all arms, including tanks, are massed to '
                                           'concentrate their striking power at the decisive '
                                           'point.',
                            'base_effects': {'unit_mods': {'category_all_armor': {'stats': {'soft_attack': 0.1,
                                                                                            'breakthrough': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []},
                            'rewards': [{'key': 'flexible_armored_battalions',
                                         'name': 'Army Mechanization Drive',
                                         'effects': {'unit_mods': {'light_tank_recon': {'stats': {},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': [{'additive': True,
                                                                                                                   'category': 'category_all_armor',
                                                                                                                   'max_organisation': 2.0}]}},
                                                     'army_mods': {'unit_medium_armor_design_cost_factor': -0.5,
                                                                   'unit_light_armor_design_cost_factor': -0.5},
                                                     'tactics': []}},
                                        {'key': 'mechanized_wave',
                                         'name': 'Mechanized Wave',
                                         'effects': {'unit_mods': {'mechanized': {'stats': {'max_organisation': 5.0,
                                                                                            'default_morale': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                                   'category_all_armor': {'stats': {'default_morale': 0.05},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'tank_desant',
                                         'name': 'Tank Desant',
                                         'effects': {'unit_mods': {'armored_signal': {'stats': {},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                                 'category': 'category_light_infantry',
                                                                                                                 'maximum_speed': 0.05}]},
                                                                   'light_tank_recon': {'stats': {},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': [{'additive': False,
                                                                                                                   'category': 'category_light_infantry',
                                                                                                                   'maximum_speed': 0.05}]}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'full_front_deployment',
                                         'name': 'Austere Logistics',
                                         'effects': {'unit_mods': {'category_all_armor': {'stats': {'reliability': 0.05,
                                                                                                    'supply_consumption': -0.02},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'continuous_offensives',
                                         'name': 'Continuous Offensives',
                                         'effects': {'unit_mods': {'category_all_armor': {'stats': {'default_morale': 0.05,
                                                                                                    'max_organisation': 3.0,
                                                                                                    'breakthrough': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}}]},
 'mobile_defense': {'key': 'mobile_defense',
                    'track': 'armor',
                    'name': 'Mobile Defense',
                    'description': 'Armored forces are useful in defense as well as attack. With '
                                   'their mobility they can rapidly occupy strong defensive '
                                   'terrain, or move in to position to counter enemy '
                                   'breakthroughs.',
                    'base_effects': {'unit_mods': {'armored_engineer': {'stats': {},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': [{'additive': True,
                                                                                                   'category': 'category_all_armor',
                                                                                                   'entrenchment': 0.02}]},
                                                   'category_all_armor': {'stats': {'defense': 0.1},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                     'army_mods': {},
                                     'tactics': []},
                    'rewards': [{'key': 'mechanized_offensive',
                                 'name': 'Battle Taxis',
                                 'effects': {'unit_mods': {'mechanized': {'stats': {'defense': 0.1,
                                                                                    'soft_attack': 0.1},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []}},
                                {'key': 'advance_under_fire',
                                 'name': 'Advance Under Fire',
                                 'effects': {'unit_mods': {'light_armor': {'stats': {'breakthrough': 0.1,
                                                                                     'default_morale': 0.2},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                           'medium_armor': {'stats': {'breakthrough': 0.1,
                                                                                      'default_morale': 0.1},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []}},
                                {'key': 'attached_support',
                                 'name': 'Tracked Combat Support',
                                 'effects': {'unit_mods': {'assault_engineer': {'stats': {'max_organisation': 10.0},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                           'armored_engineer': {'stats': {'max_organisation': 10.0},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                           'armored_signal': {'stats': {'max_organisation': 10.0},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                           'category_self_propelled_anti_air_regimental_support': {'stats': {'max_organisation': 10.0},
                                                                                                                   'terrain_modifiers': {},
                                                                                                                   'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []}},
                                {'key': 'combined_anti_armor',
                                 'name': 'Combined Anti-armor',
                                 'effects': {'unit_mods': {'anti_tank': {'stats': {},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': [{'additive': False,
                                                                                                    'category': 'category_all_armor',
                                                                                                    'hard_attack': 0.05,
                                                                                                    'ap_attack': 0.05}]},
                                                           'category_tank_destroyer_regimental_support': {'stats': {'max_organisation': 10.0},
                                                                                                          'terrain_modifiers': {},
                                                                                                          'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []}},
                                {'key': 'tank_on_tank_engagement',
                                 'name': 'Tank-on-Tank Engagement',
                                 'effects': {'unit_mods': {'category_all_armor': {'stats': {'hard_attack': 0.1,
                                                                                            'soft_attack': 0.1,
                                                                                            'ap_attack': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []}}]},
 'armored_cavalry': {'key': 'armored_cavalry',
                     'track': 'armor',
                     'name': 'Armored Cavalry',
                     'description': 'Mechanized forces backed up by fast light tanks and armored '
                                    'cars can probe for weak spots and hit the enemy where they '
                                    'are most vulnerable.',
                     'base_effects': {'unit_mods': {'armored_car': {'stats': {'max_organisation': 5.0,
                                                                              'defense': 0.1},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': []},
                                                    'mechanized': {'stats': {'max_organisation': 5.0,
                                                                             'defense': 0.05},
                                                                   'terrain_modifiers': {},
                                                                   'battalion_multipliers': []}},
                                      'army_mods': {},
                                      'tactics': []},
                     'rewards': [{'key': 'cruiser_tanks',
                                  'name': 'Cruiser Tanks',
                                  'effects': {'unit_mods': {'light_armor': {'stats': {'maximum_speed': 0.1,
                                                                                      'max_organisation': 5.0,
                                                                                      'breakthrough': 0.05},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'quick_response_force',
                                  'name': 'Motorized Security Forces',
                                  'effects': {'unit_mods': {'motorized_military_police': {'stats': {},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': [{'additive': False,
                                                                                                                     'category': 'category_vehicle_infantry',
                                                                                                                     'suppression_factor': 0.05}]},
                                                            'armored_car': {'stats': {'suppression_factor': 0.2},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'speed_as_armour',
                                  'name': 'Speed as Armour',
                                  'effects': {'unit_mods': {'light_armor': {'stats': {'maximum_speed': 0.05,
                                                                                      'breakthrough': 0.05},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                            'armored_car': {'stats': {'maximum_speed': 0.05,
                                                                                      'breakthrough': 0.1,
                                                                                      'soft_attack': 0.1},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                            'mechanized': {'stats': {'maximum_speed': 0.05,
                                                                                     'breakthrough': 0.05},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'fighting_reconnaissance',
                                  'name': 'Fighting Reconnaissance',
                                  'effects': {'unit_mods': {'armored_car_recon': {'stats': {'max_organisation': 3.0,
                                                                                            'soft_attack': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                            'light_tank_recon': {'stats': {'max_organisation': 2.0,
                                                                                           'soft_attack': 0.05},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []},
                                                            'anti_tank_battery': {'stats': {'ap_attack': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                            'mot_fire_support': {'stats': {'max_organisation': 5.0,
                                                                                           'soft_attack': 0.05,
                                                                                           'default_morale': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'sustained_deployments',
                                  'name': 'External Stowage',
                                  'effects': {'unit_mods': {'armored_car': {'stats': {'max_organisation': 5.0,
                                                                                      'soft_attack': 0.05,
                                                                                      'default_morale': 0.2},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                            'light_armor': {'stats': {'max_organisation': 5.0,
                                                                                      'soft_attack': 0.05,
                                                                                      'hard_attack': 0.1,
                                                                                      'default_morale': 0.15},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                            'mechanized': {'stats': {'max_organisation': 5.0,
                                                                                     'soft_attack': 0.05,
                                                                                     'default_morale': 0.1},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                            'motorized': {'stats': {'max_organisation': 5.0,
                                                                                    'soft_attack': 0.05,
                                                                                    'default_morale': 0.1},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}}]},
 'armored_cavalry_no_lar': {'key': 'armored_cavalry_no_lar',
                            'track': 'armor',
                            'name': 'Armored Cavalry',
                            'description': 'Mechanized forces backed up by fast light tanks and '
                                           'armored cars can probe for weak spots and hit the '
                                           'enemy where they are most vulnerable.',
                            'base_effects': {'unit_mods': {'motorized': {'stats': {'max_organisation': 5.0,
                                                                                   'defense': 0.1},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': []},
                                                           'mechanized': {'stats': {'max_organisation': 5.0,
                                                                                    'defense': 0.05},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []},
                            'rewards': [{'key': 'cruiser_tanks',
                                         'name': '$armored_cavalry_cruiser_tanks$',
                                         'effects': {'unit_mods': {'light_armor': {'stats': {'maximum_speed': 0.1,
                                                                                             'max_organisation': 5.0,
                                                                                             'breakthrough': 0.05},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'quick_response_force',
                                         'name': '$armored_cavalry_quick_response_force$',
                                         'effects': {'unit_mods': {'motorized_military_police': {'stats': {},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': [{'additive': False,
                                                                                                                            'category': 'category_vehicle_infantry',
                                                                                                                            'suppression_factor': 0.05}]}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'speed_as_armour',
                                         'name': '$armored_cavalry_speed_as_armour$',
                                         'effects': {'unit_mods': {'light_armor': {'stats': {'maximum_speed': 0.05,
                                                                                             'breakthrough': 0.05},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                                   'motorized': {'stats': {'maximum_speed': 0.05},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []},
                                                                   'mechanized': {'stats': {'maximum_speed': 0.05,
                                                                                            'breakthrough': 0.05},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'fighting_reconnaissance',
                                         'name': 'fighting_reconnaissance',
                                         'effects': {'unit_mods': {'recon': {'stats': {'max_organisation': 3.0,
                                                                                       'soft_attack': 0.05},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []},
                                                                   'light_tank_recon': {'stats': {'max_organisation': 2.0,
                                                                                                  'soft_attack': 0.05},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []},
                                                                   'anti_tank_battery': {'stats': {'max_organisation': 2.0,
                                                                                                   'ap_attack': 0.05},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'sustained_deployments',
                                         'name': '$armored_cavalry_sustained_deployments$',
                                         'effects': {'unit_mods': {'light_armor': {'stats': {'max_organisation': 5.0,
                                                                                             'soft_attack': 0.05,
                                                                                             'hard_attack': 0.1,
                                                                                             'default_morale': 0.15},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                                   'mechanized': {'stats': {'max_organisation': 5.0,
                                                                                            'soft_attack': 0.05,
                                                                                            'default_morale': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                                   'motorized': {'stats': {'max_organisation': 5.0,
                                                                                           'soft_attack': 0.05,
                                                                                           'default_morale': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []},
                                                                   'mot_fire_support': {'stats': {'max_organisation': 5.0,
                                                                                                  'soft_attack': 0.05,
                                                                                                  'default_morale': 0.1},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}}]},
 'tank_destroyer_force': {'key': 'tank_destroyer_force',
                          'track': 'armor',
                          'name': 'Tank Destroyer Force',
                          'description': 'When faced with major enemy armored threats, we cannot '
                                         'count on our first line defenses always stopping the '
                                         'foe. Defense in depth by ambushing anti-tank units is '
                                         'essential.',
                          'base_effects': {'unit_mods': {'category_all_armor': {'stats': {'defense': 0.1,
                                                                                          'hard_attack': 0.1,
                                                                                          'ap_attack': 0.1},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []}},
                                           'army_mods': {},
                                           'tactics': []},
                          'rewards': [{'key': 'mobile_anti_tank',
                                       'name': 'Mobile Anti-Tank Reserves',
                                       'effects': {'unit_mods': {'mot_anti_tank_brigade': {'stats': {'max_organisation': 8.0,
                                                                                                     'hard_attack': 0.1,
                                                                                                     'ap_attack': 0.1},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'committed_operational_units',
                                       'name': 'Organic Combat Engineer Platoons',
                                       'effects': {'unit_mods': {'assault_engineer': {'stats': {},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                                 'category': 'category_tank_destroyers',
                                                                                                                 'reliability': 0.02,
                                                                                                                 'soft_attack': 0.05,
                                                                                                                 'hard_attack': 0.1}]}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'redeployment_priority',
                                       'name': 'Rapid Riposte',
                                       'effects': {'unit_mods': {'category_tank_destroyers': {'stats': {'supply_consumption': -0.02,
                                                                                                        'default_morale': 0.1},
                                                                                              'terrain_modifiers': {},
                                                                                              'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'independent_counterattacks',
                                       'name': 'Independent Counterattacks',
                                       'effects': {'unit_mods': {'category_tank_destroyers': {'stats': {'max_organisation': 6.0,
                                                                                                        'initiative': 0.01},
                                                                                              'terrain_modifiers': {},
                                                                                              'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'selfsufficient_battalion',
                                       'name': 'Radio-Directed Breakthrough Containment',
                                       'effects': {'unit_mods': {'armored_signal': {'stats': {},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': [{'additive': False,
                                                                                                               'category': 'category_tank_destroyers',
                                                                                                               'hard_attack': 0.1,
                                                                                                               'ap_attack': 0.1}]},
                                                                 'category_tank_destroyer_regimental_support': {'stats': {'max_organisation': 5.0},
                                                                                                                'terrain_modifiers': {},
                                                                                                                'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}}]},
 'fire_concentration': {'key': 'fire_concentration',
                        'track': 'combat_support',
                        'name': 'Fire Concentration',
                        'description': 'By centralizing control of fire support assets, our army '
                                       'can concentrate firepower at the critical point rather '
                                       'than frittering it away in small packets.',
                        'base_effects': {'unit_mods': {'category_line_artillery': {'stats': {'breakthrough': 0.1,
                                                                                             'max_organisation': 10.0},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': ['tactic_overwhelming_fire']},
                        'rewards': [{'key': 'predicted_fire',
                                     'name': 'Predicted Fire',
                                     'effects': {'unit_mods': {'category_line_artillery': {'stats': {'breakthrough': 0.1},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'standing_barrage',
                                     'name': 'Prepared Gun Pits',
                                     'effects': {'unit_mods': {'artillery_brigade': {'stats': {'combat_width': -0.8},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []},
                                                               'rocket_artillery_brigade': {'stats': {'combat_width': -0.8},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'artillery_groups',
                                     'name': 'Battery Local Security',
                                     'effects': {'unit_mods': {'category_artillery': {'stats': {'soft_attack': 0.1,
                                                                                                'defense': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'dedicated_air_support',
                                     'name': 'Centralized Anti-Aircraft Support',
                                     'effects': {'unit_mods': {'category_anti_air': {'stats': {'air_attack': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'weakpoint_studies',
                                     'name': 'Flanking Fire Emplacement',
                                     'effects': {'unit_mods': {'anti_tank_brigade': {'stats': {'ap_attack': 0.1,
                                                                                               'hard_attack': 0.1},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []},
                                                               'category_regimental_support_artillery': {'stats': {'defense': 0.1,
                                                                                                                   'breakthrough': 0.1},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}}]},
 'anti_tank_frontline': {'key': 'anti_tank_frontline',
                         'track': 'combat_support',
                         'name': 'Anti-Tank Frontline',
                         'description': 'A unified approach to anti-tank defense at all tactical '
                                        'echelons, defending the flanks of friendly breakthroughs '
                                        'and channeling enemy armored attacks into pre-planned '
                                        'kill zones.',
                         'base_effects': {'unit_mods': {'engineer': {'stats': {},
                                                                     'terrain_modifiers': {},
                                                                     'battalion_multipliers': [{'additive': True,
                                                                                                'category': 'category_line_artillery',
                                                                                                'entrenchment': 0.2}]}},
                                          'army_mods': {},
                                          'tactics': []},
                         'rewards': [{'key': 'pakfront',
                                      'name': 'Pakfront',
                                      'effects': {'unit_mods': {'anti_tank_brigade': {'stats': {'ap_attack': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                                'anti_tank': {'stats': {'ap_attack': 0.1},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                                'anti_tank_battery': {'stats': {'ap_attack': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                  'army_mods': {},
                                                  'tactics': []}},
                                     {'key': 'emplacement_rotation',
                                      'name': 'Emplacement Rotation',
                                      'effects': {'unit_mods': {'anti_tank_brigade': {'stats': {'defense': 0.2,
                                                                                                'max_organisation': 10.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                  'army_mods': {},
                                                  'tactics': []}},
                                     {'key': 'weakpoint_studies',
                                      'name': 'Weak-point Studies',
                                      'effects': {'unit_mods': {'anti_tank_brigade': {'stats': {'ap_attack': 0.1,
                                                                                                'hard_attack': 0.1,
                                                                                                'soft_attack': 0.2},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                  'army_mods': {},
                                                  'tactics': []}},
                                     {'key': 'offensive_deployments',
                                      'name': 'Offensive Deployment',
                                      'effects': {'unit_mods': {'mot_anti_tank_brigade': {'stats': {'breakthrough': 0.2,
                                                                                                    'ap_attack': 0.2},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                                  'army_mods': {},
                                                  'tactics': []}},
                                     {'key': 'assault_anti_tank',
                                      'name': 'Direct Fire Bunker-Busting',
                                      'effects': {'unit_mods': {'mot_anti_tank_brigade': {'stats': {'soft_attack': 0.2,
                                                                                                    'hard_attack': 0.2},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []}},
                                                  'army_mods': {},
                                                  'tactics': []}}]},
 'flying_batteries': {'key': 'flying_batteries',
                      'track': 'combat_support',
                      'name': 'Flying Batteries',
                      'description': 'An army-wide initiative to increase the mobility of '
                                     'supporting arms so they can keep pace with rapid motorized '
                                     'advances, and go into action quickly in support.',
                      'base_effects': {'unit_mods': {'category_line_artillery': {'stats': {'soft_attack': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                       'army_mods': {},
                                       'tactics': []},
                      'rewards': [{'key': 'deployment_drills',
                                   'name': 'Deployment Drills',
                                   'effects': {'unit_mods': {'mot_rocket_artillery_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                        'soft_attack': 0.05,
                                                                                                        'breakthrough': 0.1},
                                                                                              'terrain_modifiers': {},
                                                                                              'battalion_multipliers': []},
                                                             'motorized_rocket_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                    'soft_attack': 0.05,
                                                                                                    'breakthrough': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []},
                                                             'mot_artillery_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                 'soft_attack': 0.05,
                                                                                                 'breakthrough': 0.1},
                                                                                       'terrain_modifiers': {},
                                                                                       'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'counter_battery_tasks',
                                   'name': 'Counter-battery Tasks',
                                   'effects': {'unit_mods': {'recon': {'stats': {'recon': 0.25},
                                                                       'terrain_modifiers': {},
                                                                       'battalion_multipliers': [{'additive': False,
                                                                                                  'category': 'category_line_artillery',
                                                                                                  'soft_attack': 0.05,
                                                                                                  'defense': 0.1}]},
                                                             'mot_recon': {'stats': {'recon': 0.25},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_line_artillery',
                                                                                                      'soft_attack': 0.05,
                                                                                                      'defense': 0.1}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'ballistics_corrections',
                                   'name': 'Armored Forward Observer Vehicles',
                                   'effects': {'unit_mods': {'armored_signal': {'stats': {},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': [{'additive': True,
                                                                                                           'category': 'category_line_artillery',
                                                                                                           'supply_consumption': -0.01,
                                                                                                           'max_strength': 0.2},
                                                                                                          {'additive': False,
                                                                                                           'category': 'category_line_artillery',
                                                                                                           'initiative': 0.02}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'mobile_barrages',
                                   'name': 'Fast Unlimbering',
                                   'effects': {'unit_mods': {'category_line_artillery': {'stats': {'default_morale': 0.05,
                                                                                                   'breakthrough': 0.05},
                                                                                         'terrain_modifiers': {},
                                                                                         'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'wide_dispersal_positions',
                                   'name': 'Widely Dispersed Batteries',
                                   'effects': {'unit_mods': {'mot_rocket_artillery_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                        'soft_attack': 0.05,
                                                                                                        'defense': 0.1},
                                                                                              'terrain_modifiers': {},
                                                                                              'battalion_multipliers': []},
                                                             'motorized_rocket_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                    'soft_attack': 0.05,
                                                                                                    'defense': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []},
                                                             'mot_artillery_brigade': {'stats': {'max_organisation': 10.0,
                                                                                                 'soft_attack': 0.05,
                                                                                                 'defense': 0.1},
                                                                                       'terrain_modifiers': {},
                                                                                       'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}}]},
 'air_cavalry': {'key': 'air_cavalry',
                 'track': 'combat_support',
                 'name': 'Air Cavalry',
                 'description': 'The helicopter offers the radical possibility of introducing the '
                                'third, vertical dimension into land warfare. We can configure the '
                                'army to exploit this new approach for maximum mobility and '
                                'surprise.',
                 'base_effects': {'unit_mods': {}, 'army_mods': {}, 'tactics': []},
                 'rewards': [{'key': 'airborne_observers',
                              'name': 'Heliborne Observers',
                              'effects': {'unit_mods': {'helicopter_recon': {'stats': {'max_organisation': 10.0},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': False,
                                                                                                        'category': 'category_artillery',
                                                                                                        'soft_attack': 0.1}]}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'service_and_support',
                              'name': 'Service & Support',
                              'effects': {'unit_mods': {'maintenance_company': {'stats': {},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': [{'additive': True,
                                                                                                           'category': 'category_helicopter_support_companies',
                                                                                                           'max_strength': 0.5}]}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'rescue_liasions',
                              'name': 'Rescue Liaisons',
                              'effects': {'unit_mods': {'helicopter_field_hospital': {'stats': {'max_organisation': 5.0,
                                                                                                'casualty_trickleback': 0.05},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                                 'category': 'category_all_infantry',
                                                                                                                 'max_strength': 0.05,
                                                                                                                 'default_morale': 0.05}]}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'transport_assault',
                              'name': 'Transport-Assault',
                              'effects': {'unit_mods': {'helicopter_transport': {'stats': {'breakthrough': 0.05,
                                                                                           'max_organisation': 10.0},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': [{'additive': False,
                                                                                                            'category': 'category_light_infantry',
                                                                                                            'maximum_speed': 0.2,
                                                                                                            'breakthrough': 0.05}]}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'intervention_units',
                              'name': 'Intervention Units',
                              'effects': {'unit_mods': {'helicopter_brigade': {'stats': {'max_organisation': 10.0},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': [{'additive': False,
                                                                                                          'category': 'category_all_infantry',
                                                                                                          'soft_attack': 0.1}]}},
                                          'army_mods': {},
                                          'tactics': []}}]},
 'mobile_recon_and_assault': {'key': 'mobile_recon_and_assault',
                              'track': 'combat_support',
                              'name': 'Mobile Recon & Assault',
                              'description': 'With a combined arms approach backed up by extensive '
                                             'motorization, we can use reconnaissance units to '
                                             'find the enemy, and mobile heavy weapons to rapidly '
                                             'smash them.',
                              'base_effects': {'unit_mods': {'armored_car': {'stats': {'max_organisation': 3.0},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []},
                                                             'light_armor': {'stats': {'max_organisation': 5.0},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []},
                              'rewards': [{'key': 'motorization_support',
                                           'name': 'Organic Motorized Supply',
                                           'effects': {'unit_mods': {'category_mobile_and_mobile_combat_sup': {'stats': {'maximum_speed': 0.1,
                                                                                                                         'default_morale': 0.1},
                                                                                                               'terrain_modifiers': {},
                                                                                                               'battalion_multipliers': []},
                                                                     'mot_fire_support': {'stats': {'max_organisation': 10.0,
                                                                                                    'soft_attack': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []},
                                                                     'logistics_company': {'stats': {'supply_consumption_factor': -0.05},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'long_range_reconnaissance',
                                           'name': 'Long Range Reconnaissance',
                                           'effects': {'unit_mods': {'category_recon': {'stats': {'maximum_speed': 0.15},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'mobile_operational_deployments',
                                           'name': 'Mobile Operational Deployment',
                                           'effects': {'unit_mods': {'light_tank_recon': {'stats': {},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': [{'additive': False,
                                                                                                                     'category': 'category_all_armor',
                                                                                                                     'breakthrough': 0.1}]},
                                                                     'mot_artillery_brigade': {'stats': {'soft_attack': 0.05},
                                                                                               'terrain_modifiers': {},
                                                                                               'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'self_propelled_support_elements',
                                           'name': 'Fire On The Move',
                                           'effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                           'terrain_modifiers': {},
                                                                                                           'battalion_multipliers': []},
                                                                     'category_self_propelled_anti_air': {'stats': {'air_attack': 0.15,
                                                                                                                    'soft_attack': 0.05},
                                                                                                          'terrain_modifiers': {},
                                                                                                          'battalion_multipliers': []},
                                                                     'category_tank_destroyers': {'stats': {'hard_attack': 0.1,
                                                                                                            'ap_attack': 0.03},
                                                                                                  'terrain_modifiers': {},
                                                                                                  'battalion_multipliers': []},
                                                                     'armored_car': {'stats': {'breakthrough': 0.2,
                                                                                               'default_morale': 0.2},
                                                                                     'terrain_modifiers': {},
                                                                                     'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}},
                                          {'key': 'deep_reconnaissance_focus',
                                           'name': 'Deep Reconnaissance Focus',
                                           'effects': {'unit_mods': {'category_recon': {'stats': {'maximum_speed': 0.1},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []},
                                                                     'light_tank_recon': {'stats': {'recon': 0.2,
                                                                                                    'breakthrough': 0.1},
                                                                                          'terrain_modifiers': {},
                                                                                          'battalion_multipliers': []},
                                                                     'category_tank_destroyer_regimental_support': {'stats': {'hard_attack': 0.05},
                                                                                                                    'terrain_modifiers': {},
                                                                                                                    'battalion_multipliers': []},
                                                                     'category_self_propelled_anti_air_regimental_support': {'stats': {'air_attack': 0.05},
                                                                                                                             'terrain_modifiers': {},
                                                                                                                             'battalion_multipliers': []}},
                                                       'army_mods': {},
                                                       'tactics': []}}]},
 'mobile_recon_and_assault_no_lar': {'key': 'mobile_recon_and_assault_no_lar',
                                     'track': 'combat_support',
                                     'name': 'Mobile Recon & Assault',
                                     'description': 'With a combined arms approach backed up by '
                                                    'extensive motorization, we can use '
                                                    'reconnaissance units to find the enemy, and '
                                                    'mobile heavy weapons to rapidly smash them.',
                                     'base_effects': {'unit_mods': {'light_armor': {'stats': {'max_organisation': 5.0},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                                      'army_mods': {},
                                                      'tactics': []},
                                     'rewards': [{'key': 'motorization_support',
                                                  'name': '$mobile_recon_and_assault_motorization_support$',
                                                  'effects': {'unit_mods': {'category_mobile_and_mobile_combat_sup': {'stats': {'maximum_speed': 0.1,
                                                                                                                                'default_morale': 0.1},
                                                                                                                      'terrain_modifiers': {},
                                                                                                                      'battalion_multipliers': []}},
                                                              'army_mods': {},
                                                              'tactics': []}},
                                                 {'key': 'long_range_reconnaissance',
                                                  'name': 'long_range_reconnaissance',
                                                  'effects': {'unit_mods': {'category_recon': {'stats': {'maximum_speed': 0.15},
                                                                                               'terrain_modifiers': {},
                                                                                               'battalion_multipliers': []}},
                                                              'army_mods': {},
                                                              'tactics': []}},
                                                 {'key': 'mobile_operational_deployments',
                                                  'name': '$mobile_recon_and_assault_mobile_operational_deployments$',
                                                  'effects': {'unit_mods': {'light_tank_recon': {'stats': {},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': [{'additive': False,
                                                                                                                            'category': 'category_all_armor',
                                                                                                                            'breakthrough': 0.1}]},
                                                                            'mot_artillery_brigade': {'stats': {'soft_attack': 0.05},
                                                                                                      'terrain_modifiers': {},
                                                                                                      'battalion_multipliers': []}},
                                                              'army_mods': {},
                                                              'tactics': []}},
                                                 {'key': 'self_propelled_support_elements',
                                                  'name': 'self_propelled_support_elements',
                                                  'effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                                  'terrain_modifiers': {},
                                                                                                                  'battalion_multipliers': []},
                                                                            'category_self_propelled_anti_air': {'stats': {'air_attack': 0.15,
                                                                                                                           'soft_attack': 0.05},
                                                                                                                 'terrain_modifiers': {},
                                                                                                                 'battalion_multipliers': []},
                                                                            'category_tank_destroyers': {'stats': {'hard_attack': 0.1,
                                                                                                                   'ap_attack': 0.03},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []}},
                                                              'army_mods': {},
                                                              'tactics': []}},
                                                 {'key': 'deep_reconnaissance_focus',
                                                  'name': '$mobile_recon_and_assault_deep_reconnaissance_focus$',
                                                  'effects': {'unit_mods': {'category_recon': {'stats': {'maximum_speed': 0.1},
                                                                                               'terrain_modifiers': {},
                                                                                               'battalion_multipliers': []},
                                                                            'light_tank_recon': {'stats': {'recon': 0.2,
                                                                                                           'breakthrough': 0.1},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': []},
                                                                            'category_tank_destroyer_regimental_support': {'stats': {'hard_attack': 0.05},
                                                                                                                           'terrain_modifiers': {},
                                                                                                                           'battalion_multipliers': []},
                                                                            'category_self_propelled_anti_air_regimental_support': {'stats': {'air_attack': 0.05},
                                                                                                                                    'terrain_modifiers': {},
                                                                                                                                    'battalion_multipliers': []}},
                                                              'army_mods': {},
                                                              'tactics': []}}]},
 'self_propelled_support': {'key': 'self_propelled_support',
                            'track': 'combat_support',
                            'name': 'Self-propelled Support',
                            'description': 'Securing tracked mobility and protection for as much '
                                           "the army's heavy support weapons as possible: the way "
                                           'of the future.',
                            'base_effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'soft_attack': 0.05},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': []},
                                                           'category_self_propelled_anti_air': {'stats': {'air_attack': 0.05},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []},
                                                           'category_tank_destroyers': {'stats': {'hard_attack': 0.05},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                             'army_mods': {},
                                             'tactics': []},
                            'rewards': [{'key': 'mobile_battery_management_platoons',
                                         'name': 'Mobile Fire Direction Center',
                                         'effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'max_organisation': 10.0},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []},
                                                                   'category_self_propelled_anti_air': {'stats': {'max_organisation': 10.0},
                                                                                                        'terrain_modifiers': {},
                                                                                                        'battalion_multipliers': []},
                                                                   'category_tank_destroyers': {'stats': {'max_organisation': 10.0},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'screening_attacks',
                                         'name': 'Time-On-Target Fire Missions',
                                         'effects': {'unit_mods': {'recon': {'stats': {},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': False,
                                                                                                        'category': 'category_self_propelled_artillery',
                                                                                                        'soft_attack': 0.05,
                                                                                                        'default_morale': 0.1}]},
                                                                   'mot_recon': {'stats': {},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': [{'additive': False,
                                                                                                            'category': 'category_self_propelled_artillery',
                                                                                                            'soft_attack': 0.05,
                                                                                                            'default_morale': 0.1}]},
                                                                   'light_tank_recon': {'stats': {},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': [{'additive': False,
                                                                                                                   'category': 'category_self_propelled_artillery',
                                                                                                                   'soft_attack': 0.05,
                                                                                                                   'default_morale': 0.1}]}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'all_terrain_mobility',
                                         'name': 'All-terrain Mobility',
                                         'effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'maximum_speed': 0.1},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []},
                                                                   'category_self_propelled_anti_air': {'stats': {'maximum_speed': 0.1},
                                                                                                        'terrain_modifiers': {},
                                                                                                        'battalion_multipliers': []},
                                                                   'category_tank_destroyers': {'stats': {'maximum_speed': 0.1},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'multirole_support_vehicles',
                                         'name': 'Multi-role Support Vehicles',
                                         'effects': {'unit_mods': {'category_tank_destroyer_regimental_support': {'stats': {'max_organisation': 5.0,
                                                                                                                            'hard_attack': 0.05},
                                                                                                                  'terrain_modifiers': {},
                                                                                                                  'battalion_multipliers': []},
                                                                   'category_self_propelled_anti_air_regimental_support': {'stats': {'max_organisation': 5.0,
                                                                                                                                     'air_attack': 0.05},
                                                                                                                           'terrain_modifiers': {},
                                                                                                                           'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}},
                                        {'key': 'shoot_and_scoot',
                                         'name': 'Shoot & Scoot',
                                         'effects': {'unit_mods': {'category_self_propelled_artillery': {'stats': {'max_organisation': 5.0,
                                                                                                                   'default_morale': 0.15,
                                                                                                                   'soft_attack': 0.05},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []},
                                                                   'category_self_propelled_anti_air': {'stats': {'max_organisation': 5.0,
                                                                                                                  'default_morale': 0.15,
                                                                                                                  'air_attack': 0.05},
                                                                                                        'terrain_modifiers': {},
                                                                                                        'battalion_multipliers': []},
                                                                   'category_tank_destroyers': {'stats': {'max_organisation': 5.0,
                                                                                                          'default_morale': 0.15,
                                                                                                          'hard_attack': 0.05},
                                                                                                'terrain_modifiers': {},
                                                                                                'battalion_multipliers': []}},
                                                     'army_mods': {},
                                                     'tactics': []}}]},
 'siege_artillery': {'key': 'siege_artillery',
                     'track': 'combat_support',
                     'name': 'Siege Artillery',
                     'description': 'No fixed fortification can stand for long against a steel '
                                    'rain of battleship-caliber shells.',
                     'base_effects': {'unit_mods': {'super_heavy_artillery': {'stats': {},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': [{'additive': False,
                                                                                                         'category': 'category_army',
                                                                                                         'soft_attack': 0.1,
                                                                                                         'defense': 0.1}]}},
                                      'army_mods': {},
                                      'tactics': []},
                     'rewards': [{'key': 'fortress_busters',
                                  'name': 'Fortress Busters',
                                  'effects': {'unit_mods': {'super_heavy_artillery': {'stats': {},
                                                                                      'terrain_modifiers': {'Fort': {'attack': 0.25}},
                                                                                      'battalion_multipliers': []},
                                                            'self_propelled_super_heavy_artillery': {'stats': {},
                                                                                                     'terrain_modifiers': {'Fort': {'attack': 0.25}},
                                                                                                     'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'improved_transport_preparation',
                                  'name': 'Improved Transport Preparation',
                                  'effects': {'unit_mods': {'category_line_artillery': {'stats': {'default_morale': 0.1},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []},
                                                            'super_heavy_artillery': {'stats': {'default_morale': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                            'self_propelled_super_heavy_artillery': {'stats': {'default_morale': 0.1},
                                                                                                     'terrain_modifiers': {},
                                                                                                     'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'precomputed_firing_data',
                                  'name': 'Pre-computed Firing Data',
                                  'effects': {'unit_mods': {'super_heavy_artillery': {'stats': {'max_organisation': 10.0,
                                                                                                'defense': 0.2},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                            'self_propelled_super_heavy_artillery': {'stats': {'max_organisation': 10.0,
                                                                                                               'defense': 0.2},
                                                                                                     'terrain_modifiers': {},
                                                                                                     'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'urban_strongpoint_sieges',
                                  'name': 'Advanced Fire Correction',
                                  'effects': {'unit_mods': {'category_artillery': {'stats': {'soft_attack': 0.05},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                            'super_heavy_artillery': {'stats': {},
                                                                                      'terrain_modifiers': {'Urban': {'attack': 0.1,
                                                                                                                      'defense': 0.1}},
                                                                                      'battalion_multipliers': []},
                                                            'self_propelled_super_heavy_artillery': {'stats': {},
                                                                                                     'terrain_modifiers': {'Urban': {'attack': 0.1,
                                                                                                                                     'defense': 0.1}},
                                                                                                     'battalion_multipliers': []},
                                                            'fire_support': {'stats': {'soft_attack': 0.1},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []},
                                                            'category_regimental_support_artillery': {'stats': {'soft_attack': 0.05},
                                                                                                      'terrain_modifiers': {},
                                                                                                      'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}},
                                 {'key': 'mobile_artillery_command',
                                  'name': 'Mobile Artillery Command',
                                  'effects': {'unit_mods': {'category_support_artillery': {'stats': {'max_organisation': 10.0},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []},
                                                            'self_propelled_super_heavy_artillery': {'stats': {'max_organisation': 10.0,
                                                                                                               'maximum_speed': 0.5},
                                                                                                     'terrain_modifiers': {},
                                                                                                     'battalion_multipliers': []}},
                                              'army_mods': {},
                                              'tactics': []}}]},
 'field_engineering': {'key': 'field_engineering',
                       'track': 'combat_support',
                       'name': 'Field Engineering',
                       'description': 'The role of military engineers is to build bridges and lay '
                                      'mines, as well as destroy similar works of the enemy. With '
                                      'the right equipment, training, and a willingness to spill '
                                      'sweat to spare blood, we can dominate the modern '
                                      'battlefield.',
                       'base_effects': {'unit_mods': {'engineer': {'stats': {},
                                                                   'terrain_modifiers': {'River': {'movement': 0.2},
                                                                                         'Forest': {'movement': 0.2}},
                                                                   'battalion_multipliers': []},
                                                      'assault_engineer': {'stats': {},
                                                                           'terrain_modifiers': {'River': {'movement': 0.2},
                                                                                                 'Forest': {'movement': 0.2}},
                                                                           'battalion_multipliers': []},
                                                      'pioneer_support': {'stats': {},
                                                                          'terrain_modifiers': {'River': {'movement': 0.2},
                                                                                                'Forest': {'movement': 0.2}},
                                                                          'battalion_multipliers': []}},
                                        'army_mods': {},
                                        'tactics': []},
                       'rewards': [{'key': 'rapid_fire_lane_clearance',
                                    'name': 'Rapid Fire Lane Clearance',
                                    'effects': {'unit_mods': {'engineer': {'stats': {'max_organisation': 5.0},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': True,
                                                                                                      'category': 'category_all_infantry',
                                                                                                      'entrenchment': 0.1}]},
                                                              'maintenance_company': {'stats': {'max_organisation': 5.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'sapper_fieldcraft',
                                    'name': 'Sapper Fieldcraft',
                                    'effects': {'unit_mods': {'engineer': {'stats': {'max_strength': 0.25,
                                                                                     'defense': 0.1},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                              'maintenance_company': {'stats': {'max_strength': 0.25},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'engineerdug_gun_emplacements',
                                    'name': 'Engineer-dug Gun Emplacements',
                                    'effects': {'unit_mods': {'engineer': {'stats': {},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_artillery',
                                                                                                      'soft_attack': 0.1,
                                                                                                      'defense': 0.1},
                                                                                                     {'additive': False,
                                                                                                      'category': 'category_all_infantry',
                                                                                                      'soft_attack': 0.05}]},
                                                              'field_guns': {'stats': {'soft_attack': 0.1,
                                                                                       'defense': 0.1},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'smoke_projector_training',
                                    'name': 'Smoke Projector Training',
                                    'effects': {'unit_mods': {'engineer': {'stats': {'breakthrough': 0.5},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                              'maintenance_company': {'stats': {'supply_consumption': -0.01},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                                 'category': 'category_tanks',
                                                                                                                 'reliability': 0.05,
                                                                                                                 'strength': 0.05}]}},
                                                'army_mods': {},
                                                'tactics': []}},
                                   {'key': 'charge_and_flame',
                                    'name': 'Flames & Satchel Charges',
                                    'effects': {'unit_mods': {'engineer': {'stats': {'max_organisation': 5.0,
                                                                                     'soft_attack': 0.05,
                                                                                     'hard_attack': 1.0},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                              'maintenance_company': {'stats': {'max_organisation': 5.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                              'fire_support': {'stats': {'max_organisation': 5.0,
                                                                                         'breakthrough': 0.1},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []}},
                                                'army_mods': {},
                                                'tactics': []}}]},
 'mission_type_tactics': {'key': 'mission_type_tactics',
                          'track': 'operations',
                          'name': 'Mission-Type Tactics',
                          'description': 'Our leaders should not be automatons. They must '
                                         'interpret their orders intelligently, and diverge from '
                                         'strict adherence to them if it accomplishes the mission. '
                                         'Victory is more important than blind obedience.',
                          'base_effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 15.0},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []}},
                                           'army_mods': {'command_power_gain': 0.2},
                                           'tactics': []},
                          'rewards': [{'key': 'low_level_delegation',
                                       'name': 'Low-level Delegation',
                                       'effects': {'unit_mods': {'category_all_infantry': {'stats': {'default_morale': 0.1},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []},
                                                                 'category_regimental_support_artillery': {'stats': {'max_organisation': 5.0,
                                                                                                                     'soft_attack': 0.05},
                                                                                                           'terrain_modifiers': {},
                                                                                                           'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'flexible_command',
                                       'name': 'Flexible Command',
                                       'effects': {'unit_mods': {},
                                                   'army_mods': {'org_loss_when_moving': -0.15},
                                                   'tactics': []}},
                                      {'key': 'maneouver_drills',
                                       'name': 'Combined Arms Battle Groups',
                                       'effects': {'unit_mods': {'category_all_armor': {'stats': {'maximum_speed': 0.1},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                   'army_mods': {'land_reinforce_rate': 0.02},
                                                   'tactics': []}},
                                      {'key': 'flexible_combat_formations',
                                       'name': 'Offensive Posture',
                                       'effects': {'unit_mods': {'category_all_infantry': {'stats': {'breakthrough': 0.1,
                                                                                                     'max_organisation': 10.0},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'control_zone_responsibilities',
                                       'name': 'Control Zone Responsibilities',
                                       'effects': {'unit_mods': {'category_all_infantry': {'stats': {'default_morale': 0.2},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []},
                                                                 'category_tanks': {'stats': {'default_morale': 0.1},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}}]},
 'last_stand': {'key': 'last_stand',
                'track': 'operations',
                'name': 'Desperate Defense',
                'description': 'When our backs are to the wall, and national survival is at stake, '
                               'the only option is bitter, fanatical resistance by the entire '
                               'population, turning every field, street and town into a '
                               'battleground.',
                'base_effects': {'unit_mods': {},
                                 'army_mods': {'conscription': 0.05},
                                 'tactics': []},
                'rewards': [{'key': 'werwolf_groups',
                             'name': 'Sabotage Groups',
                             'effects': {'unit_mods': {},
                                         'army_mods': {'resistance_damage_to_garrison_on_our_occupied_states': 0.25},
                                         'tactics': []}},
                            {'key': 'pocket_consolidation',
                             'name': 'Pocket Consolidation',
                             'effects': {'unit_mods': {'category_all_infantry': {'stats': {'defense': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []}},
                            {'key': 'digging_in',
                             'name': 'Trench-Huddling',
                             'effects': {'unit_mods': {'category_all_infantry': {'stats': {'entrenchment': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                         'army_mods': {'out_of_supply_factor': -0.2},
                                         'tactics': []}},
                            {'key': 'stocking_up',
                             'name': 'Supply Cache Retrieval',
                             'effects': {'unit_mods': {},
                                         'army_mods': {'no_supply_grace': 72.0},
                                         'tactics': []}},
                            {'key': 'breaking_out',
                             'name': 'Final Offensive',
                             'effects': {'unit_mods': {'category_army': {'stats': {'soft_attack': 0.15},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': []},
                                                       'category_regimental_support_artillery': {'stats': {'max_organisation': 5.0,
                                                                                                           'soft_attack': 0.1},
                                                                                                 'terrain_modifiers': {},
                                                                                                 'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': []}}]},
 'infiltration_tactics': {'key': 'infiltration_tactics',
                          'track': 'operations',
                          'name': 'Infiltration Tactics',
                          'description': 'Rather than bashing against enemy lines at their '
                                         'strongest point, we shall flow around them like water, '
                                         'maintaining offensive momentum and forcing the enemy to '
                                         'withdraw through threat of encirclement.',
                          'base_effects': {'unit_mods': {},
                                           'army_mods': {'max_planning': 0.1},
                                           'tactics': ['tactic_infantry_charge']},
                          'rewards': [{'key': 'infiltration_assault',
                                       'name': 'Infiltration Assault',
                                       'effects': {'unit_mods': {'category_army': {'stats': {'breakthrough': 0.1,
                                                                                             'max_organisation': 5.0},
                                                                                   'terrain_modifiers': {},
                                                                                   'battalion_multipliers': []},
                                                                 'fire_support': {'stats': {'soft_attack': 0.1},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'nightly_assaults',
                                       'name': 'Attacks At Night',
                                       'effects': {'unit_mods': {},
                                                   'army_mods': {'land_night_attack': 0.25},
                                                   'tactics': []}},
                                      {'key': 'self_sustaining_infiltration_units',
                                       'name': 'Self-sustaining Infiltration Units',
                                       'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 2.0},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []},
                                                                 'category_all_armor': {'stats': {'default_morale': 0.1},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                   'army_mods': {'supply_consumption_factor': -0.1,
                                                                 'command_power_gain': 0.1},
                                                   'tactics': []}},
                                      {'key': 'terrain_and_situation_assessment',
                                       'name': 'Terrain and Situation Assessment',
                                       'effects': {'unit_mods': {'recon': {'stats': {},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': [{'additive': False,
                                                                                                      'category': 'category_light_infantry',
                                                                                                      'soft_attack': 0.1},
                                                                                                     {'additive': False,
                                                                                                      'category': 'category_cavalry',
                                                                                                      'soft_attack': 0.1}]},
                                                                 'mot_recon': {'stats': {},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': [{'additive': False,
                                                                                                          'category': 'category_light_infantry',
                                                                                                          'soft_attack': 0.1},
                                                                                                         {'additive': False,
                                                                                                          'category': 'category_cavalry',
                                                                                                          'soft_attack': 0.1}]},
                                                                 'light_tank_recon': {'stats': {},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                                 'category': 'category_light_infantry',
                                                                                                                 'soft_attack': 0.1},
                                                                                                                {'additive': False,
                                                                                                                 'category': 'category_cavalry',
                                                                                                                 'soft_attack': 0.1}]},
                                                                 'category_recon': {'stats': {'recon': 1.0},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'infiltration_in_depth',
                                       'name': 'Infiltration in Depth',
                                       'effects': {'unit_mods': {},
                                                   'army_mods': {'land_reinforce_rate': 0.02,
                                                                 'org_loss_when_moving': -0.2},
                                                   'tactics': []}}]},
 'grand_assault': {'key': 'grand_assault',
                   'track': 'operations',
                   'name': 'Grand Assault',
                   'description': 'Building upon hard-earned lessons from the First World War, we '
                                  'shall adopt a deliberate and methodical approach to pre-battle '
                                  'planning. Then, when every advantage has been leveraged, we '
                                  'fall upon the enemy like an avalanche.',
                   'base_effects': {'unit_mods': {'category_army': {'stats': {'breakthrough': 0.1,
                                                                              'soft_attack': 0.05},
                                                                    'terrain_modifiers': {},
                                                                    'battalion_multipliers': []}},
                                    'army_mods': {'max_planning': 0.1},
                                    'tactics': []},
                   'rewards': [{'key': 'central_planning',
                                'name': 'Central Planning',
                                'effects': {'unit_mods': {'logistics_company': {'stats': {},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': [{'additive': False,
                                                                                                           'category': 'category_all_infantry',
                                                                                                           'defense': 0.05}]}},
                                            'army_mods': {'max_command_power': 30.0},
                                            'tactics': []}},
                               {'key': 'multiple_attack_directions',
                                'name': 'Diversionary Attacks',
                                'effects': {'unit_mods': {'category_army': {'stats': {'breakthrough': 0.15},
                                                                            'terrain_modifiers': {},
                                                                            'battalion_multipliers': []},
                                                          'fire_support': {'stats': {'soft_attack': 0.1},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []}},
                                            'army_mods': {},
                                            'tactics': []}},
                               {'key': 'combined_arms_integration',
                                'name': 'Combined Arms Integration',
                                'effects': {'unit_mods': {'category_tank_destroyer_regimental_support': {'stats': {'max_organisation': 5.0},
                                                                                                         'terrain_modifiers': {},
                                                                                                         'battalion_multipliers': []},
                                                          'anti_air_battery': {'stats': {'max_organisation': 5.0,
                                                                                         'air_attack': 0.1},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []},
                                                          'mot_fire_support': {'stats': {'max_organisation': 5.0,
                                                                                         'soft_attack': 0.1},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []}},
                                            'army_mods': {'army_bonus_air_superiority_factor': 0.05,
                                                          'coordination_bonus': 0.1},
                                            'tactics': []}},
                               {'key': 'forward_command_posts',
                                'name': 'Forward Command Posts',
                                'effects': {'unit_mods': {'logistics_company': {'stats': {},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': [{'additive': True,
                                                                                                           'category': 'category_all_infantry',
                                                                                                           'supply_consumption': -0.01}]},
                                                          'category_recon': {'stats': {'recon': 0.1},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []}},
                                            'army_mods': {},
                                            'tactics': []}},
                               {'key': 'c3i_theory',
                                'name': 'C3I',
                                'effects': {'unit_mods': {'category_all_infantry': {'stats': {'max_organisation': 8.0},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                            'army_mods': {'max_planning': 0.1},
                                            'tactics': []}}]},
 'deep_battle': {'key': 'deep_battle',
                 'track': 'operations',
                 'name': 'Deep Battle',
                 'description': 'The range and striking power of modern arms allows an enemy '
                                'defense system to be overcome by striking it to its whole depth, '
                                'simultaneously, with every weapon at our disposal.',
                 'base_effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 4.0},
                                                                   'terrain_modifiers': {},
                                                                   'battalion_multipliers': []}},
                                  'army_mods': {},
                                  'tactics': ['tactic_backhand_blow']},
                 'rewards': [{'key': 'bounding_overwatch',
                              'name': 'Bounding Overwatch',
                              'effects': {'unit_mods': {'recon': {'stats': {},
                                                                  'terrain_modifiers': {},
                                                                  'battalion_multipliers': [{'additive': False,
                                                                                             'category': 'category_light_infantry',
                                                                                             'soft_attack': 0.05,
                                                                                             'defense': 0.05}]},
                                                        'mot_recon': {'stats': {},
                                                                      'terrain_modifiers': {},
                                                                      'battalion_multipliers': [{'additive': False,
                                                                                                 'category': 'category_light_infantry',
                                                                                                 'soft_attack': 0.05,
                                                                                                 'defense': 0.05}]},
                                                        'armored_car_recon': {'stats': {},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': [{'additive': False,
                                                                                                         'category': 'category_light_infantry',
                                                                                                         'soft_attack': 0.05,
                                                                                                         'defense': 0.05}]},
                                                        'light_tank_recon': {'stats': {},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': False,
                                                                                                        'category': 'category_light_infantry',
                                                                                                        'soft_attack': 0.05,
                                                                                                        'defense': 0.05}]},
                                                        'category_vehicle_infantry': {'stats': {'max_organisation': 2.0},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []}},
                                          'army_mods': {},
                                          'tactics': []}},
                             {'key': 'operational_concentration',
                              'name': 'Operational Reserves',
                              'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 4.0},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                        'armored_car': {'stats': {'max_organisation': 4.0},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []}},
                                          'army_mods': {'land_reinforce_rate': 0.05},
                                          'tactics': []}},
                             {'key': 'maskirovka',
                              'name': 'Strategic Deception',
                              'effects': {'unit_mods': {},
                                          'army_mods': {'army_intel_to_others': -10.0,
                                                        'airforce_intel_to_others': -5.0,
                                                        'army_intel_factor': 0.05},
                                          'tactics': []}},
                             {'key': 'breakthrough_priority',
                              'name': 'Breakthrough Priority',
                              'effects': {'unit_mods': {'category_vehicle_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                'default_morale': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                        'category_tanks': {'stats': {'max_organisation': 2.0},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []},
                                                        'category_all_armor': {'stats': {'default_morale': 0.1},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []},
                                                        'armored_car': {'stats': {'max_organisation': 4.0},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []},
                                                        'mot_fire_support': {'stats': {'max_organisation': 5.0,
                                                                                       'soft_attack': 0.1},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': []}},
                                          'army_mods': {'org_loss_when_moving': -0.2},
                                          'tactics': []}},
                             {'key': 'operational_depth_control',
                              'name': 'Operational Offensive Momentum',
                              'effects': {'unit_mods': {'armored_car_recon': {'stats': {},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': [{'additive': True,
                                                                                                         'category': 'category_light_infantry',
                                                                                                         'max_organisation': 10.0}]},
                                                        'light_tank_recon': {'stats': {},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': True,
                                                                                                        'category': 'category_light_infantry',
                                                                                                        'max_organisation': 10.0}]},
                                                        'category_regimental_support_artillery': {'stats': {'max_organisation': 5.0,
                                                                                                            'soft_attack': 0.1},
                                                                                                  'terrain_modifiers': {},
                                                                                                  'battalion_multipliers': []}},
                                          'army_mods': {'org_loss_when_moving': -0.1,
                                                        'land_reinforce_rate': 0.05},
                                          'tactics': []}}]},
 'deep_battle_no_lar': {'key': 'deep_battle_no_lar',
                        'track': 'operations',
                        'name': 'Deep Battle',
                        'description': 'The range and striking power of modern arms allows an '
                                       'enemy defense system to be overcome by striking it to its '
                                       'whole depth, simultaneously, with every weapon at our '
                                       'disposal.',
                        'base_effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 4.0},
                                                                          'terrain_modifiers': {},
                                                                          'battalion_multipliers': []}},
                                         'army_mods': {},
                                         'tactics': ['tactic_backhand_blow']},
                        'rewards': [{'key': 'bounding_overwatch',
                                     'name': '$deep_battle_bounding_overwatch$',
                                     'effects': {'unit_mods': {'recon': {'stats': {},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': [{'additive': False,
                                                                                                    'category': 'category_light_infantry',
                                                                                                    'soft_attack': 0.05,
                                                                                                    'defense': 0.05}]},
                                                               'mot_recon': {'stats': {},
                                                                             'terrain_modifiers': {},
                                                                             'battalion_multipliers': [{'additive': False,
                                                                                                        'category': 'category_light_infantry',
                                                                                                        'soft_attack': 0.05,
                                                                                                        'defense': 0.05}]},
                                                               'light_tank_recon': {'stats': {},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': [{'additive': False,
                                                                                                               'category': 'category_light_infantry',
                                                                                                               'soft_attack': 0.05,
                                                                                                               'defense': 0.05}]},
                                                               'category_vehicle_infantry': {'stats': {'max_organisation': 2.0},
                                                                                             'terrain_modifiers': {},
                                                                                             'battalion_multipliers': []}},
                                                 'army_mods': {},
                                                 'tactics': []}},
                                    {'key': 'operational_concentration',
                                     'name': '$deep_battle_operational_concentration$',
                                     'effects': {'unit_mods': {'category_tanks': {'stats': {'max_organisation': 4.0},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                               'mechanized': {'stats': {'max_organisation': 10.0},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []}},
                                                 'army_mods': {'land_reinforce_rate': 0.05},
                                                 'tactics': []}},
                                    {'key': 'maskirovka',
                                     'name': '$deep_battle_maskirovka$',
                                     'effects': {'unit_mods': {},
                                                 'army_mods': {'army_intel_to_others': -10.0,
                                                               'airforce_intel_to_others': -5.0,
                                                               'army_intel_factor': 0.05},
                                                 'tactics': []}},
                                    {'key': 'breakthrough_priority',
                                     'name': '$deep_battle_breakthrough_priority$',
                                     'effects': {'unit_mods': {'category_vehicle_infantry': {'stats': {'max_organisation': 10.0,
                                                                                                       'default_morale': 0.1},
                                                                                             'terrain_modifiers': {},
                                                                                             'battalion_multipliers': []},
                                                               'category_tanks': {'stats': {'max_organisation': 2.0},
                                                                                  'terrain_modifiers': {},
                                                                                  'battalion_multipliers': []},
                                                               'category_all_armor': {'stats': {'default_morale': 0.1},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                               'mechanized': {'stats': {'breakthrough': 0.1},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []}},
                                                 'army_mods': {'org_loss_when_moving': -0.2},
                                                 'tactics': []}},
                                    {'key': 'operational_depth_control',
                                     'name': '$deep_battle_operational_depth_control$',
                                     'effects': {'unit_mods': {'recon': {'stats': {},
                                                                         'terrain_modifiers': {},
                                                                         'battalion_multipliers': [{'additive': True,
                                                                                                    'category': 'category_light_infantry',
                                                                                                    'max_organisation': 10.0}]},
                                                               'light_tank_recon': {'stats': {},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': [{'additive': True,
                                                                                                               'category': 'category_light_infantry',
                                                                                                               'max_organisation': 10.0}]}},
                                                 'army_mods': {'org_loss_when_moving': -0.1,
                                                               'land_reinforce_rate': 0.05},
                                                 'tactics': []}}]},
 'guerilla_war': {'key': 'guerilla_war',
                  'track': 'operations',
                  'name': 'Guerilla War',
                  'description': 'Wear down a superior enemy through constant low-level attacks on '
                                 'his lines of communication, eroding his will to continue the '
                                 'fight. Avoid major set-piece battles to preserve our own limited '
                                 'forces.',
                  'base_effects': {'unit_mods': {'irregular_infantry': {'stats': {'soft_attack': 0.1,
                                                                                  'defense': 0.2},
                                                                        'terrain_modifiers': {},
                                                                        'battalion_multipliers': []},
                                                 'militia': {'stats': {'soft_attack': 0.1,
                                                                       'defense': 0.2},
                                                             'terrain_modifiers': {},
                                                             'battalion_multipliers': []}},
                                   'army_mods': {},
                                   'tactics': ['tactic_guerrilla_tactics']},
                  'rewards': [{'key': 'catch_and_seize',
                               'name': 'The Enemy Will Supply Us',
                               'effects': {'unit_mods': {'category_cavalry': {'stats': {'equipment_capture_factor': 0.01},
                                                                              'terrain_modifiers': {'Plains': {'movement': 0.1}},
                                                                              'battalion_multipliers': []},
                                                         'category_light_infantry': {'stats': {'equipment_capture_factor': 0.01},
                                                                                     'terrain_modifiers': {'Plains': {'movement': 0.1}},
                                                                                     'battalion_multipliers': []}},
                                           'army_mods': {'pocket_penalty': -0.1},
                                           'tactics': []}},
                              {'key': 'galvanize_support',
                               'name': 'Galvanize Support',
                               'effects': {'unit_mods': {},
                                           'army_mods': {'army_intel_to_others': -10.0,
                                                         'army_intel_factor': 0.05,
                                                         'war_support_factor': 0.1,
                                                         'political_power_factor': 0.1,
                                                         'mobilization_speed': 0.15},
                                           'tactics': []}},
                              {'key': 'scorched_earth',
                               'name': 'Scorched Earth',
                               'effects': {'unit_mods': {'category_army': {'stats': {'defense': 0.1},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []}},
                                           'army_mods': {'resistance_damage_to_garrison_on_our_occupied_states': 0.1,
                                                         'resistance_target_on_our_occupied_states': 0.1},
                                           'tactics': []}},
                              {'key': 'urban_assaults',
                               'name': 'Urban Combat Tactics',
                               'effects': {'unit_mods': {'militia': {'stats': {},
                                                                     'terrain_modifiers': {'Urban': {'attack': 0.1,
                                                                                                     'defense': 0.1}},
                                                                     'battalion_multipliers': []},
                                                         'infantry': {'stats': {},
                                                                      'terrain_modifiers': {'Urban': {'attack': 0.1,
                                                                                                      'defense': 0.1}},
                                                                      'battalion_multipliers': []}},
                                           'army_mods': {},
                                           'tactics': []}},
                              {'key': 'defense_of_gained_power',
                               'name': 'Defense of Gained Power',
                               'effects': {'unit_mods': {'category_army': {'stats': {'defense': 0.1},
                                                                           'terrain_modifiers': {},
                                                                           'battalion_multipliers': []}},
                                           'army_mods': {'stability_factor': 0.1,
                                                         'party_popularity_stability_factor': 0.05},
                                           'tactics': []}}]},
 'rapid_domination': {'key': 'rapid_domination',
                      'track': 'operations',
                      'name': 'Rapid Domination',
                      'description': 'Asserting full-spectrum dominance over the enemy makes their '
                                     'further resistance physically and psychologically '
                                     'impossible.',
                      'base_effects': {'unit_mods': {'category_all_infantry': {'stats': {'soft_attack': 0.1},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []},
                                                     'category_line_artillery': {'stats': {'soft_attack': 0.1},
                                                                                 'terrain_modifiers': {},
                                                                                 'battalion_multipliers': []}},
                                       'army_mods': {'land_reinforce_rate': 0.02},
                                       'tactics': ['tactic_breakthrough']},
                      'rewards': [{'key': 'forward_observers',
                                   'name': 'Scouts Out',
                                   'effects': {'unit_mods': {'category_recon': {'stats': {'recon': 1.0},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': []},
                                                             'category_support_artillery': {'stats': {'soft_attack': 0.05},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': []},
                                                             'category_regimental_support_artillery': {'stats': {'breakthrough': 0.1},
                                                                                                       'terrain_modifiers': {},
                                                                                                       'battalion_multipliers': []}},
                                               'army_mods': {'land_reinforce_rate': 0.02},
                                               'tactics': []}},
                                  {'key': 'advanced_firebases',
                                   'name': 'Advanced Firebases',
                                   'effects': {'unit_mods': {'category_support_artillery': {'stats': {'supply_consumption': -0.1},
                                                                                            'terrain_modifiers': {},
                                                                                            'battalion_multipliers': [{'additive': True,
                                                                                                                       'category': 'category_army',
                                                                                                                       'default_morale': 0.1}]},
                                                             'category_regimental_support_artillery': {'stats': {'soft_attack': 0.1},
                                                                                                       'terrain_modifiers': {},
                                                                                                       'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'centralized_fire_control',
                                   'name': 'Dynamic Fire Control',
                                   'effects': {'unit_mods': {'signal_company': {'stats': {},
                                                                                'terrain_modifiers': {},
                                                                                'battalion_multipliers': [{'additive': False,
                                                                                                           'category': 'category_artillery',
                                                                                                           'soft_attack': 0.1}]}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'regimental_combat_teams',
                                   'name': 'Regimental Combat Teams',
                                   'effects': {'unit_mods': {'category_support_battalions': {'stats': {'max_organisation': 10.0,
                                                                                                       'soft_attack': 0.1},
                                                                                             'terrain_modifiers': {},
                                                                                             'battalion_multipliers': []}},
                                               'army_mods': {},
                                               'tactics': []}},
                                  {'key': 'shock_and_awe',
                                   'name': 'Shock & Awe',
                                   'effects': {'unit_mods': {'category_army': {'stats': {'soft_attack': 0.05},
                                                                               'terrain_modifiers': {},
                                                                               'battalion_multipliers': []},
                                                             'category_all_infantry': {'stats': {'soft_attack': 0.1,
                                                                                                 'hard_attack': 0.1},
                                                                                       'terrain_modifiers': {},
                                                                                       'battalion_multipliers': []}},
                                               'army_mods': {'army_bonus_air_superiority_factor': 0.1},
                                               'tactics': []}}]},
 'expeditionary_warfare': {'key': 'expeditionary_warfare',
                           'track': 'operations',
                           'name': 'Expeditionary Warfare',
                           'description': 'All the combat power in the world means little if it '
                                          'cannot get to the fight. We shall create an '
                                          'organizational emphasis on force projection capability '
                                          'in service of our strategic aims.',
                           'base_effects': {'unit_mods': {},
                                            'army_mods': {'send_volunteer_divisions_required': -0.5,
                                                          'send_volunteer_factor': 0.25,
                                                          'send_volunteers_tension': -0.1},
                                            'tactics': []},
                           'rewards': [{'key': 'staging_area_security',
                                        'name': 'Beachhead Security',
                                        'effects': {'unit_mods': {'category_army': {'stats': {'defense': 0.1},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                                    'army_mods': {'dig_in_speed_factor': 0.05,
                                                                  'out_of_supply_factor': -0.2},
                                                    'tactics': []}},
                                       {'key': 'landing_operations',
                                        'name': 'Landing Operations',
                                        'effects': {'unit_mods': {'category_army': {'stats': {'soft_attack': 0.1},
                                                                                    'terrain_modifiers': {},
                                                                                    'battalion_multipliers': []}},
                                                    'army_mods': {'naval_invasion_prep_speed': 0.2,
                                                                  'naval_invasion_penalty': -0.15,
                                                                  'naval_invasion_planning_bonus_speed': 0.2},
                                                    'tactics': []}},
                                       {'key': 'shore_fire_control_parties',
                                        'name': 'Shore Fire Control Parties',
                                        'effects': {'unit_mods': {},
                                                    'army_mods': {'shore_bombardment_bonus': 0.25},
                                                    'tactics': []}},
                                       {'key': 'breakout_emphasis',
                                        'name': 'Resupply Emphasis',
                                        'effects': {'unit_mods': {},
                                                    'army_mods': {'no_supply_grace': 32.0},
                                                    'tactics': []}},
                                       {'key': 'withdrawal_protocols',
                                        'name': 'Orderly Withdrawal Protocols',
                                        'effects': {'unit_mods': {},
                                                    'army_mods': {'org_loss_when_moving': -0.2},
                                                    'tactics': []}}]},
 'dispersed_operations': {'key': 'dispersed_operations',
                          'track': 'operations',
                          'name': 'Dispersed Operations',
                          'description': 'When the skies belong to the enemy, our armies must '
                                         'refuse to present an easy target. Dispersed formations, '
                                         'hardened logistics, and dense anti-aircraft fire let us '
                                         'fight on where we cannot contest the air.',
                          'base_effects': {'unit_mods': {},
                                           'army_mods': {'enemy_army_bonus_air_superiority_factor': -0.1,
                                                         'land_reinforce_rate': 0.05},
                                           'tactics': []},
                          'rewards': [{'key': 'camouflage_discipline',
                                       'name': 'Camouflage Discipline',
                                       'effects': {'unit_mods': {'logistics_company': {'stats': {},
                                                                                       'terrain_modifiers': {},
                                                                                       'battalion_multipliers': [{'additive': True,
                                                                                                                  'category': 'category_all_infantry',
                                                                                                                  'entrenchment': 0.1}]}},
                                                   'army_mods': {'enemy_army_bonus_air_superiority_factor': -0.15},
                                                   'tactics': []}},
                                      {'key': 'hardened_logistics',
                                       'name': 'Hardened Logistics',
                                       'effects': {'unit_mods': {'logistics_company': {'stats': {'max_organisation': 5.0},
                                                                                       'terrain_modifiers': {},
                                                                                       'battalion_multipliers': []}},
                                                   'army_mods': {'no_supply_grace': 24.0},
                                                   'tactics': []}},
                                      {'key': 'local_air_defense',
                                       'name': 'Local Air Defense',
                                       'effects': {'unit_mods': {'anti_air_battery': {'stats': {'air_attack': 0.2},
                                                                                      'terrain_modifiers': {},
                                                                                      'battalion_multipliers': []},
                                                                 'anti_air': {'stats': {'air_attack': 0.2},
                                                                              'terrain_modifiers': {},
                                                                              'battalion_multipliers': []},
                                                                 'category_self_propelled_anti_air_regimental_support': {'stats': {'air_attack': 0.2},
                                                                                                                         'terrain_modifiers': {},
                                                                                                                         'battalion_multipliers': []}},
                                                   'army_mods': {},
                                                   'tactics': []}},
                                      {'key': 'scattered_formations',
                                       'name': 'Scattered Formations',
                                       'effects': {'unit_mods': {},
                                                   'army_mods': {'cas_damage_reduction': 0.05},
                                                   'tactics': []}},
                                      {'key': 'independent_operations',
                                       'name': 'Independent Operations',
                                       'effects': {'unit_mods': {'category_all_infantry': {'stats': {'initiative': 0.01,
                                                                                                     'breakthrough': 0.1,
                                                                                                     'max_organisation': 5.0},
                                                                                           'terrain_modifiers': {},
                                                                                           'battalion_multipliers': []},
                                                                 'category_all_armor': {'stats': {'initiative': 0.01,
                                                                                                  'breakthrough': 0.1,
                                                                                                  'max_organisation': 2.0},
                                                                                        'terrain_modifiers': {},
                                                                                        'battalion_multipliers': []}},
                                                   'army_mods': {'out_of_supply_factor': -0.15},
                                                   'tactics': []}}]}}


# =============================================================================
# 2. Canonical Preset Paths & Aliases
# =============================================================================

#: Canonical HOI4 Land Doctrine preset configurations mapping each preset key
#: to its v1.19 Grand Doctrine + 4 Track Sub-Doctrines (plus optional extra
#: historical path modifiers where applicable).
CANONICAL_DOCTRINE_PRESETS: Dict[str, Dict[str, Any]] = {
    "none": {
        "key": "none",
        "name": "No Doctrine (Baseline)",
        "description": "Unmodified baseline unit statistics with no Land Doctrine bonuses applied.",
        "grand_doctrine": None,
        "subdoctrines": {
            "infantry": None,
            "combat_support": None,
            "armor": None,
            "operations": None,
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mobile_warfare": {
        "key": "mobile_warfare",
        "name": "Mobile Warfare (Blitzkrieg / Mobile Infantry)",
        "description": (
            "Canonical German Blitzkrieg doctrine combining Mobile Warfare with Mobile Infantry, "
            "Mobile Recon & Assault, Armored Spearhead, and Mission-Type Tactics. Grants massive "
            "breakthrough (+55% on tanks, +35% on infantry/motorized/mechanized), organization "
            "(+45 on infantry, +65 on motorized/mechanized, +5..8 on tanks), and recovery rate."
        ),
        "grand_doctrine": "new_mobile_warfare",
        "subdoctrines": {
            "infantry": "mobile_infantry",
            "combat_support": "mobile_recon_and_assault",
            "armor": "armored_spearhead",
            "operations": "mission_type_tactics",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mobile_warfare_blitzkrieg": {
        "key": "mobile_warfare_blitzkrieg",
        "name": "Mobile Warfare: Modern Blitzkrieg",
        "description": (
            "Mobile Warfare focused on Armored Spearhead, Mobile Infantry, Mobile Recon & Assault, "
            "and Mission-Type Tactics for maximum tank and mechanized breakthrough, organization, "
            "and recovery rate."
        ),
        "grand_doctrine": "new_mobile_warfare",
        "subdoctrines": {
            "infantry": "mobile_infantry",
            "combat_support": "mobile_recon_and_assault",
            "armor": "armored_spearhead",
            "operations": "mission_type_tactics",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mobile_warfare_desperate_defense": {
        "key": "mobile_warfare_desperate_defense",
        "name": "Mobile Warfare: Mechanized Wave / Desperate Defense",
        "description": (
            "Mobile Warfare combining Mobile Infantry, Self-propelled Support, Streamlined "
            "Deployment (Mechanized Wave), and Desperate Defense (Last Stand). Grants +5% "
            "recruitable population, +15% army-wide soft attack, +10% infantry defense & "
            "entrenchment, and strong mechanized/self-propelled armor sustain."
        ),
        "grand_doctrine": "new_mobile_warfare",
        "subdoctrines": {
            "infantry": "mobile_infantry",
            "combat_support": "self_propelled_support",
            "armor": "streamlined_deployment",
            "operations": "last_stand",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "superior_firepower": {
        "key": "superior_firepower",
        "name": "Superior Firepower (Integrated Support / Shock & Awe)",
        "description": (
            "Canonical US Superior Firepower doctrine combining Assault Infantry (Integrated "
            "Support Batteries & Low Echelon Fire Support), Mobile Recon & Assault, Mobile Defense, "
            "and Rapid Domination (Regimental Combat Teams & Shock & Awe). Massively buffs "
            "divisional and regimental support companies (+20..40 ORG, +15..35% soft attack, "
            "+20% light infantry soft attack multiplier from Support Artillery) and frontline firepower."
        ),
        "grand_doctrine": "superior_firepower",
        "subdoctrines": {
            "infantry": "assault_infantry",
            "combat_support": "mobile_recon_and_assault",
            "armor": "mobile_defense",
            "operations": "rapid_domination",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "superior_firepower_integrated_support": {
        "key": "superior_firepower_integrated_support",
        "name": "Superior Firepower: Integrated Support + Shock & Awe",
        "description": (
            "Superior Firepower with Assault Infantry (Integrated Support), Mobile Recon & Assault, "
            "Mobile Defense, and Rapid Domination (Regimental Combat Teams / Shock & Awe). Maximizes "
            "support company organization (+20..40 ORG) and soft attack alongside frontline attack."
        ),
        "grand_doctrine": "superior_firepower",
        "subdoctrines": {
            "infantry": "assault_infantry",
            "combat_support": "mobile_recon_and_assault",
            "armor": "mobile_defense",
            "operations": "rapid_domination",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "superior_firepower_dispersed_support": {
        "key": "superior_firepower_dispersed_support",
        "name": "Superior Firepower: Dispersed Support (Fire Concentration + Shock & Awe)",
        "description": (
            "Superior Firepower with Assault Infantry, Fire Concentration (Prepared Gun Pits "
            "reducing Line Artillery & Rocket Artillery combat width by -0.8, +20% breakthrough, "
            "+10 ORG, +10% artillery soft attack & defense), Mobile Defense, and Rapid Domination."
        ),
        "grand_doctrine": "superior_firepower",
        "subdoctrines": {
            "infantry": "assault_infantry",
            "combat_support": "fire_concentration",
            "armor": "mobile_defense",
            "operations": "rapid_domination",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "grand_battleplan": {
        "key": "grand_battleplan",
        "name": "Grand Battleplan (Assault / Defensive Postures)",
        "description": (
            "Canonical British/French/Italian Grand Battleplan doctrine combining Defensive Postures, "
            "Fire Concentration, Armored Infantry Support, and Grand Assault. Grants +30% Max Planning, "
            "+20% Coordination, +0.40 Infantry Entrenchment, +35% Army/Infantry Breakthrough, and "
            "strong infantry/artillery defense and soft attack."
        ),
        "grand_doctrine": "grand_battleplan",
        "subdoctrines": {
            "infantry": "defensive_postures",
            "combat_support": "fire_concentration",
            "armor": "armored_infantry_support",
            "operations": "grand_assault",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "grand_battleplan_assault": {
        "key": "grand_battleplan_assault",
        "name": "Grand Battleplan: Grand Assault",
        "description": (
            "Grand Battleplan with Defensive Postures, Fire Concentration, Armored Infantry Support, "
            "and Grand Assault (C3I Theory, Central Planning, Multiple Attack Directions)."
        ),
        "grand_doctrine": "grand_battleplan",
        "subdoctrines": {
            "infantry": "defensive_postures",
            "combat_support": "fire_concentration",
            "armor": "armored_infantry_support",
            "operations": "grand_assault",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "grand_battleplan_infiltration": {
        "key": "grand_battleplan_infiltration",
        "name": "Grand Battleplan: Infiltration Tactics",
        "description": (
            "Canonical Japanese/Finnish Grand Battleplan Infiltration path combining Individual "
            "Excellence (Commandos), Field Engineering, Armored Cavalry, and Infiltration Tactics. "
            "Grants +25% Land Night Attack, -10% Army Supply Consumption, +20% Infantry/Army "
            "Breakthrough, +1.0 Recon, and strong Engineer/Recon support multipliers."
        ),
        "grand_doctrine": "grand_battleplan",
        "subdoctrines": {
            "infantry": "commandos",
            "combat_support": "field_engineering",
            "armor": "armored_cavalry",
            "operations": "infiltration_tactics",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mass_assault": {
        "key": "mass_assault",
        "name": "Mass Assault (Deep Battle)",
        "description": (
            "Canonical Soviet Mass Assault Deep Battle doctrine combining Large Unit Tactics, "
            "Fire Concentration, Streamlined Deployment, and Deep Battle. Reduces Infantry combat "
            "width by -0.4 (from 2.0 to 1.6), reduces army supply consumption by -15% (plus per-unit "
            "supply reductions), and grants high tank/mechanized/motorized organization, recovery "
            "rate, and breakthrough."
        ),
        "grand_doctrine": "mass_assault",
        "subdoctrines": {
            "infantry": "large_unit_tactics",
            "combat_support": "fire_concentration",
            "armor": "streamlined_deployment",
            "operations": "deep_battle",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mass_assault_deep_battle": {
        "key": "mass_assault_deep_battle",
        "name": "Mass Assault: Deep Battle",
        "description": (
            "Mass Assault with Large Unit Tactics (-0.4 total Infantry combat width), Fire "
            "Concentration (-0.8 Line/Rocket Artillery combat width), Streamlined Deployment, "
            "and Deep Battle (+10 Tank ORG, +12 Motorized/Mechanized ORG, +14% Reinforce Rate, "
            "-30% Org Loss When Moving, -15% Supply Consumption)."
        ),
        "grand_doctrine": "mass_assault",
        "subdoctrines": {
            "infantry": "large_unit_tactics",
            "combat_support": "fire_concentration",
            "armor": "streamlined_deployment",
            "operations": "deep_battle",
        },
        "extra_effects": {"unit_mods": {}, "army_mods": {}, "tactics": []},
    },
    "mass_assault_mass_mobilization": {
        "key": "mass_assault_mass_mobilization",
        "name": "Mass Assault: Mass Mobilization (People's War / Guerilla Defense)",
        "description": (
            "Mass Assault Mass Mobilization path combining Large Unit Tactics (-0.4 total Infantry "
            "combat width), Field Engineering, Streamlined Deployment, and Guerilla War / Mass "
            "Mobilization. Grants -0.4 Infantry combat width, +0.30 Infantry recovery rate, "
            "+15 Infantry organization, +20% Army defense, and -15% Army supply consumption."
        ),
        "grand_doctrine": "mass_assault",
        "subdoctrines": {
            "infantry": "large_unit_tactics",
            "combat_support": "field_engineering",
            "armor": "streamlined_deployment",
            "operations": "guerilla_war",
        },
        "extra_effects": {
            "unit_mods": {
                "category_all_infantry": {
                    "stats": {
                        "default_morale": 0.20,
                        "max_organisation": 5.0,
                    },
                    "terrain_modifiers": {},
                    "battalion_multipliers": [],
                }
            },
            "army_mods": {
                "land_reinforce_rate": 0.05,
                "pocket_penalty": -0.10,
            },
            "tactics": ["tactic_human_wave_tactics"],
        },
    },
}

#: Shorthand and legacy aliases mapped to canonical preset keys.
DOCTRINE_ALIASES: Dict[str, str] = {
    "": "none",
    "no_doctrine": "none",
    "baseline": "none",
    "new_mobile_warfare": "mobile_warfare",
    "mw": "mobile_warfare",
    "mw_blitzkrieg": "mobile_warfare_blitzkrieg",
    "blitzkrieg": "mobile_warfare_blitzkrieg",
    "mw_desperate_defense": "mobile_warfare_desperate_defense",
    "mobile_warfare_mechanized_wave": "mobile_warfare_desperate_defense",
    "sf": "superior_firepower",
    "sf_integrated": "superior_firepower_integrated_support",
    "sf_integrated_support": "superior_firepower_integrated_support",
    "superior_firepower_airland_battle": "superior_firepower_integrated_support",
    "sf_dispersed": "superior_firepower_dispersed_support",
    "sf_dispersed_support": "superior_firepower_dispersed_support",
    "superior_firepower_shock_and_awe": "superior_firepower_dispersed_support",
    "gbp": "grand_battleplan",
    "gbp_assault": "grand_battleplan_assault",
    "gbp_infiltration": "grand_battleplan_infiltration",
    "ma": "mass_assault",
    "ma_deep_battle": "mass_assault_deep_battle",
    "deep_battle_doctrine": "mass_assault_deep_battle",
    "ma_mass_mobilization": "mass_assault_mass_mobilization",
    "mass_mobilization": "mass_assault_mass_mobilization",
}


# =============================================================================
# 3. Data Structures for Composed Doctrines & Resolved Effect Nodes
# =============================================================================

@dataclass
class ComposedDoctrine:
    """
    Represents a fully resolved HOI4 v1.19.4.2 Land Doctrine configuration
    (either a Canonical Preset, a Custom Grand Doctrine + 4 Sub-Doctrines,
    or a single standalone Sub-Doctrine).

    Attributes:
        key (str): Canonical or composite identifier of the doctrine.
        name (str): Human-readable display name.
        description (str): Detailed description of the doctrine path.
        grand_doctrine_key (Optional[str]): Underlying Grand Doctrine key
            (``"new_mobile_warfare"``, ``"superior_firepower"``, ``"grand_battleplan"``,
            ``"mass_assault"``, or ``None``).
        subdoctrine_keys (Dict[str, Optional[str]]): Selected sub-doctrine keys for
            each of the 4 tracks (``"infantry"``, ``"combat_support"``, ``"armor"``,
            ``"operations"``).
        unit_mods (Dict[str, Dict[str, Any]]): Aggregated per-category and per-unit_id
            stat bonuses, terrain modifiers, and ``battalion_mult`` multipliers at
            full mastery (``1.0``).
        army_mods (Dict[str, float]): Aggregated army-level modifiers at full mastery
            (e.g., ``land_reinforce_rate``, ``org_loss_when_moving``, ``max_planning``,
            ``supply_consumption_factor``, ``coordination_bonus``, ``land_night_attack``).
        tactics (List[str]): Unlocked combat tactics in order of activation.
    """

    key: str
    name: str
    description: str
    grand_doctrine_key: Optional[str] = None
    subdoctrine_keys: Dict[str, Optional[str]] = field(default_factory=dict)
    unit_mods: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    army_mods: Dict[str, float] = field(default_factory=dict)
    tactics: List[str] = field(default_factory=list)


# =============================================================================
# 4. Merging & Composition Engine
# =============================================================================

def _merge_effect_node(
    accum_unit_mods: Dict[str, Dict[str, Any]],
    accum_army_mods: Dict[str, float],
    accum_tactics: List[str],
    node: Dict[str, Any],
) -> None:
    """
    Merges a single Clausewitz effect node (from a Grand Doctrine root, Track Milestone,
    Sub-Doctrine root, or Sub-Doctrine Mastery Reward) into the cumulative accumulators.
    """
    if not node:
        return

    for target, data in node.get("unit_mods", {}).items():
        if target not in accum_unit_mods:
            accum_unit_mods[target] = {
                "stats": defaultdict(float),
                "terrain_modifiers": defaultdict(lambda: defaultdict(float)),
                "battalion_multipliers": [],
            }
        target_entry = accum_unit_mods[target]
        for stat_k, stat_v in data.get("stats", {}).items():
            target_entry["stats"][stat_k] += float(stat_v)
        for terr_name, terr_dict in data.get("terrain_modifiers", {}).items():
            for tk, tv in terr_dict.items():
                target_entry["terrain_modifiers"][terr_name][tk] += float(tv)
        for bm in data.get("battalion_multipliers", []):
            target_entry["battalion_multipliers"].append(dict(bm))

    for army_k, army_v in node.get("army_mods", {}).items():
        accum_army_mods[army_k] = accum_army_mods.get(army_k, 0.0) + float(army_v)
        # In Clausewitz, `army_morale` (e.g. in `large_unit_tactics` reward 4) grants
        # flat `default_morale` (recovery_rate) to all army units (`category_army`).
        if army_k == "army_morale":
            if "category_army" not in accum_unit_mods:
                accum_unit_mods["category_army"] = {
                    "stats": defaultdict(float),
                    "terrain_modifiers": defaultdict(lambda: defaultdict(float)),
                    "battalion_multipliers": [],
                }
            accum_unit_mods["category_army"]["stats"]["default_morale"] += float(army_v)

    for tac in node.get("tactics", []):
        if tac not in accum_tactics:
            accum_tactics.append(tac)


def compose_custom_doctrine(
    grand_doctrine: Optional[str],
    infantry_subdoctrine: Optional[str] = None,
    combat_support_subdoctrine: Optional[str] = None,
    armor_subdoctrine: Optional[str] = None,
    operations_subdoctrine: Optional[str] = None,
    artillery_subdoctrine: Optional[str] = None,
    extra_effects: Optional[Dict[str, Any]] = None,
    custom_key: Optional[str] = None,
    custom_name: Optional[str] = None,
    custom_description: Optional[str] = None,
) -> ComposedDoctrine:
    """
    Composes a complete HOI4 v1.19.4.2 Land Doctrine from any Grand Doctrine and up to
    4 Track Sub-Doctrines (``infantry``, ``combat_support`` / ``artillery``, ``armor``,
    and ``operations``).

    Args:
        grand_doctrine (Optional[str]): Grand Doctrine key (``"new_mobile_warfare"``,
            ``"mobile_warfare"``, ``"superior_firepower"``, ``"grand_battleplan"``,
            ``"mass_assault"``, or ``None``).
        infantry_subdoctrine (Optional[str]): Sub-doctrine key from ``infantry_subdoctrines.txt``
            (e.g., ``"mobile_infantry"``, ``"defensive_postures"``, ``"large_unit_tactics"``,
            ``"assault_infantry"``, ``"mounted_infantry"``, ``"commandos"``, ``"irregulars"``,
            ``"peoples_war"``, ``"great_war_infantry"``).
        combat_support_subdoctrine (Optional[str]): Sub-doctrine key from
            ``combat_support_subdoctrines.txt`` (e.g., ``"fire_concentration"``,
            ``"anti_tank_frontline"``, ``"flying_batteries"``, ``"air_cavalry"``,
            ``"mobile_recon_and_assault"``, ``"self_propelled_support"``,
            ``"siege_artillery"``, ``"field_engineering"``).
        armor_subdoctrine (Optional[str]): Sub-doctrine key from ``armor_subdoctrines.txt``
            (e.g., ``"armored_spearhead"``, ``"armored_infantry_support"``,
            ``"streamlined_deployment"``, ``"mobile_defense"``, ``"armored_cavalry"``,
            ``"tank_destroyer_force"``).
        operations_subdoctrine (Optional[str]): Sub-doctrine key from ``operations_subdoctrines.txt``
            (e.g., ``"mission_type_tactics"``, ``"last_stand"``, ``"infiltration_tactics"``,
            ``"grand_assault"``, ``"deep_battle"``, ``"guerilla_war"``, ``"rapid_domination"``,
            ``"expeditionary_warfare"``, ``"dispersed_operations"``).
        artillery_subdoctrine (Optional[str]): Alias for ``combat_support_subdoctrine``.
        extra_effects (Optional[Dict[str, Any]]): Optional additional effect node to merge.
        custom_key (Optional[str]): Optional override key for the composed doctrine.
        custom_name (Optional[str]): Optional override display name.
        custom_description (Optional[str]): Optional override description.

    Returns:
        ComposedDoctrine: Fully merged doctrine object ready for unit/pool application.
    """
    cs_sub = combat_support_subdoctrine or artillery_subdoctrine

    gd_norm = (grand_doctrine or "").strip().lower()
    if gd_norm == "mobile_warfare":
        gd_norm = "new_mobile_warfare"
    elif gd_norm in ("", "none", "no_doctrine"):
        gd_norm = ""

    accum_unit_mods: Dict[str, Dict[str, Any]] = {}
    accum_army_mods: Dict[str, float] = {}
    accum_tactics: List[str] = []

    track_selections: Dict[str, Optional[str]] = {
        "infantry": infantry_subdoctrine,
        "combat_support": cs_sub,
        "armor": armor_subdoctrine,
        "operations": operations_subdoctrine,
    }

    gd_obj = GRAND_DOCTRINES.get(gd_norm) if gd_norm else None
    if gd_norm and gd_obj is None:
        raise ValueError(
            f"Unknown Grand Doctrine {grand_doctrine!r}. Valid Grand Doctrines: "
            f"{sorted(GRAND_DOCTRINES.keys())}"
        )

    # 1. Apply Grand Doctrine Base Effects
    if gd_obj is not None:
        _merge_effect_node(accum_unit_mods, accum_army_mods, accum_tactics, gd_obj["base_effects"])

    # 2. Apply each Track's Sub-Doctrine (Base Effects + All Mastery Rewards) and Track Milestone
    track_order = ["infantry", "combat_support", "armor", "operations"]
    for idx, track_name in enumerate(track_order):
        sd_key = track_selections.get(track_name)
        if sd_key:
            sd_key_clean = sd_key.strip().lower()
            sd_obj = LAND_SUBDOCTRINES.get(sd_key_clean)
            if sd_obj is None:
                raise ValueError(
                    f"Unknown Land Sub-Doctrine {sd_key!r} for track {track_name!r}. "
                    f"Valid sub-doctrines: {sorted(LAND_SUBDOCTRINES.keys())}"
                )
            _merge_effect_node(accum_unit_mods, accum_army_mods, accum_tactics, sd_obj["base_effects"])
            for reward in sd_obj.get("rewards", []):
                _merge_effect_node(accum_unit_mods, accum_army_mods, accum_tactics, reward["effects"])

            # When a track has an active sub-doctrine, its completion unlocks the Grand Doctrine's
            # corresponding Track Milestone
            if gd_obj is not None and idx < len(gd_obj.get("milestones", [])):
                _merge_effect_node(
                    accum_unit_mods,
                    accum_army_mods,
                    accum_tactics,
                    gd_obj["milestones"][idx],
                )

    # 3. Apply any extra path effects
    if extra_effects:
        _merge_effect_node(accum_unit_mods, accum_army_mods, accum_tactics, extra_effects)

    # Finalize nested defaultdicts into regular dicts
    clean_unit_mods: Dict[str, Dict[str, Any]] = {}
    for target, d in accum_unit_mods.items():
        clean_unit_mods[target] = {
            "stats": dict(d["stats"]),
            "terrain_modifiers": {t: dict(td) for t, td in d["terrain_modifiers"].items()},
            "battalion_multipliers": list(d["battalion_multipliers"]),
        }

    if not custom_key:
        sub_parts = [track_selections[t] or "-" for t in track_order]
        custom_key = f"{gd_norm or 'custom'}:{','.join(sub_parts)}"

    if not custom_name:
        gd_title = gd_obj["name"] if gd_obj else "Custom Doctrine"
        active_sd_titles = [
            LAND_SUBDOCTRINES[track_selections[t].strip().lower()]["name"]
            for t in track_order
            if track_selections.get(t) and track_selections[t].strip().lower() in LAND_SUBDOCTRINES
        ]
        if active_sd_titles:
            custom_name = f"{gd_title} ({' + '.join(active_sd_titles)})"
        else:
            custom_name = gd_title

    if custom_description is None:
        custom_description = gd_obj["description"] if gd_obj else "Custom composed HOI4 v1.19 Land Doctrine."

    return ComposedDoctrine(
        key=custom_key,
        name=custom_name,
        description=custom_description,
        grand_doctrine_key=gd_norm or None,
        subdoctrine_keys=track_selections,
        unit_mods=clean_unit_mods,
        army_mods=dict(accum_army_mods),
        tactics=accum_tactics,
    )


def resolve_doctrine(doctrine_key: Optional[Union[str, ComposedDoctrine]]) -> ComposedDoctrine:
    """
    Resolves any ``doctrine_key`` (canonical preset name, alias, standalone sub-doctrine key,
    custom composition string ``"grand_doctrine:inf,sup,arm,ops"``, or ``ComposedDoctrine``
    instance) into a ``ComposedDoctrine``.

    Supported formats for ``doctrine_key``:
    1. ``ComposedDoctrine`` instance -> returned directly.
    2. Canonical preset or alias (e.g. ``"none"``, ``"mobile_warfare"``,
       ``"superior_firepower_integrated_support"``, ``"mass_assault_deep_battle"``,
       ``"mass_assault_mass_mobilization"``).
    3. Standalone v1.19 Sub-Doctrine key (e.g. ``"assault_infantry"``, ``"fire_concentration"``,
       ``"armored_spearhead"``, ``"deep_battle"``, ``"siege_artillery"``).
    4. Composite syntax ``"<grand_doctrine>:<infantry>,<combat_support>,<armor>,<operations>"``
       or ``"<grand_doctrine>+<sub1>+<sub2>..."``.
    """
    if isinstance(doctrine_key, ComposedDoctrine):
        return doctrine_key

    raw_key = (doctrine_key or "none").strip().lower()
    raw_key = raw_key.replace(" ", "_").replace("-", "_")

    # 1. Check aliases and canonical presets
    resolved_key = DOCTRINE_ALIASES.get(raw_key, raw_key)
    if resolved_key in CANONICAL_DOCTRINE_PRESETS:
        preset = CANONICAL_DOCTRINE_PRESETS[resolved_key]
        sds = preset["subdoctrines"]
        return compose_custom_doctrine(
            grand_doctrine=preset["grand_doctrine"],
            infantry_subdoctrine=sds.get("infantry"),
            combat_support_subdoctrine=sds.get("combat_support"),
            armor_subdoctrine=sds.get("armor"),
            operations_subdoctrine=sds.get("operations"),
            extra_effects=preset.get("extra_effects"),
            custom_key=preset["key"],
            custom_name=preset["name"],
            custom_description=preset["description"],
        )

    # 2. Check standalone v1.19 Sub-Doctrine key
    if resolved_key in LAND_SUBDOCTRINES:
        sd = LAND_SUBDOCTRINES[resolved_key]
        track = sd["track"]
        kwargs: Dict[str, Optional[str]] = {
            "infantry_subdoctrine": None,
            "combat_support_subdoctrine": None,
            "armor_subdoctrine": None,
            "operations_subdoctrine": None,
        }
        kwargs[f"{track}_subdoctrine"] = resolved_key
        return compose_custom_doctrine(
            grand_doctrine=None,
            custom_key=resolved_key,
            custom_name=f"Sub-Doctrine: {sd['name']} ({DOCTRINE_TRACKS[track]['name']} Track)",
            custom_description=sd["description"],
            **kwargs,
        )

    # 3. Check custom composition string ("grand_doctrine:inf,sup,arm,ops" or "gd+sub1+sub2...")
    if ":" in raw_key or "+" in raw_key or "," in raw_key:
        if ":" in raw_key:
            gd_part, subs_part = raw_key.split(":", 1)
            sub_tokens = [s.strip() for s in re.split(r"[,+]", subs_part) if s.strip()]
        else:
            tokens = [s.strip() for s in re.split(r"[,+]", raw_key) if s.strip()]
            if tokens and (
                tokens[0] in GRAND_DOCTRINES
                or DOCTRINE_ALIASES.get(tokens[0]) in CANONICAL_DOCTRINE_PRESETS
                or tokens[0] == "mobile_warfare"
            ):
                gd_part = tokens[0]
                sub_tokens = tokens[1:]
            else:
                gd_part = ""
                sub_tokens = tokens

        track_map: Dict[str, Optional[str]] = {
            "infantry": None,
            "combat_support": None,
            "armor": None,
            "operations": None,
        }
        track_order = ["infantry", "combat_support", "armor", "operations"]
        for idx, tok in enumerate(sub_tokens):
            if tok in ("-", "none", ""):
                continue
            if tok in LAND_SUBDOCTRINES:
                tr = LAND_SUBDOCTRINES[tok]["track"]
                track_map[tr] = tok
            elif idx < len(track_order):
                track_map[track_order[idx]] = tok

        return compose_custom_doctrine(
            grand_doctrine=gd_part or None,
            infantry_subdoctrine=track_map["infantry"],
            combat_support_subdoctrine=track_map["combat_support"],
            armor_subdoctrine=track_map["armor"],
            operations_subdoctrine=track_map["operations"],
            custom_key=raw_key,
        )

    raise ValueError(
        f"Unknown doctrine_key {doctrine_key!r}. Use list_available_doctrines() to see "
        f"canonical presets or list_all_subdoctrines() for individual v1.19 sub-doctrines."
    )


def resolve_mastery_level(year: str = "1945", mastery_level: Optional[float] = None) -> float:
    """
    Resolves the effective doctrine ``mastery_level`` in ``[0.0, 1.0]``.

    - If ``mastery_level`` is explicitly provided, clamps it to ``[0.0, 1.0]``.
    - Otherwise looks up ``year`` in ``DEFAULT_MASTERY_BY_YEAR`` (falling back to the
      closest earlier benchmark year, or ``1.0`` for years >= 1945).
    """
    if mastery_level is not None:
        return max(0.0, min(1.0, float(mastery_level)))

    yr_str = str(year).strip()
    if yr_str in DEFAULT_MASTERY_BY_YEAR:
        return DEFAULT_MASTERY_BY_YEAR[yr_str]

    if yr_str.isdigit():
        yr_int = int(yr_str)
        if yr_int <= 1934:
            return 0.0
        if yr_int >= 1945:
            return 1.0
        best_val = 0.0
        for k_str, val in sorted(DEFAULT_MASTERY_BY_YEAR.items(), key=lambda x: int(x[0])):
            if int(k_str) <= yr_int:
                best_val = val
        return best_val

    return 1.0


# =============================================================================
# 5. Exact Unit Stat & Modifier Application Functions
# =============================================================================

def _unit_matches_target(unit: Union[Battalion, SupportCompany], target: str) -> bool:
    """
    Returns True if ``unit`` matches the Clausewitz doctrine target (either by
    exact ``unit.unit_id == target`` or membership in ``unit.categories``).
    """
    if getattr(unit, "unit_id", "") == target:
        return True
    cats = getattr(unit, "categories", None) or []
    return target in cats


def _convert_clausewitz_bm_to_dataclass(
    bm_dict: Dict[str, Any],
    mastery_scale: float,
) -> BattalionMultiplier:
    """
    Converts a raw Clausewitz ``battalion_mult`` dictionary from a doctrine into a
    scaled ``BattalionMultiplier`` dataclass instance compatible with ``Division.calculate_stats()``.
    """
    cat = str(bm_dict.get("category", ""))
    additive = bool(bm_dict.get("additive", False))
    hp_bonus = float(bm_dict.get("max_strength", 0.0)) + float(bm_dict.get("strength", 0.0))

    return BattalionMultiplier(
        category=cat,
        soft_attack=float(bm_dict.get("soft_attack", 0.0)) * mastery_scale,
        hard_attack=float(bm_dict.get("hard_attack", 0.0)) * mastery_scale,
        defense=float(bm_dict.get("defense", 0.0)) * mastery_scale,
        breakthrough=float(bm_dict.get("breakthrough", 0.0)) * mastery_scale,
        max_hp=hp_bonus * mastery_scale,
        organization=float(bm_dict.get("max_organisation", 0.0)) * mastery_scale,
        recovery_rate=float(bm_dict.get("default_morale", 0.0)) * mastery_scale,
        air_attack=float(bm_dict.get("air_attack", 0.0)) * mastery_scale,
        armor=float(bm_dict.get("armor_value", bm_dict.get("armor", 0.0))) * mastery_scale,
        piercing=float(bm_dict.get("ap_attack", 0.0)) * mastery_scale,
        additive=additive,
        entrenchment=float(bm_dict.get("entrenchment", 0.0)) * mastery_scale,
        initiative=float(bm_dict.get("initiative", 0.0)) * mastery_scale,
        supply_use=float(bm_dict.get("supply_consumption", 0.0)) * mastery_scale,
    )


def _apply_composed_doctrine_to_stats_and_modifiers(
    unit: Union[Battalion, SupportCompany],
    doctrine: ComposedDoctrine,
    mastery: float,
) -> Tuple[BaseStatistics, UnitModifiers]:
    """
    Applies a ``ComposedDoctrine`` at ``mastery`` level to a ``Battalion`` or ``SupportCompany``,
    returning a newly constructed ``(BaseStatistics, UnitModifiers)`` pair following official
    HOI4 Clausewitz rules:
    1. Additive stats:
       - ``max_organisation`` -> ``organization + sum(bonus * mastery)``
       - ``default_morale`` -> ``recovery_rate + sum(bonus * mastery)``
       - ``entrenchment`` -> ``entrenchment + sum(bonus * mastery)``
       - ``initiative`` -> ``initiative + sum(bonus * mastery)``
       - ``recon`` -> ``recon + sum(bonus * mastery)``
       - ``supply_consumption_factor`` -> ``supply_consumption_factor + sum(bonus * mastery)``
       - ``combat_width`` -> ``combat_width + sum(bonus)`` when ``mastery >= 0.60``
       - ``supply_consumption`` -> ``supply_use + sum(bonus * mastery)``, then scaled by
         army-level ``supply_consumption_factor``.
    2. Multiplicative stats:
       - ``soft_attack``, ``hard_attack``, ``defense``, ``breakthrough``, ``ap_attack``
         (``piercing``), ``armor_value`` (``armor``), ``air_attack``, ``max_strength`` (``max_hp``)
         -> ``base * (1.0 + sum(pct * mastery))``.
    3. ``UnitModifiers``:
       - Clones existing ``terrain_modifiers`` and ``battalion_multipliers`` and merges all
         matching doctrine terrain modifiers and ``battalion_mult`` blocks.
    """
    raw = unit.get_stats()

    # Clone existing UnitModifiers deeply so we never mutate unit_database singletons
    cloned_terrains: Dict[str, TerrainModifier] = {}
    if unit.modifiers and unit.modifiers.terrain_modifiers:
        for t_name, tm in unit.modifiers.terrain_modifiers.items():
            cloned_terrains[t_name] = TerrainModifier(
                attack=tm.attack,
                defense=tm.defense,
                movement=tm.movement,
            )

    cloned_bms: List[BattalionMultiplier] = []
    if unit.modifiers and unit.modifiers.battalion_multipliers:
        for bm in unit.modifiers.battalion_multipliers:
            cloned_bms.append(
                BattalionMultiplier(
                    category=bm.category,
                    soft_attack=bm.soft_attack,
                    hard_attack=bm.hard_attack,
                    defense=bm.defense,
                    breakthrough=bm.breakthrough,
                    max_hp=bm.max_hp,
                    organization=bm.organization,
                    recovery_rate=bm.recovery_rate,
                    air_attack=bm.air_attack,
                    armor=bm.armor,
                    piercing=bm.piercing,
                    additive=bm.additive,
                    entrenchment=bm.entrenchment,
                    initiative=bm.initiative,
                    supply_use=bm.supply_use,
                )
            )

    if mastery <= 0.0 or doctrine.key == "none" or (not doctrine.unit_mods and not doctrine.army_mods):
        new_stats = BaseStatistics(
            soft_attack=raw.soft_attack,
            hard_attack=raw.hard_attack,
            defense=raw.defense,
            breakthrough=raw.breakthrough,
            max_hp=raw.max_hp,
            organization=raw.organization,
            combat_width=raw.combat_width,
            supply_use=raw.supply_use,
            ic_cost=raw.ic_cost,
            manpower=raw.manpower,
            armor=raw.armor,
            piercing=raw.piercing,
            hardness=raw.hardness,
            air_attack=raw.air_attack,
            entrenchment=raw.entrenchment,
            initiative=raw.initiative,
            recon=raw.recon,
            supply_consumption_factor=raw.supply_consumption_factor,
            recovery_rate=raw.recovery_rate,
        )
        return new_stats, UnitModifiers(
            terrain_modifiers=cloned_terrains,
            battalion_multipliers=cloned_bms,
        )

    # Accumulate all matching unit/category stat bonuses
    stat_bonuses: Dict[str, float] = defaultdict(float)

    for target, data in doctrine.unit_mods.items():
        if _unit_matches_target(unit, target):
            for sk, sv in data.get("stats", {}).items():
                stat_bonuses[sk] += float(sv)

            for t_name, t_dict in data.get("terrain_modifiers", {}).items():
                if t_name not in cloned_terrains:
                    cloned_terrains[t_name] = TerrainModifier()
                tm_obj = cloned_terrains[t_name]
                tm_obj.attack = round(tm_obj.attack + float(t_dict.get("attack", 0.0)) * mastery, 6)
                tm_obj.defense = round(tm_obj.defense + float(t_dict.get("defense", 0.0)) * mastery, 6)
                tm_obj.movement = round(tm_obj.movement + float(t_dict.get("movement", 0.0)) * mastery, 6)

            for bm_dict in data.get("battalion_multipliers", []):
                cloned_bms.append(_convert_clausewitz_bm_to_dataclass(bm_dict, mastery))

    # Multiplicative stats: base * (1.0 + sum_pct * mastery)
    def mult_stat(base_val: float, key: str) -> float:
        pct = stat_bonuses.get(key, 0.0) * mastery
        return round(max(0.0, base_val * (1.0 + pct)), 6)

    # Additive stats: base + sum_add * mastery
    def add_stat(base_val: float, key: str, clamp_zero: bool = True) -> float:
        delta = stat_bonuses.get(key, 0.0) * mastery
        val = base_val + delta
        return round(max(0.0, val) if clamp_zero else val, 6)

    # Discrete combat width reduction: applied in full when mastery >= 0.60
    # Only applies to line battalions that have positive base combat_width
    new_combat_width = raw.combat_width
    if raw.combat_width > 0.0 and mastery >= DISCRETE_COMBAT_WIDTH_MASTERY_THRESHOLD:
        cw_delta = stat_bonuses.get("combat_width", 0.0)
        if cw_delta != 0.0:
            new_combat_width = round(max(0.2, raw.combat_width + cw_delta), 4)

    # Supply use: apply unit-level flat supply_consumption bonus first, then army-level
    # supply_consumption_factor (e.g. -0.10 in Superior Firepower / Infiltration, -0.15 in Mass Assault)
    unit_supply_delta = stat_bonuses.get("supply_consumption", 0.0) * mastery
    army_supply_factor = doctrine.army_mods.get("supply_consumption_factor", 0.0) * mastery
    new_supply_use = max(0.0, raw.supply_use + unit_supply_delta)
    if army_supply_factor != 0.0:
        new_supply_use = max(0.0, new_supply_use * (1.0 + army_supply_factor))
    new_supply_use = round(new_supply_use, 6)

    new_stats = BaseStatistics(
        soft_attack=mult_stat(raw.soft_attack, "soft_attack"),
        hard_attack=mult_stat(raw.hard_attack, "hard_attack"),
        defense=mult_stat(raw.defense, "defense"),
        breakthrough=mult_stat(raw.breakthrough, "breakthrough"),
        max_hp=mult_stat(raw.max_hp, "max_strength"),
        organization=add_stat(raw.organization, "max_organisation"),
        combat_width=new_combat_width,
        supply_use=new_supply_use,
        ic_cost=raw.ic_cost,
        manpower=raw.manpower,
        armor=mult_stat(raw.armor, "armor_value"),
        piercing=mult_stat(raw.piercing, "ap_attack"),
        hardness=raw.hardness,
        air_attack=mult_stat(raw.air_attack, "air_attack"),
        entrenchment=add_stat(raw.entrenchment, "entrenchment", clamp_zero=False),
        initiative=add_stat(raw.initiative, "initiative", clamp_zero=False),
        recon=add_stat(raw.recon, "recon", clamp_zero=False),
        supply_consumption_factor=add_stat(
            raw.supply_consumption_factor, "supply_consumption_factor", clamp_zero=False
        ),
        recovery_rate=add_stat(raw.recovery_rate, "default_morale"),
    )

    new_modifiers = UnitModifiers(
        terrain_modifiers=cloned_terrains,
        battalion_multipliers=cloned_bms,
    )
    return new_stats, new_modifiers


def apply_doctrine_to_battalion(
    battalion: Battalion,
    doctrine_key: Union[str, ComposedDoctrine] = "none",
    year: str = "1945",
    mastery_level: Optional[float] = None,
) -> Battalion:
    """
    Applies a HOI4 v1.19.4.2 Land Doctrine to a line ``Battalion`` and returns a new
    cloned ``Battalion`` with updated ``BaseStatistics`` and ``UnitModifiers``.

    Args:
        battalion (Battalion): Source line battalion (never mutated in-place).
        doctrine_key (Union[str, ComposedDoctrine]): Canonical doctrine preset key
            (e.g., ``"mobile_warfare"``, ``"superior_firepower_integrated_support"``,
            ``"grand_battleplan_assault"``, ``"mass_assault_deep_battle"``,
            ``"mass_assault_mass_mobilization"``), standalone v1.19 sub-doctrine key,
            composite string, or ``ComposedDoctrine`` instance.
        year (str): Benchmark technology year (``"1934"``, ``"1936"``, ``"1939"``,
            ``"1940"``, ``"1945"``) used to determine default ``mastery_level`` when
            ``mastery_level`` is None.
        mastery_level (Optional[float]): Explicit doctrine mastery override in ``[0.0, 1.0]``.
            Pass ``1.0`` for full doctrine comparison at any year.

    Returns:
        Battalion: New ``Battalion`` instance with doctrine-modified statistics and modifiers.
    """
    doctrine = resolve_doctrine(doctrine_key)
    mastery = resolve_mastery_level(year=year, mastery_level=mastery_level)
    new_stats, new_modifiers = _apply_composed_doctrine_to_stats_and_modifiers(
        battalion, doctrine, mastery
    )

    return Battalion(
        name=battalion.name,
        base_stats=new_stats,
        modifiers=new_modifiers,
        unit_id=battalion.unit_id,
        group=battalion.group,
        categories=list(battalion.categories),
        year_unlocked=battalion.year_unlocked,
        is_special_project=battalion.is_special_project,
        is_country_locked=battalion.is_country_locked,
    )


def apply_doctrine_to_support(
    support: SupportCompany,
    doctrine_key: Union[str, ComposedDoctrine] = "none",
    year: str = "1945",
    mastery_level: Optional[float] = None,
) -> SupportCompany:
    """
    Applies a HOI4 v1.19.4.2 Land Doctrine to a Divisional or Regimental ``SupportCompany``
    and returns a new cloned ``SupportCompany`` with updated ``BaseStatistics`` and
    ``UnitModifiers`` (including any doctrine-unlocked ``battalion_mult`` multipliers).

    Args:
        support (SupportCompany): Source divisional or regimental support company.
        doctrine_key (Union[str, ComposedDoctrine]): Canonical doctrine key, sub-doctrine key,
            composite string, or ``ComposedDoctrine`` instance.
        year (str): Benchmark technology year (``"1934"``..``"1945"``).
        mastery_level (Optional[float]): Explicit doctrine mastery override in ``[0.0, 1.0]``.

    Returns:
        SupportCompany: New ``SupportCompany`` instance with doctrine-modified stats and
        ``battalion_mult`` modifiers.
    """
    doctrine = resolve_doctrine(doctrine_key)
    mastery = resolve_mastery_level(year=year, mastery_level=mastery_level)
    new_stats, new_modifiers = _apply_composed_doctrine_to_stats_and_modifiers(
        support, doctrine, mastery
    )

    return SupportCompany(
        name=support.name,
        base_stats=new_stats,
        modifiers=new_modifiers,
        unit_id=support.unit_id,
        is_divisional=support.is_divisional,
        is_regimental=support.is_regimental,
        allowed_battalion_groups=list(support.allowed_battalion_groups),
        same_support_type=list(support.same_support_type),
        categories=list(support.categories),
        year_unlocked=support.year_unlocked,
        is_special_project=support.is_special_project,
        is_country_locked=support.is_country_locked,
    )


def apply_doctrine_to_pool(
    battalions: Dict[str, Battalion],
    divisional_supports: Dict[str, SupportCompany],
    regimental_supports: Dict[str, SupportCompany],
    doctrine_key: Union[str, ComposedDoctrine] = "none",
    year: str = "1945",
    mastery_level: Optional[float] = None,
) -> Tuple[Dict[str, Battalion], Dict[str, SupportCompany], Dict[str, SupportCompany]]:
    """
    Applies a HOI4 v1.19.4.2 Land Doctrine across an entire unit pool of line battalions,
    divisional support companies, and regimental support companies.

    Designed for seamless integration with ``UnitPool`` in ``optimizer/base.py`` and
    division template simulation workflows.

    Args:
        battalions (Dict[str, Battalion]): Mapping of battalion name -> ``Battalion``.
        divisional_supports (Dict[str, SupportCompany]): Mapping of divisional support
            company name -> ``SupportCompany``.
        regimental_supports (Dict[str, SupportCompany]): Mapping of regimental support
            company name -> ``SupportCompany``.
        doctrine_key (Union[str, ComposedDoctrine]): Doctrine key or ``ComposedDoctrine``.
        year (str): Benchmark technology year (``"1934"``..``"1945"``).
        mastery_level (Optional[float]): Explicit doctrine mastery override in ``[0.0, 1.0]``.

    Returns:
        Tuple[Dict[str, Battalion], Dict[str, SupportCompany], Dict[str, SupportCompany]]:
        ``(new_battalions, new_divisional_supports, new_regimental_supports)``
    """
    doctrine = resolve_doctrine(doctrine_key)
    mastery = resolve_mastery_level(year=year, mastery_level=mastery_level)

    new_battalions: Dict[str, Battalion] = {
        name: apply_doctrine_to_battalion(bat, doctrine, year=year, mastery_level=mastery)
        for name, bat in battalions.items()
    }
    new_div_supports: Dict[str, SupportCompany] = {
        name: apply_doctrine_to_support(sup, doctrine, year=year, mastery_level=mastery)
        for name, sup in divisional_supports.items()
    }
    new_reg_supports: Dict[str, SupportCompany] = {
        name: apply_doctrine_to_support(reg_sup, doctrine, year=year, mastery_level=mastery)
        for name, reg_sup in regimental_supports.items()
    }
    return new_battalions, new_div_supports, new_reg_supports


# =============================================================================
# 6. Discovery, Inspection & Game-File Verification Functions
# =============================================================================

def list_available_doctrines(include_subdoctrines: bool = False) -> Dict[str, str]:
    """
    Returns a dictionary mapping available ``doctrine_key`` identifiers to their
    human-readable display names.

    By default, returns the 9 canonical Grand Doctrine preset paths (``"none"``,
    ``"mobile_warfare"``, ``"mobile_warfare_blitzkrieg"``, ``"mobile_warfare_desperate_defense"``,
    ``"superior_firepower"``, ``"superior_firepower_integrated_support"``,
    ``"superior_firepower_dispersed_support"``, ``"grand_battleplan"``,
    ``"grand_battleplan_assault"``, ``"grand_battleplan_infiltration"``,
    ``"mass_assault"``, ``"mass_assault_deep_battle"``, ``"mass_assault_mass_mobilization"``).
    When ``include_subdoctrines=True``, also includes all 34 individual v1.19 Land Sub-Doctrines.
    """
    result: Dict[str, str] = {
        k: v["name"] for k, v in CANONICAL_DOCTRINE_PRESETS.items()
    }
    if include_subdoctrines:
        for sd_key, sd_val in LAND_SUBDOCTRINES.items():
            tr_name = DOCTRINE_TRACKS.get(sd_val["track"], {}).get("name", sd_val["track"])
            result[sd_key] = f"Sub-Doctrine [{tr_name}]: {sd_val['name']}"
    return result


def list_all_subdoctrines(track: Optional[str] = None) -> Dict[str, str]:
    """
    Returns all v1.19 Land Sub-Doctrines (optionally filtered by ``track`` in
    ``{"infantry", "combat_support", "armor", "operations"}`` or ``"artillery"``).
    """
    norm_track = (track or "").strip().lower()
    if norm_track == "artillery":
        norm_track = "combat_support"

    result: Dict[str, str] = {}
    for sd_key, sd_val in LAND_SUBDOCTRINES.items():
        if not norm_track or sd_val["track"] == norm_track:
            result[sd_key] = sd_val["name"]
    return result


def get_doctrine_summary(
    doctrine_key: Union[str, ComposedDoctrine] = "none",
    year: str = "1945",
    mastery_level: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Returns a comprehensive JSON-serializable summary of the specified Land Doctrine,
    including its Grand Doctrine root, active Track Sub-Doctrines, effective mastery level,
    scaled unit/category modifiers, scaled army-level modifiers, and unlocked combat tactics.
    """
    doctrine = resolve_doctrine(doctrine_key)
    mastery = resolve_mastery_level(year=year, mastery_level=mastery_level)

    scaled_unit_mods: Dict[str, Dict[str, Any]] = {}
    for target, d in doctrine.unit_mods.items():
        scaled_stats: Dict[str, float] = {}
        for sk, sv in d.get("stats", {}).items():
            if sk == "combat_width":
                if mastery >= DISCRETE_COMBAT_WIDTH_MASTERY_THRESHOLD:
                    scaled_stats[sk] = round(float(sv), 4)
            else:
                scaled_stats[sk] = round(float(sv) * mastery, 4)
        scaled_terrains = {
            t_name: {tk: round(float(tv) * mastery, 4) for tk, tv in t_dict.items()}
            for t_name, t_dict in d.get("terrain_modifiers", {}).items()
        }
        scaled_bms = []
        for bm in d.get("battalion_multipliers", []):
            bm_copy = dict(bm)
            for bmk, bmv in list(bm_copy.items()):
                if bmk not in ("category", "additive") and isinstance(bmv, (int, float)):
                    bm_copy[bmk] = round(float(bmv) * mastery, 4)
            scaled_bms.append(bm_copy)

        scaled_unit_mods[target] = {
            "stats": scaled_stats,
            "terrain_modifiers": scaled_terrains,
            "battalion_multipliers": scaled_bms,
        }

    scaled_army_mods = {
        ak: round(float(av) * mastery, 4)
        for ak, av in doctrine.army_mods.items()
    }

    return {
        "key": doctrine.key,
        "name": doctrine.name,
        "description": doctrine.description,
        "grand_doctrine": doctrine.grand_doctrine_key,
        "subdoctrines": dict(doctrine.subdoctrine_keys),
        "year": str(year),
        "mastery_level": mastery,
        "combat_width_reductions_active": mastery >= DISCRETE_COMBAT_WIDTH_MASTERY_THRESHOLD,
        "unit_modifiers": scaled_unit_mods,
        "army_modifiers": scaled_army_mods,
        "tactics": list(doctrine.tactics) if mastery > 0.0 else [],
    }

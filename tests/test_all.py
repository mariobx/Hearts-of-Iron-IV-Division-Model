"""
Comprehensive Unit & Integration Test Suite for the HOI4 v1.19.4.2 Division
Simulation & Agnostic Optimization Framework.

Run with:
    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from typing import Any, Dict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from battalion import Battalion
from division import Division
import division_database
import doctrines
from modifiers import BattalionMultiplier, TerrainModifier, UnitModifiers
from stats import BaseStatistics, calculate_division_stats
from support_company import SupportCompany
import tank_designer
from terrain import ALL_TERRAINS, EXTENDED_TERRAINS, MOUNTAIN, PLAINS, URBAN
import unit_database
from optimizer import (
    BaseDivisionOptimizer,
    CandidateSolution,
    CatSwarmOptimizer,
    DifferentialEvolutionOptimizer,
    DivisionEvaluator,
    DivisionGenome,
    GeneticOptimizer,
    GreyWolfOptimizer,
    OPTIMIZER_REGISTRY,
    OptimizationConfig,
    ParticleSwarmOptimizer,
    RandomSearchOptimizer,
    SimulatedAnnealingOptimizer,
    UnitPool,
    create_optimizer,
    list_available_optimizers,
    register_optimizer,
    run_optimization,
)
from optimizer.dashboard import LiveDashboardServer
from optimizer.logger import TrainingTelemetryLogger, setup_logger


class TestOfficialV119Database(unittest.TestCase):
    """Verifies official HOI4 v1.19.4.2 ('Operation Postern') unit stats across all benchmark years."""

    def test_supported_years_present(self) -> None:
        expected_years = ["1934", "1936", "1939", "1940", "1945"]
        self.assertEqual(unit_database.SUPPORTED_YEARS, expected_years)
        for year in expected_years:
            self.assertIn(year, unit_database.All_Battalions)
            self.assertIn(year, unit_database.Divisional_Support_Companies)
            self.assertIn(year, unit_database.Regimental_Support_Companies)
            self.assertGreaterEqual(len(unit_database.All_Battalions[year]), 40)
            self.assertGreaterEqual(len(unit_database.Divisional_Support_Companies[year]), 40)
            self.assertEqual(len(unit_database.Regimental_Support_Companies[year]), 14)

    def test_support_company_tech_progressions(self) -> None:
        # Engineer Company entrenchment: 2.0 (1934/36) -> 2.5 (1939/40) -> 3.5 (1945)
        self.assertAlmostEqual(
            unit_database.Support_Companies["1936"]["Engineer Company"].base_stats.entrenchment,
            2.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1939"]["Engineer Company"].base_stats.entrenchment,
            2.5,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1945"]["Engineer Company"].base_stats.entrenchment,
            3.5,
        )

        # Recon Company recon: 1.0 (1934/36) -> 3.0 (1939/40) -> 7.0 (1945)
        self.assertAlmostEqual(
            unit_database.Support_Companies["1936"]["Recon Company"].base_stats.recon,
            1.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1939"]["Recon Company"].base_stats.recon,
            3.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1945"]["Recon Company"].base_stats.recon,
            7.0,
        )

        # Logistics Company supply_consumption_factor: -0.1 (1936) -> -0.2 (1939/40) -> -0.4 (1945)
        self.assertAlmostEqual(
            unit_database.Support_Companies["1936"]["Logistics Company"].base_stats.supply_consumption_factor,
            -0.1,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Logistics Company"].base_stats.supply_consumption_factor,
            -0.2,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1945"]["Logistics Company"].base_stats.supply_consumption_factor,
            -0.4,
        )

        # Signal Company initiative: 0.10 (1936) -> 0.22 (1939/40) -> 0.46 (1945)
        self.assertAlmostEqual(
            unit_database.Support_Companies["1936"]["Signal Company"].base_stats.initiative,
            0.10,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Signal Company"].base_stats.initiative,
            0.22,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1945"]["Signal Company"].base_stats.initiative,
            0.46,
        )

    def test_v119_special_projects_and_balance_changes(self) -> None:
        # Land Cruiser in v1.19.4.2: SA=75, HA=62, IC=330 (in 1940), +10% Def/Brk in 1945
        lc_40 = unit_database.Support_Companies["1940"]["Land Cruiser"]
        self.assertTrue(lc_40.is_special_project)
        self.assertTrue(lc_40.is_divisional)
        self.assertFalse(lc_40.is_regimental)
        self.assertAlmostEqual(lc_40.base_stats.soft_attack, 75.0)
        self.assertAlmostEqual(lc_40.base_stats.hard_attack, 62.0)
        self.assertAlmostEqual(lc_40.base_stats.ic_cost, 330.0)
        self.assertAlmostEqual(lc_40.base_stats.combat_width, 0.0)

        # Helicopter units have unshifted Defense=6, Breakthrough=8, Armor=4, Piercing=11
        heli_brig = unit_database.Support_Companies["1940"]["Helicopter Brigade"]
        self.assertAlmostEqual(heli_brig.base_stats.soft_attack, 0.0)
        self.assertAlmostEqual(heli_brig.base_stats.hard_attack, 0.0)
        self.assertAlmostEqual(heli_brig.base_stats.defense, 6.0)
        self.assertAlmostEqual(heli_brig.base_stats.breakthrough, 8.0)
        self.assertAlmostEqual(heli_brig.base_stats.armor, 4.0)
        self.assertAlmostEqual(heli_brig.base_stats.piercing, 11.0)

        # Armored support companies have exact v1.19 IC costs (420, 320, 300, 300)
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Armored Engineer Company"].base_stats.ic_cost,
            420.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Assault Engineer Company"].base_stats.ic_cost,
            320.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Armored Maintenance Company"].base_stats.ic_cost,
            300.0,
        )
        self.assertAlmostEqual(
            unit_database.Support_Companies["1940"]["Armored Signal Company"].base_stats.ic_cost,
            300.0,
        )

        # Super-Heavy Tank family is strictly in Divisional Support (combat_width=0), not Line Battalions
        for year in unit_database.SUPPORTED_YEARS:
            self.assertNotIn("Super-Heavy Tank", unit_database.All_Battalions[year])
            self.assertIn("Super-Heavy Tank", unit_database.Divisional_Support_Companies[year])
            sh = unit_database.Divisional_Support_Companies[year]["Super-Heavy Tank"]
            self.assertAlmostEqual(sh.base_stats.combat_width, 0.0)


class TestHOI4DivisionDesignerRules(unittest.TestCase):
    """Verifies real HOI4 v1.19.4.2 Division Designer grid, column group locks, and support rules."""

    def test_5_brigade_column_group_locks(self) -> None:
        div = Division("Column Group Test")
        b_939 = unit_database.All_Battalions["1939"]
        # Fill 5 columns with 5 distinct groups
        self.assertTrue(div.add_battalion(b_939["Infantry"]))              # col 0: infantry
        self.assertTrue(div.add_battalion(b_939["Artillery"]))             # col 1: combat_support
        self.assertTrue(div.add_battalion(b_939["Motorized Infantry"]))    # col 2: mobile
        self.assertTrue(div.add_battalion(b_939["Motorized Artillery"]))   # col 3: mobile_combat_support
        self.assertTrue(div.add_battalion(b_939["Light Tank"]))            # col 4: armor

        # 6th distinct group (armor_combat_support) must be rejected because all 5 columns are locked
        self.assertFalse(div.add_battalion(b_939["Light Tank Destroyer"]))
        with self.assertRaises(ValueError):
            div.add_battalion(b_939["Light Tank Destroyer"], strict=True)

        # Adding another Infantry fits into column 0 (which is locked to 'infantry')
        self.assertTrue(div.add_battalion(b_939["Mountaineers"]))
        self.assertEqual(len(div.regiments[0]), 2)

    def test_divisional_support_mutual_exclusivity(self) -> None:
        div = Division("Support Exclusivity Test")
        s_40 = unit_database.Divisional_Support_Companies["1940"]

        self.assertTrue(div.add_support_company(s_40["Engineer Company"]))
        # Armored Engineer shares same_support_type 'engineer' -> rejected
        self.assertFalse(div.add_support_company(s_40["Armored Engineer Company"]))

        # Helicopter Brigade has same_support_type = [helicopter_recon, helicopter_transport, helicopter_field_hospital]
        self.assertTrue(div.add_support_company(s_40["Helicopter Brigade"]))
        self.assertFalse(div.add_support_company(s_40["Helicopter Recon"]))
        self.assertFalse(div.add_support_company(s_40["Helicopter Med-Evac"]))
        self.assertFalse(div.add_support_company(s_40["Helicopter Transports"]))
        # Standard Cavalry Recon ('recon') does not conflict with Helicopter Brigade
        self.assertTrue(div.add_support_company(s_40["Recon Company"]))

    def test_regimental_support_rules_v119(self) -> None:
        div = Division("Regimental Support Rule Test")
        b_40 = unit_database.All_Battalions["1940"]
        rs_40 = unit_database.Regimental_Support_Companies["1940"]

        # Column 0: only 2 Infantry battalions -> cannot unlock Regimental Support (< 3 battalions)
        div.add_battalion(b_40["Infantry"], column=0)
        div.add_battalion(b_40["Infantry"], column=0)
        self.assertFalse(div.add_regimental_support(rs_40["Fire Support Team"], column=0))

        # Add 3rd Infantry battalion to Column 0 -> now qualifies for Fire Support Team!
        div.add_battalion(b_40["Infantry"], column=0)
        self.assertTrue(div.add_regimental_support(rs_40["Fire Support Team"], column=0))

        # Column 1: 3 Medium Tanks ('armor' group)
        for _ in range(3):
            div.add_battalion(b_40["Medium Tank"], column=1)

        # Fire Support Team only allows [infantry, mobile, combat_support] -> rejected under 'armor'!
        self.assertFalse(div.add_regimental_support(rs_40["Fire Support Team"], column=1))
        # Medium Tank Destroyer Support allows [armor, mobile_combat_support, armor_combat_support] -> accepted!
        self.assertTrue(div.add_regimental_support(rs_40["Medium Tank Destroyer Support"], column=1))

        is_valid, violations = div.validate_division_rules()
        self.assertTrue(is_valid, f"Unexpected violations: {violations}")


class TestAgnosticOptimizationAndCSO(unittest.TestCase):
    """Tests Cat Swarm Optimization (PMC7204373) and all swappable optimization methods."""

    def test_all_registered_optimizers_run_and_produce_valid_divisions(self) -> None:
        available = list_available_optimizers()
        for expected in ("cso", "ga", "pso", "de", "gwo", "sa", "random"):
            self.assertIn(expected, available)

        for method_key in ("cso", "ga", "pso", "de", "gwo", "sa", "random"):
            with self.subTest(method=method_key):
                res = run_optimization(
                    method=method_key,
                    year="1939",
                    objective="bang_for_buck",
                    terrains=["Plains", "Forest"],
                    population_size=6,
                    iterations=2,
                    battles_per_evaluation=1,
                    random_seed=42,
                )
                self.assertIn("leader", res)
                self.assertIn("best_division", res)
                best_div = res["best_division"]
                is_valid, violations = best_div.validate_division_rules()
                self.assertTrue(
                    is_valid,
                    f"Method {method_key} produced invalid division: {violations}",
                )
                self.assertGreater(res["leader"]["total_fitness"], 0.0)

    def test_custom_optimizer_plugin_registration(self) -> None:
        @register_optimizer("custom_plugin_test")
        class CustomPluginOptimizer(BaseDivisionOptimizer):
            ALGORITHM_NAME = "Custom Plugin Test Optimizer"

            def initialize_population(self) -> None:
                pass

            def step(self, iteration: int) -> Dict[str, Any]:
                scale = float(self.config.get_param("custom_step_scale", 0.5))
                vec = [scale for _ in range(45)]
                genome = DivisionGenome.from_vector(vec, self.unit_pool, self.config, rng=self.rng)
                cand = self.evaluate_genome(genome, vector=vec, iteration=iteration)
                self.population = [cand]
                return {"custom_search": 1}

        res = run_optimization(
            method="custom_plugin_test",
            year="1936",
            objective="best_overall",
            terrains=["Plains"],
            population_size=4,
            iterations=2,
            battles_per_evaluation=1,
            custom_step_scale=0.35,
        )
        self.assertEqual(res["method"], "custom_plugin_test")
        self.assertIsNotNone(res["best_division"])
        valid, violations = res["best_division"].validate_division_rules()
        self.assertTrue(valid, violations)


class TestDashboardLoggerAndCLI(unittest.TestCase):
    """Verifies LiveDashboardServer HTTP endpoints, TrainingTelemetryLogger, and CLI commands."""

    def test_live_dashboard_server_and_logger_integration(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            res = run_optimization(
                method="cso",
                year="1940",
                objective="best_overall",
                terrains=["Plains", "Mountain"],
                population_size=6,
                iterations=2,
                battles_per_evaluation=1,
                enable_dashboard=True,
                open_browser=False,
                enable_logging=True,
                log_dir=tmpdir,
            )
            self.assertIsNotNone(res["leader"])
            log_files = os.listdir(tmpdir)
            self.assertTrue(any(f.endswith(".jsonl") for f in log_files))
            self.assertTrue(any(f.endswith(".log") for f in log_files))

    def test_dashboard_http_endpoints_directly(self) -> None:
        cfg = OptimizationConfig(method="cso", year="1939", objective="bang_for_buck")
        server = LiveDashboardServer(open_browser=False, initial_config=cfg)
        url = server.start(open_browser=False)
        try:
            with urllib.request.urlopen(url + "/", timeout=3.0) as resp:
                html = resp.read().decode("utf-8")
                self.assertEqual(resp.status, 200)
                self.assertIn("HOI4", html)

            with urllib.request.urlopen(url + "/api/state", timeout=3.0) as resp:
                state = json.loads(resp.read().decode("utf-8"))
                self.assertEqual(resp.status, 200)
                self.assertEqual(state["year"], "1939")
                self.assertEqual(state["objective"], "bang_for_buck")
        finally:
            server.stop()

    def test_cli_units_and_battle_commands(self) -> None:
        proc_units = subprocess.run(
            [sys.executable, os.path.join(REPO_ROOT, "cli.py"), "units", "--year", "1939", "--category", "regimental_support"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Fire Support Team", proc_units.stdout)
        self.assertIn("Motorized Fire Support Team", proc_units.stdout)

        proc_battle = subprocess.run(
            [
                sys.executable,
                os.path.join(REPO_ROOT, "cli.py"),
                "battle",
                "--attacker",
                "medium_armor_1940",
                "--defender",
                "standard_infantry_1936",
                "--terrain",
                "Plains",
                "--trials",
                "3",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("OVERALL ATTACKER WIN RATE", proc_battle.stdout)

        with tempfile.TemporaryDirectory() as tmpdir:
            proc_compare = subprocess.run(
                [
                    sys.executable,
                    os.path.join(REPO_ROOT, "cli.py"),
                    "compare",
                    "--methods",
                    "cso,ga",
                    "--year",
                    "1939",
                    "--objective",
                    "bang_for_buck",
                    "--terrains",
                    "Plains",
                    "--population",
                    "4",
                    "--iterations",
                    "2",
                    "--battles-per-eval",
                    "1",
                    "--no-browser",
                    "--log-dir",
                    tmpdir,
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertIn("HEAD-TO-HEAD ALGORITHM COMPARISON", proc_compare.stdout)


class TestDoctrinesAndTankDesigner(unittest.TestCase):
    """Verifies official HOI4 v1.19.4.2 Land Doctrines and NSB Tank Designer modules."""

    def test_v119_land_doctrines_modifiers_and_combat_width(self) -> None:
        all_subdocs = doctrines.list_all_subdoctrines()
        self.assertGreaterEqual(len(all_subdocs), 34)

        b_45 = unit_database.All_Battalions["1945"]
        inf_base = b_45["Infantry"]
        art_base = b_45["Artillery"]

        # Mass Assault + Large Unit Tactics: Infantry combat width 2.0 - 0.4 = 1.6
        inf_ma = doctrines.apply_doctrine_to_battalion(
            inf_base,
            "mass_assault",
            year="1945",
            mastery_level=1.0,
        )
        self.assertAlmostEqual(inf_ma.base_stats.combat_width, 1.6)
        self.assertGreater(inf_ma.base_stats.organization, inf_base.base_stats.organization)

        # Superior Firepower (Dispersed Support -> fire_concentration): Artillery combat width 3.0 - 0.8 = 2.2
        art_sf = doctrines.apply_doctrine_to_battalion(
            art_base,
            "superior_firepower_dispersed_support",
            year="1945",
            mastery_level=1.0,
        )
        self.assertAlmostEqual(art_sf.base_stats.combat_width, 2.2)
        self.assertGreater(art_sf.base_stats.soft_attack, art_base.base_stats.soft_attack)

        # Superior Firepower (Integrated Support): Support Artillery ORG and soft attack boost
        sup_art_base = unit_database.Support_Companies["1945"]["Support Artillery"]
        sup_art_sf = doctrines.apply_doctrine_to_support(
            sup_art_base,
            "superior_firepower_integrated_support",
            year="1945",
            mastery_level=1.0,
        )
        self.assertGreater(sup_art_sf.base_stats.organization, sup_art_base.base_stats.organization)
        self.assertGreater(sup_art_sf.base_stats.soft_attack, sup_art_base.base_stats.soft_attack)

        # Custom composite doctrine string: "<grand>:<inf>,<combat_support>,<armor>,<operations>"
        custom_doc = "new_mobile_warfare:mobile_infantry,mobile_recon_and_assault,armored_spearhead,mission_type_tactics"
        mt_base = b_45["Medium Tank"]
        mt_mw = doctrines.apply_doctrine_to_battalion(mt_base, custom_doc, year="1945", mastery_level=1.0)
        self.assertGreater(mt_mw.base_stats.breakthrough, mt_base.base_stats.breakthrough)
        self.assertGreater(mt_mw.base_stats.organization, mt_base.base_stats.organization)

    def test_nsb_tank_designer_blueprints_and_unit_conversion(self) -> None:
        bp = tank_designer.optimize_tank_blueprint(
            chassis_class="medium",
            role="tank",
            year="1945",
            objective="nsb_meta_soft_attack",
        )
        valid, errors = bp.validate_blueprint()
        self.assertTrue(valid, f"Blueprint validation failed: {errors}")

        eq_stats = bp.calculate_equipment_stats()
        self.assertGreater(eq_stats["soft_attack"], 30.0)
        self.assertGreater(eq_stats["breakthrough"], 40.0)
        self.assertGreaterEqual(eq_stats["maximum_speed"], 4.0)

        med_bat = tank_designer.blueprint_to_unit(bp, "medium_armor", year="1945")
        self.assertIsInstance(med_bat, Battalion)
        self.assertEqual(med_bat.name, "Medium Tank")
        self.assertAlmostEqual(med_bat.base_stats.combat_width, 2.0)

    def test_optimizer_with_doctrine_and_tank_designer_1945(self) -> None:
        res = run_optimization(
            method="cso",
            year="1945",
            doctrine="superior_firepower",
            tank_design_mode="nsb_auto_optimize",
            objective="best_overall",
            terrains=["Plains", "Urban"],
            population_size=6,
            iterations=2,
            battles_per_evaluation=1,
            random_seed=42,
        )
        self.assertEqual(res["config"]["year"], "1945")
        self.assertEqual(res["config"]["doctrine"], "superior_firepower")
        self.assertEqual(res["config"]["tank_design_mode"], "nsb_auto_optimize")
        best_div = res["best_division"]
        valid, violations = best_div.validate_division_rules()
        self.assertTrue(valid, violations)

        # Verify CLI --list-doctrines and --design-tank flags
        proc_docs = subprocess.run(
            [sys.executable, os.path.join(REPO_ROOT, "cli.py"), "units", "--list-doctrines"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("superior_firepower", proc_docs.stdout)
        self.assertIn("large_unit_tactics", proc_docs.stdout)

        proc_tanks = subprocess.run(
            [sys.executable, os.path.join(REPO_ROOT, "cli.py"), "units", "--year", "1945", "--design-tank"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("NSB TANK DESIGNER BLUEPRINTS", proc_tanks.stdout)


if __name__ == "__main__":
    unittest.main()

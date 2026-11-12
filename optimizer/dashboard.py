"""
Automatic Live Training Web Dashboard for the HOI4 v1.19.4.2 Division Optimizer.

This module implements `LiveDashboardServer`, a zero-external-dependency, thread-safe
HTTP server built on Python's standard `http.server` (`ThreadingHTTPServer`),
`threading`, `json`, and `webbrowser` modules.

Whenever division optimization starts, `LiveDashboardServer`:
1. Binds to an available local port on `127.0.0.1` (defaulting to `8765` or the next
   free port, or OS-assigned port `0`) in a daemon background thread.
2. Automatically opens the user's web browser (`webbrowser.open(url)`) when
   `open_browser=True` (can be disabled via `open_browser=False` or `--no-browser`).
3. Serves a responsive, military/strategic dark-themed single-page web application at
   `GET /` that polls `GET /api/state` every 500ms.
4. Updates its internal state thread-safely after every optimizer iteration via
   `update_state(snapshot)` (aliased as `on_step` and `__call__` for direct use with
   `BaseDivisionOptimizer.on_step_callback`).

Dashboard Visual Components
---------------------------
1. **Training Status Header**:
   - Active Optimization Method (e.g., `Cat Swarm Optimization (CSO — PMC7204373)`,
     `Genetic Algorithm`, `Particle Swarm Optimization`, `Simulated Annealing`,
     `Random Search`), Target Year (`1934` / `1936` / `1939` / `1940` / `1945`),
     Objective (`Best Overall`, `Bang for Buck`, `Offensive Breakthrough`,
     `Defensive Wall`, `Terrain Specialist`), Iteration Progress Bar, Elapsed Time,
     CSO Seeking/Tracing Mode distribution, and Status (`TRAINING` / `COMPLETED`).
2. **Current #1 Leader Division Card**:
   - Division Name, Total Fitness Score, Overall Win Rate (%), Attacker Win Rate (%),
     Defender Win Rate (%), Bang-for-Buck Score, IC Cost, Combat Width, Manpower,
     Supply Use, Organization, Max HP, Soft Attack, Hard Attack, Defense, Breakthrough,
     Armor, Piercing, Hardness, Entrenchment, Recon, Initiative, Air Attack, Recovery Rate.
3. **Interactive HOI4 v1.19 Division Designer Grid**:
   - 5 **Divisional Support** slots on the left, the 5x5 **Line Brigade / Regiment
     Columns** in the center (color-coded by battalion group: `infantry`,
     `combat_support`, `mobile`, `mobile_combat_support`, `armor`,
     `armor_combat_support`), and the new v1.19 **Regimental Support** row underneath
     the 5 brigade columns.
4. **Terrain Win-Rate Breakdown**:
   - Progress bars displaying the Leader division's win rate and terrain modifiers
     across `Plains`, `Forest`, `Hills`, `Jungle`, `Mountain`, `Marsh`, `Desert`, and `Urban`.
5. **Live Fitness Convergence Chart (SVG)**:
   - Real-time line chart plotting Best Fitness and Swarm Average Fitness across
     iterations (plus multi-algorithm overlays during head-to-head `compare` runs).
6. **Top Candidates / Hall of Fame Leaderboard Table**:
   - Displays the top 5–10 divisions discovered so far with fitness, win rate, IC cost,
     bang-for-buck ratio, combat width, and composition summary.
"""

from __future__ import annotations

from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
import socket
import threading
import time
from typing import Any, Callable, Dict, List, Optional
import webbrowser

from optimizer.logger import (
    METHOD_DISPLAY_NAMES,
    OBJECTIVE_DISPLAY_NAMES,
    STANDARD_TERRAINS,
    extract_division_summary,
    get_logger,
    serialize_for_telemetry,
)


# ==============================================================================
# SINGLE-PAGE MILITARY / STRATEGIC LIVE DASHBOARD HTML TEMPLATE
# ==============================================================================

DASHBOARD_HTML: str = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HOI4 v1.19.4.2 Division Optimizer — Live Strategic Command Dashboard</title>
  <style>
    :root {
      --bg-primary: #090d14;
      --bg-secondary: #111827;
      --bg-tertiary: #1a2333;
      --bg-card-hover: #212d42;
      --border-color: #28354a;
      --border-highlight: #3b4f6b;
      --text-primary: #f1f5f9;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent-gold: #f59e0b;
      --accent-gold-dim: rgba(245, 158, 11, 0.16);
      --accent-emerald: #10b981;
      --accent-emerald-dim: rgba(16, 185, 129, 0.16);
      --accent-cyan: #06b6d4;
      --accent-cyan-dim: rgba(6, 182, 212, 0.16);
      --accent-crimson: #ef4444;
      --accent-purple: #a855f7;

      /* HOI4 Battalion Group Color Coding */
      --grp-infantry-bg: rgba(16, 185, 129, 0.18);
      --grp-infantry-border: #10b981;
      --grp-combat-support-bg: rgba(239, 68, 68, 0.18);
      --grp-combat-support-border: #ef4444;
      --grp-mobile-bg: rgba(6, 182, 212, 0.18);
      --grp-mobile-border: #06b6d4;
      --grp-mobile-support-bg: rgba(59, 130, 246, 0.18);
      --grp-mobile-support-border: #3b82f6;
      --grp-armor-bg: rgba(245, 158, 11, 0.20);
      --grp-armor-border: #f59e0b;
      --grp-armor-support-bg: rgba(168, 85, 247, 0.20);
      --grp-armor-support-border: #a855f7;
      --grp-support-bg: rgba(148, 163, 184, 0.16);
      --grp-support-border: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-primary);
      background-image:
        radial-gradient(circle at 15% 10%, rgba(245, 158, 11, 0.05) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(6, 182, 212, 0.05) 0%, transparent 45%);
      color: var(--text-primary);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      line-height: 1.45;
      padding: 18px 24px 36px;
      min-height: 100vh;
    }

    .mono {
      font-family: "JetBrains Mono", "Fira Code", "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }

    /* 1. TRAINING STATUS HEADER */
    .header-bar {
      background: linear-gradient(180deg, #151e2e 0%, #0f1623 100%);
      border: 1px solid var(--border-color);
      border-top: 3px solid var(--accent-gold);
      border-radius: 10px;
      padding: 16px 22px;
      margin-bottom: 18px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    }

    .header-top {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
    }

    .brand-title {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-insignia {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      background: var(--accent-gold-dim);
      border: 1px solid var(--accent-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      color: var(--accent-gold);
      font-size: 18px;
      letter-spacing: 0.5px;
    }

    .brand-text h1 {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 0.4px;
      color: var(--text-primary);
      text-transform: uppercase;
    }

    .brand-text p {
      font-size: 12px;
      color: var(--text-secondary);
    }

    .status-badges {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
    }

    .badge {
      padding: 5px 11px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: var(--bg-tertiary);
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }

    .badge-label {
      color: var(--text-secondary);
      font-weight: 500;
      font-size: 11px;
      text-transform: uppercase;
    }

    .badge-value {
      color: var(--text-primary);
    }

    .status-pill {
      padding: 6px 13px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .status-training {
      background: rgba(245, 158, 11, 0.18);
      color: #fbbf24;
      border: 1px solid #f59e0b;
    }

    .status-completed {
      background: rgba(16, 185, 129, 0.18);
      color: #34d399;
      border: 1px solid #10b981;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: currentColor;
      animation: pulse 1.2s infinite ease-in-out;
    }

    .status-completed .pulse-dot {
      animation: none;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.45); opacity: 0.45; }
    }

    .progress-row {
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 16px;
    }

    .progress-track {
      width: 100%;
      height: 10px;
      background: #090d14;
      border: 1px solid var(--border-color);
      border-radius: 999px;
      overflow: hidden;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #f59e0b 0%, #10b981 100%);
      transition: width 0.35s ease;
    }

    .progress-caption {
      font-size: 12px;
      color: var(--text-secondary);
      white-space: nowrap;
    }

    /* MAIN GRID LAYOUT */
    .dashboard-grid {
      display: grid;
      grid-template-columns: 1.05fr 1.25fr;
      gap: 18px;
      margin-bottom: 18px;
    }

    @media (max-width: 1200px) {
      .dashboard-grid {
        grid-template-columns: 1fr;
      }
    }

    .card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px 20px;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 11px;
      margin-bottom: 14px;
      gap: 10px;
    }

    .card-title {
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--accent-gold);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card-subtitle {
      font-size: 12px;
      color: var(--text-secondary);
    }

    /* 2. LEADER DIVISION CARD */
    .leader-banner {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-highlight);
      border-left: 4px solid var(--accent-gold);
      border-radius: 8px;
      padding: 12px 15px;
      margin-bottom: 14px;
    }

    .leader-name-row {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 4px;
    }

    .leader-name {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-primary);
    }

    .leader-comp {
      font-size: 12px;
      color: var(--accent-cyan);
      word-break: break-word;
    }

    .kpi-row {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
      margin-bottom: 14px;
    }

    @media (max-width: 720px) {
      .kpi-row {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .kpi-box {
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 12px;
      text-align: center;
    }

    .kpi-box.highlight {
      border-color: var(--accent-gold);
      background: var(--accent-gold-dim);
    }

    .kpi-label {
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-secondary);
      margin-bottom: 4px;
    }

    .kpi-val {
      font-size: 18px;
      font-weight: 700;
      color: var(--text-primary);
    }

    .kpi-box.highlight .kpi-val {
      color: var(--accent-gold);
    }

    .stats-matrix {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }

    @media (max-width: 680px) {
      .stats-matrix {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .stat-cell {
      background: #0d131f;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 7px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
    }

    .stat-name {
      color: var(--text-secondary);
    }

    .stat-num {
      font-weight: 600;
      color: var(--text-primary);
    }

    /* 3. INTERACTIVE 5x5 DIVISION DESIGNER GRID */
    .designer-wrapper {
      overflow-x: auto;
    }

    .designer-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 6px;
      min-width: 640px;
    }

    .designer-table th {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 7px 8px;
      background: #0d131f;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: var(--text-secondary);
      text-align: center;
    }

    .designer-table th.sup-header {
      border-color: var(--grp-support-border);
      color: #cbd5e1;
      width: 17%;
    }

    .col-grp-tag {
      display: block;
      font-size: 9px;
      color: var(--accent-gold);
      margin-top: 2px;
      font-weight: 600;
    }

    .unit-slot {
      height: 44px;
      border-radius: 6px;
      padding: 5px 8px;
      font-size: 11px;
      font-weight: 600;
      border: 1px solid var(--border-color);
      background: #0b101b;
      color: var(--text-muted);
      vertical-align: middle;
      text-align: center;
      transition: transform 0.12s ease, border-color 0.12s ease;
    }

    .unit-slot.filled {
      color: var(--text-primary);
    }

    .unit-slot.grp-infantry {
      background: var(--grp-infantry-bg);
      border-color: var(--grp-infantry-border);
    }

    .unit-slot.grp-combat_support {
      background: var(--grp-combat-support-bg);
      border-color: var(--grp-combat-support-border);
    }

    .unit-slot.grp-mobile {
      background: var(--grp-mobile-bg);
      border-color: var(--grp-mobile-border);
    }

    .unit-slot.grp-mobile_combat_support {
      background: var(--grp-mobile-support-bg);
      border-color: var(--grp-mobile-support-border);
    }

    .unit-slot.grp-armor {
      background: var(--grp-armor-bg);
      border-color: var(--grp-armor-border);
    }

    .unit-slot.grp-armor_combat_support {
      background: var(--grp-armor-support-bg);
      border-color: var(--grp-armor-support-border);
    }

    .unit-slot.grp-support {
      background: var(--grp-support-bg);
      border-color: var(--grp-support-border);
    }

    .unit-slot.reg-support-slot {
      border-style: dashed;
      background: rgba(168, 85, 247, 0.08);
    }

    .unit-slot.reg-support-slot.filled {
      border-style: solid;
      background: var(--grp-armor-support-bg);
      border-color: var(--grp-armor-support-border);
    }

    .slot-subtag {
      display: block;
      font-size: 9px;
      font-weight: 500;
      opacity: 0.78;
      margin-top: 2px;
    }

    .legend-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px solid var(--border-color);
      font-size: 11px;
      color: var(--text-secondary);
    }

    .legend-item {
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .legend-swatch {
      width: 10px;
      height: 10px;
      border-radius: 3px;
      display: inline-block;
    }

    /* 4. TERRAIN WIN-RATE BREAKDOWN & 5. CONVERGENCE CHART */
    .terrain-list {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }

    @media (max-width: 680px) {
      .terrain-list {
        grid-template-columns: 1fr;
      }
    }

    .terrain-item {
      background: #0d131f;
      border: 1px solid var(--border-color);
      border-radius: 7px;
      padding: 9px 12px;
    }

    .terrain-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      margin-bottom: 6px;
    }

    .terrain-name {
      font-weight: 600;
      color: var(--text-primary);
    }

    .terrain-mods {
      font-size: 10px;
      color: var(--text-secondary);
      margin-left: 6px;
    }

    .terrain-track {
      width: 100%;
      height: 8px;
      background: #070a10;
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid #1e293b;
    }

    .terrain-fill {
      height: 100%;
      width: 0%;
      border-radius: 999px;
      transition: width 0.3s ease;
    }

    /* SVG CONVERGENCE CHART */
    .chart-container {
      width: 100%;
      height: 250px;
      background: #0b101b;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px;
      position: relative;
    }

    .chart-svg {
      width: 100%;
      height: 100%;
      overflow: visible;
    }

    /* 6. HALL OF FAME LEADERBOARD TABLE */
    .table-wrapper {
      overflow-x: auto;
    }

    .hof-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }

    .hof-table th {
      text-align: left;
      padding: 10px 12px;
      background: #0d131f;
      color: var(--text-secondary);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      border-bottom: 1px solid var(--border-color);
    }

    .hof-table td {
      padding: 10px 12px;
      border-bottom: 1px solid #1e293b;
      color: var(--text-primary);
    }

    .hof-table tbody tr {
      cursor: pointer;
      transition: background 0.15s ease;
    }

    .hof-table tbody tr:hover {
      background: var(--bg-card-hover);
    }

    .hof-table tbody tr.active-row {
      background: rgba(245, 158, 11, 0.12);
    }

    .rank-pill {
      display: inline-block;
      min-width: 26px;
      padding: 2px 7px;
      border-radius: 5px;
      text-align: center;
      font-weight: 700;
      font-size: 11px;
      background: var(--bg-tertiary);
      color: var(--text-secondary);
    }

    .rank-1 {
      background: rgba(245, 158, 11, 0.25);
      color: #fbbf24;
      border: 1px solid #f59e0b;
    }

    .btn-follow {
      background: var(--bg-tertiary);
      color: var(--text-primary);
      border: 1px solid var(--accent-gold);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
    }

    .btn-follow:hover {
      background: var(--accent-gold-dim);
    }
  </style>
</head>
<body>

  <!-- 1. TRAINING STATUS HEADER -->
  <header class="header-bar">
    <div class="header-top">
      <div class="brand-title">
        <div class="brand-insignia">IV</div>
        <div class="brand-text">
          <h1>HOI4 v1.19.4.2 Division Optimizer — Live Telemetry</h1>
          <p id="hdr-method-full">Algorithm-Agnostic Division Optimization &amp; Multi-Terrain Combat Simulator</p>
        </div>
      </div>

      <div class="status-badges">
        <div class="badge">
          <span class="badge-label">Year</span>
          <span class="badge-value mono" id="hdr-year">1940</span>
        </div>
        <div class="badge">
          <span class="badge-label">Objective</span>
          <span class="badge-value" id="hdr-objective">Best Overall</span>
        </div>
        <div class="badge" id="hdr-modes-badge" style="display: none;">
          <span class="badge-label">Mode / Telemetry</span>
          <span class="badge-value mono" id="hdr-modes"></span>
        </div>
        <div class="badge">
          <span class="badge-label">Evaluations</span>
          <span class="badge-value mono" id="hdr-evals">0</span>
        </div>
        <div class="badge">
          <span class="badge-label">Elapsed</span>
          <span class="badge-value mono" id="hdr-elapsed">0.0s</span>
        </div>
        <div class="status-pill status-training" id="hdr-status-pill">
          <span class="pulse-dot"></span>
          <span id="hdr-status-text">TRAINING</span>
        </div>
      </div>
    </div>

    <div class="progress-row">
      <div class="progress-track">
        <div class="progress-fill" id="hdr-progress-fill"></div>
      </div>
      <div class="progress-caption mono" id="hdr-progress-text">Iteration 0 / 0 (0%)</div>
    </div>
  </header>

  <!-- TOP ROW: 2. CURRENT #1 LEADER CARD + 3. 5x5 DIVISION DESIGNER GRID -->
  <section class="dashboard-grid">
    <!-- 2. CURRENT #1 LEADER DIVISION CARD -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <span id="leader-card-title">#1 Current Leader Division</span>
        </div>
        <div>
          <button class="btn-follow" id="btn-reset-leader" style="display:none;" onclick="selectCandidateIndex(-1)">
            Return to Live #1 Leader
          </button>
          <span class="card-subtitle mono" id="leader-valid-tag">VALID v1.19 TEMPLATE</span>
        </div>
      </div>

      <div class="leader-banner">
        <div class="leader-name-row">
          <div class="leader-name" id="ldr-name">Awaiting First Iteration...</div>
          <div class="mono" style="font-size:12px; color:var(--accent-gold);" id="ldr-method-tag"></div>
        </div>
        <div class="leader-comp mono" id="ldr-comp">Initializing swarm population...</div>
      </div>

      <div class="kpi-row">
        <div class="kpi-box highlight">
          <div class="kpi-label">Total Fitness</div>
          <div class="kpi-val mono" id="kpi-fitness">0.000</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-label">Overall Win %</div>
          <div class="kpi-val mono" id="kpi-win">0.0%</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-label">Attacker Win %</div>
          <div class="kpi-val mono" id="kpi-att-win">0.0%</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-label">Defender Win %</div>
          <div class="kpi-val mono" id="kpi-def-win">0.0%</div>
        </div>
        <div class="kpi-box">
          <div class="kpi-label">Bang / Buck</div>
          <div class="kpi-val mono" id="kpi-bfb">0.00</div>
        </div>
      </div>

      <div class="stats-matrix">
        <div class="stat-cell"><span class="stat-name">IC Cost</span><span class="stat-num mono" id="st-ic">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Combat Width</span><span class="stat-num mono" id="st-width">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Organization</span><span class="stat-num mono" id="st-org">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Max HP</span><span class="stat-num mono" id="st-hp">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Soft Attack</span><span class="stat-num mono" id="st-sa">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Hard Attack</span><span class="stat-num mono" id="st-ha">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Defense</span><span class="stat-num mono" id="st-def">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Breakthrough</span><span class="stat-num mono" id="st-brk">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Armor</span><span class="stat-num mono" id="st-arm">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Piercing</span><span class="stat-num mono" id="st-prc">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Hardness</span><span class="stat-num mono" id="st-hrd">0.0%</span></div>
        <div class="stat-cell"><span class="stat-name">Manpower</span><span class="stat-num mono" id="st-mp">0</span></div>
        <div class="stat-cell"><span class="stat-name">Supply Use</span><span class="stat-num mono" id="st-sup">0.00</span></div>
        <div class="stat-cell"><span class="stat-name">Entrenchment</span><span class="stat-num mono" id="st-ent">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Recon</span><span class="stat-num mono" id="st-rec">0.0</span></div>
        <div class="stat-cell"><span class="stat-name">Initiative</span><span class="stat-num mono" id="st-ini">0.00</span></div>
      </div>
    </div>

    <!-- 3. INTERACTIVE HOI4 v1.19 DIVISION DESIGNER GRID -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">HOI4 v1.19.4.2 Division Designer Grid (5x5 Regiments + Support)</div>
        <div class="card-subtitle">Brigade Group Column Locks &amp; Regimental Support</div>
      </div>

      <div class="designer-wrapper">
        <table class="designer-table">
          <thead>
            <tr>
              <th class="sup-header">Divisional Support<span class="col-grp-tag">Max 5 Unique Types</span></th>
              <th id="col-hdr-0">Regiment 1<span class="col-grp-tag" id="col-grp-0">Empty</span></th>
              <th id="col-hdr-1">Regiment 2<span class="col-grp-tag" id="col-grp-1">Empty</span></th>
              <th id="col-hdr-2">Regiment 3<span class="col-grp-tag" id="col-grp-2">Empty</span></th>
              <th id="col-hdr-3">Regiment 4<span class="col-grp-tag" id="col-grp-3">Empty</span></th>
              <th id="col-hdr-4">Regiment 5<span class="col-grp-tag" id="col-grp-4">Empty</span></th>
            </tr>
          </thead>
          <tbody id="designer-grid-body">
            <!-- Populated dynamically by JS -->
          </tbody>
        </table>
      </div>

      <div class="legend-bar">
        <span class="legend-item"><span class="legend-swatch" style="background:#10b981;"></span>Infantry</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#ef4444;"></span>Combat Support</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#06b6d4;"></span>Mobile</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#3b82f6;"></span>Mobile Support</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#f59e0b;"></span>Armor</span>
        <span class="legend-item"><span class="legend-swatch" style="background:#a855f7;"></span>Armor Support / v1.19 Regimental</span>
      </div>
    </div>
  </section>

  <!-- MIDDLE ROW: 4. TERRAIN WIN-RATE BREAKDOWN + 5. CONVERGENCE CHART -->
  <section class="dashboard-grid">
    <!-- 4. TERRAIN WIN-RATE BREAKDOWN -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">Multi-Terrain Win-Rate Breakdown</div>
        <div class="card-subtitle">Attacker + Defender Combined Trials Across 8 Terrains</div>
      </div>
      <div class="terrain-list" id="terrain-bars-container">
        <!-- Populated dynamically by JS -->
      </div>
    </div>

    <!-- 5. LIVE FITNESS CONVERGENCE CHART -->
    <div class="card">
      <div class="card-header">
        <div class="card-title">Live Fitness Convergence Curve</div>
        <div class="card-subtitle">
          <span style="color:#f59e0b; font-weight:700;">&#9644; Best Fitness</span> &nbsp;&nbsp;
          <span style="color:#06b6d4; font-weight:700;">&#9645; Population Mean</span>
        </div>
      </div>
      <div class="chart-container">
        <svg class="chart-svg" id="convergence-svg" viewBox="0 0 600 220" preserveAspectRatio="none"></svg>
      </div>
    </div>
  </section>

  <!-- BOTTOM ROW: 6. HALL OF FAME TOP CANDIDATES LEADERBOARD -->
  <section class="card">
    <div class="card-header">
      <div class="card-title">Hall of Fame — Top Candidate Divisions Discovered</div>
      <div class="card-subtitle">Click any row to inspect its 5x5 Regiment Grid &amp; Combat Statistics</div>
    </div>
    <div class="table-wrapper">
      <table class="hof-table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Division Template</th>
            <th>Fitness</th>
            <th>Overall Win %</th>
            <th>Att / Def Win %</th>
            <th>IC Cost</th>
            <th>Bang/Buck</th>
            <th>Width</th>
            <th>ORG</th>
            <th>SA / HA</th>
            <th>Armor / Piercing</th>
            <th>Composition Summary</th>
          </tr>
        </thead>
        <tbody id="hof-tbody">
          <!-- Populated dynamically by JS -->
        </tbody>
      </table>
    </div>
  </section>

  <script>
    let latestState = null;
    let selectedCandidateIdx = -1; // -1 means follow live #1 leader

    function selectCandidateIndex(idx) {
      selectedCandidateIdx = idx;
      const resetBtn = document.getElementById("btn-reset-leader");
      const titleEl = document.getElementById("leader-card-title");
      if (idx === -1) {
        resetBtn.style.display = "none";
        titleEl.textContent = "#1 Current Leader Division";
      } else {
        resetBtn.style.display = "inline-block";
        titleEl.textContent = "Inspecting Hall of Fame Candidate #" + (idx + 1);
      }
      if (latestState) {
        renderDashboard(latestState);
      }
    }

    function escapeHtml(str) {
      if (str === null || str === undefined) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    function winRateColor(pct) {
      if (pct >= 70) return "#10b981";
      if (pct >= 50) return "#f59e0b";
      return "#ef4444";
    }

    function renderDesignerGrid(divSummary) {
      const grid = (divSummary && divSummary.grid) ? divSummary.grid : {
        support: [],
        regiments: [[], [], [], [], []],
        column_groups: [null, null, null, null, null],
        regimental_support: [null, null, null, null, null]
      };

      for (let c = 0; c < 5; c++) {
        const grp = (grid.column_groups && grid.column_groups[c]) ? grid.column_groups[c] : null;
        const grpEl = document.getElementById("col-grp-" + c);
        if (grpEl) {
          grpEl.textContent = grp ? grp.replace(/_/g, " ") : "Empty";
        }
      }

      const tbody = document.getElementById("designer-grid-body");
      let html = "";

      for (let r = 0; r < 5; r++) {
        html += "<tr>";
        // Left column: Divisional Support slot r
        const supName = (grid.support && grid.support[r]) ? grid.support[r] : null;
        if (supName) {
          html += `<td class="unit-slot filled grp-support">${escapeHtml(supName)}<span class="slot-subtag">Divisional Support</span></td>`;
        } else {
          html += `<td class="unit-slot">Support Slot ${r + 1}</td>`;
        }

        // 5 Regiment columns
        for (let c = 0; c < 5; c++) {
          const colList = (grid.regiments && grid.regiments[c]) ? grid.regiments[c] : [];
          const cell = (r < colList.length) ? colList[r] : null;
          if (cell && cell.name) {
            const grpClass = "grp-" + (cell.group || "infantry");
            const grpLabel = (cell.group || "infantry").replace(/_/g, " ");
            html += `<td class="unit-slot filled ${escapeHtml(grpClass)}">${escapeHtml(cell.name)}<span class="slot-subtag">${escapeHtml(grpLabel)}</span></td>`;
          } else {
            html += `<td class="unit-slot">&mdash;</td>`;
          }
        }
        html += "</tr>";
      }

      // 6th row: HOI4 v1.19 Regimental Support Row
      html += "<tr>";
      html += `<td class="unit-slot reg-support-slot" style="color:#c084fc; font-weight:700;">v1.19 Regimental Support<span class="slot-subtag">Unlocks at &ge;3 Battalions</span></td>`;
      for (let c = 0; c < 5; c++) {
        const colList = (grid.regiments && grid.regiments[c]) ? grid.regiments[c] : [];
        const regSup = (grid.regimental_support && grid.regimental_support[c]) ? grid.regimental_support[c] : null;
        const unlocked = colList.length >= 3;
        if (regSup) {
          html += `<td class="unit-slot reg-support-slot filled">${escapeHtml(regSup)}<span class="slot-subtag">Regimental Support</span></td>`;
        } else if (unlocked) {
          html += `<td class="unit-slot reg-support-slot" style="color:#94a3b8;">Unlocked (Empty)<span class="slot-subtag">${colList.length}/5 Battalions</span></td>`;
        } else {
          html += `<td class="unit-slot reg-support-slot">Locked (${colList.length}/3 Bats)</td>`;
        }
      }
      html += "</tr>";
      tbody.innerHTML = html;
    }

    function renderTerrainBreakdown(divSummary) {
      const container = document.getElementById("terrain-bars-container");
      const twr = (divSummary && divSummary.terrain_win_rates) ? divSummary.terrain_win_rates : {};
      const tmods = (divSummary && divSummary.terrain_modifiers) ? divSummary.terrain_modifiers : {};
      const terrains = ["Plains", "Forest", "Hills", "Jungle", "Mountain", "Marsh", "Desert", "Urban"];

      let html = "";
      for (const tName of terrains) {
        const wr = (twr[tName] !== undefined) ? Number(twr[tName]) * 100.0 : 0.0;
        const clamped = Math.max(0.0, Math.min(100.0, wr));
        const color = winRateColor(clamped);
        let modText = "";
        if (tmods[tName]) {
          const attMod = Math.round((Number(tmods[tName].attack || 0) * 100));
          const defMod = Math.round((Number(tmods[tName].defense || 0) * 100));
          const attSign = attMod >= 0 ? "+" : "";
          const defSign = defMod >= 0 ? "+" : "";
          modText = `Att ${attSign}${attMod}% / Def ${defSign}${defMod}%`;
        }
        html += `
          <div class="terrain-item">
            <div class="terrain-top">
              <div>
                <span class="terrain-name">${escapeHtml(tName)}</span>
                <span class="terrain-mods mono">${escapeHtml(modText)}</span>
              </div>
              <span class="mono" style="font-weight:700; color:${color};">${clamped.toFixed(1)}%</span>
            </div>
            <div class="terrain-track">
              <div class="terrain-fill" style="width:${clamped.toFixed(1)}%; background:${color};"></div>
            </div>
          </div>
        `;
      }
      container.innerHTML = html;
    }

    function renderConvergenceChart(history) {
      const svg = document.getElementById("convergence-svg");
      if (!history || history.length === 0) {
        svg.innerHTML = `<text x="300" y="115" text-anchor="middle" fill="#64748b" font-size="13">Waiting for iteration telemetry...</text>`;
        return;
      }

      const W = 600, H = 220;
      const padL = 48, padR = 18, padT = 16, padB = 28;
      const plotW = W - padL - padR;
      const plotH = H - padT - padB;

      const bestVals = history.map(d => Number(d.best_fitness || 0));
      const meanVals = history.map(d => Number(d.mean_fitness !== undefined ? d.mean_fitness : (d.avg_fitness || 0)));
      const allVals = bestVals.concat(meanVals);

      let minY = Math.min(...allVals);
      let maxY = Math.max(...allVals);
      if (maxY - minY < 1e-4) {
        minY = Math.max(0, minY - 0.05);
        maxY = maxY + 0.05;
      } else {
        const margin = (maxY - minY) * 0.1;
        minY = Math.max(0, minY - margin);
        maxY = maxY + margin;
      }

      function xCoord(idx) {
        if (history.length <= 1) return padL + plotW / 2;
        return padL + (idx / (history.length - 1)) * plotW;
      }

      function yCoord(val) {
        return padT + plotH - ((val - minY) / (maxY - minY)) * plotH;
      }

      let svgContent = "";
      // Horizontal grid lines
      for (let g = 0; g <= 4; g++) {
        const yVal = minY + (g / 4) * (maxY - minY);
        const yPx = yCoord(yVal);
        svgContent += `<line x1="${padL}" y1="${yPx.toFixed(1)}" x2="${W - padR}" y2="${yPx.toFixed(1)}" stroke="#1e293b" stroke-width="1" />`;
        svgContent += `<text x="${padL - 6}" y="${(yPx + 4).toFixed(1)}" text-anchor="end" fill="#64748b" font-size="10" font-family="monospace">${yVal.toFixed(2)}</text>`;
      }

      // Mean polyline
      const meanPts = meanVals.map((v, i) => `${xCoord(i).toFixed(1)},${yCoord(v).toFixed(1)}`).join(" ");
      svgContent += `<polyline fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="5,4" points="${meanPts}" />`;

      // Best polyline + area fill
      const bestPts = bestVals.map((v, i) => `${xCoord(i).toFixed(1)},${yCoord(v).toFixed(1)}`).join(" ");
      const firstX = xCoord(0).toFixed(1);
      const lastX = xCoord(history.length - 1).toFixed(1);
      const baseLineY = (padT + plotH).toFixed(1);
      svgContent += `<polygon fill="rgba(245, 158, 11, 0.10)" points="${firstX},${baseLineY} ${bestPts} ${lastX},${baseLineY}" />`;
      svgContent += `<polyline fill="none" stroke="#f59e0b" stroke-width="2.6" points="${bestPts}" />`;

      // Endpoints
      bestVals.forEach((v, i) => {
        if (i === bestVals.length - 1 || history.length <= 20) {
          svgContent += `<circle cx="${xCoord(i).toFixed(1)}" cy="${yCoord(v).toFixed(1)}" r="3.5" fill="#f59e0b" />`;
        }
      });

      // X-axis labels
      const firstIter = history[0].iteration || 1;
      const lastIter = history[history.length - 1].iteration || history.length;
      svgContent += `<text x="${padL}" y="${H - 6}" text-anchor="start" fill="#64748b" font-size="10" font-family="monospace">Iter ${firstIter}</text>`;
      svgContent += `<text x="${W - padR}" y="${H - 6}" text-anchor="end" fill="#64748b" font-size="10" font-family="monospace">Iter ${lastIter}</text>`;

      svg.innerHTML = svgContent;
    }

    function renderLeaderboard(topCandidates) {
      const tbody = document.getElementById("hof-tbody");
      if (!topCandidates || topCandidates.length === 0) {
        tbody.innerHTML = `<tr><td colspan="12" style="text-align:center; color:#64748b; padding:18px;">No candidates evaluated yet...</td></tr>`;
        return;
      }

      let html = "";
      topCandidates.forEach((cand, idx) => {
        const st = cand.stats || {};
        const isSelected = (selectedCandidateIdx === idx) || (selectedCandidateIdx === -1 && idx === 0);
        const rowClass = isSelected ? "active-row" : "";
        const rankClass = idx === 0 ? "rank-pill rank-1" : "rank-pill";
        const winPct = (Number(cand.win_rate || 0) * 100).toFixed(1);
        const attPct = (Number(cand.attacker_win_rate || 0) * 100).toFixed(1);
        const defPct = (Number(cand.defender_win_rate || 0) * 100).toFixed(1);
        html += `
          <tr class="${rowClass}" onclick="selectCandidateIndex(${idx})">
            <td><span class="${rankClass}">#${idx + 1}</span></td>
            <td style="font-weight:600;">${escapeHtml(cand.name || "Candidate")}</td>
            <td class="mono" style="color:#f59e0b; font-weight:700;">${Number(cand.total_fitness || 0).toFixed(4)}</td>
            <td class="mono" style="color:${winRateColor(Number(winPct))}; font-weight:700;">${winPct}%</td>
            <td class="mono">${attPct}% / ${defPct}%</td>
            <td class="mono">${Number(st.ic_cost || 0).toFixed(0)}</td>
            <td class="mono">${Number(cand.bang_for_buck_score || 0).toFixed(3)}</td>
            <td class="mono">${Number(st.combat_width || 0).toFixed(0)}</td>
            <td class="mono">${Number(st.organization || 0).toFixed(1)}</td>
            <td class="mono">${Number(st.soft_attack || 0).toFixed(0)} / ${Number(st.hard_attack || 0).toFixed(0)}</td>
            <td class="mono">${Number(st.armor || 0).toFixed(1)} / ${Number(st.piercing || 0).toFixed(1)}</td>
            <td class="mono" style="font-size:11px; color:#94a3b8;">${escapeHtml(cand.composition_summary || "")}</td>
          </tr>
        `;
      });
      tbody.innerHTML = html;
    }

    function renderDashboard(state) {
      latestState = state;
      document.getElementById("hdr-method-full").textContent = state.method_display || state.algorithm_name || state.method || "Division Optimizer";
      document.getElementById("hdr-year").textContent = state.year || "1940";
      document.getElementById("hdr-objective").textContent = state.objective_display || state.objective || "Best Overall";
      document.getElementById("hdr-evals").textContent = `${state.total_evaluations || 0} (cache: ${state.cache_hits || 0})`;
      document.getElementById("hdr-elapsed").textContent = `${Number(state.elapsed_seconds || 0).toFixed(1)}s`;

      // Mode counts & algorithm-specific telemetry badge (algorithm-agnostic)
      const modesBadge = document.getElementById("hdr-modes-badge");
      const modeCounts = state.mode_counts || {};
      const algoMeta = state.algorithm_metadata || {};
      const customMetrics = state.custom_metrics || {};
      const telemetryParts = [];
      for (const [k, v] of Object.entries(modeCounts)) {
        telemetryParts.push(`${k}: ${v}`);
      }
      for (const [k, v] of Object.entries(algoMeta)) {
        if (typeof v !== "object") telemetryParts.push(`${k}: ${v}`);
      }
      for (const [k, v] of Object.entries(customMetrics)) {
        if (typeof v !== "object") telemetryParts.push(`${k}: ${v}`);
      }
      if (telemetryParts.length > 0) {
        modesBadge.style.display = "inline-flex";
        document.getElementById("hdr-modes").textContent = telemetryParts.join(" | ");
      } else {
        modesBadge.style.display = "none";
      }

      // Status pill
      const statusPill = document.getElementById("hdr-status-pill");
      const statusText = document.getElementById("hdr-status-text");
      const statusStr = (state.status || "TRAINING").toUpperCase();
      statusText.textContent = statusStr;
      if (statusStr === "COMPLETED") {
        statusPill.className = "status-pill status-completed";
      } else {
        statusPill.className = "status-pill status-training";
      }

      // Progress bar
      const iter = Number(state.iteration || 0);
      const totalIter = Math.max(1, Number(state.total_iterations || 1));
      const pct = Math.min(100, Math.round((iter / totalIter) * 100));
      document.getElementById("hdr-progress-fill").style.width = pct + "%";
      document.getElementById("hdr-progress-text").textContent = `Iteration ${iter} / ${totalIter} (${pct}%)`;

      // Active division to display on card & 5x5 grid
      const topList = state.top_candidates || [];
      let activeDiv = state.leader || {};
      if (selectedCandidateIdx >= 0 && selectedCandidateIdx < topList.length) {
        activeDiv = topList[selectedCandidateIdx];
      }

      const st = activeDiv.stats || {};
      document.getElementById("ldr-name").textContent = activeDiv.name || "Awaiting Evaluation...";
      document.getElementById("ldr-method-tag").textContent = activeDiv.method ? `[${activeDiv.method}]` : "";
      document.getElementById("ldr-comp").textContent = activeDiv.composition_summary || "";
      document.getElementById("kpi-fitness").textContent = Number(activeDiv.total_fitness || 0).toFixed(4);
      document.getElementById("kpi-win").textContent = (Number(activeDiv.win_rate || 0) * 100).toFixed(1) + "%";
      document.getElementById("kpi-att-win").textContent = (Number(activeDiv.attacker_win_rate || 0) * 100).toFixed(1) + "%";
      document.getElementById("kpi-def-win").textContent = (Number(activeDiv.defender_win_rate || 0) * 100).toFixed(1) + "%";
      document.getElementById("kpi-bfb").textContent = Number(activeDiv.bang_for_buck_score || 0).toFixed(3);

      document.getElementById("st-ic").textContent = Number(st.ic_cost || 0).toFixed(1);
      document.getElementById("st-width").textContent = Number(st.combat_width || 0).toFixed(1);
      document.getElementById("st-org").textContent = Number(st.organization || 0).toFixed(1);
      document.getElementById("st-hp").textContent = Number(st.max_hp || 0).toFixed(1);
      document.getElementById("st-sa").textContent = Number(st.soft_attack || 0).toFixed(1);
      document.getElementById("st-ha").textContent = Number(st.hard_attack || 0).toFixed(1);
      document.getElementById("st-def").textContent = Number(st.defense || 0).toFixed(1);
      document.getElementById("st-brk").textContent = Number(st.breakthrough || 0).toFixed(1);
      document.getElementById("st-arm").textContent = Number(st.armor || 0).toFixed(1);
      document.getElementById("st-prc").textContent = Number(st.piercing || 0).toFixed(1);
      document.getElementById("st-hrd").textContent = (Number(st.hardness || 0) * 100).toFixed(1) + "%";
      document.getElementById("st-mp").textContent = Number(st.manpower || 0).toFixed(0);
      document.getElementById("st-sup").textContent = Number(st.supply_use || 0).toFixed(2);
      document.getElementById("st-ent").textContent = Number(st.entrenchment || 0).toFixed(1);
      document.getElementById("st-rec").textContent = Number(st.recon || 0).toFixed(1);
      document.getElementById("st-ini").textContent = Number(st.initiative || 0).toFixed(2);

      renderDesignerGrid(activeDiv);
      renderTerrainBreakdown(activeDiv);
      renderConvergenceChart(state.fitness_history || []);
      renderLeaderboard(topList);
    }

    async function pollState() {
      try {
        const res = await fetch("/api/state", { cache: "no-store" });
        if (res.ok) {
          const data = await res.json();
          renderDashboard(data);
        }
      } catch (err) {
        // Server may be shutting down or restarting
      }
    }

    pollState();
    setInterval(pollState, 500);
  </script>
</body>
</html>
"""


# ==============================================================================
# LIVE DASHBOARD SERVER IMPLEMENTATION
# ==============================================================================

class LiveDashboardServer:
    """
    Zero-external-dependency, thread-safe live HTTP server that displays real-time
    HOI4 division optimization progress in the user's web browser.

    Usage Example
    -------------
    ```python
    dashboard = LiveDashboardServer(open_browser=True)
    url = dashboard.start()
    optimizer = create_optimizer(config, on_step_callback=dashboard.update_state)
    result = optimizer.run()
    dashboard.mark_completed(result)
    dashboard.stop()
    ```
    """

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 0,
        preferred_port: int = 8765,
        open_browser: bool = True,
        logger: Optional[logging.Logger] = None,
        initial_config: Any = None,
    ) -> None:
        """
        Initialize the live dashboard server.

        Parameters
        ----------
        host : str, default="127.0.0.1"
            Local interface address to bind.
        port : int, default=0
            Explicit port to bind. If `0`, tries `preferred_port` (`8765..8799`)
            first and falls back to an OS-assigned free port (`0`).
        preferred_port : int, default=8765
            Preferred starting port when `port == 0`.
        open_browser : bool, default=True
            Whether to automatically launch the user's web browser when `start()`
            is called. Set `False` for headless tests or `--no-browser` CLI runs.
        logger : Optional[logging.Logger], default=None
            Logger instance for server lifecycle messages.
        initial_config : Any, optional
            Optional `OptimizationConfig` or dict to seed initial metadata before
            iteration 1 completes.
        """
        self.host = host
        self.requested_port = port
        self.preferred_port = preferred_port
        self.open_browser = open_browser
        self.logger = logger or get_logger("hoi4_optimizer")

        self.port: int = 0
        self.url: str = ""
        self._server: Optional[ThreadingHTTPServer] = None
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        self._start_time = time.time()

        cfg_dict = serialize_for_telemetry(initial_config) if initial_config is not None else {}
        if not isinstance(cfg_dict, dict):
            cfg_dict = {}

        method_key = str(cfg_dict.get("method", "cso")).lower()
        obj_key = str(cfg_dict.get("objective", "best_overall")).lower()

        self._state: Dict[str, Any] = {
            "status": "TRAINING",
            "method": method_key,
            "method_display": METHOD_DISPLAY_NAMES.get(method_key, method_key.upper()),
            "algorithm_name": METHOD_DISPLAY_NAMES.get(method_key, method_key.upper()),
            "year": str(cfg_dict.get("year", "1940")),
            "objective": obj_key,
            "objective_display": OBJECTIVE_DISPLAY_NAMES.get(obj_key, obj_key),
            "iteration": 0,
            "total_iterations": int(cfg_dict.get("iterations", 30)),
            "elapsed_seconds": 0.0,
            "best_fitness": 0.0,
            "mean_fitness": 0.0,
            "leader": extract_division_summary(None),
            "top_candidates": [],
            "fitness_history": [],
            "mode_counts": {},
            "total_evaluations": 0,
            "cache_hits": 0,
            "comparison_runs": {},
            "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        }

    def _bind_http_server(self) -> ThreadingHTTPServer:
        """Bind `ThreadingHTTPServer` to the requested or next available local port."""
        dashboard_ref = self

        class DashboardRequestHandler(BaseHTTPRequestHandler):
            """HTTP request handler serving `/` and `/api/state`."""

            def do_GET(self) -> None:
                path = self.path.split("?", 1)[0]
                if path in ("/", "/index.html"):
                    body = DASHBOARD_HTML.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(body)
                elif path == "/api/state":
                    payload_str = dashboard_ref.get_state_json()
                    body = payload_str.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
                    self.end_headers()
                    self.wfile.write(body)
                elif path == "/api/health":
                    health = json.dumps(
                        {"status": "ok", "url": dashboard_ref.url, "port": dashboard_ref.port}
                    ).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Content-Length", str(len(health)))
                    self.end_headers()
                    self.wfile.write(health)
                else:
                    self.send_response(404)
                    self.end_headers()

            def log_message(self, format: str, *args: Any) -> None:
                """Silence standard HTTP access logs so console training output stays clean."""
                return

        if self.requested_port > 0:
            candidate_ports = [self.requested_port, 0]
        else:
            candidate_ports = list(range(self.preferred_port, self.preferred_port + 25)) + [0]

        last_err: Optional[Exception] = None
        for p in candidate_ports:
            try:
                server = ThreadingHTTPServer((self.host, p), DashboardRequestHandler)
                server.daemon_threads = True
                return server
            except OSError as exc:
                last_err = exc
                continue

        raise RuntimeError(f"Failed to bind LiveDashboardServer on {self.host}: {last_err}")

    def start(self, open_browser: Optional[bool] = None) -> str:
        """
        Start the background HTTP server thread and optionally open the browser.

        Parameters
        ----------
        open_browser : Optional[bool], default=None
            Override `self.open_browser` if specified.

        Returns
        -------
        str
            The local URL (`http://127.0.0.1:<port>/`) of the live dashboard.
        """
        if self._server is not None:
            return self.url

        self._server = self._bind_http_server()
        self.port = int(self._server.server_address[1])
        self.url = f"http://{self.host}:{self.port}/"

        self._thread = threading.Thread(
            target=self._server.serve_forever,
            name="HOI4-LiveDashboardServer",
            daemon=True,
        )
        self._thread.start()

        self.logger.info("Live Training Web Dashboard started at: %s", self.url)

        should_open = self.open_browser if open_browser is None else open_browser
        if should_open:
            try:
                webbrowser.open(self.url, new=2)
                self.logger.info("Launched web browser for live training dashboard: %s", self.url)
            except Exception as exc:
                self.logger.warning("Could not auto-open web browser (%s); visit %s manually.", exc, self.url)

        return self.url

    def stop(self) -> None:
        """Gracefully shut down the background HTTP server thread."""
        server = self._server
        if server is not None:
            self._server = None
            try:
                server.shutdown()
                server.server_close()
            except Exception:
                pass
            self.logger.info("Live Training Web Dashboard stopped (%s).", self.url)

    def get_state(self) -> Dict[str, Any]:
        """Return a thread-safe shallow copy of the current dashboard state."""
        with self._lock:
            return dict(self._state)

    def get_state_json(self) -> str:
        """Return the current dashboard state serialized as a JSON string."""
        with self._lock:
            return json.dumps(self._state, ensure_ascii=False)

    def update_state(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        """
        Thread-safely update the live dashboard state from an optimizer step snapshot.

        Parameters
        ----------
        snapshot : Dict[str, Any]
            Telemetry dictionary passed to `on_step_callback(snapshot)`.

        Returns
        -------
        Dict[str, Any]
            Updated normalized dashboard state dictionary.
        """
        raw = serialize_for_telemetry(snapshot)
        if not isinstance(raw, dict):
            return self.get_state()

        with self._lock:
            method_key = str(raw.get("method") or self._state.get("method") or "cso").lower()
            obj_key = str(raw.get("objective") or self._state.get("objective") or "best_overall").lower()
            year_str = str(raw.get("year") or self._state.get("year") or "1940")

            leader_raw = raw.get("leader") or raw.get("best_candidate")
            leader_summary = (
                extract_division_summary(leader_raw)
                if leader_raw is not None
                else self._state["leader"]
            )
            if not leader_summary.get("method"):
                leader_summary["method"] = method_key.upper()

            raw_top = raw.get("top_candidates") or raw.get("hall_of_fame") or []
            top_summaries: List[Dict[str, Any]] = []
            if isinstance(raw_top, list):
                for item in raw_top[:10]:
                    s = extract_division_summary(item)
                    if not s.get("method"):
                        s["method"] = method_key.upper()
                    top_summaries.append(s)
            if not top_summaries and leader_summary["total_fitness"] > 0:
                top_summaries = [leader_summary]

            # Normalize fitness history list
            raw_history = raw.get("fitness_history")
            history_list: List[Dict[str, Any]] = []
            if isinstance(raw_history, list) and raw_history:
                for idx, entry in enumerate(raw_history, start=1):
                    if isinstance(entry, dict):
                        history_list.append({
                            "iteration": int(entry.get("iteration", idx)),
                            "best_fitness": float(entry.get("best_fitness", 0.0) or 0.0),
                            "mean_fitness": float(
                                entry.get("mean_fitness")
                                if entry.get("mean_fitness") is not None
                                else (entry.get("avg_fitness", 0.0) or 0.0)
                            ),
                            "win_rate": float(entry.get("win_rate", 0.0) or 0.0),
                        })
                    elif isinstance(entry, (int, float)):
                        history_list.append({
                            "iteration": idx,
                            "best_fitness": float(entry),
                            "mean_fitness": float(entry),
                            "win_rate": leader_summary["win_rate"],
                        })
            else:
                history_list = list(self._state.get("fitness_history", []))
                iter_num = int(raw.get("iteration", len(history_list) + 1))
                best_f = float(raw.get("best_fitness", leader_summary["total_fitness"]) or 0.0)
                mean_f = float(raw.get("mean_fitness", raw.get("avg_fitness", best_f)) or 0.0)
                if iter_num > 0:
                    history_list.append({
                        "iteration": iter_num,
                        "best_fitness": best_f,
                        "mean_fitness": mean_f,
                        "win_rate": leader_summary["win_rate"],
                    })

            elapsed = float(
                raw.get("elapsed_seconds")
                if raw.get("elapsed_seconds") is not None
                else (time.time() - self._start_time)
            )

            self._state.update({
                "status": str(raw.get("status", "TRAINING")).upper(),
                "method": method_key,
                "method_display": str(
                    raw.get("algorithm_name")
                    or METHOD_DISPLAY_NAMES.get(method_key, method_key.upper())
                ),
                "algorithm_name": str(
                    raw.get("algorithm_name")
                    or METHOD_DISPLAY_NAMES.get(method_key, method_key.upper())
                ),
                "year": year_str,
                "objective": obj_key,
                "objective_display": OBJECTIVE_DISPLAY_NAMES.get(obj_key, obj_key),
                "iteration": int(raw.get("iteration", self._state["iteration"])),
                "total_iterations": int(raw.get("total_iterations", self._state["total_iterations"])),
                "elapsed_seconds": round(elapsed, 2),
                "best_fitness": leader_summary["total_fitness"],
                "mean_fitness": float(raw.get("mean_fitness", raw.get("avg_fitness", 0.0)) or 0.0),
                "leader": leader_summary,
                "top_candidates": top_summaries,
                "fitness_history": history_list,
                "mode_counts": raw.get("mode_counts") or {},
                "algorithm_metadata": raw.get("algorithm_metadata") or {},
                "custom_metrics": raw.get("custom_metrics") or {},
                "total_evaluations": int(raw.get("total_evaluations", self._state.get("total_evaluations", 0))),
                "cache_hits": int(raw.get("cache_hits", self._state.get("cache_hits", 0))),
                "updated_at_utc": datetime.now(timezone.utc).isoformat(),
            })
            return dict(self._state)

    # Aliases so `LiveDashboardServer` instance can be passed directly as `on_step_callback`
    on_step = update_state
    __call__ = update_state

    def mark_completed(self, final_result: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Mark the optimization run as `COMPLETED` on the live dashboard, optionally
        merging final result fields.
        """
        if isinstance(final_result, dict):
            merged = dict(final_result)
            merged["status"] = "COMPLETED"
            if "iteration" not in merged:
                merged["iteration"] = self._state.get("total_iterations", self._state.get("iteration", 1))
            return self.update_state(merged)

        with self._lock:
            self._state["status"] = "COMPLETED"
            self._state["iteration"] = max(
                int(self._state.get("iteration", 0)),
                int(self._state.get("total_iterations", 0)),
            )
            self._state["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
            return dict(self._state)

    def record_comparison_method(self, method_key: str, result: Dict[str, Any]) -> None:
        """
        Record a completed algorithm's result during a multi-algorithm `compare` run,
        updating the Hall of Fame leaderboard across all compared algorithms.
        """
        serialized = serialize_for_telemetry(result)
        if not isinstance(serialized, dict):
            return
        leader_summary = extract_division_summary(serialized.get("leader", serialized.get("best_candidate")))
        leader_summary["method"] = method_key.upper()
        leader_summary["name"] = f"[{method_key.upper()}] {leader_summary['name']}"

        with self._lock:
            comp_runs = dict(self._state.get("comparison_runs", {}))
            comp_runs[method_key] = {
                "method": method_key,
                "leader": leader_summary,
                "elapsed_seconds": serialized.get("elapsed_seconds", 0.0),
                "fitness_history": serialized.get("fitness_history", []),
            }
            self._state["comparison_runs"] = comp_runs

            # Merge all comparison leaders into the top_candidates Hall of Fame
            combined_leaders = [v["leader"] for v in comp_runs.values()]
            combined_leaders.sort(key=lambda c: c["total_fitness"], reverse=True)
            self._state["top_candidates"] = combined_leaders
            if combined_leaders:
                self._state["leader"] = combined_leaders[0]
                self._state["best_fitness"] = combined_leaders[0]["total_fitness"]

    def __enter__(self) -> LiveDashboardServer:
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.stop()

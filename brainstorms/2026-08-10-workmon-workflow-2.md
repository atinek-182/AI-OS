# WorkMon Workflows 1 & 2: Complete Discovery & Architecture Master Spec
Date: 2026-08-10 · Goal: Master Technical Blueprint for WorkMon Unified Workflow Engine · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Unified Vision**: WorkMon (Workforce / Workflow Monitoring & Automation Engine) fusing **Workflow 1** (Core Business & Lead Pipelines) and **Workflow 2** (Operational Task Health & Subagent Monitoring) into **n8n as the Main Orchestration Hub**.
- **Self-Evolution & Auto-Improvement Engine**: After every workflow run, WorkMon extracts error patterns, appends new safeguards to `references/GLOBAL_ERROR_PREVENTION_RULES.md`, executes `python scripts/sync_global_rules.py` to keep agent system prompts (`AGENTS.md`, `GEMINI.md`) synchronized, and triggers `graphify update .`.
- **Proactive Skill & Tool Recommendation Engine**: Scans execution logs for workflow friction, querying `brain-aios/wiki/research/skills-library/` and proposing new specialized tools or skills to Atinek Maurya automatically.
- **Monitoring Strategy**: Non-intrusive local Python watchdog (`workmon_sensor.py`) polling active PIDs, tracking log velocity (`mtime`), and scanning stdout/stderr for critical error signatures (`Traceback`, `WinError`, `TimeoutError`, `403 Forbidden`, `invalid_grant`).
- **n8n Topology**: Hybrid Push Webhook (sub-second telemetry POSTs) + Periodic 5-minute n8n Cron Heartbeat check. Local fallback log (`scratch/workmon_fallback.json`) ensures 100% operation if n8n is offline.
- **Self-Healing Policy**: Smart Auto-Mitigation (3x retry backoff + automated `aios_gws_health_check.py` auth recovery + zombie PID termination).
- **Dual Zero-Fee Dashboard**: Syncs real-time task states to Notion Database (`WorkMon Dashboard`) and Google Sheets via dynamic header mapping (`getHeaderMap`).

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **WorkMon**: Unified Workforce / Workflow Monitoring & Automation Engine within ZORIXEL AIOS ecosystem.
- **WorkMon Workflow 1**: Primary business automation stream (Lead intake, client outreach, n8n orchestration, and content research).
- **WorkMon Workflow 2**: Operational monitoring module focused on real-time task health tracking, subagent state monitoring, failure triage, and alert dispatch.
- **n8n Central Hub**: Self-hosted / local n8n instance serving as the primary visual orchestration platform.
- **Auto-Improvement Loop**: Post-execution feedback cycle that logs new error safeguards to `GLOBAL_ERROR_PREVENTION_RULES.md` and updates AST dependency graphs.
- **Skill Suggestion Engine**: Automated analyzer that scans execution bottlenecks and recommends skill/tool upgrades from `skills-library/`.

## Complete Q&A Log & Decisions
1. **Q1 — Objective**: Operational Task Health & Subagent Monitoring (Option B).
2. **Q2 — Detection**: Hybrid PID Polling + Log Timestamp Velocity + Regex Error Sweep (Option A + C).
3. **Q3 — Alerting**: Dual-Channel (Terminal ASCII Banner + n8n/Notion/Sheets DB Status Tags).
4. **Q4 — Self-Healing**: Smart Auto-Mitigation (3x retry backoff + auth refresh cascade + zombie PID kill).
5. **Q5 — n8n Topology**: Hybrid Push Webhook + Periodic 5-min n8n Heartbeat Poll (Option A).
6. **Q6 — Data Schema**: Standard Operating Schema (Task Name/ID, Source, Status, PID & Host, Log Snippet, Retry Count, Last Heartbeat).

## System Architecture Blueprint

```
+-----------------------------------------------------------------------------------+
|                            LOCAL OS PROCESS ENGINE                                |
|  +---------------------------+       +-----------------------------------------+  |
|  | Subagent / Python Worker | ----> | Log Redirection (.system_generated/)    |  |
|  +---------------------------+       +-----------------------------------------+  |
|                                                           |                       |
|                                                           v                       |
|  +-----------------------------------------------------------------------------+  |
|  |               WorkMon Local Watchdog Sensor (workmon_sensor.py)             |  |
|  |  - PID & CPU Health Polling                                                 |  |
|  |  - Log mtime Velocity Check (Stall Detection > 3m)                           |  |
|  |  - Regex Error Signature Scan (Traceback, WinError, 403, invalid_grant)       |  |
|  |  - Local Fallback Log (scratch/workmon_fallback.json)                         |  |
|  +-----------------------------------------------------------------------------+  |
+------------------------------------------|----------------------------------------+
                                           | HTTP POST Webhook
                                           v
+-----------------------------------------------------------------------------------+
|                              n8n CENTRAL HUB ENGINE                               |
|  +-----------------------------------------------------------------------------+  |
|  | Webhook Input Node  /  5-Min Schedule Heartbeat Node                        |  |
|  +-----------------------------------------------------------------------------+  |
|                                           |                                       |
|                  +------------------------+------------------------+              |
|                  |                                                 |              |
|                  v                                                 v              |
|   +------------------------------+                 +---------------------------+  |
|   | Notion DB Sync Node          |                 | Google Sheets Sync Node   |  |
|   | (WorkMon Dashboard)          |                 | (Zero-Fee Backup Log)     |  |
|   +------------------------------+                 +---------------------------+  |
|                  |                                                 |              |
|                  +------------------------+------------------------+              |
|                                           |                                       |
|                                           v                                       |
|  +-----------------------------------------------------------------------------+  |
|  |                       AUTO-IMPROVEMENT & SUGGESTION ENGINE                  |  |
|  |  1. Append Error Rules -> references/GLOBAL_ERROR_PREVENTION_RULES.md       |  |
|  |  2. Execute -> python scripts/sync_global_rules.py                            |  |
|  |  3. Update AST -> python scripts/graphify_runner.py update .                 |  |
|  |  4. Skill Suggestion -> Scan brain-aios/wiki/research/skills-library/         |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

## Implementation Components
1. **`scripts/workmon_sensor.py`**: Non-intrusive Python monitoring daemon.
2. **`n8n/workflows/workmon_master_hub.json`**: Importable n8n workflow for central routing, Notion DB sync, Sheets sync, and auto-improvement triggers.
3. **`scripts/workmon_auto_evolver.py`**: Post-run rule sync and skill/tool suggestion engine.
4. **`docs/specs/SPEC-workmon-master.md`**: Formal technical specification.

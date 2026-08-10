---
title: WorkMon Workflows 1 & 2 Unified Engine Master Specification
domain: architecture
summary: Complete technical specification, telemetry topology, n8n hub integration, auto-evolution rules, and SOPs for WorkMon Workflows 1 & 2.
critical_directives:
- Keep local Python watchdog sensor decoupled from n8n network availability.
- Append all newly caught task failure patterns to references/GLOBAL_ERROR_PREVENTION_RULES.md.
- Maintain zero subscription fees by using native n8n, Notion DB, and Google Sheets integrations.
section_outline:
- WorkMon Workflows 1 & 2 Unified Engine Master Specification
- Overview & System Architecture
- Telemetry & Health Monitoring Engine
- n8n Central Hub Integration
- Auto-Evolution & Skill Suggestion Protocol
- Verification & Operational SOPs
read_triggers:
- When working on WorkMon workflow specs in docs/specs/SPEC-workmon-master.md
- When deploying n8n workflows for WorkMon
tags:
- architecture
- workmon
- n8n
- monitoring
updated: '2026-08-10'
---

# WorkMon Workflows 1 & 2 Unified Engine Master Specification

## Overview & System Architecture

WorkMon (Workforce / Workflow Monitoring & Automation Engine) unifies:
- **WorkMon Workflow 1**: Core business logic, lead acquisition pipelines, and n8n main orchestration flows.
- **WorkMon Workflow 2**: Real-time task health monitoring, process PID tracking, log modification velocity (`mtime`), failure triage, and auto-mitigation.

The system uses a **decoupled architecture**:
1. **Local Sensor Layer (`scripts/workmon_sensor.py`)**: Lightweight Python daemon running on the local host. Operates independently of network connectivity, polling process health and writing to local fallback logs (`scratch/workmon_fallback.json`) if external endpoints are unreachable.
2. **Central Hub Layer (`n8n/workflows/workmon_master_hub.json`)**: Self-hosted n8n instance serving as the primary visual orchestration dashboard, handling webhook ingestion (`POST /webhook/workmon-telemetry`), 5-minute heartbeat checks, and dispatching updates to Notion and Google Sheets.
3. **Auto-Evolution Layer (`scripts/workmon_auto_evolver.py`)**: Post-run improvement engine that extracts error tracebacks, registers new rules into `references/GLOBAL_ERROR_PREVENTION_RULES.md`, executes `sync_global_rules.py`, updates AST dependency graphs via `graphify_runner.py`, and suggests tool upgrades from `brain-aios/wiki/research/skills-library/`.

---

## Telemetry & Health Monitoring Engine

### Health Decision Matrix

| Metric / Check | Threshold | Action Taken |
|---|---|---|
| **PID Active Check** | Process dead / unexpected termination | Status: `CRASHED` -> Trigger auto-mitigation retry. |
| **Log Modification Timestamp (`mtime`)** | `mtime` > 180 seconds | Status: `STALLED` -> Log velocity warning, prepare zombie termination. |
| **Regex Error Scan** | Matches `Traceback`, `WinError`, `TimeoutError`, `403 Forbidden` | Status: `FAILED` -> Extract error traceback. |
| **Auth Error Signature** | Matches `invalid_grant` or `403` | Status: `AUTH_EXPIRED` -> Execute `aios_gws_health_check.py`. |

---

## n8n Central Hub Integration

WorkMon connects to n8n via:
- **Primary Endpoint**: `http://localhost:5678/webhook/workmon-telemetry`
- **Payload Schema**:
  ```json
  {
    "task_id": "task_104",
    "workflow_source": "WorkMon Workflow 2",
    "status": "HEALTHY",
    "pid": 14820,
    "pid_active": true,
    "idle_seconds": 12.4,
    "errors": [],
    "timestamp": "2026-08-10T12:30:00Z",
    "host": "AIOS-Host"
  }
  ```

---

## Auto-Evolution & Skill Suggestion Protocol

After every workflow run, the `workmon_auto_evolver.py` script executes:
1. **Rule Synchronization**: Appends new failure prevention rules to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and runs `python scripts/sync_global_rules.py` so all AI agents update system prompts inline.
2. **Graphify AST Update**: Executes `python scripts/graphify_runner.py build` to refresh dependency graphs across workspace hubs.
3. **Skill & Tool Recommendations**: Scans `brain-aios/wiki/research/skills-library/` against task keywords and prints proactive skill suggestions to the console and log.

---

## Operational SOPs

### 1. Manual Health Check
```bash
python scripts/workmon_sensor.py --test-run
```

### 2. Manual Auto-Evolution Test
```bash
python scripts/workmon_auto_evolver.py --test-run
```

### 3. n8n Import SOP
Import `d:\AI-OS\n8n\workflows\workmon_master_hub.json` directly into your local n8n instance and activate the workflow.

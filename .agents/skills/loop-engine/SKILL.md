---
title: ZORIXEL AIOS Native Loop Engineering Engine (`/loop-engine`)
domain: skill
summary: Native AIOS dynamic loop engineering and self-healing feedback cycle engine. Converts open-ended tasks into bounded,
  self-verifying, receipt-logging iteration loops across TDD, doc sync, visual QA, security sweeps, and Autoresearch score
  optimization.
critical_directives:
- Strictly enforce the 6-phase cycle: Observe -> Choose -> Act -> Verify -> Record -> Stop.
- Support both static playbooks in LOOPS.md and dynamic loop generation (--dynamic) derived from workspace inspection.
- Bridge seamlessly with Autoresearch (/autoresearch-manage) for numeric score-driven optimization trials.
- Follow zero-emoji mandate across all receipts, playbooks, and terminal outputs.
section_outline:
- ZORIXEL AIOS Native Loop Engineering Engine (`/loop-engine`)
- Overview & Tri-Mode Execution
- The 6-Phase Feedback Cycle Architecture
- Dynamic Loop Generation & Autoresearch Bridge
- 9 Operational Workflows
- Active AIOS Loop Playbook Registry
- 5 Core AIOS Usage Scenarios
- Execution Receipt Standard & LOOPS.md Protocol
- Inter-Skill Connections & SDLC Handoff Pipeline
read_triggers:
- When working on skill in .agents/skills/loop-engine/SKILL.md
- When reading context for ZORIXEL AIOS Native Loop Engineering Engine
tags:
- skill
- SKILL
- loop-engine
updated: '2026-08-08'
name: loop-engine
description: Native AIOS dynamic loop engineering engine. Discovers, crafts, audits, adapts, runs, and debriefs repeatable
  self-healing feedback loops for TDD, doc sync, visual QA, security sweeps, and Autoresearch score optimization with LOOPS.md
  receipt logging.
argument-hint: '[loop_name_or_goal] [--run|--craft|--audit|--debrief|--dynamic] [--save]'
---

# ZORIXEL AIOS Native Loop Engineering Engine (`/loop-engine`)

## Overview & Tri-Mode Execution

This skill is the native loop engineering, dynamic playbook generator, and self-healing feedback engine for Atinek Maurya's AIOS (`AI-OS`). It adapts the core feedback-loop principles of `loopy` and unifies them with Karpathy's `autoresearch` score optimization engine into a production-grade, zero-emoji, receipt-logging meta-skill.

Invokable via:
- **Slash Command**: `/loop-engine [playbook_or_goal] [--run|--craft|--audit|--debrief|--dynamic] [--save]`
- **Dynamic Intent**: Triggered automatically when multi-pass tasks (TDD error sweeps, visual QA adjustments, security audits, doc syncs, or prompt optimization) require iterative execution with explicit stopping criteria.
- **Programmatic Inter-Skill Calling**: Called by parent skills (`/tdd`, `/website-design-engine`, `/vibesec`, `/graphify`, `/autoresearch-manage`, `/storm-research-project`).

---

## The 6-Phase Feedback Cycle Architecture

Every loop executed by this engine strictly adheres to the following 6-phase sequence:

1. **Observe**: Collect fresh environment state, error logs, git diffs, or screenshot metrics. Never act on stale assumptions.
2. **Choose**: Select exactly ONE bounded, high-leverage surgical action based on explicit criteria.
3. **Act**: Apply the single reversible modification (code fix, CSS token change, prompt mutation).
4. **Verify**: Execute a deterministic, reproducible acceptance check (automated test, Playwright audit, `prepare.py` score).
5. **Record**: Log pass details, evidence, score delta, and state changes to the execution receipt in `LOOPS.md`.
6. **Stop or Repeat**: Evaluate terminal stopping conditions (Success, Clean No-Op, Stagnation/Plateau, Guardrail Breach). If terminal state is met, exit cleanly and return receipt; otherwise proceed to next bounded pass.

---

## Dynamic Loop Generation & Autoresearch Bridge

### 1. Dynamic Playbook Generation (`--dynamic`)
When invoked with `--dynamic` or given a non-standard task, `/loop-engine`:
1. Scans workspace files, git diffs, lint logs, or research briefs.
2. Synthesizes a runtime loop specification with customized observation targets, action bounds, verification scripts, and stopping thresholds.
3. Executes the generated loop in bounded passes without polluting permanent configuration.
4. Offers to save high-performing dynamic playbooks to `LOOPS.md`.

### 2. Autoresearch Engine Bridge (`/autoresearch-manage`)
When an optimization task requires numerical score maximization (e.g. prompt token efficiency, algorithm speed, UI conversion rating):
1. `/loop-engine` invokes `python scripts/manage_autoresearch.py add [target]` to bootstrap `trials/[target]/` (`program.md`, `train.py`, `prepare.py`).
2. Runs the Autoresearch mutation loop autonomously, testing candidate code in `train.py` against `prepare.py`.
3. Commits score improvements to git, reverts regressions, and logs results in `results.tsv`.
4. Appends final optimization receipt to `LOOPS.md` and registers clean artifacts.

---

## 9 Operational Workflows

| Workflow | Purpose | Trigger / Command | Key Output |
|---|---|---|---|
| **Discover** | Analyze workspace or session logs for repeated manual tasks | `/loop-engine --discover` | `LOOPS.md` candidate entries |
| **Find** | Locate matching pre-configured loop playbooks in `LOOPS.md` | `/loop-engine --find [goal]` | Recommended playbook |
| **Audit** | Diagnose weak acceptance gates or missing terminal bounds | `/loop-engine --audit [playbook]` | Repaired playbook spec |
| **Adapt** | Tailor a baseline loop to a specific module or service | `/loop-engine --adapt [playbook]` | Adapted playbook |
| **Craft** | 6-question Socratic interview to build a new custom loop | `/loop-engine --craft` | Custom playbook entry |
| **Run** | Bounded pass execution with real-time verification & receipt logging | `/loop-engine [playbook] --run` | `LOOPS.md` execution receipt |
| **Debrief** | Analyze run receipts to identify bottlenecks or threshold tweaks | `/loop-engine --debrief [receipt_id]` | Optimization recommendations |
| **Save** | Append accepted loop definition to workspace `LOOPS.md` | `/loop-engine --save` | Updated `LOOPS.md` |
| **Publish** | Prepare verified loop playbook for distribution | `/loop-engine --publish` | Clean markdown playbook |

---

## 5 Core AIOS Usage Scenarios

### Scenario 1: Autonomous Prompt & Skill Optimization (`prompt-opt`)
- **Bridge**: `/loop-engine` + `/autoresearch-manage`.
- **Target**: System prompts in `.agents/skills/` and LLM agent instructions.
- **Mechanism**: Mutates candidate prompt in `train.py`, scores output precision & token count in `prepare.py`, commits score improvements.

### Scenario 2: Web App Performance & Visual QA (`visual-qa`)
- **Bridge**: `/loop-engine` + `/website-design-engine` + `/hallmark`.
- **Target**: Next.js & React dashboards, landing pages, and slide decks.
- **Mechanism**: Captures 5-viewport Playwright screenshots, measures layout contrast and alignment, applies CSS token fixes, stops at 100% score compliance.

### Scenario 3: Autonomous Code Refactoring & TDD Error Sweeps (`tdd-sweep`)
- **Bridge**: `/loop-engine` + `/tdd` + `/systematic-debugging`.
- **Target**: Failing unit tests, syntax errors, or type errors across Python/TypeScript packages.
- **Mechanism**: Isolates stack trace, makes 1 surgical edit per pass, verifies via `pytest`/`npm test`, stops on 100% pass rate.

### Scenario 4: Market Intel & Content Auto-Evolution (`research-opt`)
- **Bridge**: `/loop-engine` + `/storm-research-project` + `/carousel-copy`.
- **Target**: Client acquisition briefs, offer positioning, and YouTube script hooks.
- **Mechanism**: Iteratively extracts competitor data, scores hook contrast and value density, refines copy until high-converting.

### Scenario 5: SecurityOS Zero-Trust Hardening (`security-sweep`)
- **Bridge**: `/loop-engine` + `/security-os` + `/vibesec`.
- **Target**: Pre-commit security audits and API permission boundaries.
- **Mechanism**: Executes `security_os_runner.py audit .`, applies zero-trust patches, re-audits until 0 Critical and 0 High findings remain.

---

## Execution Receipt Standard & `LOOPS.md` Protocol

When running a loop, the engine appends an immutable run receipt to `LOOPS.md` under `## Execution Receipts`:

```markdown
### Receipt: [Loop Name] - [YYYY-MM-DD HH:MM]
- **Status**: SUCCESS / STAGNATED / GUARDRAIL_BREACH
- **Total Passes**: X / Max Y
- **Pass Summary**:
  - Pass 1: [Observed issue] -> [Action taken] -> [Verification result / Score]
  - Pass 2: [Observed issue] -> [Action taken] -> [Verification result / Score]
- **Final Evidence**: [Test log snippet / Score metric]
- **Terminal Stopping Reason**: [Reason for exit]
```

---

## Inter-Skill Connections & SDLC Handoff Pipeline

- **Autoresearch Engine**: Invokes `python scripts/manage_autoresearch.py` and `trials/runner.py` for numeric score optimization.
- **SDLC Master Engine**: Connects to Phase 3 (Build), Phase 4 (Verify), and Phase 5 (Review) across all engineering workflows.
- **Research Engine**: Connects to `@.agents/skills/storm-research-project` for iterative market and competitive intelligence sweeps.

# Scenario 1: Autonomous Prompt & Skill Optimization Trial Setup (`prompt-opt`)
Date: 2026-08-09 · Goal: Detailed Socratic discovery for Scenario 1 optimization trial · Operator: Atinek Maurya

## Executive Summary & Concept Overview

This document captures the detailed discovery and parameter setup for **Scenario 1: Autonomous Prompt & Skill Optimization (`prompt-opt`)**.

### How Scenario 1 Works Under the Hood
1. **Target Selection**: We pick an active AIOS skill or prompt template (e.g. `roast`, `carousel-copy`, or `website-design-engine`).
2. **Trial Bootstrapping**: We run `python scripts/manage_autoresearch.py add prompt_optimizer_v1` to create `trials/prompt_optimizer_v1/`:
   - `program.md`: Instructions guiding the autonomous agent on how to mutate `train.py`.
   - `train.py`: Contains the system prompt / skill instructions being optimized.
   - `prepare.py`: The scoring harness that evaluates output against test inputs, scoring token efficiency, formatting, zero fluff, and zero-emoji compliance.
   - `results.tsv`: Append-only log recording score history after every pass.
3. **Loop Execution**: `/loop-engine` runs bounded passes. If `prepare.py` score increases, git commits `train.py`. If score drops or stagnates, edits are reverted.

---

## Socratic Discovery Q&A Log

### Q1 — Target Prompt / Skill Selection
- **Concept**: Selecting the exact skill file in `.agents/skills/` to mutate and evaluate.
- **Options**:
  1. `roast` skill (`.agents/skills/roast/SKILL.md`) [RECOMMENDED]
  2. `carousel-copy` skill (`.agents/skills/carousel-copy/SKILL.md`)
  3. `website-design-engine` skill (`.agents/skills/website-design-engine/SKILL.md`)
  4. Custom prompt/skill specified by operator
- **Rationale**: The `roast` skill is invoked frequently across discovery and code reviews; optimizing its token conciseness and red-teaming rigor yields immediate productivity gains.

### Q2 — Scoring Criteria & Weighting Strategy
- **Concept**: How `prepare.py` evaluates candidate outputs on a 0-100 numeric scale.
- **Options**:
  1. Balanced Score: 40% Accuracy & Rule Compliance, 30% Token Conciseness, 30% Structural Clarity [RECOMMENDED]
  2. Token Compression Focus: 60% Token Efficiency, 40% Accuracy
  3. Structural Rigor Focus: 70% Accuracy & Zero Fluff, 30% Formatting
- **Rationale**: Balanced scoring ensures prompts become shorter and sharper without sacrificing analytical rigor.

### Q3 — Stopping Criteria & Execution Bounds
- **Concept**: Defining when the loop exits autonomously.
- **Options**:
  1. Score Plateau: Stop after 3 consecutive passes with <2% score improvement [RECOMMENDED]
  2. Fixed Pass Cap: Run exactly 10 passes and select highest score
  3. Target Score: Stop immediately when score reaches >=95/100
- **Rationale**: Score plateau prevents diminishing returns while allowing maximum optimization depth.

### Q4 — Winning Artifact Promotion Policy
- **Concept**: What happens when an optimized prompt outperforms the current version.
- **Options**:
  1. Auto-apply winning prompt to target `SKILL.md` and append receipt to `LOOPS.md` [RECOMMENDED]
  2. Show visual diff preview and require operator confirmation before updating target file
- **Rationale**: Auto-applying creates true autonomous self-improvement, backed by git history for safety.

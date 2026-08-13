# Wave 3 Ingestion & Component Vault Processing: Discovery & Brainstorm Notes
Date: 2026-08-12 · Goal: Design Codrops Hub-Inspired Component Studio Dashboard for 175+ Component Repositories · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Dedicated Skill Created**: [.agents/skills/component-vault-engine/SKILL.md](file:///d:/AI-OS/.agents/skills/component-vault-engine/SKILL.md)
  - Auto-trigger frontmatter: Activated on any chat bootup when working on the Component Hub gallery or adapting vault components into Next.js/React.
  - Fully locks in Q1-Q5 decisions, security 127.0.0.1 binding, Playwright QA protocol, CSS Modules scoping, GPU memory cleanup, and Context7 MCP auto-triggers.
- **Skill Auto-Upgrade Protocol**:
  - Whenever a new security flaw or technical fix is uncovered in ANY future chat:
    1. Logged to `references/GLOBAL_ERROR_PREVENTION_RULES.md`.
    2. Executed `python scripts/sync_global_rules.py` to auto-update `AGENTS.md` and `GEMINI.md` inline.
    3. Appended fix to `references/component-adaptation-rules.md` and `.agents/skills/component-vault-engine/SKILL.md`.
- **New Chat Execution Workflow**:
  - In a new chat, operator simply types: *"Hey, let's create the Component Studio Dashboard gallery for my 175 components now."*
  - AI auto-triggers `component-vault-engine`, recovers all Q1-Q5 decisions, and executes the 3-wave build on `http://127.0.0.1:8080`.

## Domain Vocabulary & Glossary
- **`component-vault-engine`**: Master AIOS skill governing the 175+ component vault, gallery build spec, and React refactoring pipeline.
- **Global Rule Sync Engine (`sync_global_rules.py`)**: Script that propagates new security rules across system prompts (`AGENTS.md` & `GEMINI.md`).

## Q&A Log
### Q1 — Q5 Configuration Decisions
- **Captured**: Q1 Option A, Q2 Option A, Q3 Option C, Q4 Option B, Q5 Option A confirmed & locked into `component-vault-engine` SKILL.md.

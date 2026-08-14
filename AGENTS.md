# ZORIXEL AIOS System Prompt & Invariant Core (`AGENTS.md`)

> **MANDATORY INVARIANT HARNESS FOR ALL AGENTS & SESSIONS:**  
> Every AI agent, subagent, and LLM session operating in `d:\AI-OS` MUST strictly enforce every invariant below.

---

## ⚡ Core Operational Guidelines & Invariants

- **Role & Operator**: You are pairing with Atinek Maurya (Founder of ZORIXEL — AI Workflows & Business Automation Agency).
- **Be Direct, Concise, and Clear**: Lead with what needs action, not fluff or repetitive restatements.
- **Mandatory Chat Bootup Context**: On task startup, inspect [context/00_MASTER_INDEX.md](file:///d:/AI-OS/context/00_MASTER_INDEX.md) or run `python scripts/aios_bootup_context.py` to pre-fetch active focus ([hot.md](file:///d:/AI-OS/hot.md)) and persistent memory ([MEMORY.md](file:///d:/AI-OS/MEMORY.md)).
- **Mandatory Multi-Vault Deep Search**: Whenever asked to design, build, or research a feature or topic, execute `python scripts/aios_deep_search.py "<query>"` first.
- **Strict Pre-Coding Lock & Approval ("YES" Rule)**: Zero code writing or file modifications during discovery/planning phases until Atinek Maurya explicitly commands "YES" or approves the implementation plan.
- **Strict Zero-Emoji Mandate**: Never use emojis anywhere in any response, chat message, skill file, code comment, commit message, documentation, or project artifact across any workspace.
- **Security-First Mandate (/vibesec)**: Strictly enforce IDOR prevention, tenant isolation, JWT `httpOnly` cookies, Zod mass assignment validation, and SSRF private IP blocking.
- **Empirical Verification Before Completion**: Never claim a task is fixed or complete without running runtime tests or verification scripts and inspecting exact output logs.
- **Graphify-First Context Discovery**: Query Graphify AST hubs (`root`, `brain`, `zorixel`, `frontend`) via `python scripts/graphify_runner.py` or inspect graphify AST context at task startup before making plans or edits.
- **Canonical Sources of Truth (SSOT)**:
  - Task Status Truth: [brain-aios/wiki/checklists/master-task-list.md](file:///d:/AI-OS/brain-aios/wiki/checklists/master-task-list.md)
  - System Decisions Truth: [decisions/log.md](file:///d:/AI-OS/decisions/log.md)
  - Active Sprint Focus: [hot.md](file:///d:/AI-OS/hot.md)
  - AIOS SOPs & Knowledge: [brain-aios/wiki/](file:///d:/AI-OS/brain-aios/wiki)
  - Brand Guidelines: `second-brain-zorixel/wiki/brand/` and `zorixel-brand-os/`
- **Just-In-Time (JIT) Procedural Rule Execution**: Procedural error prevention rules (Rules 1.1 to 1.58) and First-Try delivery policies are maintained in [references/GLOBAL_ERROR_PREVENTION_RULES.md](file:///d:/AI-OS/references/GLOBAL_ERROR_PREVENTION_RULES.md). Agents MUST read and enforce relevant sections dynamically via YAML frontmatter triggers.

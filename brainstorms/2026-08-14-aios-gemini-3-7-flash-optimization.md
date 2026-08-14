# Gemini 3.7 Flash (High Reasoning) AIOS Optimization: Discovery & Brainstorm Notes
Date: 2026-08-14 · Goal: System-wide optimization of ZORIXEL AIOS architecture, prompts, skills, context engineering, and execution loops tailored to Gemini 3.7 Flash High Reasoning capabilities · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Core Model Shift**: Upgrading workspace workflows from legacy prompting and verbose linear guardrails to Gemini 3.7 Flash with High Reasoning (Thinking Engine).
- **Primary Optimization Pillars**:
  1. System Prompt & Rule Architecture: Pruning duplicated inline tables, separating core system invariants from modular JIT references.
  2. Extended Thinking & Autonomous Loops: Calibrating reasoning depth for `/grill-me`, `/roast`, `/loop-engine`, and 6-Phase SDLC.
  3. Context Engineering & AST Retrieval: Optimizing Graphify, Rich YAML Frontmatter, and Sub-Vault indexing for fast 1M+ context window synthesis.
  4. Tool Calling & Execution Ergonomics: Compact tool outputs, parallel execution, and automated self-healing execution loops.
  5. Agency Deliverables & Client Sprints: Accelerating $1,500-$5,000 AI workflow and web UI sprint pipelines with zero fee tooling.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Hybrid Reasoning (Thinking Budget)**: Gemini 3.7 Flash's capability to generate dynamic internal chain-of-thought traces before emitting tool calls and responses.
- **Just-In-Time (JIT) Context**: Loading atomic, phase-specific reference documents on demand rather than loading monolithic vaults into system prompt.
- **System Invariants vs Operational References**: Core rules that must never be violated (security, zero-emoji, brand colors) kept in primary prompt vs procedural SOPs loaded via frontmatter triggers.
- **Autonomous Feedback Loop**: Closed-loop execution cycle (Observe -> Choose -> Act -> Verify -> Record -> Stop) powered by 3.7 Flash reasoning self-correction.

## Q&A Log

### Q1 — System Prompt & Rule Architecture (Invariants vs JIT Modular Loading)
- **Concept Explained**: Gemini 3.7 Flash High combines deep internal reasoning (extended thinking budget) with high-speed execution. Overly verbose, duplicated inline rule tables (such as duplicating 58 error rules across `AGENTS.md` and `GEMINI.md`) consume baseline context window and create unnecessary token overhead. By distinguishing between core system invariants (strict security boundaries, zero-emoji mandate, brand color tokens, pre-coding lock) and modular JIT operational references loaded via frontmatter triggers and AST queries, 3.7 Flash can apply its full reasoning power directly to task architecture and code synthesis.
- **Asked**: How should we structure the core system prompt rules across `AGENTS.md`, `GEMINI.md`, and `references/GLOBAL_ERROR_PREVENTION_RULES.md` for Gemini 3.7 Flash High?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Strict Invariant Core + JIT Modular Loading. Keep absolute system invariants (Security boundaries, Zero-Emoji, Brand Identity, Pre-Coding Lock, Source of Truth hierarchy) in `AGENTS.md`/`GEMINI.md`, while modularizing the 58+ procedural error rules into JIT references loaded dynamically via frontmatter triggers and Graphify AST queries.
  2. Option B: Monolithic Inline Rule Tables. Retain all 58+ rules duplicated verbatim inside both `AGENTS.md` and `GEMINI.md` system prompts on every single message turn.
  3. Option C: Domain-Clustered Dynamic Rules. Group rules into 5 domain bundles (Web Design, Fullstack TS/Next.js, Client SaaS/n8n, Terminal/OS, Security) and load only the relevant bundle per task.
- **Captured Decision**: Hybrid Model — Strict Invariant Core in system prompts (`AGENTS.md` and `GEMINI.md`) + Domain-Clustered JIT Rule Modules (`references/GLOBAL_ERROR_PREVENTION_RULES.md` and domain bundles) loaded dynamically via frontmatter triggers and AST queries.
- **Rationale & Trade-offs**: Eliminates 250+ lines of duplicate prompt noise on every turn, optimizes context tokens for 3.7 Flash, and keeps hard system invariants (Security, Zero-Emoji, Brand Identity, Pre-Coding Lock) permanently enforced while loading deep error matrices JIT.

### Q2 — Skill Library Pruning & Tier 1 Master Skill Consolidation (.agents/skills)
- **Concept Explained**: The `.agents/skills/` directory currently contains 127 skill folders. Analysis reveals significant splintering and duplicate aliases (e.g. `grill-me` / `grill-with-docs` / `grilling`, `to-spec` / `mattpocock-to-spec`, `to-tickets` / `mattpocock-to-tickets`, `wayfinder` / `mattpocock-wayfinder`, `tdd` / `test-driven-development`, `browser-testing` / `browser-testing-with-devtools`, `storm-research` / `storm-research-project`). For Gemini 3.7 Flash High, having multiple ambiguous skill names for the same core capability can cause fuzzy intent matching and wasted tool context. Unifying duplicate fragments into authoritative Tier 1 master skills with rich dual-trigger frontmatter and symlink/redirect aliases makes skill discovery 100% deterministic.
- **Asked**: How should we organize and prune the 127 skills in `.agents/skills/` to maximize Gemini 3.7 Flash High's routing precision and prevent capability dilution?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Master Skill Consolidation + Clean Aliasing. Consolidate overlapping skill fragments into single authoritative Tier 1 master skills (e.g., unify `grilling`/`grill-with-docs` into `grill-me`; unify `tdd` into `test-driven-development`; unify `to-spec` into `mattpocock-to-spec`), updating YAML frontmatter aliases and descriptions so both shorthand and full commands route cleanly to one source of truth.
  2. Option B: Complete Pruning to Minimum Core (Retain ~30 Essential Skills Only). Aggressively archive niche and experimental skills into `brain-aios/wiki/research/skills-library/` (Tier 2 cold storage) and keep only the top ~30 core skills in `.agents/skills/`.
  3. Option C: Keep All 127 Skills As-Is. Maintain all separate folders and variations, adding frontmatter tags to differentiate slight variations.
- **Captured Decision**: Option A — Authoritative Master Skill Consolidation + Clean Aliasing. Unify all duplicate and splintered skill folders into authoritative Tier 1 Master Skills with frontmatter alias triggers.
- **Rationale & Trade-offs**: Retains 100% of capabilities while eliminating folder drift and intent ambiguity, allowing Gemini 3.7 Flash High to match skills deterministically.

### Q3 — Vault Architecture, Root Information Realignment & MEMORY.md Restructuring
- **Concept Explained**: Atinek Maurya identified that despite having 8 specialized vaults (`brain-aios`, `second-brain-zorixel`, `zorixel-brand-os`, `SecurityOs`, `references/awwwards-research-vault`, `clients/`, `audits/`, `decisions/`), vast amounts of domain lore, brand identity rules, client drafts, MCP API docs, and procedural error tables are currently dumped directly into the AIOS root (`MEMORY.md`, `AGENTS.md`, `GEMINI.md`, `WORKSPACE_MAP.md`, and loose `references/*.md`). The adversarial `/roast` council diagnosed this as 'Root Hoarding Syndrome' and SSOT (Single Source of Truth) violations.
- **Asked**: How should we realign and migrate root information into their canonical vaults to achieve a clean 3-Layer Architecture (Immutable Core Prompt <4KB -> Session Cache `hot.md` <2KB -> Distributed JIT Vaults)?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Full 3-Layer Vault Cleanse & MEMORY.md Restructure.
     - Move Brand Identity, Copy & Lore -> `second-brain-zorixel/wiki/brand/` and `zorixel-brand-os/`.
     - Move MCP API docs (8 loose files in `references/`) -> `brain-aios/wiki/mcp-servers/`.
     - Move stray client brainstorms -> `clients/001-vashishthya-research-edu/`.
     - Restructure `MEMORY.md` into 4 clean categorized sections (Operator Baseline, Pricing Corridors, Tech Environment, Core Milestones) and purge duplicate error matrices.
     - Replace 94KB monolithic `WORKSPACE_MAP.md` with a compact high-level vault directory index delegating deep queries to Graphify AST.
  2. Option B: Partial Vault Migration (Keep MEMORY.md & References as-is, migrate only brand lore).
  3. Option C: Leave Root Files Intact and rely solely on frontmatter headers.
- **Captured Decision**: Option A — Full 3-Layer Vault Cleanse & MEMORY.md Restructuring. Move brand lore to `second-brain-zorixel/`, MCP API docs to `brain-aios/wiki/mcp-servers/`, client drafts to `clients/`, restructure `MEMORY.md` into 4 clean sections (~5KB), and compress `WORKSPACE_MAP.md` into a compact high-level index.
- **Rationale & Trade-offs**: Permanently eliminates Root Hoarding Syndrome, establishes 100% Single Source of Truth (SSOT), and removes over 128KB of root clutter.

### Q4 — Execution Rollout Strategy & Atomic Safety Verification
- **Concept Explained**: Modifying system prompts, merging 35+ skill folders, moving reference docs into vaults, and restructuring `MEMORY.md` requires strict zero-downtime execution. If files are moved without updating alias triggers or if `sync_global_rules.py` isn't patched first, the prompt truncation bug could re-trigger or aliases could break. Structuring execution into 4 sequential, self-verifying batches (Batch A: System Prompts & sync script -> Batch B: Skill Consolidation -> Batch C: Vault Realignment & Memory Restructure -> Batch D: 3.7 Flash Loop Calibration & Full Health Sweep) guarantees zero capability loss and 100% verification at every step.
- **Asked**: How should we stage and execute the optimization rollout?
- **Options Provided**:
  1. Option A [RECOMMENDED]: 4-Batch Sequential Execution with Automated Verification.
     - Batch A (P0): Fix prompt truncation in `AGENTS.md`/`GEMINI.md` and patch `sync_global_rules.py`.
     - Batch B (P1): Run automated skill consolidator script (`scripts/aios_skills_consolidator.py`) to merge 35+ duplicate folders into master skills with alias triggers.
     - Batch C (P1): Re-home MCP docs, brand lore, client brainstorms, restructure `MEMORY.md`, and compress `WORKSPACE_MAP.md`.
     - Batch D (P2): Calibrate 3.7 Flash autonomous loop runners and execute master health sweep (`aios_bootup_context.py`, `graphify_runner.py status`, `aios_master_runner.py health`).
  2. Option B: Step-by-Step Interactive Approval (Pause and ask for explicit operator approval before starting each individual batch).
  3. Option C: Single Big-Bang Batch (Run all refactorings simultaneously in one execution wave).
- **Captured Decision**: Option A — 4-Batch Sequential Execution with Automated Verification. Proceed through Batches A -> B -> C -> D sequentially with automated tests and health checks between batches.
- **Rationale & Trade-offs**: Ensures zero-downtime execution, guarantees prompt truncation is permanently fixed first, and verifies system integrity at every step.

### Q5 — The "Brain Inversion" Crisis & Full AIOS Filesystem Reformation
- **Concept Explained**: The AIOS was architected with `brain-aios` as the central Obsidian vault holding all system knowledge, checklists, SOPs, postmortems, and manuals. However, a full audit revealed that the workspace root (`d:\AI-OS`) has become a sprawling warehouse holding 16 postmortem files (250KB+) in `brain-aios/wiki/experiences/postmortems/`, 25 loose files (including a 1.5MB JSON file `23-sites-matrix.json` and 8 MCP API files) in `references/`, standalone `EXPANSIONS.md` and `LOOPS.md` at root, duplicate `templates/` at root, and 60+ un-archived brainstorms. Meanwhile, `brain-aios/wiki/` subfolders remained sparse. Moving these knowledge assets into `brain-aios/wiki/` restores the intended PKM architecture: the root workspace becomes a lean **Execution Harness**, and `brain-aios` becomes the true **Unified Knowledge Brain**.
- **Asked**: How should we execute the full filesystem knowledge migration into `brain-aios` and restructure the non-core directories?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Complete Brain Vault Realignment & Root Cleanup.
     - Move 16 postmortems from `brain-aios/wiki/experiences/postmortems/` to `brain-aios/wiki/experiences/postmortems/` with an `INDEX.md`, then remove the redundant root `brain-aios/wiki/experiences/postmortems/` folder.
     - Move 8 MCP API cheat sheets (`references/*-api.md`) to `brain-aios/wiki/mcp-servers/`.
     - Move `EXPANSIONS.md` and `LOOPS.md` to `brain-aios/wiki/sops/`.
     - Move framework guides (`3ms-framework.md`, `aios-architecture-guide.md`, `utility-scripts.md`, `aios-user-manual.md`, `antigravity-skills-guide.md`) to `brain-aios/wiki/sops/` and `wiki/strategy/`.
     - Move the 1.5MB `23-sites-matrix.json` to `references/awwwards-research-vault/data/`.
     - Merge root `templates/` into `brain-aios/wiki/templates/` and purge duplicate root folder.
     - Archive completed past brainstorms into `brainstorms/archives/`.
  2. Option B: Partial Move (Move postmortems and MCP APIs only, leave manuals at root).
  3. Option C: Keep Files at Root and create soft-links.
- **Captured Decision**: Option A (Modified) — Complete Brain Vault Realignment & Root Cleanup with `EXPANSIONS.md` and `LOOPS.md` preserved at root.
  - Keep `EXPANSIONS.md` and `LOOPS.md` at root as concise top-level system anchors.
  - Move 16 postmortems (`brain-aios/wiki/experiences/postmortems/`) -> `brain-aios/wiki/experiences/postmortems/` with an `INDEX.md`, then remove `brain-aios/wiki/experiences/postmortems/`.
  - Move 8 MCP API cheat sheets (`references/*-api.md`) -> `brain-aios/wiki/mcp-servers/`.
  - Move framework guides (`brain-aios/wiki/strategy/3ms-framework.md`, `brain-aios/wiki/sops/aios-architecture-guide.md`, `brain-aios/wiki/sops/utility-scripts.md`, etc.) -> `brain-aios/wiki/sops/` and `wiki/strategy/`.
  - Relocate 1.5MB `23-sites-matrix.json` -> `references/awwwards-research-vault/data/`.
  - Merge root `templates/` into `brain-aios/wiki/templates/`.
  - Archive completed past sprint brainstorms into `brainstorms/archives/`.
- **Rationale & Trade-offs**: Keeps essential root anchors (`EXPANSIONS.md`, `LOOPS.md`) readily accessible while moving all deep knowledge into `brain-aios`, restoring true Obsidian Brain PKM topology.

### Q6 — Skill Instruction Densification & Global Automated Link Refactoring
- **Concept Explained**: Many of the 127 skills were written during earlier, non-reasoning eras with 150–300 lines of repetitive procedural boilerplate ("think about X", "remember Y", duplicate error tables). For Gemini 3.7 Flash with High Reasoning, excessive conversational prompt scaffolding creates cognitive drag and token bloat. 3.7 Flash excels on **High-Signal, Outcome-Oriented Declarative Skills** (5-Part Standard: Frontmatter Triggers -> Parameters & Contracts -> Hard Invariants -> Declarative Steps -> Deterministic Verification Command). Furthermore, moving files to `brain-aios` requires an automated, regex-safe link refactor script (`scripts/aios_link_and_skill_optimizer.py`) to dry-run, validate, and update all path references across all `.agents/skills/`, `scripts/`, and `context/` files in one atomic pass.
- **Asked**: How should we execute the skill densification and global link refactoring?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Automated Python Link Refactor + High-Signal Skill Densification.
     - Deploy `scripts/aios_link_and_skill_optimizer.py` to update all path references across all skills, scripts, and context files.
     - Densify skills to the 5-Part Standard (stripping conversational filler, duplicate tables, and verbose handholding, while keeping 100% of capabilities, security boundaries, zero-emoji rules, and verification checks).
     - Run automated verification sweeps (`scripts/verify_skills.py` and `scripts/aios_master_runner.py health`).
  2. Option B: Automated Link Refactoring Only (Update paths, keep skill instructions as-is).
  3. Option C: Manual File-by-File Review.
- **Captured Decision**: Option A — Automated Python Link Refactor + High-Signal Skill Densification. Deploy `scripts/aios_link_and_skill_optimizer.py` to update all paths across skills, scripts, and context files, and densify master skills to the 5-Part High-Signal Standard.
- **Rationale & Trade-offs**: Eliminates broken links, slashes skill token footprints by 40-60%, and maximizes Gemini 3.7 Flash High reasoning speed and precision.

### Q7 — Autonomous Self-Upgrading Skill Engine (10x Compound Mastery Loop)
- **Concept Explained**: To make every skill get 10x more powerful with each run, we design a closed-loop **Autonomous Skill Auto-Evolution Engine** (`scripts/aios_skill_evolver.py`). At the conclusion of any skill run (e.g. `/website-design-engine`, `/tdd`, `/MW01-zero-subscription-client-os`), the system evaluates execution telemetry (tool errors resolved, operator feedback, new script flags discovered). To prevent prompt poisoning, semantic drift, or YAML corruption, mutations are strictly confined to a dedicated `## ⚡ Learned Edge Cases & Execution Recipes` section with an immutable invariant lock (Zero-Emoji, Vibesec boundaries cannot be weakened) and a 5-item LRU (Least Recently Used) capacity limit with automated schema validation and rollback backup (`SKILL.md.bak`).
- **Asked**: How should we configure and deploy the Autonomous Self-Upgrading Skill Engine?
- **Options Provided**:
  1. Option A [RECOMMENDED]: Dedicated Python Compiler Engine (`scripts/aios_skill_evolver.py`) + Guarded Mutation Grammar.
     - Deploy `scripts/aios_skill_evolver.py` with YAML schema validation, token size ceiling (<120 lines), immutable invariant locks, and automatic `.bak` rollbacks.
     - Add standardized post-execution auto-evolution hooks to all Tier 1 Master Skills.
     - Use 5-slot LRU pruning so skills stay hyper-dense and only retain the highest-impact real-world recipes.
  2. Option B: Centralized Heuristic Store (Keep SKILL.md static and save learned rules into a central `brain-aios/wiki/sops/learned_heuristics.json`).
  3. Option C: Manual Skill Upgrades via `/improve-system` only.
- **Captured Decision**: Option A (Enhanced) — Autonomous Self-Upgrading Skill Engine via Post-Execution `/roast` & Web Research Discovery Loop.
  - At the conclusion of a skill run, the system triggers a post-execution auto-evolution cycle:
    1. **Adversarial Audit (`/roast <skill> --deep`)**: Red-teams the executed output and identifies capability bottlenecks.
    2. **Active Web Research (`search_web`)**: Queries bleeding-edge industry benchmarks, newest API versions, and community standards.
    3. **Cross-Skill Synergy Synthesis**: Identifies integrations with adjacent workspace skills.
    4. **Guarded Compiler (`scripts/aios_skill_evolver.py`)**: Compiles the distilled 10x capability into the skill's `## ⚡ Learned Edge Cases & Execution Recipes` section with YAML schema validation, invariant locks, and 5-slot LRU pruning (<120 lines).
- **Rationale & Trade-offs**: Empowers skills to autonomously discover new state-of-the-art patterns from the live web and cross-skill synergies, continuously compounding in strength without human intervention or prompt bloat.

## Open Flags & Deferred Decisions
- [x] System prompt deduplication and token optimization (Resolved in Q1: Hybrid Invariant Core + JIT Domain Bundles)
- [x] Skill library consolidation and alias cleanup (.agents/skills) (Resolved in Q2: Option A Master Skills + Aliases)
- [x] Vault architecture and root information realignment (Resolved in Q3: Option A 3-Layer Cleanse)
- [x] Execution rollout strategy and atomic safety staging (Resolved in Q4: Option A 4-Batch Sequential Execution)
- [x] Complete AIOS knowledge migration into `brain-aios` vault (Resolved in Q5: Option A Modified with root EXPANSIONS/LOOPS)
- [x] Skill instruction densification and global automated link refactoring (Resolved in Q6: Option A Link Refactor + 5-Part Standard)
- [x] Autonomous self-upgrading skill engine architecture (Resolved in Q7: Option A Enhanced with `/roast` + Web Search)
- [ ] Final Pre-Coding "YES" confirmation and implementation plan creation









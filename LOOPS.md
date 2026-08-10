# ZORIXEL AIOS Master Loop Playbook Registry (`LOOPS.md`)

This file is the canonical registry for repeatable, self-healing loop playbooks and execution receipts across the ZORIXEL AIOS workspace.

---

## Active Workspace Playbooks

### Playbook 01: TDD Error Sweep (`tdd-sweep`)
- **Category**: Code Quality & Testing
- **Trigger**: Failing unit tests, type errors (`tsc`), or syntax errors during build.
- **Max Passes**: 5
- **Sequence**:
  1. Observe: Capture exact test failure stack trace or compiler error log.
  2. Choose: Select single failing test or error line to fix surgically.
  3. Act: Apply one code edit.
  4. Verify: Re-run test runner (`pytest` / `npm test`).
  5. Record: Log pass result and remaining error count.
  6. Stop: Exit when all tests pass (SUCCESS) or error count remains unchanged for 3 passes (STAGNATED).

### Playbook 02: Documentation & Master Index Sync (`doc-sync`)
- **Category**: Workspace Integrity
- **Trigger**: Creation or modification of codebase modules, skills, or architecture docs.
- **Max Passes**: 3
- **Sequence**:
  1. Observe: Identify modified files across `.agents/skills/`, `references/`, `brainstorms/`, or `context/`.
  2. Choose: Select outdated index file (`00_MASTER_INDEX.md`, `hot.md`, `MEMORY.md`, or `WORKSPACE_MAP.md`).
  3. Act: Update link references and title summaries.
  4. Verify: Execute `python scripts/aios_bootup_context.py`.
  5. Record: Log updated files and verification state.
  6. Stop: Exit when bootup context returns clean with zero broken links (SUCCESS).

### Playbook 03: Playwright Visual QA Sweep (`visual-qa`)
- **Category**: Frontend & UI Design
- **Trigger**: UI changes on web applications, landing pages, or presentation slides.
- **Max Passes**: 4
- **Sequence**:
  1. Observe: Capture 5-viewport Playwright screenshots (Desktop 1440, Laptop 1024, Tablet 768, Mobile 375, Fold 320).
  2. Choose: Select single worst visual defect (typography collision, contrast gap, layout overflow).
  3. Act: Adjust CSS token or layout style.
  4. Verify: Re-run `python scripts/verify_design_milestone.py`.
  5. Record: Log visual score delta and remaining defects.
  6. Stop: Exit when visual score reaches 100% compliance across all 5 viewports (SUCCESS).

### Playbook 04: SecurityOS Anti-Vulnerability Sweep (`security-sweep`)
- **Category**: Security & Hardening
- **Trigger**: Pre-commit security audits, API modifications, or auth changes.
- **Max Passes**: 4
- **Sequence**:
  1. Observe: Run `python scripts/security_os_runner.py audit .` and inspect findings.
  2. Choose: Select highest severity vulnerability (IDOR, SSRF, prompt injection, hardcoded secret).
  3. Act: Apply zero-trust remediation fix.
  4. Verify: Re-run security auditor script.
  5. Record: Log vulnerability remediation delta.
  6. Stop: Exit when 0 Critical and 0 High vulnerabilities remain (SUCCESS).

### Playbook 05: Graphify AST Knowledge Graph Sync (`graphify-sync`)
- **Category**: System Architecture
- **Trigger**: Refactoring or adding structural codebase files.
- **Max Passes**: 2
- **Sequence**:
  1. Observe: Check modified AST node files.
  2. Choose: Target updated package or module directory.
  3. Act: Run `python scripts/graphify_runner.py update .`.
  4. Verify: Run `graphify diff` and inspect topology changes.
  5. Record: Log graph update receipt.
  6. Stop: Exit when AST topology is clean and synchronized (SUCCESS).

---

---

## Master Workflows Registry

### Master Workflow 01: Zero-Subscription Client Operations & Automation OS (`MW01-zero-subscription-client-os`)
- **Blueprint Manual**: [.agents/skills/domain-skills/workflows/MW01_zero_subscription_client_os.md](file:///d:/AI-OS/.agents/skills/domain-skills/workflows/MW01_zero_subscription_client_os.md)
- **Status**: ✅ **ACTIVE & DEPLOYABLE**
- **Skills Combined**: `grill-me` (5–10 Socratic questions per phase) + `roast` (7-persona council per phase) + `zero-paywall-client-os` + `n8n` + `gws-automation-engine` + `notion-sync` + `notion-formula-builder` + `pdf` + `xlsx` + `docx` + `to-questionnaire`.
- **Core Capability**: 100% zero-fee client agency automations using self-hosted n8n (`npx n8n` / Docker), Google Sheets / Supabase / Notion, Apps Script live 2-way sync, automated status-driven Python document engine (`pdf`/`xlsx`/`docx`), WhatsApp/Gmail/SMS webhooks, and interactive HTML + PDF client handoff dashboards. Executes `/grill-me` (5–10 questions) AND `/roast` (7-persona audit) at every single phase before code/asset generation. Proactively prompts operator in chat when new tools/skills are added.

---

## Execution Receipts Log

*No execution receipts logged yet. Receipts will automatically append here upon `/loop-engine` executions.*


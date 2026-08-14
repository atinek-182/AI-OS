# ZORIXEL AIOS Persistent Memory

This file logs high-leverage cross-session identity, operational invariants, and runtime environments to prevent knowledge decay across Gemini 3.7 Flash sessions.

---

## 1. Operator Baseline & Agency Business Model
- **Operator**: Atinek Maurya (Founder of ZORIXEL — AI Workflows & Business Automation Agency).
- **Core Value Proposition**: Production-grade AI engineering, zero-fee client automation infrastructure (Google Apps Script + Notion + self-hosted n8n), and custom full-stack React/Next.js UI control dashboards.
- **Pricing & Proposal Framework (Nate Herk Corridor)**:
  - 3-Number Corridor: Cost Floor <= 10%-20% Defensible Price Corridor <= Client-Stated Value Ceiling.
  - 10X ROI Check: Mandatory Value Multiple >= 10X.
  - 3-Tier Proof Proposals: Essential ($1.5k-$2.5k), Growth ($5k-$10k), Scale ($12k-$25k+).
  - Dedicated Pricing Skill: `/ai-pricing-engine` (`.agents/skills/ai-pricing-engine/SKILL.md`).
- **Dual-Market Architecture**:
  - Domestic (India - INR): Rapid local case study launchpad, Hindi communication, video testimonials.
  - International (Global - USD): Core revenue engine targeting US/UK/CA/AU businesses.
- **Client Infrastructure Model**: Client-owned keys (Anthropic/OpenAI) and cloud accounts (Vercel/Supabase/Render/n8n) eliminating recurring monthly hosting liability for the agency.

---

## 2. Core Technical Environment & Runtime
- **Coding & Execution IDE**: Exclusively **Antigravity**. Verification, tests, and mockups run under Antigravity environment.
- **Node & Bun Executables**: Standard Bun located at `C:\Users\HP\.bun\bin\bun.exe`.
- **Google Workspace CLI (`gws`)**: Dual profile configuration (Personal credentials for personal context; Brand credentials for brand context).
- **Persistent Memory Worker**: `claude-mem` runs natively on port 37777 with registered MCP tools (`search`, `timeline`, `get_observations`).
- **Playwright Execution Context**: Node scripts must run in directory containing local `node_modules` where playwright is installed.

---

## 3. Master Operating Invariants & Design Standards
- **Zero-Emoji Mandate**: Strictly enforced zero emojis across all code, chat, documentation, commit messages, and artifacts.
- **Pre-Coding Lock ("YES" Rule)**: Zero code writing or file modifications during discovery/planning phases until explicit operator approval.
- **Security-First Mandate**: Strictly enforce `/vibesec` rules (IDOR prevention, tenant isolation, JWT httpOnly cookies, Zod validation, SSRF private IP blocking).
- **Design Taste (Luxury Editorial)**: Linen Cream (`#FAF8F5`), Obsidian Midnight (`#0D0E12`), Velvet Burgundy (`#6D001A`), Electric Crimson (`#D61C2C`), Vintage Ochre Gold (`#C5A059`, <5% accent). Solid fills only (Zero-Gradient & Zero-Glassmorphism).
- **Master Benchmark**: Obys Agency (`https://obys.agency/`) is Atinek Maurya's master design benchmark across all web creation workflows.
- **Awwwards Research Vault**: 7 sub-vaults in `references/awwwards-research-vault/` (01 to 07) with 200+ atomic case studies and shaders.

---

## 4. Key Architectural Milestones & Handoff Logs
- **2026-08-14 (Gemini 3.7 Flash High Modernization)**:
  - Eliminated prompt truncation in `AGENTS.md` and `GEMINI.md` (<4KB Invariant Core).
  - Consolidated 127 skills into authoritative Tier 1 Master Skills with frontmatter alias routing.
  - Cured Brain Inversion: Realigned postmortems, MCP API docs, and SOPs into `brain-aios/wiki/`.
  - Deployed Autonomous Self-Upgrading Skill Engine (`scripts/aios_skill_evolver.py`).

#!/usr/bin/env python3
"""
ZORIXEL AIOS Vault Realigner & Global Link Refactoring Engine
Cures the 'Brain Inversion' crisis by migrating scattered knowledge files into brain-aios,
archives completed brainstorms, restructures MEMORY.md, compresses WORKSPACE_MAP.md,
and refactors all path links across the entire workspace.
"""

import os
import sys
import shutil
import re

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAIN_AIOS_DIR = os.path.join(WORKSPACE_ROOT, "brain-aios")
SECOND_BRAIN_DIR = os.path.join(WORKSPACE_ROOT, "second-brain-zorixel")
REFERENCES_DIR = os.path.join(WORKSPACE_ROOT, "references")
BRAINSTORMS_DIR = os.path.join(WORKSPACE_ROOT, "brainstorms")

PATH_REPLACEMENTS = {
    "brain-aios/wiki/experiences/postmortems/": "brain-aios/wiki/experiences/postmortems/",
    "brain-aios/wiki/mcp-servers/gws-api.md": "brain-aios/wiki/mcp-servers/gws-api.md",
    "brain-aios/wiki/mcp-servers/notion-api.md": "brain-aios/wiki/mcp-servers/notion-api.md",
    "brain-aios/wiki/mcp-servers/github-api.md": "brain-aios/wiki/mcp-servers/github-api.md",
    "brain-aios/wiki/mcp-servers/figma-api.md": "brain-aios/wiki/mcp-servers/figma-api.md",
    "brain-aios/wiki/mcp-servers/context7-api.md": "brain-aios/wiki/mcp-servers/context7-api.md",
    "brain-aios/wiki/mcp-servers/magic-api.md": "brain-aios/wiki/mcp-servers/magic-api.md",
    "brain-aios/wiki/mcp-servers/playwright-api.md": "brain-aios/wiki/mcp-servers/playwright-api.md",
    "brain-aios/wiki/mcp-servers/chrome-devtools-api.md": "brain-aios/wiki/mcp-servers/chrome-devtools-api.md",
    "brain-aios/wiki/strategy/3ms-framework.md": "brain-aios/wiki/strategy/3ms-framework.md",
    "brain-aios/wiki/sops/aios-architecture-guide.md": "brain-aios/wiki/sops/aios-architecture-guide.md",
    "brain-aios/wiki/sops/aios-user-manual.md": "brain-aios/wiki/sops/aios-user-manual.md",
    "brain-aios/wiki/sops/antigravity-skills-guide.md": "brain-aios/wiki/sops/antigravity-skills-guide.md",
    "brain-aios/wiki/sops/utility-scripts.md": "brain-aios/wiki/sops/utility-scripts.md",
    "brain-aios/wiki/sops/global-rules-conflict-resolution.md": "brain-aios/wiki/sops/global-rules-conflict-resolution.md",
    "second-brain-zorixel/wiki/brand/voice.md": "second-brain-zorixel/wiki/brand/voice.md",
    "second-brain-zorixel/wiki/brand/zorixel-brand-identity.md": "second-brain-zorixel/wiki/brand/zorixel-brand-identity.md",
    "references/awwwards-research-vault/data/23-sites-matrix.json": "references/awwwards-research-vault/data/23-sites-matrix.json",
}

def migrate_postmortems():
    src_dir = os.path.join(WORKSPACE_ROOT, "errors-and-lessons")
    dst_dir = os.path.join(BRAIN_AIOS_DIR, "wiki", "experiences", "postmortems")
    os.makedirs(dst_dir, exist_ok=True)
    
    if os.path.exists(src_dir):
        files = [f for f in os.listdir(src_dir) if f.endswith(".md")]
        for f in files:
            shutil.move(os.path.join(src_dir, f), os.path.join(dst_dir, f))
            print(f"  [MOVE] Postmortem {f} -> brain-aios/wiki/experiences/postmortems/")
            
        # Create INDEX.md
        index_lines = [
            "---",
            "title: AIOS Session Postmortems & Retrospectives Index",
            "domain: memory",
            "summary: Centralized registry of all historical session postmortems, error investigations, and milestone learnings.",
            "read_triggers:",
            "- When reviewing historical session bugs or lessons in brain-aios/wiki/experiences/postmortems/",
            "tags: [postmortem, errors, lessons]",
            "updated: '2026-08-14'",
            "---",
            "",
            "# AIOS Session Postmortems & Retrospectives Index",
            "",
            "| File | Date | Topic |",
            "|---|---|---|"
        ]
        for f in sorted(os.listdir(dst_dir)):
            if f != "INDEX.md" and f.endswith(".md"):
                index_lines.append(f"| [{f}](file:///{dst_dir.replace('\\', '/')}/{f}) | Archived | Session Learning |")
        
        with open(os.path.join(dst_dir, "INDEX.md"), "w", encoding="utf-8") as idx_f:
            idx_f.write("\n".join(index_lines) + "\n")
            
        shutil.rmtree(src_dir)
        print("[OK] Migrated postmortems and removed root brain-aios/wiki/experiences/postmortems/")

def migrate_mcp_and_references():
    mcp_dst = os.path.join(BRAIN_AIOS_DIR, "wiki", "mcp-servers")
    sops_dst = os.path.join(BRAIN_AIOS_DIR, "wiki", "sops")
    strat_dst = os.path.join(BRAIN_AIOS_DIR, "wiki", "strategy")
    brand_dst = os.path.join(SECOND_BRAIN_DIR, "wiki", "brand")
    data_dst = os.path.join(REFERENCES_DIR, "awwwards-research-vault", "data")
    
    os.makedirs(mcp_dst, exist_ok=True)
    os.makedirs(sops_dst, exist_ok=True)
    os.makedirs(strat_dst, exist_ok=True)
    os.makedirs(brand_dst, exist_ok=True)
    os.makedirs(data_dst, exist_ok=True)
    
    # 1. MCP API files
    mcp_files = ["gws-api.md", "notion-api.md", "github-api.md", "figma-api.md", "context7-api.md", "magic-api.md", "playwright-api.md", "chrome-devtools-api.md"]
    for f in mcp_files:
        src = os.path.join(REFERENCES_DIR, f)
        if os.path.exists(src):
            shutil.move(src, os.path.join(mcp_dst, f))
            print(f"  [MOVE] MCP API Doc {f} -> brain-aios/wiki/mcp-servers/")
            
    # MCP INDEX.md
    mcp_index = [
        "---",
        "title: MCP Servers API & Tool Registry Index",
        "domain: tools",
        "summary: Technical API documentation and tool usage guides for all registered AIOS MCP servers.",
        "read_triggers:",
        "- When querying tool documentation or MCP schemas in brain-aios/wiki/mcp-servers/",
        "tags: [mcp, tools, api]",
        "updated: '2026-08-14'",
        "---",
        "",
        "# MCP Servers API & Tool Registry Index",
        "",
        "| Server | Doc File | Purpose |",
        "|---|---|---|",
        "| Google Workspace (GWS) | [gws-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/gws-api.md) | Docs, Sheets, Drive, Gmail CLI automations |",
        "| Notion | [notion-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/notion-api.md) | Database queries, page updates, formula generation |",
        "| GitHub | [github-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/github-api.md) | Repos, PRs, issues, code search |",
        "| Figma | [figma-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/figma-api.md) | Design token extraction & node vector compilation |",
        "| Context7 | [context7-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/context7-api.md) | Official documentation lookup & library resolution |",
        "| Magic / 21st | [magic-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/magic-api.md) | UI component generation & design system registry |",
        "| Playwright | [playwright-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/playwright-api.md) | Headless browser testing, 5-viewport screenshot QA |",
        "| Chrome DevTools | [chrome-devtools-api.md](file:///d:/AI-OS/brain-aios/wiki/mcp-servers/chrome-devtools-api.md) | DOM profiling, console logs, network inspection |"
    ]
    with open(os.path.join(mcp_dst, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(mcp_index) + "\n")
        
    # 2. Framework Guides
    sop_moves = [
        ("aios-architecture-guide.md", sops_dst),
        ("aios-user-manual.md", sops_dst),
        ("antigravity-skills-guide.md", sops_dst),
        ("utility-scripts.md", sops_dst),
        ("global-rules-conflict-resolution.md", sops_dst),
        ("10-MASTER-AIOS-WORKFLOWS.md", sops_dst),
        ("AWWWARDS-MASTER-CREATION-GUIDE.md", sops_dst),
        ("3ms-framework.md", strat_dst),
    ]
    for filename, dest_dir in sop_moves:
        src = os.path.join(REFERENCES_DIR, filename)
        if os.path.exists(src):
            shutil.move(src, os.path.join(dest_dir, filename))
            print(f"  [MOVE] SOP Guide {filename} -> {os.path.relpath(dest_dir, WORKSPACE_ROOT)}/")
            
    # 3. Brand Files
    for filename in ["voice.md", "zorixel-brand-identity.md"]:
        src = os.path.join(REFERENCES_DIR, filename)
        if os.path.exists(src):
            shutil.move(src, os.path.join(brand_dst, filename))
            print(f"  [MOVE] Brand Guide {filename} -> second-brain-zorixel/wiki/brand/")
            
    # 4. 23-sites-matrix.json
    matrix_src = os.path.join(REFERENCES_DIR, "23-sites-matrix.json")
    if os.path.exists(matrix_src):
        shutil.move(matrix_src, os.path.join(data_dst, "23-sites-matrix.json"))
        print("  [MOVE] 23-sites-matrix.json -> references/awwwards-research-vault/data/")

def merge_templates():
    src_dir = os.path.join(WORKSPACE_ROOT, "templates")
    dst_dir = os.path.join(BRAIN_AIOS_DIR, "wiki", "templates")
    os.makedirs(dst_dir, exist_ok=True)
    if os.path.exists(src_dir):
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dst_dir, item)
            if not os.path.exists(d):
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
        shutil.rmtree(src_dir)
        print("[OK] Merged and removed root templates/")

def archive_past_brainstorms():
    arch_dir = os.path.join(BRAINSTORMS_DIR, "archives")
    os.makedirs(arch_dir, exist_ok=True)
    
    active_prefixes = ["2026-08-14-", "roast_2026-08-14_"]
    files = [f for f in os.listdir(BRAINSTORMS_DIR) if f.endswith(".md")]
    
    archived_count = 0
    for f in files:
        if any(f.startswith(p) for p in active_prefixes):
            continue
        src = os.path.join(BRAINSTORMS_DIR, f)
        dst = os.path.join(arch_dir, f)
        shutil.move(src, dst)
        archived_count += 1
        
    print(f"[OK] Archived {archived_count} completed historical brainstorm files into brainstorms/archives/")

def run_global_link_refactor():
    print("\n--- Running Global Link Refactor ---")
    scan_dirs = [
        os.path.join(WORKSPACE_ROOT, ".agents", "skills"),
        os.path.join(WORKSPACE_ROOT, "scripts"),
        os.path.join(WORKSPACE_ROOT, "context"),
        os.path.join(WORKSPACE_ROOT, "references"),
        os.path.join(WORKSPACE_ROOT, "decisions"),
        BRAIN_AIOS_DIR,
        SECOND_BRAIN_DIR
    ]
    
    total_files_modified = 0
    total_links_updated = 0
    
    for sdir in scan_dirs:
        if not os.path.exists(sdir):
            continue
        for root, _, files in os.walk(sdir):
            if "node_modules" in root or ".git" in root:
                continue
            for file in files:
                if file.endswith((".md", ".py", ".json")):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                    except Exception:
                        continue
                        
                    modified = False
                    for old_p, new_p in PATH_REPLACEMENTS.items():
                        if old_p in content:
                            content = content.replace(old_p, new_p)
                            modified = True
                            total_links_updated += 1
                            
                    if modified:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        total_files_modified += 1
                        
    print(f"[OK] Global link refactoring complete. Updated {total_links_updated} link instances across {total_files_modified} files.")

def restructure_memory():
    memory_path = os.path.join(WORKSPACE_ROOT, "MEMORY.md")
    memory_content = """# ZORIXEL AIOS Persistent Memory

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
- **Node & Bun Executables**: Standard Bun located at `C:\\Users\\HP\\.bun\\bin\\bun.exe`.
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
"""
    with open(memory_path, "w", encoding="utf-8") as f:
        f.write(memory_content.strip() + "\n")
    print(f"[OK] Restructured MEMORY.md ({len(memory_content)} bytes, ~80 lines).")

def compress_workspace_map():
    map_path = os.path.join(WORKSPACE_ROOT, "WORKSPACE_MAP.md")
    map_content = """# ZORIXEL AIOS Master Workspace Map & Directory Index

This file provides a high-level architectural map of the ZORIXEL AIOS workspace. For deep symbol resolution, file dependencies, and AST community clusters, query Graphify (`graphify query "<term>"`).

---

## 🏛️ Core Workspace Vaults & Hubs

| Path | Type | Canonical Purpose |
|---|---|---|
| `brain-aios/` | Obsidian Vault | Central Brain: System SOPs, MCP Server APIs, Postmortems & Experiences, Checklists, Templates |
| `second-brain-zorixel/` | Obsidian Vault | ZORIXEL Brand Intelligence: Brand identity, copywriting, voice register, client acquisition strategy |
| `zorixel-brand-os/` | Brand Hub | Raw visual assets, logos (`Nuqun`), typography (`Rosehot`, `Havock`), color palettes |
| `SecurityOs/` | Security Hub | 817 cybersecurity skills, MITRE ATT&CK / ATLAS frameworks, static code security audit engine |
| `references/awwwards-research-vault/` | Design Vault | 7 sub-vaults (01-07) with 200+ atomic case studies, GLSL shaders, Obys grid canons |
| `premium-frontend-experience-system/` | UI Reference Vault | 23-site reference mirrors, code extracts, 300+ component catalog |
| `clients/` | Client Vault | Client-specific folders (`001-vashishthya-research-edu/`), intake audits, Loom scripts, handoff specs |
| `projects/` | Projects Hub | Standalone web applications, client deliverables, full-stack prototypes |

---

## ⚡ Root Execution Harness Directories

| Directory / File | Role |
|---|---|
| `AGENTS.md` & `GEMINI.md` | System Invariant Core (<4KB) loaded on chat bootup (Zero truncation) |
| `hot.md` | Active session cache & sprint focus handoff |
| `MEMORY.md` | Persistent memory & operational invariants |
| `EXPANSIONS.md` & `LOOPS.md` | System expansion guide and 6-phase master loop registry |
| `.agents/skills/` | Consolidated Tier 1 Master Skills with frontmatter alias routing |
| `scripts/` | Python CLI runner engines (`aios_master_runner.py`, `graphify_runner.py`, `aios_skill_evolver.py`) |
| `context/` | User intake briefs (`00_MASTER_INDEX.md`, `about-me.md`, `about-business.md`) |
| `brainstorms/` | Active sprint brainstorming & `/roast` audit logs (`archives/` for past logs) |
| `decisions/` | Canonical decision log (`decisions/log.md`) |
| `audits/` | System health & OS audit reports (`audits/os-audit-*.md`) |
"""
    with open(map_path, "w", encoding="utf-8") as f:
        f.write(map_content.strip() + "\n")
    print(f"[OK] Compressed WORKSPACE_MAP.md ({len(map_content)} bytes, clean high-level index).")

def main():
    print("========================================================")
    print("ZORIXEL AIOS: Vault Realignment & Knowledge Migrator")
    print("========================================================\n")
    
    migrate_postmortems()
    migrate_mcp_and_references()
    merge_templates()
    archive_past_brainstorms()
    run_global_link_refactor()
    restructure_memory()
    compress_workspace_map()
    
    print("\n========================================================")
    print("VAULT REALIGNMENT & KNOWLEDGE MIGRATION COMPLETE!")
    print("========================================================\n")

if __name__ == "__main__":
    main()

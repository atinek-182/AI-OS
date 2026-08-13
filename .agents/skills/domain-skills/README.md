---
title: AI-OS Domain Skills Registry
domain: skill
summary: This directory contains pre-recorded, site-specific operational procedures (SOPs), DOM selector maps, and edge-case
  handling rules for web automation. Each site domain gets a dedicated folder named after its primary hostname slug (e.g.
  `github`, `lin
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- AI-OS Domain Skills Registry
- Folder Structure
- How It Works
- Adding a Domain Skill
read_triggers:
- When working on skill in .agents/skills/domain-skills/README.md
- When reading context for AI-OS Domain Skills Registry
tags:
- skill
- README
updated: '2026-08-08'
---

# AI-OS Domain Skills Registry

This directory contains pre-recorded, site-specific operational procedures (SOPs), DOM selector maps, and edge-case handling rules for web automation.

## Folder Structure

Each site domain gets a dedicated folder named after its primary hostname slug (e.g. `github`, `linkedin`, `notion`, `figma`, `vercel`):

```text
.agents/skills/domain-skills/
  ├── github/
  │   └── SOP.md
  ├── linkedin/
  │   └── SOP.md
  └── notion/
      └── SOP.md
```

## How It Works

When any AI-OS Playwright or browser agent navigates to a URL (e.g., `https://github.com/zorixel/ai-os`), `scripts/aios_browser_engine.py` calls `get_domain_skills(url)`.

If a matching domain folder exists under `.agents/skills/domain-skills/<domain_slug>/`, all matching Markdown files in that folder are automatically loaded and injected into the agent prompt, providing pre-verified selectors and site navigation rules without re-exploring the DOM.

## Adding a Domain Skill

When an agent completes a complex navigation or interaction flow on a site:
1. Create `.agents/skills/domain-skills/<domain_slug>/SOP.md`.
2. Document key CSS selectors, modal handling rules, and multi-step form navigation paths.

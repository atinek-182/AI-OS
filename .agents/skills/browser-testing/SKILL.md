---
title: AI-OS Browser Automation & Testing Standard
domain: skill
summary: This skill establishes the standard execution protocol for browser automation, visual QA, and form interaction across
  AI-OS using Playwright and `scripts/aios_browser_engine.py`. When interacting with React, Vue, or Ember state-managed forms,
  standar
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- AI-OS Browser Automation & Testing Standard
- Core Execution Guidelines
- 1. Framework-Aware Input Filling
- Generate pure JS snippet and execute inside Playwright page context
- 2. Domain Skill Resolution
read_triggers:
- When executing browser automation or visual regression testing in AI-OS
tags:
- browser
- testing
- playwright
- aios_browser_engine
updated: '2026-08-08'
name: browser-testing
description: Guidelines and utility standards for web browser testing, page interaction, and visual QA in AI-OS using Playwright
  and aios_browser_engine.py.
---

# AI-OS Browser Automation & Testing Standard

This skill establishes the standard execution protocol for browser automation, visual QA, and form interaction across AI-OS using Playwright and `scripts/aios_browser_engine.py`.

## Core Execution Guidelines

### 1. Framework-Aware Input Filling
When interacting with React, Vue, or Ember state-managed forms, standard `.fill()` may fail to trigger framework state listeners. Always use `fill_framework_input_js(selector, text)` from `scripts/aios_browser_engine.py` to inject values via prototype setters and dispatch synthetic `input` and `change` events.

```python
from scripts.aios_browser_engine import fill_framework_input_js

# Generate pure JS snippet and execute inside Playwright page context
js_code = fill_framework_input_js("#search-input", "ZORIXEL AI Agency")
page.evaluate(js_code)
```

### 2. Domain Skill Resolution
Before navigating to a target URL for automated interaction, run `get_domain_skills(url)` to load pre-recorded DOM selectors and site SOPs:

```python
from scripts.aios_browser_engine import get_domain_skills

skills = get_domain_skills("https://github.com/zorixel")
for s in skills:
    print(f"Loaded SOP: {s['filename']} for domain {s['domain']}")
```

### 3. Visual Click Debug Overlays
When debugging element click accuracy in headless browser tests, draw crosshair targets on screenshot artifacts using `capture_debug_click`:

```python
from scripts.aios_browser_engine import capture_debug_click

# Overlay red crosshair target at (x=240, y=180) on screenshot artifact
capture_debug_click("artifacts/test_run.png", 240, 180)
```

### 4. Non-Blocking Dialog Handling
To prevent native browser popups (`alert`, `confirm`, `prompt`, `beforeunload`) from hanging the execution thread, attach `setup_dialog_handler(page)` prior to page actions.

### 5. Automatic Site-Specific Domain Skill Integration
Whenever new web automation scripts, CSS selector maps, or site interaction SOPs are added for any domain (e.g. GitHub, LinkedIn, Notion, Vercel, Stripe), automatically structure and save them under `.agents/skills/domain-skills/<domain_slug>/SOP.md`. Future browser automation runs will automatically resolve and inject these domain skills via `get_domain_skills(url)`.

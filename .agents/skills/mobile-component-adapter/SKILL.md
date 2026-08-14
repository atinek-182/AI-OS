---
name: mobile-component-adapter
description: Canonical process skill for auditing and adapting third-party UI component references for 95% mobile-first performance, fluid relative units, touch interactions, SecurityOS compliance, and 3-stage /roast red-teaming.
title: Mobile Component Adapter & Audit Engine (`/mobile-component-adapter`)
domain: skill
summary: Canonical process skill for auditing and adapting third-party UI component references for 95% mobile-first performance, fluid relative units, touch interactions, SecurityOS compliance, and 3-stage /roast red-teaming.
critical_directives:
  - Do NOT write implementation code until explicit operator approval ('YES').
  - Run the full /roast skill 3 separate times across 3 distinct lifecycle stages.
  - Enforce SecurityOS (/vibesec) verification on all mobile component feature specs.
  - Enforce zero hardcoded px units on mobile viewports (< 768px). Use clamp(), rem, vw, vh, and %.
  - Wrap desktop hover states inside @media (hover: hover) and (pointer: fine).
  - Enforce zero emojis across all generated reports, code specs, and documentation.
section_outline:
  - Overview & Tri-Mode Execution
  - Execution Pipeline (Phase 0 to Phase 5)
  - The 3-Stage Full /roast Invocation Loop
  - WebGL & GPU Mobile Safeguards
  - Hybrid Responsive Typography Standard
  - Output Artifact Schema
read_triggers:
  - When working on skill in .agents/skills/mobile-component-adapter/SKILL.md
  - When reading context for Mobile Component Adapter & Audit Engine (`/mobile-component-adapter`)
tags:
  - skill
  - SKILL
  - mobile-first
  - component-adapter
updated: '2026-08-13'
---

# Mobile Component Adapter & Audit Engine (`/mobile-component-adapter`)

## Overview & Tri-Mode Execution

The `/mobile-component-adapter` skill is the canonical discovery and adaptation gate for converting desktop UI component references into high-converting, 95% Mobile-First React TypeScript (`.tsx`) specifications.

Invokable via:
- **Slash Command**: `/mobile-component-adapter [component_name_or_path]`
- **Dynamic Intent Matching**: Auto-triggered whenever an external UI component is ingested, analyzed, or prepared for mobile conversion.
- **Inter-Skill Calling**: Invoked programmatically by `/website-design-engine`, `/ingest-repo`, `/scrape-component`, `/six-file-context-methodology`.

---

## The 3-Stage Full `/roast` Invocation Loop

This skill executes the full 5-persona `/roast` council **3 SEPARATE TIMES** across 3 distinct lifecycle stages:

| Stage | Focus & Scope | Command | Auto-Patch Rule |
| --- | --- | --- | --- |
| **Stage 1** | Pre-Flight & Raw Desktop Reference Audit | `/roast [component] --domain code` | Halts and auto-patches desktop hover traps, fixed `px` layouts, non-GPU CSS animations, and memory leaks. |
| **Stage 2** | Fluid Relative Units & Touch Ergonomics Audit | `/roast [component] --domain copy` | Halts and auto-patches un-clamped typography, missing 48px touch targets, and un-encapsulated hover states. |
| **Stage 3** | Technical Feature Spec & SecurityOS Audit | `/roast [component] --domain code --deep` | Halts and auto-patches SecurityOS violations (`/vibesec`), missing `gsap.context()` cleanup handlers, and input sanitization gaps. |

---

## Step-by-Step Execution Pipeline

### Phase 0: 390px Mobile Viewport Pre-Flight Check
1. Target single component path or name (e.g. `reference/side-navigation-with-wipe-effectosmo`).
2. Inspect raw HTML, CSS, and JS source files.
3. Identify desktop-only pitfalls:
   - Desktop mousemove or hover event listeners.
   - Non-composite CSS animations (`height`, `width`, `top`, `left`, `margin`, `box-shadow`).
   - Fixed `px` dimensions or un-responsive containers.
   - Missing GPU context cleanup handlers.

### Phase 1: STORM 7-Lens Mobile Motion & Network Research
Synthesize a 7-lens research briefing covering:
- **Systems Architect**: Mobile-first hydration, touch bounding area (48px x 48px min).
- **Vibesec Security Pen-Tester**: Form input sanitization, CSRF mitigation, safe URL routing.
- **DB & Scaling Specialist**: Asset payload optimization (< 85KB JS initial load), Zero CLS.
- **Frontend UX & Motion Lead**: Hover isolation (`@media (hover: hover)`), touch micro-presses (`:active { transform: scale(0.97); }`), 60 FPS GPU acceleration (`translate3d`, `opacity`, `will-change`).
- **Product & SaaS Economist**: Sticky mobile action bar (`1-Click WhatsApp Desk` + `Call Office Desk`).
- **AI Latency Specialist**: Mobile FCP < 0.9s on 4G networks.
- **Developer Ergonomics Auditor**: Scoped CSS Modules (`styles.module.css`).

Save briefing to `storm-reports/{component-slug}-mobile-briefing.html`.

### Phase 2: Stage 1 Roast Audit (`/roast --domain code`)
Run `/roast [component] --domain code`. If verdict is `RESHAPE` or `KILL`, generate `ROAST_REFINEMENT_SPEC` and apply required fixes before proceeding.

### Phase 3: Stage 2 Roast Audit (`/roast --domain copy`)
Run `/roast [component] --domain copy`. Verify fluid relative typography (`clamp()`, `rem`, `vw`, `vh`) and touch interaction feedback. Apply required fixes.

### Phase 4: Stage 3 Roast & SecurityOS Audit (`/roast --domain code --deep`)
Run `/roast [component] --domain code --deep`. Verify SecurityOS compliance (`/vibesec`), Zod input schemas, and React `gsap.context()` unmount handlers.

### Phase 5: Technical Feature Spec Generation
Compile output feature specification to `context/specs/SPEC-{component-slug}.md`.

---

## WebGL & GPU Mobile Safeguards

For WebGL, Three.js, or 3D Canvas components on mobile (< 768px):
1. Clamp device pixel ratio: `const dpr = Math.min(window.devicePixelRatio, 1.5);`.
2. Reduce particle count / polygon complexity by 60% on touch viewports.
3. Pause animation frame loops when offscreen using `IntersectionObserver`.

---

## Hybrid Responsive Typography Standard

- **Desktop Protection (`@media (min-width: 1024px)`)**: Keeps rigid desktop layout precision locked.
- **Mobile/Tablet Viewports (`< 768px`)**: Uses fluid `clamp(min, preferred, max)` with relative `rem` and `vw` units so text scales down smoothly on 320px–390px screens without horizontal overflow.

---

## Output Artifact Schema (`context/specs/SPEC-{slug}.md`)

```markdown
# Feature Spec: [Component Name] (Mobile-First Adaptation)

## 1. Component Architecture & Dependencies
- Target Stack: Next.js 15 App Router, React 19 TypeScript (`.tsx`), `'use client'`.
- External Libraries: GSAP (`CustomEase`), Lucide React.

## 2. Scoped CSS Module Tokens (`styles.module.css`)
- Dynamic Theme Variables (Supports Dark vs Light hero contrast inversion).
- Fluid Relative Units (`rem`, `vh`, `vw`, `clamp()`).
- Progressive Hover Isolation (`@media (hover: hover) and (pointer: fine)`).
- Active Touch Feedback (`:active { transform: scale(0.97); }`).

## 3. Touch & Animation Lifecycle Guide
- GSAP Timeline definition.
- `useEffect` hook with `gsap.context()` cleanup.
- Escape key and backdrop overlay click handlers.

## 4. SecurityOS & Mobile Performance Verification Checklist
- [ ] Next.js 15 `'use client'` Directive
- [ ] CSS Modules Isolation (`styles.module.css`)
- [ ] Relative Fluid Units Only (`rem`, `em`, `%`, `vw`, `vh`, `clamp()`) — Zero hardcoded `px`
- [ ] Progressive Hover Encapsulation (`@media (hover: hover) and (pointer: fine)`)
- [ ] Mobile Touch Active Micro-Press (`:active { transform: scale(0.97); }`)
- [ ] Minimum 48px Touch Target Area on Mobile Viewports
- [ ] GSAP Memory Cleanup via `gsap.context()` in `useEffect` hook
## Autonomous Skill Evolution & Error Learning Protocol

At the completion of every execution of this skill:

1. **Error & Glitch Pattern Learning**:
   - If a mobile rendering glitch, touch listener bug, or browser layout anomaly (e.g., iOS Safari dynamic toolbar height shifts `100vh` vs `100dvh`) is discovered during auditing or verification:
     - Register the new rule in `references/GLOBAL_ERROR_PREVENTION_RULES.md`.
     - Execute `python scripts/sync_global_rules.py` so all system prompts (`AGENTS.md` and `GEMINI.md`) auto-update workspace-wide.
     - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content`.

2. **Novel Micro-Interaction Harvesting**:
   - Save extracted mobile CSS animation patterns, fluid `clamp()` math formulas, and touch micro-press setups into `references/component-vault/` and `MEMORY.md` to enrich future component specs across AIOS.

3. **Graphify & Decision Log Update**:
   - Run `python scripts/graphify_runner.py build` to update AST knowledge graphs.
   - Record decision receipts and audit scores in `decisions/log.md` and `WORKSPACE_MAP.md`.


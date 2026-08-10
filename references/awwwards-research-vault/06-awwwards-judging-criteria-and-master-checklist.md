---
title: Awwwards Research Vault 06 - Judging Criteria & Master Checklist
domain: reference
summary: Official Awwwards 4-category weighted judging criteria (Design 40%, Usability 30%, Creativity 20%, Content 10%), 5-pass prepare.py scoring harness rubric, and master pre-flight quality checklist for AIOS web creation.
critical_directives:
- Strictly enforce Awwwards 4-category weighting in prepare.py evaluator.
- Incorporate Human-in-the-Loop Visual Rating Gate (Atinek Maurya 1-line feedback) after Playwright 5-viewport sweeps.
- Follow zero-emoji mandate across all checklists, scoring scripts, and receipts.
section_outline:
- Awwwards Research Vault 06 - Judging Criteria & Master Checklist
- Official Awwwards 4-Category Weighted Scoring System
- The 5-Pass prepare.py Evaluator Rubric
- Human-in-the-Loop Visual Rating Gate Protocol
- Master Pre-Flight Quality Checklist
read_triggers:
- When working on reference in references/awwwards-research-vault/06-awwwards-judging-criteria-and-master-checklist.md
- When reading context for Awwwards Judging Criteria & Master Checklist
tags:
- reference
- awwwards
- judging-criteria
- checklist
updated: '2026-08-09'
---

# Awwwards Research Vault 06 - Judging Criteria & Master Checklist

## Overview

This document details the official Awwwards 4-category weighted judging criteria, the `prepare.py` 5-pass scoring rubric, and the master pre-flight quality checklist for AIOS web creation.

---

## Official Awwwards 4-Category Weighted Scoring System

Awwwards Site of the Day submissions are evaluated across 4 weighted categories:

1. **Design (40% Weight)**:
   Visual aesthetics, Obys spatial rhythm (140px vertical padding), poster typography, OKLCH color physics, contrast ratios, and visual hierarchy.
2. **Usability (30% Weight)**:
   Navigation clarity, fast load performance, Core Web Vitals (INP < 200ms, 60fps), responsive layout integrity across 5 viewports (320px to 1920px), and zero broken links.
3. **Creativity (20% Weight)**:
   Originality, custom interactive shaders (`radiant-shaders`), Lenis smooth inertia scroll, GSAP ScrollTrigger scrollytelling, and magnetic micro-physics.
4. **Content (10% Weight)**:
   Copywriting clarity, zero fluff, editorial storytelling, and high-impact visual assets.

---

## The 5-Pass `prepare.py` Evaluator Rubric

The `website-design-engine` v5.1 runs up to 5 passes evaluated by `prepare.py`:

- **Pass 1: Layout & Obys Rhythm (25 Points)**: Obys 140px desktop section padding, 12-column bento grid, Havock/Rosehot display headline typography.
- **Pass 2: Color Math & Textures (20 Points)**: OKLCH dopamine-monochromatic color tokens, 3% SVG noise texture overlay, zero soft gradients, zero glassmorphism.
- **Pass 3: Motion Stack & GSAP (25 Points)**: Lenis smooth scroll initialization, GSAP ScrollTrigger scrollytelling pin cards, split-text character reveals, magnetic cursors.
- **Pass 4: WebGL Stage & Shaders (15 Points)**: Interactive fragment shader canvas stage from `C:\Users\HP\Downloads\Components` or `pbakaus/radiant`.
- **Pass 5: Playwright QA & Anti-Slop Audit (15 Points)**: `hallmark_runner.py` 57 quality gates, Playwright 5-viewport screenshot sweep (320px, 375px, 768px, 1024px, 1440px).

---

## Human-in-the-Loop Visual Rating Gate Protocol

After Pass 5 completes Playwright screenshot sweeps:
1. The engine presents 5-viewport screenshot previews to Atinek Maurya.
2. Atinek Maurya provides a 1-line visual rating (e.g. *"Score 8/10, increase hero headline contrast and adjust bento card 2 gap"*).
3. The engine incorporates the visual feedback for pass refinement if score is `< 90/100` or visual rating is `< 8/10`.

---

## Master Pre-Flight Quality Checklist

- [ ] Obys 140px-160px desktop vertical section padding verified in CSS.
- [ ] Display headlines > 64px specify `line-height: 1.28` and minimum `margin-bottom: 28px`.
- [ ] Zero soft purple/blue gradients or glassmorphism backdrop blurs present.
- [ ] OKLCH color tokens and 3% SVG noise overlay applied.
- [ ] Lenis smooth scroll initialized and synced with GSAP `ScrollTrigger.update`.
- [ ] Animated layers promoted to GPU via `will-change: transform`.
- [ ] WebGL fragment shader canvas stage or ASCII video player embedded.
- [ ] SVG path morphing page transition (`SVG-Page-transition`) and preloader reveal configured.
- [ ] Playwright 5-viewport screenshot sweep passes with 0 visual overflows.
- [ ] Human visual rating >= 8/10 confirmed by Atinek Maurya.
- [ ] Zero emojis across all code, styles, commit messages, and receipts.

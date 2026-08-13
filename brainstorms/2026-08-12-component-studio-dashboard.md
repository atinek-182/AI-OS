# 175+ Component Studio Dashboard & AI Gallery: Discovery & Brainstorm Notes
Date: 2026-08-12 · Goal: Build Codrops-Inspired Visual Component Studio Gallery (`http://127.0.0.1:8080`) & AI Selection Registry · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Vault Location**: `C:\Users\HP\Downloads\Components` (175 component repos across 9 taxonomy categories).
- **Server Architecture**: Lightweight local Python HTTP server (`scripts/start_components_server.py`) strictly bound to `127.0.0.1:8080` with directory traversal protection.
- **Gallery Specs**: Visual Codrops dark-mode UI with live search, 9 category filters, Playwright PNG preview cards, `#001` - `#175` ID badges, and 1-click `[Copy for AI]` prompt buttons.
- **AI Selection Registry**: `components_ai_registry.json` mapping every component ID to tech stack, entry point, animation type, and parametric React refactoring guide.

## Domain Vocabulary & Glossary (`CONTEXT.md` updates)
- **Component Studio Dashboard**: Local web interface serving the 175 component repos with live iframe preview modals and external tab launchers.
- **Component ID**: Canonical 3-digit identifier (`COMP-001` to `COMP-175`) matching taxonomical catalog index.
- **Class 1 Repo**: Pure static HTML/JS/CSS/WebGL repository directly launchable via HTTP server without npm install.
- **Class 2 Repo**: Full-stack Next.js/Vite repository requiring npm dev server build scripts.

## Q&A Log
### Q1 — UI Theme & Visual Aesthetic Architecture
- **Concept Explained**: ZORIXEL brand styling for the Component Studio Dashboard (`index.html`).
- **Captured Decision**: Option A — ZORIXEL Dark Studio (Obsidian Midnight `#0D0E12`, Solid Crimson `#D61C2C` accents, Linen Cream `#FAF8F5` text, Outfit font).

### Q2 — Live Demo Launch Mode
- **Concept Explained**: How components open when clicked from dashboard cards.
- **Captured Decision**: Option B — Direct New Tab Launch (`target="_blank"`) at `http://127.0.0.1:8080/[rel_path]/index.html` for 100% fullscreen canvas resolution.

### Q3 — Automated Playwright Thumbnail Generation
- **Concept Explained**: Playwright screenshot generation timing for 175 components.
- **Captured Decision**: Option A (Modified) — Automated Playwright sweep capturing PNG screenshots into `public/thumbnails/` after an explicit **3.0-second delay** per component to guarantee WebGL, Canvas, and GSAP shaders are 100% initialized.

### Q4 — AI Prompt Copying Format
- **Concept Explained**: Clipboard payload format when clicking `[Copy for AI]`.
- **Captured Decision**: Option A — Full Adaptation Prompt with file path, component ID, description, tech stack, and parametric React refactoring instructions (`'use client'`, CSS Modules, `useEffect` GPU cleanup).

### Q5 — Component Health Classification & Automated Verification
- **Concept Explained**: Differentiating Class 1 static HTML repos (launch directly via HTTP server without npm) from Class 2 build-dependent repos (require `package.json` / `npm install`).
- **Captured Decision**: Automated 2-Tier Health Scanner Script (`scripts/scan_component_health.py`):
  1. **Class 1 (Static Serving)**: Scans for `index.html` at root or in `dist/`/`public/`/`js/`. If present and loads without 404/CORS console errors in Playwright, marked `[STATUS: READY / CLASS-1 STATIC]`.
  2. **Class 2 (NPM Build Required)**: If no static `index.html` exists and `package.json` contains `vite`, `next`, or `webpack`, marked `[STATUS: REQUIRES NPM DEV SERVER / CLASS-2]`.
  3. **Visual Badge Tagging**: Dashboard cards display crisp status badges:
     - `STATIC READY` (Green border + 1-click open)
     - `NPM BUILD REQD` (Amber border + instructions & launch command button)
     - `MISSING ENTRY` (Red border + warning log)


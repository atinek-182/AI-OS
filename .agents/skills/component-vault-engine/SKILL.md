---
title: ZORIXEL AIOS Component Vault & Studio Engine (`component-vault-engine`)
domain: skill
summary: Dedicated master skill and execution protocol for managing, serving, and adapting Atinek Maurya's 175+ hand-picked component vault in C:\Users\HP\Downloads\Components into Next.js/React projects. Enforces 127.0.0.1 localhost server isolation, Playwright visual QA, parametric prop refactoring, GPU memory cleanup, and automated Context7 MCP documentation lookup.
critical_directives:
- ALWAYS bind local Python HTTP server strictly to 127.0.0.1:8080 (loopback interface) with directory traversal protection.
- ALWAYS add 'use client' and return explicit GPU memory cleanup (renderer.dispose(), geometry.dispose(), ScrollTrigger.kill()) in React useEffect.
- ALWAYS scope CSS via CSS Modules (styles.module.css) or Tailwind to prevent global style leakage.
- ALWAYS query Context7 MCP (resolve-library-id, query-docs) automatically before adapting component code.
- NEVER claim a component works without running Playwright headless browser screenshots and verifying 0 console errors.
read_triggers:
- When asked to create, launch, or serve the Component Studio Dashboard gallery in C:\Users\HP\Downloads\Components
- When selecting, adapting, or refactoring any component from the 175+ component vault into Next.js or React
- When querying component_manifest.json or components_ai_registry.json
- When working with Codrops, WebGL, Three.js, GSAP, Lenis, or Anime.js component repos
tags:
- skill
- SKILL
- components
- webgl
- gsap
- nextjs
updated: '2026-08-12'
name: component-vault-engine
description: Master Component Studio Dashboard generator, AI Component Registry manager, and component adaptation engine for Atinek Maurya's 175+ hand-picked component vault in C:\Users\HP\Downloads\Components. Auto-triggered whenever creating the Component Hub gallery or adapting any vault component into Next.js/React.
argument-hint: '[gallery_build | adapt_component COMP-XXX | verify_vault]'
---

# ZORIXEL AIOS Component Vault & Studio Engine (`component-vault-engine`)

## Overview & Operational Purpose

This skill is the permanent operational standard for managing Atinek Maurya's **175+ hand-picked component repositories** located at `C:\Users\HP\Downloads\Components`. It governs:
1. **The Interactive Component Studio Hub**: Generating a Codrops-inspired visual web gallery served over `http://127.0.0.1:8080` with Playwright PNG preview cards, visual `#001` - `#175` numbers, and 1-click `[Copy for AI]` prompt buttons.
2. **Multi-Tech Refactoring Protocol**: Converting raw Anime.js, WebGL, Three.js, Canvas, and GSAP code into reusable React TypeScript (`.tsx`) components with parametric typed props (`headline`, `primaryColor`, `bgImage`).
3. **Empirical Verification & SecurityOS**: Verifying component health via Playwright headless browser sweeps and enforcing strict 127.0.0.1 loopback isolation.

---

## Locked Architectural Decisions (Q1 – Q5)

| Setting / Spec | Selected Choice | Execution Standard |
|---|---|---|
| **Gallery Demo Launch** | **Option A (New Tab)** | Opens live component in a new browser tab (`target="_blank"`) for 100% fullscreen canvas resolution. |
| **Gallery Visual Cards** | **Option A (Playwright PNGs)** | Headless Playwright script takes crisp `.png` screenshots of live components into `public/thumbnails/`. |
| **AI Prompt System** | **Option C (Visual # + Button)** | Cards feature visual numbers (`#001` - `#175`) + 1-click `[Copy for AI]` prompt buttons. |
| **Multi-Demo Nav** | **Option B (Default Demo 1)** | Opens `index.html` by default; uses native Codrops top header nav links for Demo 2/3. |
| **Component Adaptation** | **Option A (Parametric Props)** | Refactors components into React `.tsx` files with typed props (`CustomComponentProps`), keeping 3D math & shaders 100% intact. |

---

## 1. Local HTTP Server & Security OS Protocol (`/vibesec`)

1. **Localhost Loopback Isolation**:
   - The server script `scripts/start_components_server.py` MUST bind strictly to `127.0.0.1:8080` (`server_address = ('127.0.0.1', 8080)`).
   - NEVER bind to `0.0.0.0` or allow external LAN access.
2. **Directory Traversal Protection**:
   - Enforce `os.path.commonpath` checking on all requested URLs to block `../` path climbing outside `C:\Users\HP\Downloads\Components`.
3. **Pure Static Serving**:
   - Pure static HTTP file serving only. Zero dynamic command execution over HTTP.

---

## 2. Multi-Tech React / Next.js Refactoring Standard

When adapting any vault component into a React / Next.js project:

### Rule 2.1: Client Boundary & Hooks
- Always add `'use client';` at the top of any component file importing Three.js, WebGL shaders, Canvas, or GSAP.

### Rule 2.2: CSS Isolation & Scoping
- Never import raw global `.css` files.
- Refactor styling into **CSS Modules** (`[component].module.css`) or inline Tailwind classes to prevent global CSS collisions.

### Rule 2.3: GPU Memory & Animation Cleanup
- Every `useEffect` or `useGSAP` hook initializing Three.js or GSAP MUST return a cleanup function:
  ```typescript
  useEffect(() => {
    // ... Three.js / GSAP setup ...
    return () => {
      renderer.dispose();
      geometry.dispose();
      material.dispose();
      ScrollTrigger.getAll().forEach(t => t.kill());
    };
  }, []);
  ```

### Rule 2.4: Barba.js Replacement in Next.js
- Replace Barba.js PJAX page routing with Next.js native `template.tsx` + Framer Motion / GSAP FLIP page transitions.

### Rule 2.5: Automated Context7 MCP Documentation Sourcing
- Before writing or modifying third-party library code (Three.js, GSAP, Anime.js, Lenis, Motion), the agent MUST automatically invoke `context7` (`resolve-library-id` -> `query-docs`).

---

## 3. Empirical Playwright Visual QA Protocol

Before claiming any component is ready:
1. Launch `scripts/aios_browser_engine.py` or Playwright Node runner against `http://127.0.0.1:8080/[rel_path]`.
2. Inspect Playwright devtools console logs for JavaScript errors or 404 resource failures.
3. Capture a visual PNG screenshot. Verify non-blank canvas output.

---

## 4. Auto-Evolution & Skill Maintenance

At the completion of every component adaptation task:
1. Append any new edge-case fixes or shader optimizations to `references/component-adaptation-rules.md`.
2. Update `SKILL.md` with newly learned component patterns.

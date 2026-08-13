# ZORIXEL AIOS Component Adaptation Rules Registry (`references/component-adaptation-rules.md`)
Date: 2026-08-12 · Domain: WebGL, Three.js, GSAP, Canvas, React & Next.js 15 App Router

## Core Refactoring Rules
1. **'use client' Boundary**: Always prepend `'use client';` to all motion/shader component files.
2. **CSS Module Scoping**: Never pollute global CSS namespace. Refactor Codrops styles to `[Component].module.css`.
3. **GPU Memory Cleanup**: Always dispose of Three.js geometry, material, texture, and WebGLRenderer instances on unmount.
4. **Context 7 Pre-Flight**: Automatically query `context7` (`resolve-library-id`, `query-docs`) before generating third-party animation code.
5. **Parametric Props Standard**: Expose `headline`, `subheadline`, `primaryColor`, `accentColor`, `bgImage` as props while preserving math and shaders 100%.

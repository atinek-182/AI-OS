---
title: Awwwards Research Vault 05 - Case Studies, Tutorials & Component Ingestion
domain: reference
summary: Research document compiling case studies of Site of the Day winners, step-by-step tutorials for Lenis/GSAP/WebGL, and codebase ingestion notes for 24 local components in C:\Users\HP\Downloads\Components.
critical_directives:
- Sourcing components: Primary source is local Awwwards vault (C:\Users\HP\Downloads\Components). Generic 300+ component library is permanently discarded.
- Index 24 local component repositories for Awwwards builds.
- Follow zero-emoji mandate across all case studies and code breakdowns.
section_outline:
- Awwwards Research Vault 05 - Case Studies, Tutorials & Component Ingestion
- Case Studies of Site of the Day Winners
- Tutorials & Technical Breakdown Index
- Local Component Ingestion Registry (C:\Users\HP\Downloads\Components)
read_triggers:
- When working on reference in references/awwwards-research-vault/05-awwwards-case-studies-and-tutorials.md
- When reading context for Awwwards Case Studies, Tutorials & Component Ingestion
tags:
- reference
- awwwards
- case-studies
- tutorials
- components
updated: '2026-08-09'
---

# Awwwards Research Vault 05 - Case Studies, Tutorials & Component Ingestion

## Overview

This research document compiles real-world case studies of Awwwards Site of the Day winners, step-by-step technical tutorials, and codebase mapping for the 24 local component repositories in `C:\Users\HP\Downloads\Components`.

---

## Case Studies of Site of the Day Winners

### Case Study 1: Obys Agency (`Obys-clone`)
- **Award**: Site of the Month / Developer of the Year.
- **Key Breakthrough**: Poster-style display typography combined with left-aligned body baselines and Obys spatial rhythm (140px vertical section padding).
- **Lessons**: Typography is visual graphic art. Generous section padding creates luxury editorial feel.

### Case Study 2: Spylt Awwwards Showcase (`Spylt-awward-clone`)
- **Award**: Site of the Day.
- **Key Breakthrough**: 12-column asymmetric bento grid layout with 3D card tilt and scroll-triggered depth stacking.
- **Lessons**: Bento cards must feature subtle 3D tilt micro-physics and high-contrast dark surfaces.

### Case Study 3: Mojito Agency (`mojito-awwwards-website`)
- **Award**: Site of the Day.
- **Key Breakthrough**: Alternating scroll rhythm (Tension & Release), Lenis smooth momentum scroll, and fluid SVG page transitions.
- **Lessons**: Alternate high-density 3D/bento sections with clean typography manifesto sections.

### Case Study 4: Alex Streza Portfolio & SOTY Architectural Checklist
- **Source**: Medium (*A Guide on Building Awwwards-Worthy Websites*).
- **Key Breakthrough**: Combining Astro static site generation (SSG) for lightweight DOM payload with isolated React client components (`@react-three/fiber`, `@react-three/drei`) for 3D CSR canvas stages.
- **Lessons**: SOTY sites win through microinteractions, controlled state randomness, oversized font scales, custom cursors, and magnetic CTA physics. GSAP is the industry standard #1 for scroll timeline pins.

### Case Study 5: Typographic Extended Font Standards (DesignYourWay Research)
- **Source**: DesignYourWay (*What is an Extended Font?*).
- **Key Breakthrough**: Extended typefaces are handcrafted at the font glyph level, maintaining balanced stroke weights across wide proportions.
- **Lessons**: Never use `transform: scaleX(1.3)` or artificial horizontal stretching. Use variable fonts with `font-variation-settings: "wdth" 125` or CSS `font-stretch: expanded` for zero-latency hero headlines. Barlow Expanded, Trade Gothic Extended, and Akira Expanded are prime choices.

### Case Study 6: Pioneer — Corn Revolutionized (Resn — Site of the Year 2020 Winner)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: Vertical scrollytelling wrapped in an infinite loop (seed-to-harvest metaphor).
- **Lessons**: 3D interactive corncob model with networked particle overlays, subtle wind particle physics, and dark ambient lighting focusing 100% on the hero product.

### Case Study 7: Das Falter Inferno (Wild.as — SOTD Winner)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: Conceptual dystopian online story riffing on Dante's Inferno (black mirror on modern society).
- **Lessons**: 3% SVG noise texture overlay, scene-specific ambient soundscapes, dramatic curtain reveals transitioning to an Eden bliss final scene.

### Case Study 8: ChungiYoo Portfolio (Art Direction by Zhenya Rynzhuk)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: Unboxed fluid content hierarchy, soft luxury color palette, animated illustrations inside rounded cards.
- **Lessons**: Parallax scroll reveals, high-contrast display typography, and smooth tab transitions.

### Case Study 9: Carine Roitfeld (Numbered Studio & AskPhill)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: High-fashion Vogue aesthetic with a mysterious black-and-white full-screen video hero header.
- **Lessons**: Minimalist monochrome typography, smooth video playback synchronization, elegant spatial rhythm.

### Case Study 10: WelcomeToSeason16 (LeBron James Lakers Campaign)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: Duo-toned yellow/purple Lakers color theme, pop-culture storytelling, Pokemon-style player reveal.
- **Lessons**: Brushy typography reveals (`overflow: hidden` translateY masking), staggered element fade-ins, scroll parallax.

### Case Study 11: PulpFingers (Classic SOTD Winner)
- **Source**: Medium (*How to Win an Awwward* by Nick Ungerer).
- **Key Breakthrough**: Tactile paper-like quality with playful fonts, non-traditional complementary colors, and simple illustrations.
- **Lessons**: Demonstrates that simplicity and strong concept triumph over heavy high-production assets.

### Case Study 12: iyO One — Audio Computer (Google X Moonshot SOTD Showcase)
- **Source**: Awwwards Official Case Study (`iyO - Case Study: selling the world's first audio computer`).
- **Key Breakthrough**: GPGPU simulation of 1.6 million particles forming Chladni soundwave patterns that morph into text without opacity crossfades.
- **Lessons**: Scroll-driven Z-axis interactive 3D CAD exploded hardware view down-rezzed to Draco-compressed glTF, single-page `Taxi.js` route transition engine for flat JS memory, and 44% GPU fragment workload reduction via `Math.min(devicePixelRatio, 1.5)`.

### Case Study 13: The New Obys (Obys Agency Studio Redesign — Studio of the Year Winner)
- **Source**: Awwwards Official Case Study (`The New Obys`).
- **Key Breakthrough**: Typeface-first architecture (`OTF Obys NG` custom font created before wireframing to drive all spacing and grid math). Dynamic logo experience morphing from old to new logo on initial load.
- **Lessons**: Extreme zero-bundle performance. Server built on **Bun**, React used strictly for server-side HTML rendering with **0kb React bundle sent to client**, custom TypeScript animation engine using native `requestAnimationFrame` + Web Animations API + plain CSS + WebGL.

### Case Study 14: Fluid Glass (Exo Ape Studio SOTD Showcase)
- **Source**: Awwwards Official Case Study (`Fluid Glass - Case Study` by Exo Ape).
- **Key Breakthrough**: Digital Hospitality micro-interaction (dynamic floating Navigation Island that automatically expands upon reaching page bottom).
- **Lessons**: Infinite continuous project scroll (scrolling to page bottom transitions directly into the next project case study without pagination breaks). Built with Nuxt.js, Storyblok, GSAP ScrollTrigger, and subtle SVG detail animations.

### Case Study 15: Trionn Agency Architecture (Coordinating GSAP, Three.js, Lenis & Web Audio)
- **Source**: Codrops Case Study (`The Architecture Behind Trionn`).
- **Key Breakthrough**: Master choreography pipeline integrating Lenis smooth scroll inertia, GSAP ScrollTrigger timeline pins, Three.js WebGL canvas stage, and Web Audio API spatial soundscapes.
- **Lessons**: Centralized ticker manager loop. Pipe `lenis.on('scroll', ScrollTrigger.update)` into `gsap.ticker.add()` and update WebGL shader `uTime` uniforms synchronously to eliminate micro-stuttering across 3D canvas and DOM elements.

### Case Study 16: Building Cerebrium (3D WebGL vs WebGPU Production Decisions)
- **Source**: Codrops Case Study (`Building Cerebrium: Making Serverless Infrastructure Tangible`).
- **Key Breakthrough**: Three.js `onBeforeCompile()` GLSL material injection and static mesh network pulse shader (zero CPU vertex motion; glowing pulses animated along UV Y-axis).
- **Lessons**: Use WebGLRenderer with `onBeforeCompile()` for zero startup latency on mobile. Pre-compile FBO ping-pong particle textures. Use Cinema 4D unit helper cubes to export light coordinates into Three.js.

### Case Study 17: PX PUSH (CRT Convex Monitor Shader Simulation)
- **Source**: Codrops Case Study (`The Department Is Open: Building the PX PUSH Website`).
- **Key Breakthrough**: Single fixed overlay `Wrapper.vue` simulating a 1980s convex CRT monitor sitting continuously above all page routes.
- **Lessons**: Scanline CSS keyframe animation (`scanline 8s linear infinite`), backdrop-filter bloom (`backdrop-filter: blur(10px)`), and curved vignette (`crt.png scale(1.02)`).

### Case Study 18: ZERO (Interactive 3D Narrative Engineering)
- **Source**: Codrops Case Study (`ZERO: The Engineering Behind a Defiant Interactive Narrative`).
- **Key Breakthrough**: Scrollytelling narrative engine combining custom camera spline curves with WebGL fragment shader noise transitions.
- **Lessons**: Pre-bind camera keyframe paths along 3D splines, tying scroll distance directly to camera progress float `uProgress`.

### Case Study 19: The Sleepers (Atmospheric WebGL with Lightweight Techniques)
- **Source**: Codrops Case Study (`The Sleepers`).
- **Key Breakthrough**: Low-overhead atmospheric WebGL fog, subtle particle dust pass, and post-processing bloom running on mobile GPUs.
- **Lessons**: Render WebGL canvas at `Math.min(window.devicePixelRatio, 1.5)` to cut shader workload by 44% while maintaining 60fps.

### Case Study 20: Between Print and Digital (MERSI Studio Case Study)
- **Source**: Codrops Case Study (`Between Print and Digital: The Making of MERSI's Website`).
- **Key Breakthrough**: Merging editorial magazine grid layouts with smooth WebGL page transitions and kinetic typography reveals.
- **Lessons**: Combine fixed editorial grid baselines with fluid SVG curtain transitions and split-text character reveals.






---

## Tutorials & Technical Breakdown Index

### Tutorial 1: Lenis & GSAP ScrollTrigger Sync
- **Topic**: Seamless momentum scroll without native browser scroll stutter.
- **Key Formula**: Register `ScrollTrigger`, initialize `Lenis`, pipe `lenis.on('scroll', ScrollTrigger.update)`, and add `lenis.raf` to GSAP ticker loop.

### Tutorial 2: WebGL Liquid Image Distortion Slider
- **Topic**: Custom WebGL fragment shader image transition on hover/drag (`Custom_WEBGL_Slider`).
- **Key Formula**: Pass current texture, next texture, and progress float `uProgress` to GLSL fragment shader, applying `sin(uv.y * 10.0 + uProgress * 3.14159) * 0.05` distortion wave.

### Tutorial 3: SVG Path Morphing Page Transition
- **Topic**: Morphing SVG path curtain reveal during multi-page routing (`SVG-Page-transition`).
- **Key Formula**: Animate SVG `d` attribute path string from `M 0 100 Q 50 100 100 100` to `M 0 0 Q 50 0 100 0` using GSAP timeline `power4.inOut` easing.

### Tutorial 4: Video-Based Theme Changer Protocol
- **Topic**: Swapping background video stages on theme toggle (`theme-toggle.rdsx.dev`).
- **Key Formula**: Preload dark and light video assets, cross-fading video element opacities and playback positions synchronously.

---

## Local Component Ingestion Registry (`C:\Users\HP\Downloads\Components`)

The engine indexes 24 specialized component repositories:

1. `Obys-clone`: Layout math, Obys padding, and smooth typography reveals.
2. `Spylt-awward-clone`: Bento grid card physics and depth layering.
3. `mojito-awwwards-website`: Scroll choreography and dark theme architecture.
4. `Custom_WEBGL_Slider`: GLSL liquid image distortion slider.
5. `webgl-ascii-hero`: ASCII-rendered WebGL canvas hero.
6. `3D-sticky-cards`: GSAP ScrollTrigger 3D card pin stack.
7. `LandingPage-Reveal`: Preloader animation and curtain reveal.
8. `SVG-Page-transition`: Morphing SVG path page transition.
9. `Insane-PRELOADER`: High-impact loader animation sequence.
10. `Dragon-Scroll-Effect`: Custom scroll-driven SVG/canvas physics.
11. `Smooth-scroll-Slider`: Inertia horizontal scroll slider.
12. `shader-gallary`: WebGL fragment and vertex shader collection.
13. `Prototype-studio-rebuilt`: Studio portfolio layout architecture.
14. `AW-2025-Portfolio`: 2025 Awwwards portfolio showcase code.
15. `creative-kai`: Creative developer portfolio layout.
16. `3D_CARD`: 3D tilt and depth card physics.
17. `3d-scroll-effect`: Depth-based 3D scroll transitions.
18. `ASCII-Video-Player`: Real-time ASCII video player engine.
19. `butterflies`: Canvas particle/physics stage.
20. `css-only-background-image-grids-animation`: CSS grid background dynamics.
21. `gsap-inertia-card-animations-showcasechallenge-2-entry-2`: GSAP inertia card motion showcase.
22. `hyper-scroll`: High-velocity scroll-triggered layout transitions.
23. `reverse-scrolling-columns`: Dual-direction opposing scroll column layout.
24. `theme-toggle.rdsx.dev`: Video theme switcher integration protocol.

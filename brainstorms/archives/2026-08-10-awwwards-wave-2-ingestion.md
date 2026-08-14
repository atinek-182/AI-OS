# Awwwards Research Vault Ingestion Wave 2: Discovery & Brainstorm Notes
Date: 2026-08-10 · Goal: Line-by-Line Extraction & Ingestion of 23 Granularity Master Breakdowns into Awwwards Research Vault · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Target**: Parse 24 Granularity Master breakdowns in `premium-frontend-experience-system/vault-references/` into the 7 sub-vault directories of `references/awwwards-research-vault/`.
- **Pre-Execution Roast Verdict**: GO with 3 pre-wave 2 fixes (Top-level `INDEX.md` update for sub-vault 07, `WAVE2_INGESTION_STATUS.md` tracker creation, and 23-Site Master Matrix synthesis).

## Domain Vocabulary & Glossary
- **Granularity Master**: An exhaustive line-by-line breakdown file of a world-class award-winning website (e.g. Obys Agency, Resn, Locomotive, Active Theory) detailing its visual architecture, typography math, motion engine, WebGL shaders, scrollytelling dynamics, and UX psychology.
- **Sub-Vault**: A specialized category folder under `references/awwwards-research-vault/` containing atomic Markdown documentation for runtime agent discovery.

## Q&A Log
### Q1 — Ingestion Execution Scope & Batching Strategy
- **Concept Explained**: Ingestion involves reading all 24 Granularity Master breakdown files line-by-line and extracting raw code snippets, GLSL shaders, typography math formulas, GSAP/Lenis scroll choreography, and design principles into their corresponding atomic sub-vault files (`01-design-principles`, `02-typography-grid`, `03-gsap-lenis`, `04-webgl-shaders`, `05-case-studies`, `06-judging-criteria`, `07-ux-psychology`). Batching determines whether we process all 24 files in a single unified script execution or group them by site archetype.
- **Asked**: How should we structure the execution batches for the 24 Granularity Master files during Wave 2 line-by-line parsing?
- **Options Provided**:
  1. **Option A (Single-Pass Unified Script Batch)**: Execute a single automated line-by-line parser script (`scripts/ingest_wave2_granularity_masters.py`) that sweeps all 24 files simultaneously, categorizes code/principles, and updates sub-vaults in one pass. [RECOMMENDED]
  2. **Option B (Archetype Cluster Batching)**: Process the 24 sites in 4 separate archetype clusters (e.g., 3D Immersive, Editorial Minimalist, Interactive Typography, Kinetic E-Commerce) with individual visual QA checks after each cluster.
  3. **Option C (Manual File-by-File Review)**: Sequentially process each site file one by one with manual operator confirmation after each file.
- **Captured Decision**: Option 3 (Interactive File-by-File / Site-Group Review)
- **Rationale & Trade-offs**: Enables high-granularity inspection per site breakdown, allowing Atinek Maurya to review extracted principles and code snippets sequentially for maximum design intelligence absorption.

### Q2 — Structural Pre-Fix Sequencing & Site 1 Launch
- **Concept Explained**: The 3 structural pre-fixes identified in the adversarial `/roast` audit (registering sub-vault `07` in top-level `INDEX.md`, creating `WAVE2_INGESTION_STATUS.md`, and setting up `05-23-site-master-matrix.md`) set up the index routing and tracking infrastructure for all 24 sites. Pre-executing them ensures every site parsed during file-by-file review is indexed and logged live.
- **Asked**: Should we execute the 3 structural pre-fixes to prepare the index and tracker before beginning file-by-file review of Site 1?
- **Options Provided**:
  1. **Option A (Infrastructure Pre-Fixes First)**: Complete all 3 structural fixes first to ensure sub-vault 07 is fully indexed and `WAVE2_INGESTION_STATUS.md` is ready to record live per-site status, then present Site 1 (`active-theory-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Inline Infrastructure Updates)**: Defer infrastructure fixes until after reviewing Site 1.
- **Captured Decision**: Option A (Infrastructure Pre-Fixes First)
- **Rationale & Trade-offs**: Guarantees zero unindexed sub-vaults and establishes live per-site tracking across `WAVE2_INGESTION_STATUS.md` before site #1 review begins.

### Q3 — Site 1: Active Theory Granularity Ingestion
- **Concept Explained**: Active Theory's breakdown covers their proprietary Hydra WebGL framework, texture hydration preloader (0% -> 100%), particle repulsion math, 3D camera Z-axis scrubbing, Web Audio synthesizer feedback, and OKLCH cosmic void dark tokens (`oklch(0.06 0.01 260)`). Atomic extraction splits these across Sub-Vault 04 (WebGL), Sub-Vault 03 (Motion & Audio), and Sub-Vault 01 (Color Fills).
- **Asked**: How should we structure the atomic sub-vault destination files for Site 1 (`active-theory-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 3-Sub-Vault Atomic Ingestion)**: Create `04-webgl-threejs-fragment-shaders/05-active-theory-hydra-canvas-and-audio.md`, `03-gsap-lenis-motion-scrollytelling/04-active-theory-particle-audio-motion.md`, and record OKLCH tokens into `01-design-principles-and-aesthetics/`, then mark Site 1 as `[DONE]` in `WAVE2_INGESTION_STATUS.md`. [RECOMMENDED]
  2. **Option B (Consolidated Single Case Study File)**: Place the entire Active Theory extraction into a single file under `05-case-studies-and-tutorials/`.
- **Captured Decision**: Option 1 Upgraded (Full 7-Sub-Vault Ingestion + Awwwards JSON Case Study Enrichment)
- **Rationale & Trade-offs**: Mandates complete 360-degree extraction of design principles, typography math, motion soundscapes, GLSL fragment shaders, portfolio case studies, judging rubrics, and digital hospitality psychology across all 7 sub-vaults (01-07) for every site breakdown.

### Q4 — Site 2 Review: Ashley Brooke Granularity Master
- **Concept Explained**: Ashley Brooke's breakdown (`ashley-brooke-cs-granularity-master.md`) covers high-fashion editorial grid layouts, dynamic hover inertia cursor displacement, subtle image tilt physics, and luxury branding typography.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion for Site 2 (`ashley-brooke-cs-granularity-master.md`) enriched with matching Awwwards JSON case study data?
- **Options Provided**:
  1. **Option A (Proceed with Site 2 Full 7-Sub-Vault Ingestion)**: Ingest Ashley Brooke across all 7 sub-vaults, update `WAVE2_INGESTION_STATUS.md`, and advance to Site 3. [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 1 to inspect created sub-vault files before proceeding to Site 2.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid momentum across the 24-site queue while enforcing the 7-sub-vault quality standard.

### Q5 — Site 3 Review: Champions 4 Good Granularity Master
- **Concept Explained**: Champions 4 Good breakdown covers draggable flick-card physics (`[data-flick-cards-dragger]`), fonts-loaded gate hydration (`.is-ready.fonts-loaded`), Finsweet form mechanics, and high-energy contrast tokens (`#FAFAF8`, `#0A0A0C`, `#FF3366`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 3 (`champions-4-good-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Champions 4 Good, cross-reference Awwwards JSON case studies, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 4 (`detroit-paris-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 2 to review generated roast report `roast_2026-08-10_wave2_sites1_2_ingestion.md`.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains maximum momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q6 — Site 4 Review: Detroit Paris Granularity Master
- **Concept Explained**: Detroit Paris breakdown covers luxury AI video production aesthetics, HLS.js 1.6.11 stream preloader buffers, `data-video-on-hover` video playback mechanics, Barlow font stack typography, and pure dark palette (`#050505`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 4 (`detroit-paris-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Detroit Paris, check Awwwards JSON case studies, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 5 (`follow-art-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 3 to inspect created sub-vault files before proceeding to Site 4.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q7 — Site 5 Review: Follow Art Granularity Master
- **Concept Explained**: Follow Art breakdown covers Vide Infra Studio's rebellious digital art platform aesthetics, `HeadingNow` & `Hardbop` typography, sticky layer scrollytelling (`.section__layer--sticky`), electric cobalt blue tokens (`#0000FF`), and button hover accent micro-interactions (`.btn__hover-accent`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 5 (`follow-art-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Follow Art, check Awwwards JSON case studies, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 6 (`gehry-getty-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 4 to inspect created sub-vault files before proceeding to Site 5.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q8 — Site 6 Review: Gehry Getty Granularity Master
- **Concept Explained**: Gehry Getty breakdown covers Getty Research Institute's 3D architectural model stage (`getty_formStudy.glb`), Basis Universal WASM texture transcoders (`basis_transcoder.wasm`), 3D world-to-screen hotspot coordinate projections (`Hotspot.032182a1.js`), timecoded audio transcript synchronization, Playfair Display serif typography, and Archival Warm Paper tokens (`#F2F0EB`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 6 (`gehry-getty-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Gehry Getty, check Awwwards JSON case studies, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 7 (`good-fella-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 5 to inspect created sub-vault files before proceeding to Site 6.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q9 — Site 7 Review: Good Fella Granularity Master
- **Concept Explained**: Good Fella breakdown covers Julian & Adrian Fella's Munich studio architecture, Vercel Geist Mono variable typography, Next.js Turbopack SSR with Sanity CMS, `LazyCustomCursor` pointer physics, `PreloaderScrollLock` entrance states, and electric red contrast tokens (`#FF0000`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 7 (`good-fella-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Good Fella, check Awwwards JSON case studies, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 8 (`grids-obys-agency-deep-research.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 6 to inspect created sub-vault files before proceeding to Site 7.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q10 — Site 8 Review: Grids by Obys Agency Deep Research
- **Concept Explained**: Grids by Obys Agency breakdown covers Obys' 4 core grid archetypes (12/10/8 Column Grid, Van De Graaff Canon diagonal power lines, Rectangular/Modular 16-col splitting, and Baseline Grid math), margin standards (30px/60px/80px), and 20px constant gutters.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 8 (`grids-obys-agency-deep-research.md`) enriched with Awwwards JSON Obys case study entries (entries 005 & 020)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Obys Grid Deep Research, enrich with Awwwards JSON Obys case studies (entries 005 & 020), update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 9 (`grids-obys-agency-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 7 to inspect created sub-vault files before proceeding to Site 8.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q11 — Site 9 Review: Grids by Obys Agency Granularity Master
- **Concept Explained**: Obys Agency Granularity Master provides full code extracts: `grid-distortion.glsl` GLSL fragment shader, `GridCanvas.tsx`, `ObysHeaderNav.tsx`, `GridSystemCard.tsx`, `grid-scroll-physics.js`, `Georgia` + `Nobel` + `Courier New` typography, and OKLCH Onyx/Gold/Red color tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 9 (`grids-obys-agency-granularity-master.md`) as Favorite #1 Master Benchmark?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Obys Granularity Master, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 10 (`jasmine-gunarto-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 8 to inspect created sub-vault files before proceeding to Site 9.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q12 — Site 10 Review: Jasmine Gunarto Granularity Master
- **Concept Explained**: Jasmine Gunarto breakdown covers high-fashion editorial portfolio mechanics, Taxi.js SPA page transitions (`data-taxi`), `MagneticButton` cursor physics, live location/clock header, Obsidian Black (`#090909`), Cream Off-White (`#EBEAE4`), and Earth Brown (`#341C09`) aesthetics.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 10 (`jasmine-gunarto-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Jasmine Gunarto, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 11 (`locomotive-agency-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 9 to inspect created sub-vault files before proceeding to Site 10.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q13 — Site 11 Review: Locomotive Agency Granularity Master
- **Concept Explained**: Locomotive Agency breakdown covers the Montréal agency architecture, Locomotive Scroll v5 (`data-scroll-speed="2"`), 20 GLSL fragment shaders (`shader_01_fragment.glsl` to `shader_20_fragment.glsl`), 109 extracted React components, SVG curtain preloader, and OKLCH Deep Charcoal/Crimson Red tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 11 (`locomotive-agency-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Locomotive Agency, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 12 (`made-in-evolve-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 10 to inspect created sub-vault files before proceeding to Site 11.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q14 — Site 12 Review: Made In Evolve Granularity Master
- **Concept Explained**: Made In Evolve breakdown covers the Modena Italy boutique agency architecture, cellular grid preloader (`loader__cell`), CircleType.js curved text path SVG engine, Unicorn Studio 3D WebGL shader integration, Barba.js SPA router, and Off-White (`#F4F4F0`) / Neon Lime (`#C3FF00`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 12 (`made-in-evolve-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Made In Evolve, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 13 (`merci-michel-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 11 to inspect created sub-vault files before proceeding to Site 12.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q15 — Site 13 Review: Merci Michel Granularity Master
- **Concept Explained**: Merci Michel breakdown covers the Parisian gamified WebGL studio architecture (2 SOTY, 6 SOTM, 41 SOTD), Howler.js spatial audio engine, Three.js particle bloom stage vector displacement ($\mathbf{D} = \mathbf{P}_{cursor} - \mathbf{P}_{particle}$), 35 extracted React components, and OKLCH Neon Crimson/Electric Purple tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 13 (`merci-michel-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Merci Michel, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 14 (`off-menu-design-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 12 to inspect created sub-vault files before proceeding to Site 13.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q16 — Site 14 Review: Off Menu Design Granularity Master
- **Concept Explained**: Off Menu Design breakdown covers Hunter Hammonds' AI agency architecture, Remi AI video avatar (`remi_dark@2x.mp4`), `RemiAIChatWidget.tsx`, 3D sphere orbital portfolio carousel (`OrbitalPortfolioCarousel.tsx`), difference blend mode cursor, and Pure Dark (`#000000`) / Electric Blue (`#3B82F6`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 14 (`off-menu-design-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Off Menu Design, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 15 (`oryzo-ai-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 13 to inspect created sub-vault files before proceeding to Site 14.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q17 — Site 15 Review: Oryzo AI Granularity Master
- **Concept Explained**: Oryzo AI breakdown covers Lusion's WebGL Gaussian Splat sorter WASM runtime (`splat_sorter_bg-BfJrILzx.wasm`), Rive WASM engine (`rive.wasm`), 60,582px scroll body height driving 7 camera keyframes (`CAMERA_ANIM.buf`), raw 3D mesh buffers (`coaster.buf`, `hand.buf`), and Pure Black (`#000000`) / Satirical Orange (`#F97316`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 15 (`oryzo-ai-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Oryzo AI, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 16 (`outfit-hello-hello-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 14 to inspect created sub-vault files before proceeding to Site 15.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q18 — Site 16 Review: Outfit Hello Hello Granularity Master
- **Concept Explained**: Outfit Hello Hello breakdown covers ++hellohello studio's (Montevideo, Uruguay) typeface-first fashion showcase, `Neue Haas Grotesk Text Pro` with `-0.05em` negative tracking, `data-theme="red"` dynamic theme engine, Electric Red (`#FF0001`) / Heritage Cream (`#EDE4DD`) tokens, and full-screen red hero banner (`CREATIVITY IN MOTION`).
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 16 (`outfit-hello-hello-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Outfit Hello Hello, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 17 (`resn-corn-revolution-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 15 to inspect created sub-vault files before proceeding to Site 16.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q19 — Site 17 Review: Resn Corn Revolution Granularity Master
- **Concept Explained**: Resn Corn Revolution breakdown covers Resn's (New Zealand & Netherlands, 14 Agency of the Year titles) WebGL 3D particle engine, 6 custom GLSL fragment shaders (`shader_01` to `shader_06`), Howler.js scroll-velocity modulated audio, particle repulsion math ($\mathbf{D} = \mathbf{P}_{cursor} - \mathbf{P}_{particle}$), and Dark Moss (`#070a06`) / Chlorophyll Green (`#22c55e`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 17 (`resn-corn-revolution-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Resn Corn Revolution, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 18 (`sondaven-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 16 to inspect created sub-vault files before proceeding to Site 17.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q20 — Site 18 Review: Sondaven Granularity Master
- **Concept Explained**: Sondaven breakdown covers the Ukrainian luxury resort architecture (`sondaven.com/en`), Barba.js 20x12 grid cell dither SPA transition, drag-along-path SVG Summer/Winter slider (`path.getPointAtLength`), 3D Y-axis 180-degree card flip form submit (`rotateY: -180`), and OKLCH Gold (`#a89474`) / Charcoal (`#2c2824`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 18 (`sondaven-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Sondaven, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 19 (`the-line-studio-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 17 to inspect created sub-vault files before proceeding to Site 18.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q21 — Site 19 Review: The Line Studio Granularity Master
- **Concept Explained**: The Line Studio breakdown covers THE LINE Studio (London animation studio), rotated card page transitions (`rotate(4deg)` to `rotate(-4deg)`), DenimVF variable font stack with per-letter kerning (`.letter-A` down to `-0.07em`), electric red FPS preloader counter, red acetate multiply blend effect, and Electric Red (`#FF391E`) / Studio Grey (`#DDDEE2`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 19 (`the-line-studio-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for The Line Studio, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 20 (`the-shift-tokyo-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 18 to inspect created sub-vault files before proceeding to Site 19.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q22 — Site 20 Review: The Shift Tokyo Granularity Master
- **Concept Explained**: The Shift Tokyo breakdown covers The Shift Creative Collective's (Tokyo, Japan) Japanese neo-brutalist architecture, live Tokyo clock indicator (`東京 18:42:09 JST`), WebGL liquid wave distortion shader (`tokyo-glsl-distortion.glsl`), `Everett` + `YakuHanJP` font stack, electric coral custom cursor (`#FE4249`), and Pitch Dark (`#0B0B0B`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 20 (`the-shift-tokyo-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for The Shift Tokyo, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 21 (`tresmares-capital-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 19 to inspect created sub-vault files before proceeding to Site 20.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q23 — Site 21 Review: Tresmares Capital Granularity Master
- **Concept Explained**: Tresmares Capital breakdown covers Dgrees Studio's (Madrid, Spain) high-trust financial private equity architecture, `PP Fragment Serif` + `PP Neue Montreal` font stack, Taxi.js SPA transition router (`data-taxi-view="default"`), CookieYes GDPR integration, and Deep Obsidian (`#0B0E14`) / Terracotta Peak Red (`#D94A38`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 21 (`tresmares-capital-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Tresmares Capital, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 22 (`trionn-agency-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 20 to inspect created sub-vault files before proceeding to Site 21.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q24 — Site 22 Review: TRIONN Agency Granularity Master
- **Concept Explained**: TRIONN Agency breakdown covers TRIONN® AI-Powered Digital Studio, 134 modular React components (`Hero_Section_01.tsx`, `Nav_Header_01.tsx`), 16 GLSL WebGL shaders (`shader_01_fragment.glsl`), dual-ring magnetic cursor follower, Web Audio feedback engine, and Obsidian Dark `oklch(0.12 0.01 260)` (`#0D0E12`) / Indigo Glow `oklch(0.55 0.22 275)` (`#6366F1`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 22 (`trionn-agency-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for TRIONN Agency, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 23 (`truck-n-roll-granularity-master.md`). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 21 to inspect created sub-vault files before proceeding to Site 22.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q25 — Site 23 Review: Truck 'n Roll Granularity Master
- **Concept Explained**: Truck 'n Roll breakdown covers Locomotive®'s (Montreal, QC) heavy industrial logistics architecture, `Druk` + `GT America` + `Space Mono` font stack, Swup SPA page transitions (`#swup`), hover caption metadata engine (`HoverCaption-B_8cR76t.js`), and Dark Charcoal (`#0E0F12`) / Crimson Red (`#E53935`) tokens.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion and `/roast` audit for Site 23 (`truck-n-roll-granularity-master.md`)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit)**: Execute full 7-sub-vault extraction for Truck 'n Roll, update `WAVE2_INGESTION_STATUS.md`, run the `/roast` council audit, and present Site 24 (`unleashing-best-granularity-master.md` - the FINAL site in Wave 2!). [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 22 to inspect created sub-vault files before proceeding to Site 23.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A maintains rapid execution momentum across the 24-site queue while keeping the 7-sub-vault zero-loss standard intact.

### Q26 — Site 24 Review: Unleashing Best Granularity Master (FINAL WAVE 2 SITE!)
- **Concept Explained**: Unleashing Best breakdown covers Victor Work's executive showcase platform, 6 dynamic palette theme runtimes (`.colorGreen`, `.colorOrange`, `.colorBlue`), circular progress ring custom cursor (`.custom-c` `10rem`), `GrifinitoLMedium` font stack (`0.52083vw` fluid math), and GSAP 400% pin scrollytelling.
- **Asked**: Shall we proceed with full 7-sub-vault atomic ingestion, `/roast` audit, and celebrate 100% completion of Wave 2 (24/24 Sites Ingested)?
- **Options Provided**:
  1. **Option A (Full 7-Sub-Vault Ingestion + Roast Audit + Wave 2 Completion)**: Execute full 7-sub-vault extraction for Unleashing Best, update `WAVE2_INGESTION_STATUS.md`, run the final `/roast` council audit, and mark Wave 2 100% complete! [RECOMMENDED]
  2. **Option B (Pause for Review)**: Pause after Site 23 to inspect created sub-vault files before proceeding to Site 24.
- **Captured Decision**: [PENDING OPERATOR ANSWER]
- **Rationale & Trade-offs**: Option A completes the entire 24-site Wave 2 Awwwards vault ingestion sprint with zero-loss 7-sub-vault atomic precision.

## Open Flags & Deferred Decisions
- [x] Fix 1: Register sub-vault 07 in `references/awwwards-research-vault/INDEX.md` (Verified: Already registered)
- [x] Fix 2: Generate `scratch/awwwards_ingestion_raw/WAVE2_INGESTION_STATUS.md` (Created: 24-site status tracker)
- [x] Fix 3: Create `05-23-site-master-matrix.md` mapping to component vault (Created: 23-site design matrix)

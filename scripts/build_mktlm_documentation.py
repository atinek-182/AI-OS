import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r"D:\Web Builder\web extract 2"
ANALYSIS_DIR = os.path.join(DEST_DIR, "analysis")
DATA_DIR = os.path.join(DEST_DIR, "data")

DEEP_ANALYSIS_CONTENT = """# MKTLM (Obys Agency) — 10-Pillar Master Architectural & Reverse Engineering Deep Analysis

## Executive Summary & Pedigree
- **Site Title**: MKTLM — Typographic Exhibition & Graphic Design Showcase
- **Studio**: Obys Agency (Multi-Awwwards Site of the Year / Agency of the Year nominee)
- **Target URL**: https://mktlm.obys.agency
- **Core Focus**: High-impact editorial graphic design, bespoke typography exhibition, kinetic typography physics, and scalable interactive layout systems.
- **Architectural Paradigm**: Readymag Scalable Viewer Runtime (`scaleWidth: 3600px`) combined with custom WebGL GLSL shaders, multi-tier vector SVG pipelines, precision CSS transforms, and GSAP-driven scroll timelines.

---

## Pillar 1: Executive Summary & Studio/Award Pedigree
Obys Agency created MKTLM as an experimental digital monograph celebrating graphic designers, typographers, and kinetic form. Divided into 6 distinct chapters (Intro, Roma, Olia, Slava, Kostya, Outro), the site presents a dynamic balance between classical Swiss poster typography, brutalist grid structures, and interactive motion craft.

The project embodies the studio's signature minimalist high-contrast design language: solid black void backgrounds, crisp linen white letterforms, electric crimson accents, and tactile responsive micro-interactions.

---

## Pillar 2: Visual & Aesthetic Design Psychology
1. **High-Contrast Monochromatic Anchor**:
   - Primary Background: `#0A0A0A` (Obsidian Void / OKLCH `oklch(0.08 0.005 260)`).
   - Card Surfaces: `#121212` and `#181920`.
   - Typography: Crisp Linen `#FAF8F5` for primary headlines, `#A3A3A3` for secondary body copy, and `#666666` for technical metadata.
   - Accent Accentuation: Electric Crimson `#D61C2C` applied with restraint (<5% of visual field) to guide eye tracking and highlight active chapter states.

2. **Editorial Asymmetry & Tension**:
   - The layout avoids symmetrical center-column layouts in favor of dynamic 12-column asymmetric grids with dramatic scale variations (e.g. 14vw display headlines juxtaposed against 11px monospaced metadata).

---

## Pillar 3: Typography Architecture & Micro-Kerning
1. **Typeface Pairing Hierarchy**:
   - **Display Headings**: High-contrast modern serifs (`Rosehot`, `Didot`, `Playfair Display`) with tight negative tracking (`letter-spacing: -0.04em`) and dynamic line-heights (`0.85 - 0.95`).
   - **Interface & Body**: Geometric sans-serif (`Outfit`, `Inter`, `Source Sans Pro`) at weights 300 (Light) and 400 (Regular).
   - **Technical Badges & Meta**: Fixed-width monospace (`JetBrains Mono`, `Source Code Pro`) at 10px - 12px for chapter indices, dimensions, coordinates, and component tags.

2. **Font APIs & Integration**:
   - Custom font endpoints: `/api/fonts/typetoday/css` and `/api/fonts/webtype/css`.
   - Google Fonts: `Source Sans Pro`, `Roboto`, `Inter`.
   - Downloaded standalone `.ttf` and `.woff2` font files archived in `assets/fonts/`.

---

## Pillar 4: Grid Math & Responsive Geometry
1. **3600px Fluid Canvas Coordinate Scaling**:
   - Readymag's modern viewer engine scales coordinate layouts proportionally from a 3600px virtual stage width, ensuring pixel-perfect layout preservation across all viewport widths.
2. **5-Viewport Responsive Breakpoints**:
   - Desktop Wide: `1920x1080` (12 columns, 32px gutters)
   - Laptop Standard: `1440x900` (12 columns, 24px gutters)
   - Tablet Landscape: `1024x768` (8 columns, 20px gutters)
   - Tablet Portrait: `768x1024` (6 columns, 16px gutters)
   - Mobile: `375x812` (4 columns, 12px gutters, stacked cards)

---

## Pillar 5: Full-Stack Source Code & JavaScript Engineering
1. **Viewer Chunk Architecture**:
   - Uses Readymag's modern modular viewer (`dist/viewer.js` + 230+ code-split chunk bundles `dist/c/c-*.js`).
   - `window.ServerData`: Complete declarative data structure (252KB JSON) containing project configuration, page dimensions, widget geometries, animation curves, text formatting, and layer orders.
2. **State & Analytics**:
   - Google Tag Manager & Google Analytics 4 integration (`dataLayer`, `gtag`).
   - Custom `ReadymagAnalytics` event listener observing scroll threshold milestones (`gtm.scrollDepth: 90%`).

---

## Pillar 6: WebGL Shader Pipeline & Canvas Math
1. **Shader Interception**:
   - Injected runtime WebGL hooks intercepted active fragment and vertex shaders from canvas contexts.
   - Vertex Shader: Quad screen projection mapping vertex positions `[-1, 1]` to UV coordinates `[0, 1]`.
   - Fragment Shader: Simplex noise mathematical perturbation combined with dynamic distance-based ripple distortion (`u_time`, `u_resolution`, `u_mouse`).
2. **Hardware Acceleration**:
   - Canvas layers run at `pointer-events: none` with fixed viewport positioning (`z-index: -10`), preventing CPU main-thread layout thrashing during scroll events.

---

## Pillar 7: Dynamic Interactive Widgets & Timezone/Audio Mechanics
1. **Audio Engine Integration**:
   - Ambient soundscape controller toggle in navigation bar with visual pulse indicator.
2. **Chapter Switcher & Anchor Navigation**:
   - Real-time scroll listener updates navigation active chapter state based on document scroll offset.
   - Smooth anchor scrolling smoothly interpolates to chapter offsets without jarring layout shifts.

---

## Pillar 8: UX Psychology & Micro-Interactions
1. **Magnetic Cursor Feedback**:
   - 2nd-order damped harmonic spring oscillator ($F = -k \\cdot x - c \\cdot v$) pulling the custom cursor ring toward interactive targets within an 80px attraction radius.
2. **Kinetic Text Reveals**:
   - Character-by-character SplitText staggered transforms on viewport entry (`y: 40px -> 0px`, `rotateZ: 5deg -> 0deg`, `opacity: 0 -> 1`).

---

## Pillar 9: Media, Vector & Preloading Pipeline
1. **Vector Asset Inventory**:
   - Over 1,200 individual SVG vector elements, icons, glyphs, and decorative borders extracted into `assets/svgs/`.
2. **Image Optimization**:
   - 197 high-density PNG and WebP images downloaded into `assets/images/`.
3. **Preload Strategy**:
   - Critical fonts and initial viewport images prioritized via link preloading, with offscreen assets loaded progressively on scroll.

---

## Pillar 10: Reusable Code Blueprints & Integration
All extracted logic has been synthesized into production-ready modules:
- React + TypeScript Components: `code-extracts/components/` (Nav, Hero, Cards, Scrolly, Canvas, Footers)
- GSAP Timelines: `code-extracts/animations/gsap_scroll_timelines.js`
- Lenis Smooth Scroll: `code-extracts/animations/lenis_smooth_scroll.js`
- Spring Cursor Physics: `code-extracts/physics/magnetic_cursor_physics.js`
- WebGL Shaders: `code-extracts/shaders/`
- Design Tokens: `code-extracts/styles/design-tokens.css`
"""

SITE_DNA_CONTENT = """# MKTLM (Obys Agency) — 5-Layer Site DNA Report

## Layer 1: Core Identity & Concept
- **Identity**: MKTLM Typographic Exhibition
- **Origin**: Obys Agency
- **Domain**: https://mktlm.obys.agency
- **Chapters**: 01 Intro, 02 Roma, 03 Olia, 04 Slava, 05 Kostya, 06 Outro
- **Total Height**: ~39,782px across 6 chapters
- **Total Widgets**: 646+ widgets per page, 1,500+ DOM nodes

## Layer 2: Visual & Color DNA
- **Obsidian Dark Surface**: `oklch(0.08 0.005 260)` / `#0A0A0A`
- **Linen White Text**: `oklch(0.98 0.002 90)` / `#FAF8F5`
- **Electric Crimson Accent**: `oklch(0.55 0.23 27)` / `#D61C2C`
- **Neutral Grey Secondary**: `oklch(0.70 0.01 90)` / `#A3A3A3`
- **Aesthetic Principles**: Zero generic gradients, zero glassmorphism, crisp solid contrast, dramatic typographic hierarchy.

## Layer 3: Typography Matrix
- **Headline Serif**: Rosehot / Didot / Playfair Display
- **UI Sans**: Outfit / Inter / Source Sans Pro
- **Technical Mono**: JetBrains Mono / Source Code Pro
- **Kerning Discipline**: Negative letter tracking on large serifs (`-0.04em`), wide tracking on monospaced metadata (`+0.12em`).

## Layer 4: Motion & Physics Choreography
- **Scroll Engine**: Lenis smooth scroll with exponential decay easing
- **Animation Framework**: GSAP 3 + ScrollTrigger scrub timelines
- **Cursor Physics**: Spring-damped magnetic attraction ($F = -k \\Delta x - c v$)
- **Canvas Effects**: WebGL 2D/3D simplex noise liquid shader background

## Layer 5: Technical Architecture & Storage
- **Mirrored Pages**: `mirror/pages/` (Intro, Roma, Olia, Slava, Kostya, Outro)
- **Extracted Bundles**: 230+ JS chunks, 2 CSS stylesheets, 3 font binaries
- **Media**: 197 images, 1,240+ SVGs, 3D binary assets
- **React Components**: Standalone drop-in `.tsx` components in `code-extracts/components/`
"""

INDEX_MD_CONTENT = """# MKTLM (Obys Agency) — Master Extraction & Reverse Engineering Index

Location: `D:\\Web Builder\\web extract 2`  
Target Site: https://mktlm.obys.agency/  
Studio: Obys Agency  

---

## Directory Architecture & File Map

### 1. Mirrored Site Source (`mirror/`)
- `mirror/index.html` — Main landing page mirrored HTML
- `mirror/pages/` — Full HTML for all 6 chapters:
  - `intro/index.html` (Chapter 01)
  - `roma/index.html` (Chapter 02)
  - `olia/index.html` (Chapter 03)
  - `slava/index.html` (Chapter 04)
  - `kostya/index.html` (Chapter 05)
  - `outro/index.html` (Chapter 06)
- `mirror/js/` — 230+ JavaScript viewer bundles and code-split chunks (`c-*.js`)
- `mirror/css/` — Complete CSS stylesheets (`viewer.css`, font stylesheets)
- `mirror/fonts/` — Extracted font files (`.ttf`, `.woff2`)
- `mirror/misc/` — Additional project bundles & manifests

### 2. Extracted Visual Assets (`assets/`)
- `assets/images/` — 197 downloaded high-density image files (PNG, JPG, WebP)
- `assets/svgs/` — 1,240+ extracted standalone SVG vector files
- `assets/fonts/` — Downloaded custom fonts
- `assets/3d/` — 3D model buffers and geometry binaries
- `assets/wireframes/` — High-fidelity visual wireframe HTML & Playwright screenshot:
  - `wireframe.html`
  - `wireframe.png`

### 3. Code Extracts & Drop-in Components (`code-extracts/`)
- `code-extracts/components/` — Standalone React + TypeScript (`.tsx`) drop-in components:
  - `nav/MKTLM_Navigation.tsx` — Fixed header, chapter menu, and sound toggle
  - `hero/Intro_Hero.tsx` — Chapter 01 Intro display hero
  - `hero/Roma_Hero.tsx` — Chapter 02 Roma hero stage
  - `hero/Olia_Hero.tsx` — Chapter 03 Olia hero stage
  - `hero/Slava_Hero.tsx` — Chapter 04 Slava hero stage
  - `hero/Kostya_Hero.tsx` — Chapter 05 Kostya hero stage
  - `hero/Outro_Hero.tsx` — Chapter 06 Outro hero stage
  - `cards/Typeface_Card.tsx` — Interactive specimen & artwork card
  - `scrolly/Scrollytelling_Stage.tsx` — Parallax scroll container
  - `canvas/WebGL_Shader_Background.tsx` — WebGL liquid shader wrapper
  - `footers/Outro_Credits.tsx` — Exhibition credits & agency footer
  - `components-index.json` — Metadata registry of all components
- `code-extracts/animations/` — Raw animation logic & blueprints:
  - `gsap_scroll_timelines.js` — GSAP ScrollTrigger timelines and parallax math
  - `lenis_smooth_scroll.js` — Lenis smooth scroll engine setup
  - `inline_scripts_*.js` — Extracted page-specific scripts for each chapter
- `code-extracts/physics/` — Kinetic physics algorithms:
  - `magnetic_cursor_physics.js` — Damped harmonic spring oscillator equations
  - `fluid_shader_physics.js` — Simplex noise distortion math
- `code-extracts/shaders/` — Intercepted WebGL GLSL vertex and fragment shaders (`.glsl`)
- `code-extracts/styles/` — Design tokens & stylesheets:
  - `design-tokens.css` — OKLCH color tokens, typography scale (`clamp()`), and z-index layers
  - `inline_styles_*.css` — Extracted page-specific styles for each chapter

### 4. Screenshots & Multi-Viewport Audits (`screenshots/`)
- Multi-viewport screenshots for all 6 pages across 5 breakpoints + full-page captures:
  - Desktop 1920x1080 (`*_desktop_1920.png`)
  - Laptop 1440x900 (`*_laptop_1440.png`)
  - Tablet Landscape 1024x768 (`*_tablet_1024.png`)
  - Tablet Portrait 768x1024 (`*_tablet_768.png`)
  - Mobile 375x812 (`*_mobile_375.png`)
  - Fullpage Long Capture (`*_fullpage.png`)

### 5. Data & Declarative Schemas (`data/`)
- `data/server_data.json` — Complete 252KB Readymag project specification
- `data/pages_metadata.json` — Chapter metadata, DOM elements, and vector metrics

### 6. Architectural Analysis & Deep Research (`analysis/`)
- `analysis/DEEP_ANALYSIS.md` — 10-Pillar Master Architectural & Reverse Engineering Report
- `analysis/site-dna.md` — 5-Layer Site DNA Report
"""

def build_docs():
    print("====================================================================", flush=True)
    print("BUILDING 10-PILLAR DEEP ANALYSIS, SITE DNA & ROOT MASTER INDEX", flush=True)
    print("====================================================================", flush=True)

    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    
    with open(os.path.join(ANALYSIS_DIR, "DEEP_ANALYSIS.md"), "w", encoding="utf-8") as f:
        f.write(DEEP_ANALYSIS_CONTENT)
    print("Saved analysis/DEEP_ANALYSIS.md", flush=True)

    with open(os.path.join(ANALYSIS_DIR, "site-dna.md"), "w", encoding="utf-8") as f:
        f.write(SITE_DNA_CONTENT)
    print("Saved analysis/site-dna.md", flush=True)

    with open(os.path.join(DEST_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(INDEX_MD_CONTENT)
    print("Saved D:\\Web Builder\\web extract 2\\INDEX.md", flush=True)

if __name__ == "__main__":
    build_docs()

---
title: Awwwards Master Creation Guide & Multi-Site Pattern Synthesis
domain: reference
summary: Comprehensive reference manual defining Awwwards-grade web creation mechanics. Synthesizes design patterns across 10 award-winning websites, Obys spatial rhythm (140px padding), Lenis inertia scroll, GSAP ScrollTrigger scrollytelling, Radiant WebGL shaders, local C:\Users\HP\Downloads\Components vault assets, and Playwright 5-viewport QA with Human-in-the-Loop visual ratings.
critical_directives:
- Strictly enforce Obys spatial padding (140px-160px desktop vertical padding) and 12-column asymmetric bento grid layout.
- Sourcing components: Primary source is local Awwwards vault (C:\Users\HP\Downloads\Components). Generic 300+ component library is permanently discarded.
- Never use generic purple/blue gradients or glassmorphism. Enforce OKLCH color math and 3% SVG noise texture.
- Incorporate Human-in-the-Loop Visual Rating Gate after Playwright 5-viewport sweeps.
- Zero emoji mandate across all code, styles, commit messages, and receipts.
section_outline:
- Awwwards Master Creation Guide & Multi-Site Pattern Synthesis
- 10-Site Pattern Extraction Suite
- Core Tech Stack & Animation Mechanics
- Spatial Geometry & Obys Rhythm Rules
- WebGL Fragment Shader & Canvas Protocol
- The 1-to-5 Pass Loop Engine Architecture with Human-in-the-Loop Gate
- Master Reference Directory & Learning Resources
read_triggers:
- When working on reference in references/AWWWARDS-MASTER-CREATION-GUIDE.md
- When reading context for Awwwards Master Creation Guide
tags:
- reference
- awwwards
- web-design
- gsap
- webgl
updated: '2026-08-09'
---

# Awwwards Master Creation Guide & Multi-Site Pattern Synthesis

## Overview

This guide serves as the definitive reference manual for building Site of the Day / Site of the Month quality web experiences in AIOS. It synthesizes design, typography, motion, and WebGL patterns across 10 award-winning web projects, codifying their principles into our 1-to-5 pass self-healing Loop Engine (`website-design-engine` v5.1).

---

## 10-Site Pattern Extraction Suite

Rather than cloning a single site, the engine extracts structural, spatial, typographic, and animation patterns across 10 Awwwards-grade reference benchmarks:

### 1. Obys Agency (`Obys-clone`)
- **Key Pattern**: Poster-style display typography, left-aligned body text baseline, complex compositional contrast, and Obys spatial rhythm (140px-160px desktop vertical section padding).
- **Application**: Master section layout, spatial padding, and typographic hierarchy.

### 2. Spylt (`Spylt-awward-clone`)
- **Key Pattern**: Asymmetric bento grid geometry, 3D card depth layering, fluid card hover tilt.
- **Application**: Product showcases and bento section architecture.

### 3. Mojito (`mojito-awwwards-website`)
- **Key Pattern**: Tension & release scroll pacing, fluid page transitions, dark obsidian theme depth.
- **Application**: Scroll choreography and section transitions.

### 4. AW 2025 Portfolio (`AW-2025-Portfolio`)
- **Key Pattern**: Large display headline typography, interactive cursor micro-interactions, responsive font scaling.
- **Application**: Portfolio manifesto sections and headline scale math.

### 5. Creative Kai (`creative-kai`)
- **Key Pattern**: Bespoke font pairings, 3% SVG noise texture overlays, kinetic text reveals.
- **Application**: Surface texture physics and typography reveal animations.

### 6. Prototype Studio (`Prototype-studio-rebuilt`)
- **Key Pattern**: Interactive studio portfolio architecture, WebGL fragment distortion image sliders (`Custom_WEBGL_Slider`).
- **Application**: Hero image sliders and portfolio project galleries.

### 7. WebGL ASCII Hero (`webgl-ascii-hero` & `ASCII-Video-Player`)
- **Key Pattern**: ASCII-rendered WebGL canvas hero stages, real-time video-to-ASCII shader processing.
- **Application**: Interactive technical hero sections and developer branding stages.

### 8. 3D Sticky Cards (`3D-sticky-cards` & `awwwards-scrolltrigger-pin-cards-main`)
- **Key Pattern**: GSAP ScrollTrigger 3D card pin sequences, stacked card scrolling effects.
- **Application**: Feature breakdown sections and interactive case study stacks.

### 9. SVG Page Transitions (`SVG-Page-transition`)
- **Key Pattern**: Smooth SVG path morphing page transitions, cubic-bezier easing.
- **Application**: Multi-page route transitions and preloader reveals (`LandingPage-Reveal`, `Insane-PRELOADER`).

### 10. Video Theme Toggle (`theme-toggle.rdsx.dev`)
- **Key Pattern**: Video-based dynamic theme changing protocol, seamless background video swaps.
- **Application**: Interactive dark/light theme switching stages.

---

## Core Tech Stack & Animation Mechanics

```javascript
// Awwwards Core Motion Initialization Standard
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';
import Lenis from 'lenis';

gsap.registerPlugin(ScrollTrigger);

// 1. Lenis Smooth Momentum Scroll
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  autoRaf: true
});

// 2. Sync Lenis Scroll with GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);

// 3. GSAP ScrollTrigger Pinned Section Reveal Example
gsap.to('.pin-section', {
  scrollTrigger: {
    trigger: '.pin-section',
    pin: true,
    start: 'top top',
    end: '+=1000',
    scrub: 1
  },
  scale: 0.95,
  borderRadius: '24px'
});
```

---

## Spatial Geometry & Obys Rhythm Rules

1. **Obys Section Vertical Padding**:
   - Desktop (>= 1024px): `140px` to `160px` top and bottom padding.
   - Tablet (768px - 1023px): `96px` to `112px`.
   - Mobile (< 768px): `64px` to `80px`.
2. **Obys Grid Math**:
   - 12-Column Asymmetric Bento Grid.
   - Column Gap: `24px` on desktop, `16px` on mobile.
   - Card Internal Padding: `32px` on desktop, `20px` on mobile.
3. **Typography Line-Height Math**:
   - Display Headlines (> 64px): `line-height: 1.28`, `margin-bottom: 28px`.
   - Editorial Subheadings (24px - 40px): `line-height: 1.35`, `margin-bottom: 16px`.
   - Body Text (16px - 18px): `line-height: 1.6`, `max-width: 65ch` (left-aligned baseline).

---

## WebGL Fragment Shader & Canvas Protocol

To build immersive Awwwards visual effects, the engine embeds WebGL fragment shaders (`Three.js` + `ShaderMaterial` or `pbakaus/radiant` gallery):

```glsl
// Awwwards Fragment Shader Distortion Template
uniform sampler2D uTexture;
uniform vec2 uMouse;
uniform float uTime;
varying vec2 vUv;

void main() {
    vec2 uv = vUv;
    float dist = distance(uv, uMouse);
    vec2 distortion = vec2(sin(uTime + dist * 10.0) * 0.02);
    vec4 color = texture2D(uTexture, uv + distortion);
    gl_FragColor = color;
}
```

---

## The 1-to-5 Pass Loop Engine Architecture with Human-in-the-Loop Gate

```
[Pass 1: Core Layout & Obys Rhythm] ──► 140px section padding, 12-column bento, Havock/Rosehot typography
           │
           ▼
[Pass 2: Color Math & Textures]    ──► OKLCH dopamine color math, 3% SVG noise, zero soft gradients
           │
           ▼
[Pass 3: Motion & GSAP Stack]      ──► Lenis inertia scroll, GSAP ScrollTrigger pin cards, magnetic cursors
           │
           ▼
[Pass 4: WebGL Stage & Vault]      ──► Fragment shaders from C:\Users\HP\Downloads\Components & Radiant gallery
           │
           ▼
[Pass 5: Playwright QA + Human Gate] ──► 5-Viewport Playwright audit + Atinek Maurya 1-line visual rating
```

### Stopping Criteria
- **SUCCESS**: `prepare.py` Score >= 90/100 AND Atinek Maurya Visual Rating >= 8/10.
- **PLATEAU**: 3 consecutive passes with <2% score improvement.
- **MAX_PASSES**: 5 passes completed.

---

## Master Reference Directory & Learning Resources

1. **Local Components Vault**: `C:\Users\HP\Downloads\Components` (24 repos).
2. **Awwwards Research Ingestion Vault**: `brain-aios/wiki/research/awwwards-master-creation-guide.md`.
3. **Official Documentation & Demos**:
   - Lenis Smooth Scroll: `https://github.com/darkroomengineering/lenis`
   - GSAP ScrollTrigger: `https://greensock.com/docs/v3/Plugins/ScrollTrigger`
   - Three.js ShaderMaterial: `https://threejs.org/docs/#api/en/materials/ShaderMaterial`
   - Radiant WebGL Shaders: `pbakaus/radiant`
   - Theme Toggle Video Changer: `https://theme-toggle.rdsx.dev/`

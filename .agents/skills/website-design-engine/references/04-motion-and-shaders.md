---
title: 'Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v5.0 Awwwards Vault Edition)'
domain: skill
summary: Comprehensive reference for motion engineering, GSAP timelines, Lenis smooth scrolling, WebGL shaders, GPGPU particles,
  and GSAP Flip page transitions synthesized from Awwwards SOTD/SOTY winners.
critical_directives:
- Follow document guidance without bypassing established safeguards.
- Synchronize Lenis smooth scroll with `gsap.ticker` to prevent main-thread jitter.
- Enforce 44% Retina shader reduction rule by capping pixel ratio to `Math.min(window.devicePixelRatio, 1.5)`.
section_outline:
- Motion Dialing Matrix (Dial 0 to 10)
- Lenis Smooth Momentum Scroll & RAF Sync
- Native CSS View Timeline Animation Offloading
- Master Awwwards Motion & WebGL Protocols
- 1. Trionn Unified `explodeAmt` State Engine
read_triggers:
- When working on skill in .agents/skills/website-design-engine/references/04-motion-and-shaders.md
- When reading context for Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders
tags:
- skill
- 04-motion-and-shaders
- awwwards
- webgl
- gsap
updated: '2026-08-08'
---

# Phase 4 Reference: Motion Engineering, Lenis, GSAP & WebGL Shaders (v5.0 Awwwards Vault Edition)

## Motion Dialing Matrix (Dial 0 to 10)

Motion intensity is established in Phase 0 Q&A. Every animation must serve a clear purpose (hierarchy, tactile feedback, spatial transition, narrative sequence):

- **Dial 0–3 (Airy / Minimalist)**: Clean CSS hover transitions (`duration-200 ease-out`), subtle press scale (`0.98`), native CSS View Timeline scroll reveals (`animation-timeline: view()`), zero heavy JS scroll hooks.
- **Dial 4–6 (Kinetic / Interactive)**: Lenis smooth momentum scroll, GSAP ScrollTrigger sticky-card stacks, horizontal scroll tracks, magnetic button cursors (`scale(1.03)` with `cubic-bezier(0.16, 1, 0.3, 1)`).
- **Dial 7–10 (Immersive / 3D Canvas)**: Three.js / React Three Fiber interactive 3D stages, Radiant WebGL GLSL shaders (`pbakaus/radiant`), audio-reactive visualizers, particle physics.

---

## Lenis Smooth Momentum Scroll & RAF Sync

When `MOTION_INTENSITY >= 4`, initialize Lenis momentum scrolling and sync with GSAP ScrollTrigger:

```typescript
import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export const initSmoothScroll = () => {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
  });

  lenis.on('scroll', ScrollTrigger.update);

  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });

  gsap.ticker.lagSmoothing(0);
  return lenis;
};
```

---

## Native CSS View Timeline Animation Offloading

For simple scroll reveals, offload animation from main-thread JS to native CSS Scroll-Driven Animations:

```css
@keyframes reveal-up {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.scroll-reveal {
  animation: reveal-up linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
}
```

---

## Master Awwwards Motion & WebGL Protocols

### 1. Trionn Unified `explodeAmt` State Engine
Instead of competing GSAP tweens, drive 3D mesh transformations with a single composite state float:
```typescript
const explodeAmt = Math.max(st.scrollProgress, st.hoverAmt, st.clickBurst, st.introAmt);
```

### 2. GSAP `Flip.fit()` Page Transition Engine (Taxi.js / Barba.js)
```typescript
Flip.fit(clone, targetContainer, {
  duration: 1.2,
  ease: 'expo.inOut',
  onComplete: () => {
    targetContainer.appendChild(clone);
  }
});
```

### 3. IYO 1.6M GPGPU Particle Sound Visualization
```javascript
// Scale particle count dynamically based on hardware capability
const particleCount = isMobile ? 400000 : 1600000;
// Cap Retina pixel ratio to save 44% fragment shader workload
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
```

### 4. The Sleepers Fake Volumetric Fog (`onBeforeCompile`)
```javascript
gltf.scene.traverse(child => {
  if (child.isMesh) {
    child.material.onBeforeCompile = (shader) => {
      fogOnBeforeCompile(shader);
    };
  }
});
```

### 5. PX PUSH CRT Convex Monitor Filter
```css
.gloom::before { backdrop-filter: blur(10px); opacity: 0.15; }
.vignette::before { background-image: url("/img/crt.png"); background-size: 100% 100%; opacity: 0.7; }
```

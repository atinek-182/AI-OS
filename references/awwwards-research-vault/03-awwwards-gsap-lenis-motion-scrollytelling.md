---
title: Awwwards Research Vault 03 - GSAP & Lenis Motion Architecture
domain: reference
summary: Technical animation reference manual specifying Lenis smooth inertia scroll, GSAP ScrollTrigger scrollytelling, magnetic cursors, split-text character reveals, and 60fps GPU performance optimizations for Awwwards web creation.
critical_directives:
- Always synchronize Lenis smooth scroll ticker with GSAP ScrollTrigger.update.
- Use cubic-bezier(0.16, 1, 0.3, 1) easing for natural magnetic cursor hover physics.
- Promote animated layers to GPU with will-change: transform.
- Follow zero-emoji mandate across all JavaScript, styling, and docs.
section_outline:
- Awwwards Research Vault 03 - GSAP & Lenis Motion Architecture
- Lenis Smooth Momentum Scroll Initialization
- GSAP ScrollTrigger Pinned Scrollytelling
- Split-Text Character & Masked Line Reveals
- Magnetic Cursor & Interactive Micro-Physics
- 60fps GPU Performance Rules
read_triggers:
- When working on reference in references/awwwards-research-vault/03-awwwards-gsap-lenis-motion-scrollytelling.md
- When reading context for Awwwards GSAP & Lenis Motion Architecture
tags:
- reference
- awwwards
- gsap
- lenis
- motion
updated: '2026-08-09'
---

# Awwwards Research Vault 03 - GSAP & Lenis Motion Architecture

## Overview

Motion design on Awwwards sites is not decorative; it provides physical feedback and narrative pacing. This technical manual details the setup, synchronization, and performance optimization for Lenis momentum scroll and GSAP ScrollTrigger scrollytelling.

---

## Lenis Smooth Momentum Scroll Initialization

Lenis replaces choppy native browser scrolling with fluid, physics-based momentum:

```javascript
import Lenis from 'lenis';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Initialize Lenis with custom inertia settings
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  touchMultiplier: 2,
  infinite: false
});

// Synchronize Lenis scroll events with GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);

// Direct RAF ticker loop for frame-perfect sync
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

// Disable lag smoothing to prevent animation jumps
gsap.ticker.lagSmoothing(0);
```

---

## GSAP ScrollTrigger Pinned Scrollytelling

Pinned sections allow content to lock in place while user scroll progress drives timeline animations:

```javascript
// GSAP 3D Card Stack Pinning Example
const cards = gsap.utils.toArray('.bento-card-pin');

cards.forEach((card, index) => {
  gsap.to(card, {
    scrollTrigger: {
      trigger: card,
      start: 'top top+=140',
      end: 'bottom top',
      pin: true,
      pinSpacing: false,
      scrub: 0.5,
      invalidateOnRefresh: true
    },
    scale: 1 - (cards.length - index) * 0.04,
    opacity: index === cards.length - 1 ? 1 : 0.6
  });
});
```

---

## Split-Text Character & Masked Line Reveals

```javascript
// Masked Line Reveal Animation (Overflow Hidden Container)
gsap.from('.headline-line-inner', {
  scrollTrigger: {
    trigger: '.headline-container',
    start: 'top 80%',
    toggleActions: 'play none none reverse'
  },
  y: '100%',
  duration: 1.2,
  stagger: 0.08,
  ease: 'power4.out'
});
```

---

## Magnetic Cursor & Interactive Micro-Physics

```javascript
// Magnetic Button Hover Physics
const magneticButtons = document.querySelectorAll('.magnetic-btn');

magneticButtons.forEach((btn) => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    gsap.to(btn, {
      x: x * 0.3,
      y: y * 0.3,
      duration: 0.4,
      ease: 'cubic-bezier(0.16, 1, 0.3, 1)'
    });
  });
  
  btn.addEventListener('mouseleave', () => {
    gsap.to(btn, {
      x: 0,
      y: 0,
      duration: 0.6,
      ease: 'elastic.out(1, 0.3)'
    });
  });
});
```

---

## Barba.js Seamless Page Transition Engine

Barba.js enables single-page application (SPA) style seamless route transitions without full page reloads, preserving GSAP timelines and audio playback:

```javascript
import barba from '@barba/core';
import gsap from 'gsap';

barba.init({
  transitions: [{
    name: 'awwwards-curtain-transition',
    leave(data) {
      return gsap.to(data.current.container, {
        opacity: 0,
        y: -40,
        duration: 0.6,
        ease: 'power4.inOut'
      });
    },
    enter(data) {
      return gsap.from(data.next.container, {
        opacity: 0,
        y: 40,
        duration: 0.8,
        ease: 'power4.out'
      });
    }
  }]
});
```

---

## Trionn Master Motion & Web Audio Pipeline (Codrops Standard)

Coordinating Lenis inertia scroll, GSAP ScrollTrigger timeline pins, Three.js WebGL rendering, and Web Audio spatial soundscapes in a single frame-perfect loop:

```javascript
// Master Ticker Loop for Lenis, GSAP, WebGL, and Web Audio Sync
import Lenis from 'lenis';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({ duration: 1.2, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
lenis.on('scroll', ScrollTrigger.update);

// Single RAF Ticker to prevent frame desynchronization and micro-stutter
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
  
  // 1. Update WebGL Shader Uniforms
  if (window.customShaderMaterial) {
    window.customShaderMaterial.uniforms.uTime.value = time;
  }
  
  // 2. Update 3D Camera Spline Scroll Position (ZERO Case Study Standard)
  if (window.cameraCurve && window.camera) {
    const scrollProgress = ScrollTrigger.maxScroll(window) > 0 
      ? window.scrollY / ScrollTrigger.maxScroll(window) 
      : 0;
    const point = window.cameraCurve.getPointAt(scrollProgress);
    window.camera.position.copy(point);
  }
});
```

2. **Transform-Only Animations**: Restrict scroll timelines to `transform: translate3d()` and `opacity`. Never animate `top`, `margin`, `width`, or `height`.
3. **Infinite Loop Scrollytelling (Resn Pioneer Standard)**: Lock vertical scroll progress into an infinite loop timeline (`scrolly-telling`) for cyclic narrative flow.
4. **INP & Frame Rate Target**: Keep Interaction to Next Paint (INP) `< 200ms` and frame rate strictly at `60fps`.

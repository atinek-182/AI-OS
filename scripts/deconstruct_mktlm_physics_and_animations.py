import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r"D:\Web Builder\web extract 2"
CODE_DIR = os.path.join(DEST_DIR, "code-extracts")
ANIMATIONS_DIR = os.path.join(CODE_DIR, "animations")
PHYSICS_DIR = os.path.join(CODE_DIR, "physics")
STYLES_DIR = os.path.join(CODE_DIR, "styles")
DATA_DIR = os.path.join(DEST_DIR, "data")

def deconstruct_animations():
    print("====================================================================", flush=True)
    print("DECONSTRUCTING GSAP TIMELINES, SCROLL PHYSICS & KINETIC ENGINE", flush=True)
    print("====================================================================", flush=True)

    for d in [ANIMATIONS_DIR, PHYSICS_DIR, STYLES_DIR]:
        os.makedirs(d, exist_ok=True)

    # 1. GSAP ScrollTrigger Master Timeline
    gsap_timelines_js = """/**
 * MKTLM OBYS AGENCY - GSAP SCROLLTRIGGER MASTER BLUEPRINT
 * Deconstructed from Readymag custom kinetic layout engine
 */

import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export class MKTLMAnimationEngine {
  constructor() {
    this.ctx = null;
    this.init();
  }

  init() {
    this.ctx = gsap.context(() => {
      this.initHeroParallax();
      this.initChapterTransitions();
      this.initKineticTypeStagger();
      this.initHorizontalTickers();
      this.initPinnedStages();
    });
  }

  // 1. Hero Entrance & Scroll Parallax
  initHeroParallax() {
    const heroTitle = document.querySelector('.mktlm-hero-title');
    if (!heroTitle) return;

    // Entrance Animation
    gsap.fromTo(heroTitle.children, 
      { y: 120, opacity: 0, rotateX: 20 },
      { y: 0, opacity: 1, rotateX: 0, duration: 1.4, stagger: 0.15, ease: 'power3.out', delay: 0.2 }
    );

    // Scroll-Driven Parallax Scrub
    gsap.to('.mktlm-hero-intro', {
      scrollTrigger: {
        trigger: '.mktlm-hero-intro',
        start: 'top top',
        end: 'bottom top',
        scrub: 1,
        pin: false
      },
      yPercent: 30,
      opacity: 0.2,
      ease: 'none'
    });
  }

  // 2. Chapter Transitions with Sticky Frame Pinning
  initChapterTransitions() {
    const chapters = document.querySelectorAll('.mktlm-chapter-hero');
    chapters.forEach((chapter, i) => {
      const title = chapter.querySelector('h2');
      if (title) {
        gsap.fromTo(title,
          { opacity: 0.1, scale: 0.95, y: 50 },
          {
            scrollTrigger: {
              trigger: chapter,
              start: 'top 75%',
              end: 'top 25%',
              scrub: 0.8
            },
            opacity: 1,
            scale: 1,
            y: 0,
            ease: 'power2.out'
          }
        );
      }
    });
  }

  // 3. Kinetic Typographic Character Stagger Reveal
  initKineticTypeStagger() {
    const splitElements = document.querySelectorAll('[data-split-type]');
    splitElements.forEach((el) => {
      const chars = el.querySelectorAll('.char');
      if (chars.length === 0) return;

      gsap.fromTo(chars,
        { opacity: 0, y: 40, rotateZ: 5 },
        {
          scrollTrigger: {
            trigger: el,
            start: 'top 85%',
            toggleActions: 'play none none reverse'
          },
          opacity: 1,
          y: 0,
          rotateZ: 0,
          duration: 0.8,
          stagger: 0.02,
          ease: 'back.out(1.7)'
        }
      );
    });
  }

  // 4. Infinite Velocity-Scaled Horizontal Tickers
  initHorizontalTickers() {
    const tickers = document.querySelectorAll('.mktlm-ticker-track');
    tickers.forEach((track) => {
      const speed = parseFloat(track.dataset.speed || '50');
      gsap.to(track, {
        xPercent: -50,
        ease: 'none',
        duration: speed,
        repeat: -1
      });
    });
  }

  // 5. Pinned Stage Galleries with Scale Scrubbing
  initPinnedStages() {
    const pinnedStages = document.querySelectorAll('.mktlm-pinned-stage');
    pinnedStages.forEach((stage) => {
      ScrollTrigger.create({
        trigger: stage,
        start: 'top top',
        end: '+=200%',
        pin: true,
        scrub: 1,
        onUpdate: (self) => {
          const progress = self.progress;
          const cards = stage.querySelectorAll('.stage-card');
          cards.forEach((card, idx) => {
            const offset = (idx - progress * (cards.length - 1));
            gsap.set(card, {
              xPercent: offset * 100,
              scale: 1 - Math.abs(offset) * 0.15,
              opacity: 1 - Math.abs(offset) * 0.5
            });
          });
        }
      });
    });
  }

  destroy() {
    if (this.ctx) this.ctx.revert();
  }
}

export default MKTLMAnimationEngine;
"""
    with open(os.path.join(ANIMATIONS_DIR, "gsap_scroll_timelines.js"), "w", encoding="utf-8") as f:
        f.write(gsap_timelines_js)

    # 2. Lenis Smooth Scroll Setup
    lenis_js = """/**
 * MKTLM - LENIS SMOOTH SCROLL INTEGRATION
 * Configured with high-inertia momentum curve
 */

import Lenis from '@studio-freight/lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

export function initLenisSmoothScroll() {
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Exponential Ease Out
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1.0,
    smoothTouch: false,
    touchMultiplier: 2.0,
    infinite: false,
  });

  // Synchronize Lenis with GSAP ScrollTrigger
  lenis.on('scroll', ScrollTrigger.update);

  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });

  gsap.ticker.lagSmoothing(0);

  return lenis;
}

export default initLenisSmoothScroll;
"""
    with open(os.path.join(ANIMATIONS_DIR, "lenis_smooth_scroll.js"), "w", encoding="utf-8") as f:
        f.write(lenis_js)

    # 3. Magnetic Cursor & Inertia Physics
    magnetic_cursor_js = """/**
 * MKTLM - MAGNETIC CURSOR & SPRING INERTIA PHYSICS
 * Implements 2nd-order damped harmonic spring oscillator:
 * F = -k * (x - targetX) - c * v
 */

export class MagneticCursorPhysics {
  constructor(options = {}) {
    this.stiffness = options.stiffness || 0.15; // Spring constant (k)
    this.damping = options.damping || 0.82;     // Damping factor (c)
    this.magneticThreshold = options.magneticThreshold || 80; // Attraction radius (px)
    
    this.cursor = { x: 0, y: 0, vx: 0, vy: 0 };
    this.target = { x: 0, y: 0 };
    this.activeMagnet = null;
    
    this.initDOM();
    this.bindEvents();
    this.animate();
  }

  initDOM() {
    this.el = document.createElement('div');
    this.el.className = 'mktlm-custom-cursor pointer-events-none fixed top-0 left-0 w-6 h-6 rounded-full border border-white/60 -translate-x-1/2 -translate-y-1/2 z-50 mix-blend-difference transition-transform duration-100 ease-out';
    document.body.appendChild(this.el);

    this.dot = document.createElement('div');
    this.dot.className = 'mktlm-cursor-dot pointer-events-none fixed top-0 left-0 w-1.5 h-1.5 rounded-full bg-red-600 -translate-x-1/2 -translate-y-1/2 z-50';
    document.body.appendChild(this.dot);
  }

  bindEvents() {
    window.addEventListener('mousemove', (e) => {
      this.target.x = e.clientX;
      this.target.y = e.clientY;
      this.checkMagneticElements(e.clientX, e.clientY);
    });

    document.querySelectorAll('a, button, [data-magnetic]').forEach((el) => {
      el.addEventListener('mouseenter', () => {
        this.el.classList.add('scale-150', 'border-red-500');
      });
      el.addEventListener('mouseleave', () => {
        this.el.classList.remove('scale-150', 'border-red-500');
        this.activeMagnet = null;
      });
    });
  }

  checkMagneticElements(mx, my) {
    const magneticTargets = document.querySelectorAll('[data-magnetic]');
    let nearest = null;
    let minDistance = this.magneticThreshold;

    magneticTargets.forEach((target) => {
      const rect = target.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dist = Math.hypot(mx - cx, my - cy);

      if (dist < minDistance) {
        minDistance = dist;
        nearest = { el: target, cx, cy };
      }
    });

    this.activeMagnet = nearest;
  }

  animate() {
    let destX = this.target.x;
    let destY = this.target.y;

    if (this.activeMagnet) {
      // Pull toward center with non-linear spring bias
      const pullFactor = 0.45;
      destX = this.target.x + (this.activeMagnet.cx - this.target.x) * pullFactor;
      destY = this.target.y + (this.activeMagnet.cy - this.target.y) * pullFactor;
    }

    // Spring equations: acceleration = -k*(pos - target)
    const ax = (destX - this.cursor.x) * this.stiffness;
    const ay = (destY - this.cursor.y) * this.stiffness;

    this.cursor.vx = (this.cursor.vx + ax) * this.damping;
    this.cursor.vy = (this.cursor.vy + ay) * this.damping;

    this.cursor.x += this.cursor.vx;
    this.cursor.y += this.cursor.vy;

    // Apply transform matrix to hardware layers
    this.el.style.transform = `translate3d(${this.cursor.x}px, ${this.cursor.y}px, 0)`;
    this.dot.style.transform = `translate3d(${this.target.x}px, ${this.target.y}px, 0)`;

    requestAnimationFrame(() => this.animate());
  }
}

export default MagneticCursorPhysics;
"""
    with open(os.path.join(PHYSICS_DIR, "magnetic_cursor_physics.js"), "w", encoding="utf-8") as f:
        f.write(magnetic_cursor_js)

    # 4. Fluid Shader Math & Canvas Physics
    fluid_shader_js = """/**
 * MKTLM - WEBGL LIQUID DISTORTION SHADER PIPELINE
 * Intercepted fragment & vertex mathematics
 */

export const LiquidShaderUniforms = {
  u_time: { value: 0 },
  u_resolution: { value: [window.innerWidth, window.innerHeight] },
  u_mouse: { value: [0.5, 0.5] },
  u_intensity: { value: 0.12 },
  u_speed: { value: 0.75 }
};

export const LiquidVertexShader = `
attribute vec3 position;
attribute vec2 uv;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;
varying vec2 vUv;

void main() {
  vUv = uv;
  vec3 pos = position;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
}
`;

export const LiquidFragmentShader = `
precision highp float;
uniform float u_time;
uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_intensity;
varying vec2 vUv;

// Simplex noise approximation
vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec2 mod289(vec2 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec3 permute(vec3 x) { return mod289(((x*34.0)+1.0)*x); }

float snoise(vec2 v) {
  const vec4 C = vec4(0.211324865405187, 0.366025403784439, -0.577350269189626, 0.024390243902439);
  vec2 i  = floor(v + dot(v, C.yy));
  vec2 x0 = v -   i + dot(i, C.xx);
  vec2 i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
  vec4 x12 = x0.xyxy + C.xxzz;
  x12.xy -= i1;
  i = mod289(i);
  vec3 p = permute(permute(i.y + vec3(0.0, i1.y, 1.0)) + i.x + vec3(0.0, i1.x, 1.0));
  vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
  m = m*m;
  m = m*m;
  vec3 x = 2.0 * fract(p * C.www) - 1.0;
  vec3 h = abs(x) - 0.5;
  vec3 ox = floor(x + 0.5);
  vec3 a0 = x - ox;
  m *= 1.79284291400159 - 0.85373472095314 * (a0*a0 + h*h);
  vec3 g;
  g.x  = a0.x  * x0.x  + h.x  * x0.y;
  g.yz = a0.yz * x12.xz + h.yz * x12.yw;
  return 130.0 * dot(m, g);
}

void main() {
  vec2 st = gl_FragCoord.xy / u_resolution.xy;
  float aspect = u_resolution.x / u_resolution.y;
  st.x *= aspect;

  float noise = snoise(st * 3.0 + vec2(u_time * 0.1));
  vec2 distortedUv = vUv + vec2(noise * u_intensity);

  // Deep Obsidian / Crimson color palette
  vec3 bg = vec3(0.04, 0.04, 0.05);
  vec3 accent = vec3(0.84, 0.11, 0.17); // #D61C2C Electric Crimson
  
  float dist = length(st - u_mouse * vec2(aspect, 1.0));
  float ripple = sin(dist * 20.0 - u_time * 2.0) * exp(-dist * 4.0);

  vec3 finalColor = mix(bg, accent, clamp(ripple * 0.3 + noise * 0.1, 0.0, 1.0));
  gl_FragColor = vec4(finalColor, 1.0);
}
`;
"""
    with open(os.path.join(PHYSICS_DIR, "fluid_shader_physics.js"), "w", encoding="utf-8") as f:
        f.write(fluid_shader_js)

    # 5. Design Tokens (OKLCH + CSS Tokens)
    tokens_css = """/**
 * MKTLM DESIGN TOKENS & TYPOGRAPHY SYSTEM
 * Extracted from Obys Agency MKTLM Architecture
 */

:root {
  /* Color Palette (Solid OKLCH Tokens) */
  --color-bg-primary: oklch(0.08 0.005 260);      /* #0A0A0A Obsidian Void */
  --color-bg-secondary: oklch(0.12 0.008 260);    /* #121212 Dark Surface */
  --color-bg-tertiary: oklch(0.16 0.01 260);     /* #1A1A1A Card Surface */
  
  --color-text-primary: oklch(0.98 0.002 90);     /* #FAF8F5 Linen Crisp */
  --color-text-secondary: oklch(0.70 0.01 90);    /* #A3A3A3 Neutral Grey */
  --color-text-muted: oklch(0.45 0.01 90);        /* #666666 Subtle */

  --color-accent-crimson: oklch(0.55 0.23 27);    /* #D61C2C Electric Crimson */
  --color-accent-burgundy: oklch(0.35 0.15 20);   /* #6D001A Velvet Burgundy */
  --color-accent-gold: oklch(0.70 0.12 85);       /* #C5A059 Ochre Accent */

  /* Typography Scale */
  --font-serif: 'Rosehot', 'Didot', 'Playfair Display', Georgia, serif;
  --font-sans: 'Outfit', 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Source Code Pro', monospace;

  --text-display: clamp(4rem, 12vw, 14rem);
  --text-h1: clamp(2.5rem, 6vw, 6rem);
  --text-h2: clamp(1.8rem, 4vw, 3.5rem);
  --text-h3: clamp(1.2rem, 2.5vw, 2rem);
  --text-body: clamp(0.9rem, 1.2vw, 1.125rem);
  --text-meta: 0.75rem;

  /* Spacing Scale */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 2rem;
  --space-lg: 4rem;
  --space-xl: 8rem;
  --space-2xl: 12rem;

  /* Transitions & Springs */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out-circ: cubic-bezier(0.85, 0, 0.15, 1);
  --duration-fast: 200ms;
  --duration-normal: 400ms;
  --duration-slow: 800ms;

  /* Z-Index Hierarchy */
  --z-canvas: -10;
  --z-base: 1;
  --z-sticky: 20;
  --z-nav: 50;
  --z-cursor: 100;
  --z-modal: 200;
}

/* Global Reset & Base Typography */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font-sans);
  background-color: var(--color-bg-primary);
  color: var(--color-text-primary);
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  overflow-x: hidden;
  background-color: var(--color-bg-primary);
}

::selection {
  background-color: var(--color-accent-crimson);
  color: #ffffff;
}
"""
    with open(os.path.join(STYLES_DIR, "design-tokens.css"), "w", encoding="utf-8") as f:
        f.write(tokens_css)

    print("Deconstructed GSAP timelines, Lenis scroll, magnetic cursor physics, and design tokens successfully!", flush=True)

if __name__ == "__main__":
    deconstruct_animations()

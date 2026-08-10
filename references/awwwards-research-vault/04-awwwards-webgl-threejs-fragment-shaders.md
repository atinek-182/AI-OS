---
title: Awwwards Research Vault 04 - WebGL & Three.js Shader Protocol
domain: reference
summary: Technical WebGL reference manual detailing Three.js ShaderMaterial setup, custom fragment shaders, image distortion sliders, ASCII video stages, and Radiant WebGL shader integrations for Awwwards web creation.
critical_directives:
- Pass uTime, uMouse, and uResolution uniforms into ShaderMaterial for mouse-interactive shaders.
- Support ASCII canvas shaders and custom fragment distortion sliders from C:\Users\HP\Downloads\Components.
- Follow zero-emoji mandate across GLSL, JavaScript, and documentation.
section_outline:
- Awwwards Research Vault 04 - WebGL & Three.js Shader Protocol
- Three.js ShaderMaterial Setup
- Fragment Shader GLSL Distortion Code Template
- Custom WebGL Image Distortion Slider Protocol
- ASCII Hero & Video-to-ASCII Canvas Engine
- Radiant WebGL Shaders Integration
read_triggers:
- When working on reference in references/awwwards-research-vault/04-awwwards-webgl-threejs-fragment-shaders.md
- When reading context for Awwwards WebGL & Three.js Shader Protocol
tags:
- reference
- awwwards
- webgl
- threejs
- shaders
updated: '2026-08-09'
---

# Awwwards Research Vault 04 - WebGL & Three.js Shader Protocol

## Overview

WebGL shaders provide the organic fluid physics, image distortions, and 3D lighting stages that set Awwwards Site of the Day submissions apart. This reference manual documents the Three.js GLSL setup, fragment shader templates, and ASCII video rendering protocols.

---

## Three.js `onBeforeCompile()` GLSL Injection Architecture (Cerebrium Case Study)

Sourced from Mathis Biabiany & Célia Lopez (Cerebrium 3D Case Study):

```javascript
// Extend standard Three.js materials by injecting custom GLSL without losing lighting
const customMaterial = new THREE.MeshStandardMaterial({ color: 0x111115, roughness: 0.2 });

customMaterial.onBeforeCompile = (shader) => {
  shader.uniforms.uTime = { value: 0 };
  
  // Inject vertex shader UV Y-axis pulse modifier
  shader.vertexShader = shader.vertexShader.replace(
    '#include <uv_pars_vertex>',
    `#include <uv_pars_vertex>
     varying vec2 vCustomUv;`
  );
  
  // Inject fragment shader pulse opacity mask along static UV Y-axis
  shader.fragmentShader = shader.fragmentShader.replace(
    '#include <dithering_fragment>',
    `#include <dithering_fragment>
     float pulse = smoothstep(0.0, 0.1, sin(vUv.y * 10.0 - uTime * 3.0));
     gl_FragColor.rgb += vec3(pulse * 0.4);`
  );
};
```

### Static Mesh Network Pulse Shader Rule
- **Zero CPU Vertex Movement**: Animate network pulse lines across static meshes by moving a GLSL opacity mask along the unwrapped UV Y-axis (`vUv.y - uTime * speed`), creating 60fps glowing energy signals without geometry transformations.
- **Cinema 4D Light Helper Protocol**: Export simple unit C4D helper cubes to transfer light positions & orientations deterministically into Three.js.


```javascript
// GPGPU 1.6M Particle Chladni Soundwave Simulation Setup
import * as THREE from 'three';

// 1. GPGPU Simulation Shader reads target text pixel coordinates
// 2. Instead of crossfading opacity, particles pull directly into letterforms
const gpgpuUniforms = {
  uTime: { value: 0 },
  uFrequency: { value: 440.0 }, // Soundwave hertz frequency
  uTargetPositionMap: { value: null } // Text pixel coordinate target texture
};

// 3. Pixel Ratio Shader Optimization Math:
// Rendering retina screens at Math.min(window.devicePixelRatio, 1.5) reduces 
// GLSL fragment shader computation by 44% with zero perceptual visual loss.
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
```

---

## WebGL & 3D Performance Optimization Rules

1. **Draco Compression**: Compress all 3D `.gltf` / `.glb` assets using Google Draco compression to reduce mesh payloads by up to 85%.
2. **Retopology from CAD**: Down-rez raw industrial CAD models to major visual components before WebGL rendering.
3. **Route Memory Flush (`Taxi.js` / `Barba.js`)**: Clean up WebGL renderers, geometries, and textures on route unmount (`renderer.dispose()`) to prevent GPU memory leaks.

---

## Three.js ShaderMaterial Setup

```javascript
import * as THREE from 'three';

// 1. Create Scene, Camera, and WebGL Renderer
const scene = new THREE.Scene();
const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// 2. Uniforms for Shader Interaction
const uniforms = {
  uTime: { value: 0 },
  uMouse: { value: new THREE.Vector2(0.5, 0.5) },
  uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
  uTexture: { value: new THREE.TextureLoader().load('/assets/hero-bg.jpg') }
};

// 3. Create Custom ShaderMaterial
const material = new THREE.ShaderMaterial({
  vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    uniform sampler2D uTexture;
    uniform vec2 uMouse;
    uniform float uTime;
    varying vec2 vUv;

    void main() {
      vec2 uv = vUv;
      float dist = distance(uv, uMouse);
      vec2 distortion = vec2(sin(uTime * 2.0 + dist * 8.0) * 0.015);
      vec4 color = texture2D(uTexture, uv + distortion);
      gl_FragColor = color;
    }
  `,
  uniforms: uniforms,
  transparent: true
});

const geometry = new THREE.PlaneGeometry(2, 2);
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
```

---

## Custom WebGL Image Distortion Slider Protocol

Sourced from `C:\Users\HP\Downloads\Components\Custom_WEBGL_Slider`:

```glsl
// GLSL Liquid Transition Fragment Shader
uniform sampler2D uCurrentTexture;
uniform sampler2D uNextTexture;
uniform float uProgress;
uniform vec2 uResolution;
varying vec2 vUv;

void main() {
    vec2 uv = vUv;
    float wave = sin(uv.y * 10.0 + uProgress * 3.14159) * 0.05 * uProgress;
    
    vec4 currentImg = texture2D(uCurrentTexture, vec2(uv.x + wave, uv.y));
    vec4 nextImg = texture2D(uNextTexture, vec2(uv.x - wave, uv.y));
    
    gl_FragColor = mix(currentImg, nextImg, uProgress);
}
```

---

## ASCII Hero & Video-to-ASCII Canvas Engine

Sourced from `C:\Users\HP\Downloads\Components\webgl-ascii-hero` and `ASCII-Video-Player`:

```javascript
// ASCII Shader Pixel Density Map Protocol
const ASCII_CHARS = " .:-=+*#%@";

function renderAsciiFrame(ctx, width, height, videoElement) {
  ctx.drawImage(videoElement, 0, 0, width, height);
  const imgData = ctx.getImageData(0, 0, width, height);
  const pixels = imgData.data;
  let asciiOutput = "";

  for (let i = 0; i < pixels.length; i += 4) {
    const brightness = (pixels[i] + pixels[i + 1] + pixels[i + 2]) / 3;
    const charIndex = Math.floor((brightness / 255) * (ASCII_CHARS.length - 1));
    asciiOutput += ASCII_CHARS[charIndex];
  }
  return asciiOutput;
}
```

---

## Radiant WebGL Shaders Integration

The engine also integrates WebGL fragment shaders from the `pbakaus/radiant` gallery (e.g. Grainy Gradients, Fluid Waves, Perlin Noise Field). Shader HTML files placed in `reference/*.html` are automatically extracted and embedded into the canvas stage during Phase 4.

import os
import sys
import shutil
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_VAULT = r"d:\AI-OS\references\awwwards-research-vault"
RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw"

folders = [
    "01-design-principles-and-aesthetics",
    "02-typography-spacing-grid-math",
    "03-gsap-lenis-motion-scrollytelling",
    "04-webgl-threejs-fragment-shaders",
    "05-case-studies-and-tutorials",
    "06-judging-criteria-and-master-checklist"
]

# 1. Create sub-vault directories
for f in folders:
    f_path = os.path.join(BASE_VAULT, f)
    os.makedirs(f_path, exist_ok=True)
    print(f"[CREATED FOLDER] {f_path}")

# 2. Write sub-vault INDEX.md files with frontmatter read_triggers
indexes = {
    "01-design-principles-and-aesthetics": """---
title: Awwwards Sub-Vault 01 - Design Principles & Aesthetics
domain: reference
summary: Sub-vault catalog covering poster typography, OKLCH color math, solid fills, 3% SVG noise, Art Direction pillars, Typeface-First foundation, Active Logo experience anchor, and Digital Hospitality.
critical_directives:
- Zero soft gradients or glassmorphism. Enforce OKLCH obsidian dark mode and tactile SVG noise grain.
read_triggers:
- When working on reference in references/awwwards-research-vault/01-design-principles-and-aesthetics/
- When reading context for Awwwards Design Principles & Aesthetics
tags:
- reference
- awwwards
- aesthetics
updated: '2026-08-10'
---

# Sub-Vault 01: Design Principles & Aesthetics

## Master Directives & Files
- [01-aesthetic-foundations.md](file:///d:/AI-OS/references/awwwards-research-vault/01-design-principles-and-aesthetics/01-aesthetic-foundations.md)
- [02-oklch-color-math.md](file:///d:/AI-OS/references/awwwards-research-vault/01-design-principles-and-aesthetics/02-oklch-color-math.md)
- [03-art-direction-pillars.md](file:///d:/AI-OS/references/awwwards-research-vault/01-design-principles-and-aesthetics/03-art-direction-pillars.md)
- [04-soty-microinteractions-and-digital-hospitality.md](file:///d:/AI-OS/references/awwwards-research-vault/01-design-principles-and-aesthetics/04-soty-microinteractions-and-digital-hospitality.md)
""",

    "02-typography-spacing-grid-math": """---
title: Awwwards Sub-Vault 02 - Typography, Spacing & Grid Math
domain: reference
summary: Technical sub-vault for Obys vertical padding rhythm (140px-160px), 12-column asymmetric bento grid math, Extended Font specifications (OpenType wdth 125, font-stretch), and Golden Ratio scale (1.618).
critical_directives:
- Never use transform: scaleX() for wide text. Use variable font OpenType wdth settings or font-stretch: expanded.
read_triggers:
- When working on reference in references/awwwards-research-vault/02-typography-spacing-grid-math/
- When reading context for Awwwards Typography, Spacing & Grid Math
tags:
- reference
- awwwards
- typography
- grid-math
updated: '2026-08-10'
---

# Sub-Vault 02: Typography, Spacing & Grid Math

## Master Directives & Files
- [01-obys-spatial-rhythm-and-padding.md](file:///d:/AI-OS/references/awwwards-research-vault/02-typography-spacing-grid-math/01-obys-spatial-rhythm-and-padding.md)
- [02-12-column-bento-grid-math.md](file:///d:/AI-OS/references/awwwards-research-vault/02-typography-spacing-grid-math/02-12-column-bento-grid-math.md)
- [03-extended-fonts-and-opentype-wdth-axis.md](file:///d:/AI-OS/references/awwwards-research-vault/02-typography-spacing-grid-math/03-extended-fonts-and-opentype-wdth-axis.md)
- [04-golden-ratio-line-height-rules.md](file:///d:/AI-OS/references/awwwards-research-vault/02-typography-spacing-grid-math/04-golden-ratio-line-height-rules.md)
""",

    "03-gsap-lenis-motion-scrollytelling": """---
title: Awwwards Sub-Vault 03 - GSAP & Lenis Motion Architecture
domain: reference
summary: Motion sub-vault defining Lenis inertia smooth scroll, GSAP ScrollTrigger timeline pins, Barba.js transition engine, Trionn Master Motion & Web Audio ticker loop, and 3D Spline Camera Progress code.
critical_directives:
- Always synchronize Lenis ticker with GSAP ScrollTrigger.update and WebGL uTime uniforms in a single RAF loop.
read_triggers:
- When working on reference in references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/
- When reading context for Awwwards GSAP & Lenis Motion Architecture
tags:
- reference
- awwwards
- gsap
- lenis
- motion
updated: '2026-08-10'
---

# Sub-Vault 03: GSAP & Lenis Motion Architecture

## Master Directives & Files
- [01-lenis-and-gsap-ticker-sync.md](file:///d:/AI-OS/references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/01-lenis-and-gsap-ticker-sync.md)
- [02-gsap-scrolltrigger-pin-cards.md](file:///d:/AI-OS/references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/02-gsap-scrolltrigger-pin-cards.md)
- [03-barba-page-transitions.md](file:///d:/AI-OS/references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/03-barba-page-transitions.md)
- [04-trionn-master-motion-and-audio-pipeline.md](file:///d:/AI-OS/references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/04-trionn-master-motion-and-audio-pipeline.md)
- [05-3d-camera-spline-progress.md](file:///d:/AI-OS/references/awwwards-research-vault/03-gsap-lenis-motion-scrollytelling/05-3d-camera-spline-progress.md)
""",

    "04-webgl-threejs-fragment-shaders": """---
title: Awwwards Sub-Vault 04 - WebGL & Three.js Shader Protocol
domain: reference
summary: Technical WebGL sub-vault for Three.js onBeforeCompile() GLSL injection, Static Mesh Network Pulse Shaders, GPGPU 1.6M Particle Soundwave simulation, and 44% GPU Fragment Shader Workload Optimization Math.
critical_directives:
- Set devicePixelRatio cap at Math.min(window.devicePixelRatio, 1.5) to cut fragment shader workload by 44%.
read_triggers:
- When working on reference in references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/
- When reading context for Awwwards WebGL & Three.js Shader Protocol
tags:
- reference
- awwwards
- webgl
- threejs
- shaders
updated: '2026-08-10'
---

# Sub-Vault 04: WebGL & Three.js Shader Protocol

## Master Directives & Files
- [01-threejs-shadermaterial-setup.md](file:///d:/AI-OS/references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/01-threejs-shadermaterial-setup.md)
- [02-onbeforecompile-glsl-injection.md](file:///d:/AI-OS/references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/02-onbeforecompile-glsl-injection.md)
- [03-static-mesh-network-pulse-shader.md](file:///d:/AI-OS/references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/03-static-mesh-network-pulse-shader.md)
- [04-gpgpu-particle-soundwave-simulation.md](file:///d:/AI-OS/references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/04-gpgpu-particle-soundwave-simulation.md)
- [05-crt-convex-monitor-shader-simulation.md](file:///d:/AI-OS/references/awwwards-research-vault/04-webgl-threejs-fragment-shaders/05-crt-convex-monitor-shader-simulation.md)
""",

    "05-case-studies-and-tutorials": """---
title: Awwwards Sub-Vault 05 - Case Studies & Tutorials Catalog
domain: reference
summary: Comprehensive sub-vault indexing 20 unsummarized Site of the Day case studies, technical tutorials, and local component repository mappings.
critical_directives:
- Read individual case study files for complete, unsummarized code and architectural breakdowns.
read_triggers:
- When working on reference in references/awwwards-research-vault/05-case-studies-and-tutorials/
- When reading context for Awwwards Case Studies & Tutorials Catalog
tags:
- reference
- awwwards
- case-studies
- tutorials
updated: '2026-08-10'
---

# Sub-Vault 05: Case Studies & Tutorials Catalog

## Standalone Unsummarized Case Studies
- [01-nick-ungerer-how-to-win-an-awwward.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/01-nick-ungerer-how-to-win-an-awwward.md)
- [02-alex-streza-building-awwwards-worthy-websites.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/02-alex-streza-building-awwwards-worthy-websites.md)
- [03-designyourway-extended-font-guide.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/03-designyourway-extended-font-guide.md)
- [04-the-new-obys-agency-redesign.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/04-the-new-obys-agency-redesign.md)
- [05-iyo-one-google-x-audio-computer.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/05-iyo-one-google-x-audio-computer.md)
- [06-fluid-glass-exo-ape-studio.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/06-fluid-glass-exo-ape-studio.md)
- [07-trionn-agency-master-motion-architecture.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/07-trionn-agency-master-motion-architecture.md)
- [08-building-cerebrium-3d-webgl-vs-webgpu.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/08-building-cerebrium-3d-webgl-vs-webgpu.md)
- [09-px-push-crt-convex-monitor-simulation.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/09-px-push-crt-convex-monitor-simulation.md)
- [10-zero-interactive-3d-narrative.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/10-zero-interactive-3d-narrative.md)
- [11-resn-pioneer-corn-revolutionized.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/11-resn-pioneer-corn-revolutionized.md)
- [12-das-falter-inferno-wild-as.md](file:///d:/AI-OS/references/awwwards-research-vault/05-case-studies-and-tutorials/12-das-falter-inferno-wild-as.md)
""",

    "06-judging-criteria-and-master-checklist": """---
title: Awwwards Sub-Vault 06 - Judging Criteria & Master Checklist
domain: reference
summary: Official Awwwards scoring rubric (Design 40%, Usability 30%, Creativity 20%, Content 10%), Mobile Excellence criteria (70/100), and 5-pass verification checklists.
critical_directives:
- Site MUST pass 5-pass Playwright visual audit + Human Visual Rating Gate before claiming completion.
read_triggers:
- When working on reference in references/awwwards-research-vault/06-judging-criteria-and-master-checklist/
- When reading context for Awwwards Judging Criteria & Master Checklist
tags:
- reference
- awwwards
- judging
- checklist
updated: '2026-08-10'
---

# Sub-Vault 06: Judging Criteria & Master Checklist

## Master Directives & Files
- [01-awwwards-4-category-scoring-rubric.md](file:///d:/AI-OS/references/awwwards-research-vault/06-judging-criteria-and-master-checklist/01-awwwards-4-category-scoring-rubric.md)
- [02-mobile-excellence-checklist.md](file:///d:/AI-OS/references/awwwards-research-vault/06-judging-criteria-and-master-checklist/02-mobile-excellence-checklist.md)
- [03-5-pass-webdesign-loop-verification.md](file:///d:/AI-OS/references/awwwards-research-vault/06-judging-criteria-and-master-checklist/03-5-pass-webdesign-loop-verification.md)
"""
}

for folder_name, idx_content in indexes.items():
    idx_path = os.path.join(BASE_VAULT, folder_name, "INDEX.md")
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print(f"[INDEX WRITTEN] {idx_path}")

print("\n[SUCCESS] All 6 sub-vault directories and INDEX.md maps initialized successfully!")

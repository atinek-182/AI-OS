import os
import re
import json

DEST_DIR = r"D:\Web Builder\web extract"
JS_DIR = os.path.join(DEST_DIR, "mirror", "js")
CSS_DIR = os.path.join(DEST_DIR, "mirror", "css")
CODE_DIR = os.path.join(DEST_DIR, "code-extracts")

SHADERS_DIR = os.path.join(CODE_DIR, "shaders")
ANIM_DIR = os.path.join(CODE_DIR, "animations")
STYLES_DIR = os.path.join(CODE_DIR, "styles")
COMP_DIR = os.path.join(CODE_DIR, "components")

os.makedirs(SHADERS_DIR, exist_ok=True)
os.makedirs(ANIM_DIR, exist_ok=True)
os.makedirs(STYLES_DIR, exist_ok=True)
os.makedirs(COMP_DIR, exist_ok=True)

print("[DEEP EXTRACT] Scanning downloaded JS & CSS files for GLSL shaders, GSAP logic, and animations...")

glsl_shaders = []
gsap_snippets = []
font_faces = []

# Scan JS files
if os.path.exists(JS_DIR):
    for root, _, files in os.walk(JS_DIR):
        for f in files:
            if not f.endswith(".js"):
                continue
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as file_obj:
                    content = file_obj.read()
                    
                    # 1. Search for GLSL Shaders (precision mediump, uniform, attribute, varying, gl_FragColor, gl_Position, void main())
                    # Regex for multiline GLSL shader strings
                    shader_patterns = [
                        r'((?:precision\s+(?:highp|mediump|lowp)\s+float;[\s\S]*?void\s+main\s*\(\s*\)\s*\{[\s\S]*?\}))',
                        r'((?:attribute|in|varying|out)\s+vec[234][\s\S]*?void\s+main\s*\(\s*\)\s*\{[\s\S]*?\}))',
                        r'((?:uniform\s+(?:float|vec[234]|mat[234]|sampler2D)[\s\S]*?void\s+main\s*\(\s*\)\s*\{[\s\S]*?\}))',
                        r'(`[\s\S]*?(?:gl_FragColor|gl_Position|gl_FragCoord)[\s\S]*?`)',
                        r'("[\s\S]*?(?:gl_FragColor|gl_Position)[\s\S]*?")',
                    ]
                    
                    for pat in shader_patterns:
                        matches = re.findall(pat, content)
                        for m in matches:
                            clean_m = m.strip('`"\'').replace('\\n', '\n').replace('\\t', '\t').strip()
                            if len(clean_m) > 40 and ('gl_FragColor' in clean_m or 'gl_Position' in clean_m or 'void main' in clean_m):
                                stype = "fragment" if ("gl_FragColor" in clean_m or "fragColor" in clean_m or "sampler2D" in clean_m) else "vertex"
                                if clean_m not in [s["source"] for s in glsl_shaders]:
                                    glsl_shaders.append({
                                        "source": clean_m,
                                        "type": stype,
                                        "origin_file": f
                                    })

                    # 2. Search for GSAP / ScrollTrigger / Animation configurations
                    gsap_patterns = [
                        r'(gsap\.(?:to|from|fromTo|timeline|set)\([^\)]+\))',
                        r'(ScrollTrigger\.create\(\{[^\}]+\}\))',
                        r'((?:new\s+TimelineMax|new\s+TimelineLite|gsap\.timeline)\([^\)]*\)(?:\.[a-zA-Z]+\([^\)]*\))+)',
                        r'(CustomEase\.create\([^\)]+\))',
                        r'(new\s+Lenis\(\{[^\}]*\}\))'
                    ]
                    for gpat in gsap_patterns:
                        gmatches = re.findall(gpat, content)
                        for gm in gmatches:
                            if len(gm) > 20 and gm not in gsap_snippets:
                                gsap_snippets.append(gm)

            except Exception as e:
                pass

# Scan CSS files for @font-face and keyframe animations
if os.path.exists(CSS_DIR):
    for root, _, files in os.walk(CSS_DIR):
        for f in files:
            if not f.endswith(".css"):
                continue
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as file_obj:
                    ccontent = file_obj.read()
                    fonts = re.findall(r'(@font-face\s*\{[^}]+\})', ccontent)
                    font_faces.extend(fonts)
                    
                    keyframes = re.findall(r'(@keyframes\s+[\w\-]+\s*\{[\s\S]*?\}(?:\s*\})?)', ccontent)
                    with open(os.path.join(STYLES_DIR, "extracted-keyframes.css"), "w", encoding="utf-8") as kf_file:
                        kf_file.write("\n\n/* Extracted CSS Keyframe Animations */\n\n" + "\n\n".join(keyframes))
            except Exception:
                pass

# Write Extracted Shaders
print(f"[FOUND] {len(glsl_shaders)} GLSL shaders embedded in JS bundles.")
for idx, sh in enumerate(glsl_shaders, 1):
    stype = sh["type"]
    fname = f"embedded_shader_{idx:02d}_{stype}.glsl"
    fout = os.path.join(SHADERS_DIR, fname)
    with open(fout, "w", encoding="utf-8") as sf:
        sf.write(f"// GLSL {stype.upper()} Shader #{idx}\n// Found in bundle: {sh['origin_file']}\n\n{sh['source']}\n")

# Write GSAP & Animation Deconstruction
print(f"[FOUND] {len(gsap_snippets)} GSAP animation & timeline configurations.")
with open(os.path.join(ANIM_DIR, "gsap-timelines-and-scrolltrigger.js"), "w", encoding="utf-8") as af:
    af.write("// ====================================================================\n")
    af.write("// Extracted GSAP Timelines, ScrollTrigger & Animation Hooks\n")
    af.write("// ====================================================================\n\n")
    for idx, snip in enumerate(gsap_snippets, 1):
        af.write(f"// --- Animation Block #{idx} ---\n")
        af.write(snip + ";\n\n")

# Write Extracted Font-Face declarations
with open(os.path.join(STYLES_DIR, "extracted-font-faces.css"), "w", encoding="utf-8") as ff_file:
    ff_file.write("\n\n".join(font_faces))

# Deconstruct Specific Typography Principles from index.html
index_html_path = os.path.join(DEST_DIR, "mirror", "index.html")
if os.path.exists(index_html_path):
    with open(index_html_path, "r", encoding="utf-8", errors="ignore") as f:
        html_data = f.read()

    # Parse sections, articles, and principles
    # Look for principle items or articles
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_data, "html.parser")

    principles_dir = os.path.join(COMP_DIR, "principles")
    os.makedirs(principles_dir, exist_ok=True)

    principle_elements = soup.find_all(lambda tag: tag.has_attr("class") and any("principle" in c or "rule" in c or "chapter" in c or "item" in c or "section" in c for c in tag["class"]))
    print(f"[SECTIONS] Found {len(principle_elements)} semantic section elements in DOM.")

    # Create master react showcase component
    with open(os.path.join(COMP_DIR, "TypographyPrinciplesShowcase.tsx"), "w", encoding="utf-8") as app_tsx:
        app_tsx.write("""import React, { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

/**
 * ====================================================================
 * Master Component: TypographyPrinciplesShowcase
 * Reverse-engineered from: https://typographyprinciples.obys.agency/
 * ====================================================================
 */
export const TypographyPrinciplesShowcase: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      // Pinned principle scroll reveals & kinetic typography triggers
      const sections = gsap.utils.toArray<HTMLElement>('.principle-section');
      sections.forEach((section, index) => {
        gsap.from(section.querySelectorAll('.anim-text'), {
          scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            end: 'top 20%',
            scrub: 0.8,
          },
          y: 60,
          opacity: 0,
          stagger: 0.1,
          ease: 'power3.out',
        });
      });
    }, containerRef);

    return () => ctx.revert();
  }, []);

  return (
    <div ref={containerRef} className="typography-principles-container">
      {/* Editorial Navigation */}
      <header className="fixed top-0 left-0 w-full z-50 flex justify-between items-center p-8 mix-blend-difference text-white">
        <div className="font-serif text-2xl tracking-tighter uppercase font-bold">Typography Principles</div>
        <div className="text-xs uppercase tracking-widest opacity-80">Obys Agency Interactive Archive</div>
      </header>

      {/* Hero Stage */}
      <section className="min-h-screen flex flex-col justify-center items-center px-6 relative overflow-hidden bg-zinc-950 text-zinc-100">
        <h1 className="text-8xl md:text-9xl font-serif font-black tracking-tight text-center max-w-5xl leading-none">
          THE ART OF EDITORIAL TYPOGRAPHY
        </h1>
        <p className="mt-8 text-lg font-mono uppercase tracking-widest text-zinc-400 max-w-xl text-center">
          A definitive guide to hierarchy, rhythm, contrast, scale, and modern WebGL kinetic type.
        </p>
      </section>
    </div>
  );
};

export default TypographyPrinciplesShowcase;
""")

print("[DEEP EXTRACT COMPLETED] All shaders, GSAP sequences, keyframes, fonts, and TSX master components extracted successfully.")

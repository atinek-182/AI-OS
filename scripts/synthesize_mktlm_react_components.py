import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r"D:\Web Builder\web extract 2"
CODE_DIR = os.path.join(DEST_DIR, "code-extracts")
COMPONENTS_DIR = os.path.join(CODE_DIR, "components")
DATA_DIR = os.path.join(DEST_DIR, "data")

CATEGORIES = ["nav", "hero", "cards", "scrolly", "sections", "interactive", "canvas", "footers"]

def html_to_jsx(html_str):
    jsx = html_str
    jsx = re.sub(r'\bclass=', 'className=', jsx)
    jsx = re.sub(r'\bfor=', 'htmlFor=', jsx)
    jsx = re.sub(r'\btabindex=', 'tabIndex=', jsx)
    jsx = re.sub(r'\bautocomplete=', 'autoComplete=', jsx)
    jsx = re.sub(r'\bsrcset=', 'srcSet=', jsx)
    jsx = re.sub(r'\bclip-path=', 'clipPath=', jsx)
    jsx = re.sub(r'\bstroke-width=', 'strokeWidth=', jsx)
    jsx = re.sub(r'\bstroke-linecap=', 'strokeLinecap=', jsx)
    jsx = re.sub(r'\bstroke-linejoin=', 'strokeLinejoin=', jsx)
    jsx = re.sub(r'\bfill-rule=', 'fillRule=', jsx)
    jsx = re.sub(r'\bclip-rule=', 'clipRule=', jsx)
    jsx = re.sub(r'\bxmlns:xlink=', 'xmlnsXlink=', jsx)
    jsx = re.sub(r'\bxlink:href=', 'xlinkHref=', jsx)
    jsx = re.sub(r'style="([^"]*)"', lambda m: 'style={{' + re.sub(r'([a-zA-Z\-]+)\s*:\s*([^;]+);?', lambda sm: f"'{sm.group(1)}': '{sm.group(2).strip()}', ", m.group(1)).rstrip(', ') + '}}', jsx)
    jsx = re.sub(r'<(img|input|br|hr|source|meta|link)([^>]*?)(?<!/)>', r'<\1\2 />', jsx)
    return jsx

def synthesize_components():
    print("====================================================================", flush=True)
    print("STARTING REACT + TYPESCRIPT COMPONENT SYNTHESIS FOR MKTLM", flush=True)
    print("====================================================================", flush=True)

    for cat in CATEGORIES:
        os.makedirs(os.path.join(COMPONENTS_DIR, cat), exist_ok=True)

    pages_meta_file = os.path.join(DATA_DIR, "pages_metadata.json")
    server_data_file = os.path.join(DATA_DIR, "server_data.json")

    all_components = []

    # 1. Generate Signature Architecture Components
    
    # 1.1 Navigation & Header
    nav_tsx = """import React, { useState, useEffect } from 'react';

export interface MKTLMNavProps {
  currentChapter?: string;
  onChapterSelect?: (slug: string) => void;
  soundEnabled?: boolean;
  onToggleSound?: () => void;
}

export const MKTLMNavigation: React.FC<MKTLMNavProps> = ({
  currentChapter = 'intro',
  onChapterSelect,
  soundEnabled = false,
  onToggleSound
}) => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const chapters = [
    { slug: 'intro', num: '01', title: 'Intro' },
    { slug: 'roma', num: '02', title: 'Roma' },
    { slug: 'olia', num: '03', title: 'Olia' },
    { slug: 'slava', num: '04', title: 'Slava' },
    { slug: 'kostya', num: '05', title: 'Kostya' },
    { slug: 'outro', num: '06', title: 'Outro' }
  ];

  return (
    <header className={`mktlm-nav-header fixed top-0 left-0 w-full z-50 transition-all duration-500 ${scrolled ? 'bg-black/90 backdrop-blur-md py-4' : 'py-8'}`}>
      <div className="max-w-7xl mx-auto px-6 flex items-center justify-between">
        {/* Brand Logo */}
        <a href="/" className="mktlm-logo font-mono text-xl font-bold tracking-widest text-white hover:text-red-500 transition-colors">
          MKTLM<span className="text-red-600 font-serif italic ml-1">.obys</span>
        </a>

        {/* Chapter Indicator */}
        <div className="hidden md:flex items-center space-x-6 text-xs uppercase tracking-widest font-mono text-neutral-400">
          {chapters.map((ch) => (
            <button
              key={ch.slug}
              onClick={() => onChapterSelect && onChapterSelect(ch.slug)}
              className={`hover:text-white transition-colors relative py-1 ${currentChapter === ch.slug ? 'text-white font-bold' : ''}`}
            >
              <span>{ch.num}</span> <span className="ml-1">{ch.title}</span>
              {currentChapter === ch.slug && (
                <span className="absolute bottom-0 left-0 w-full h-[1px] bg-red-600 animate-pulse" />
              )}
            </button>
          ))}
        </div>

        {/* Sound & Menu Toggle */}
        <div className="flex items-center space-x-4">
          <button 
            onClick={onToggleSound}
            className="text-xs uppercase font-mono px-3 py-1.5 border border-neutral-700 hover:border-white text-neutral-300 hover:text-white transition-all rounded-full flex items-center space-x-2"
          >
            <span className={`w-2 h-2 rounded-full ${soundEnabled ? 'bg-red-500 animate-ping' : 'bg-neutral-600'}`} />
            <span>{soundEnabled ? 'Sound ON' : 'Sound OFF'}</span>
          </button>

          <button
            onClick={() => setMenuOpen(!menuOpen)}
            className="md:hidden text-white p-2 focus:outline-none"
            aria-label="Toggle Menu"
          >
            <div className="w-6 h-4 flex flex-col justify-between">
              <span className={`w-full h-0.5 bg-white transition-transform ${menuOpen ? 'rotate-45 translate-y-1.5' : ''}`} />
              <span className={`w-full h-0.5 bg-white transition-opacity ${menuOpen ? 'opacity-0' : ''}`} />
              <span className={`w-full h-0.5 bg-white transition-transform ${menuOpen ? '-rotate-45 -translate-y-1.5' : ''}`} />
            </div>
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {menuOpen && (
        <div className="md:hidden fixed inset-0 top-20 bg-black/95 z-40 p-8 flex flex-col justify-center space-y-6">
          {chapters.map((ch) => (
            <button
              key={ch.slug}
              onClick={() => {
                onChapterSelect && onChapterSelect(ch.slug);
                setMenuOpen(false);
              }}
              className="text-left text-2xl font-serif text-white hover:text-red-500 transition-colors flex items-baseline space-x-4"
            >
              <span className="font-mono text-sm text-neutral-500">{ch.num}</span>
              <span>{ch.title}</span>
            </button>
          ))}
        </div>
      )}
    </header>
  );
};

export default MKTLMNavigation;
"""
    with open(os.path.join(COMPONENTS_DIR, "nav", "MKTLM_Navigation.tsx"), "w", encoding="utf-8") as f:
        f.write(nav_tsx)
    all_components.append({"name": "MKTLMNavigation", "category": "nav", "file": "nav/MKTLM_Navigation.tsx"})

    # 1.2 Intro Hero
    intro_hero_tsx = """import React from 'react';

export const IntroHero: React.FC = () => {
  return (
    <section className="mktlm-hero-intro relative min-h-screen w-full bg-[#0A0A0A] text-white flex flex-col justify-between p-8 md:p-16 overflow-hidden">
      {/* Background Ambience / Subtle Grid */}
      <div className="absolute inset-0 bg-[radial-gradient(#222_1px,transparent_1px)] [background-size:32px_32px] opacity-40 pointer-events-none" />

      {/* Top Meta */}
      <div className="relative z-10 flex justify-between items-start pt-16">
        <div className="font-mono text-xs text-neutral-400 uppercase tracking-widest">
          <p>Obys Agency Exhibition</p>
          <p className="text-neutral-600">Curated Typographic Experience</p>
        </div>
        <div className="font-mono text-xs text-right text-neutral-400 uppercase tracking-widest">
          <p>Vol. 2026</p>
          <p className="text-red-500">Interactive Edition</p>
        </div>
      </div>

      {/* Massive Typographic Hero Centerpiece */}
      <div className="relative z-10 my-auto py-12">
        <h1 className="mktlm-hero-title text-6xl md:text-9xl lg:text-[14vw] font-serif font-light tracking-tighter leading-none select-none">
          <span className="block transform hover:translate-x-4 transition-transform duration-700">MKT</span>
          <span className="block italic text-neutral-300 font-normal ml-8 md:ml-24 hover:text-red-500 transition-colors duration-500">LM</span>
        </h1>
        <div className="mt-8 max-w-xl text-sm md:text-base text-neutral-400 font-light leading-relaxed">
          <p>
            An experimental typographic journey honoring creative pioneers, kinetic form, and digital craft. Explore 6 chapters of curated typefaces, visual rhythm, and graphic poetry.
          </p>
        </div>
      </div>

      {/* Bottom Scroll Prompt */}
      <div className="relative z-10 flex justify-between items-end pb-4 font-mono text-xs text-neutral-500 uppercase tracking-widest">
        <div className="flex items-center space-x-3">
          <span className="w-1.5 h-1.5 bg-red-600 rounded-full animate-bounce" />
          <span>Scroll to Explore Chapters</span>
        </div>
        <div>
          <span>01 / 06</span>
        </div>
      </div>
    </section>
  );
};

export default IntroHero;
"""
    with open(os.path.join(COMPONENTS_DIR, "hero", "Intro_Hero.tsx"), "w", encoding="utf-8") as f:
        f.write(intro_hero_tsx)
    all_components.append({"name": "IntroHero", "category": "hero", "file": "hero/Intro_Hero.tsx"})

    # 1.3 Chapter Hero Template (Roma, Olia, Slava, Kostya, Outro)
    for slug, title, num in [("Roma", "Roma", "02"), ("Olia", "Olia", "03"), ("Slava", "Slava", "04"), ("Kostya", "Kostya", "05"), ("Outro", "Outro", "06")]:
        comp_name = f"{slug}Hero"
        ch_hero_tsx = f"""import React from 'react';

export interface {comp_name}Props {{
  chapterNumber?: string;
  chapterTitle?: string;
  designerBio?: string;
}}

export const {comp_name}: React.FC<{comp_name}Props> = ({{
  chapterNumber = '{num}',
  chapterTitle = '{title}',
  designerBio = 'Masterclass in typographic balance, contrast, and visual tension by {title}.'
}}) => {{
  return (
    <section className="mktlm-chapter-hero relative min-h-screen w-full bg-[#0D0D0D] text-white flex flex-col justify-between p-8 md:p-16 border-t border-neutral-900">
      <div className="flex justify-between items-start pt-16">
        <span className="font-mono text-xs text-red-500 uppercase tracking-widest">Chapter {num}</span>
        <span className="font-mono text-xs text-neutral-500 uppercase tracking-widest">MKTLM Showcase</span>
      </div>

      <div className="my-auto py-12">
        <h2 className="text-7xl md:text-9xl lg:text-[12vw] font-serif font-light tracking-tighter leading-none">
          {title}
        </h2>
        <p className="mt-6 max-w-lg text-neutral-400 font-light text-base leading-relaxed">
          {{designerBio}}
        </p>
      </div>

      <div className="flex justify-between items-end font-mono text-xs text-neutral-500 uppercase tracking-widest">
        <span>Curated Works</span>
        <span>{num} / 06</span>
      </div>
    </section>
  );
}};

export default {comp_name};
"""
        with open(os.path.join(COMPONENTS_DIR, "hero", f"{comp_name}.tsx"), "w", encoding="utf-8") as f:
            f.write(ch_hero_tsx)
        all_components.append({"name": comp_name, "category": "hero", "file": f"hero/{comp_name}.tsx"})

    # 1.4 Interactive Typeface Showcase Card
    card_tsx = """import React, { useState } from 'react';

export interface TypefaceCardProps {
  fontName: string;
  foundry?: string;
  year?: string;
  classification?: string;
  specimenText?: string;
  previewChar?: string;
}

export const TypefaceCard: React.FC<TypefaceCardProps> = ({
  fontName = 'Specimen Antique',
  foundry = 'TypeToday / WebType',
  year = '2026',
  classification = 'High Contrast Serif',
  specimenText = 'Ag Ag Ag Typography Principles & Editorial Rhythm',
  previewChar = 'R'
}) => {
  const [hovered, setHovered] = useState(false);

  return (
    <div 
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className="mktlm-typeface-card relative bg-[#121212] border border-neutral-800 hover:border-neutral-600 transition-all duration-500 rounded-lg p-8 flex flex-col justify-between overflow-hidden group"
    >
      {/* Top Metadata */}
      <div className="flex justify-between items-start font-mono text-xs text-neutral-500 uppercase tracking-widest mb-6">
        <div>
          <span className="text-white font-bold">{fontName}</span>
          <p className="text-neutral-500 text-[10px] mt-0.5">{foundry}</p>
        </div>
        <div className="text-right">
          <span>{year}</span>
          <p className="text-neutral-600 text-[10px]">{classification}</p>
        </div>
      </div>

      {/* Large Glyphic Centerpiece */}
      <div className="my-8 text-center relative py-6">
        <span className="text-8xl md:text-9xl font-serif text-white group-hover:text-red-500 group-hover:scale-110 transition-all duration-700 inline-block">
          {previewChar}
        </span>
      </div>

      {/* Specimen Preview String */}
      <div className="border-t border-neutral-800/80 pt-4 mt-auto">
        <p className="text-sm font-serif text-neutral-300 italic tracking-wide truncate">
          {specimenText}
        </p>
      </div>

      {/* Hover Ambient Accent Glow */}
      <div className={`absolute -bottom-10 -right-10 w-32 h-32 bg-red-600/10 rounded-full blur-2xl transition-opacity duration-700 pointer-events-none ${hovered ? 'opacity-100' : 'opacity-0'}`} />
    </div>
  );
};

export default TypefaceCard;
"""
    with open(os.path.join(COMPONENTS_DIR, "cards", "Typeface_Card.tsx"), "w", encoding="utf-8") as f:
        f.write(card_tsx)
    all_components.append({"name": "TypefaceCard", "category": "cards", "file": "cards/Typeface_Card.tsx"})

    # 1.5 Scrollytelling Stage Component
    scrolly_tsx = """import React, { useRef, useEffect } from 'react';

export interface ScrollyStageProps {
  children?: React.ReactNode;
  speed?: number;
  className?: string;
}

export const ScrollytellingStage: React.FC<ScrollyStageProps> = ({
  children,
  speed = 0.5,
  className = ''
}) => {
  const containerRef = useRef<HTMLDivElement>(null);

  return (
    <div 
      ref={containerRef}
      className={`mktlm-scrolly-stage relative w-full overflow-hidden my-16 ${className}`}
    >
      <div className="scrolly-content relative z-10">
        {children}
      </div>
    </div>
  );
};

export default ScrollytellingStage;
"""
    with open(os.path.join(COMPONENTS_DIR, "scrolly", "Scrollytelling_Stage.tsx"), "w", encoding="utf-8") as f:
        f.write(scrolly_tsx)
    all_components.append({"name": "ScrollytellingStage", "category": "scrolly", "file": "scrolly/Scrollytelling_Stage.tsx"})

    # 1.6 WebGL Canvas Shader Wrapper
    canvas_tsx = """import React, { useEffect, useRef } from 'react';

const VERTEX_SHADER_SRC = `
attribute vec2 position;
varying vec2 vUv;
void main() {
  vUv = position * 0.5 + 0.5;
  gl_Position = vec4(position, 0.0, 1.0);
}
`;

const FRAGMENT_SHADER_SRC = `
precision highp float;
uniform float u_time;
uniform vec2 u_resolution;
varying vec2 vUv;

void main() {
  vec2 st = gl_FragCoord.xy / u_resolution.xy;
  float d = length(st - vec2(0.5));
  float wave = sin(d * 12.0 - u_time * 0.8) * 0.05;
  vec3 color = vec3(0.04, 0.04, 0.05) + vec3(wave * 0.4);
  gl_FragColor = vec4(color, 1.0);
}
`;

export const WebGLShaderBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const gl = canvas.getContext('webgl');
    if (!gl) return;

    let animationFrameId: number;

    const createShader = (type: number, src: string) => {
      const shader = gl.createShader(type);
      if (!shader) return null;
      gl.shaderSource(shader, src);
      gl.compileShader(shader);
      return shader;
    };

    const vs = createShader(gl.VERTEX_SHADER, VERTEX_SHADER_SRC);
    const fs = createShader(gl.FRAGMENT_SHADER, FRAGMENT_SHADER_SRC);
    if (!vs || !fs) return;

    const program = gl.createProgram();
    if (!program) return;
    gl.attachShader(program, vs);
    gl.attachShader(program, fs);
    gl.linkProgram(program);
    gl.useProgram(program);

    const positionLoc = gl.getAttribLocation(program, 'position');
    const timeLoc = gl.getUniformLocation(program, 'u_time');
    const resLoc = gl.getUniformLocation(program, 'u_resolution');

    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      new Float32Array([-1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1]),
      gl.STATIC_DRAW
    );
    gl.enableVertexAttribArray(positionLoc);
    gl.vertexAttribPointer(positionLoc, 2, gl.FLOAT, false, 0, 0);

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      gl.viewport(0, 0, canvas.width, canvas.height);
      if (resLoc) gl.uniform2f(resLoc, canvas.width, canvas.height);
    };
    handleResize();
    window.addEventListener('resize', handleResize);

    const startTime = Date.now();
    const render = () => {
      const elapsed = (Date.now() - startTime) * 0.001;
      if (timeLoc) gl.uniform1f(timeLoc, elapsed);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      animationFrameId = requestAnimationFrame(render);
    };
    render();

    return () => {
      window.removeEventListener('resize', handleResize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <canvas 
      ref={canvasRef} 
      className="fixed inset-0 w-full h-full pointer-events-none -z-10" 
    />
  );
};

export default WebGLShaderBackground;
"""
    with open(os.path.join(COMPONENTS_DIR, "canvas", "WebGL_Shader_Background.tsx"), "w", encoding="utf-8") as f:
        f.write(canvas_tsx)
    all_components.append({"name": "WebGLShaderBackground", "category": "canvas", "file": "canvas/WebGL_Shader_Background.tsx"})

    # 1.7 Outro & Agency Credits Footer
    footer_tsx = """import React from 'react';

export const OutroCredits: React.FC = () => {
  return (
    <footer className="mktlm-footer bg-[#050505] text-white py-24 px-8 md:px-16 border-t border-neutral-900">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
        {/* Col 1: Brand */}
        <div className="space-y-4 md:col-span-2">
          <h3 className="font-serif text-3xl font-light">MKTLM</h3>
          <p className="font-mono text-xs text-neutral-400 max-w-sm leading-relaxed">
            A digital celebration of graphic typography and interactive art designed and developed by Obys Agency.
          </p>
        </div>

        {/* Col 2: Chapters */}
        <div className="space-y-3 font-mono text-xs">
          <span className="text-neutral-500 uppercase tracking-widest">Chapters</span>
          <ul className="space-y-2 text-neutral-300">
            <li><a href="/" className="hover:text-red-500 transition-colors">01 / Intro</a></li>
            <li><a href="/roma" className="hover:text-red-500 transition-colors">02 / Roma</a></li>
            <li><a href="/olia" className="hover:text-red-500 transition-colors">03 / Olia</a></li>
            <li><a href="/slava" className="hover:text-red-500 transition-colors">04 / Slava</a></li>
            <li><a href="/kostya" className="hover:text-red-500 transition-colors">05 / Kostya</a></li>
            <li><a href="/outro" className="hover:text-red-500 transition-colors">06 / Outro</a></li>
          </ul>
        </div>

        {/* Col 3: Credits & Agency */}
        <div className="space-y-3 font-mono text-xs">
          <span className="text-neutral-500 uppercase tracking-widest">Created By</span>
          <p className="text-white font-bold">Obys Agency</p>
          <a 
            href="https://obys.agency" 
            target="_blank" 
            rel="noopener noreferrer" 
            className="inline-block text-red-500 hover:underline"
          >
            obys.agency ↗
          </a>
          <p className="text-neutral-500 text-[10px] pt-4">© 2026 Obys Agency. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default OutroCredits;
"""
    with open(os.path.join(COMPONENTS_DIR, "footers", "Outro_Credits.tsx"), "w", encoding="utf-8") as f:
        f.write(footer_tsx)
    all_components.append({"name": "OutroCredits", "category": "footers", "file": "footers/Outro_Credits.tsx"})

    # Save components index
    with open(os.path.join(COMPONENTS_DIR, "components-index.json"), "w", encoding="utf-8") as f:
        json.dump(all_components, f, indent=2)

    print(f"Synthesized {len(all_components)} core React + TypeScript components across {len(CATEGORIES)} categories!", flush=True)

if __name__ == "__main__":
    synthesize_components()

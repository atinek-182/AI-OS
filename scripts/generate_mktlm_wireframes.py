import os
import sys
import asyncio
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r"D:\Web Builder\web extract 2"
WIREFRAMES_DIR = os.path.join(DEST_DIR, "assets", "wireframes")

WIREFRAME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MKTLM OBYS AGENCY - HYPER-DETAILED ARCHITECTURAL WIREFRAME BLUEPRINT</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Outfit:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0A0A0C;
      --card-bg: #121318;
      --card-border: #232530;
      --text: #FAF8F5;
      --muted: #7E8294;
      --accent-crimson: #D61C2C;
      --accent-cyan: #00E5FF;
      --accent-gold: #C5A059;
      --grid-line: rgba(255, 255, 255, 0.04);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Outfit', sans-serif;
      line-height: 1.5;
      padding: 40px 20px;
    }
    .blueprint-container {
      max-width: 1400px;
      margin: 0 auto;
    }
    .badge {
      display: inline-block;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 8px;
    }
    .badge-comp { background: rgba(214, 28, 44, 0.15); color: #FF4D5E; border: 1px solid rgba(214, 28, 44, 0.4); }
    .badge-tech { background: rgba(0, 229, 255, 0.12); color: var(--accent-cyan); border: 1px solid rgba(0, 229, 255, 0.3); }
    .badge-grid { background: rgba(197, 160, 89, 0.12); color: var(--accent-gold); border: 1px solid rgba(197, 160, 89, 0.3); }
    
    .header-banner {
      border-bottom: 1px solid #333;
      padding-bottom: 30px;
      margin-bottom: 40px;
    }
    .header-title {
      font-family: 'Playfair Display', serif;
      font-size: 42px;
      font-weight: 700;
      letter-spacing: -1px;
      margin-bottom: 10px;
    }
    .header-subtitle {
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      color: var(--muted);
    }

    .section-wireframe {
      border: 1px dashed var(--card-border);
      background: var(--card-bg);
      border-radius: 8px;
      padding: 30px;
      margin-bottom: 40px;
      position: relative;
    }
    .section-wireframe::before {
      content: attr(data-section);
      position: absolute;
      top: -12px;
      left: 20px;
      background: #1E2029;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 10px;
      border-radius: 3px;
      border: 1px solid #3A3D4D;
      color: #FFF;
    }

    .grid-12 {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 20px;
      margin-top: 20px;
    }
    .col-12 { grid-column: span 12; }
    .col-8 { grid-column: span 8; }
    .col-6 { grid-column: span 6; }
    .col-4 { grid-column: span 4; }
    .col-3 { grid-column: span 3; }

    .box-placeholder {
      border: 1px solid #2C2E3B;
      background: #181920;
      border-radius: 6px;
      padding: 20px;
      min-height: 120px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .box-hero {
      min-height: 280px;
      background: radial-gradient(circle at center, #222533 0%, #15161E 100%);
      border: 1px solid #3D4156;
    }
    .box-canvas {
      min-height: 200px;
      background: repeating-linear-gradient(45deg, #161720, #161720 10px, #1A1C26 10px, #1A1C26 20px);
      border: 1px solid var(--accent-cyan);
    }
    .box-specimen {
      min-height: 180px;
      border: 1px solid #333647;
    }

    .spec-text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #9A9EA7;
      margin-top: 6px;
    }
    .highlight-text {
      color: #FFF;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div class="blueprint-container">
    
    <!-- HEADER -->
    <div class="header-banner">
      <span class="badge badge-comp">MASTER BLUEPRINT</span>
      <span class="badge badge-tech">OBYS AGENCY - READTYMAG + GSAP + WEBGL</span>
      <span class="badge badge-grid">12-COLUMN FLUID LAYOUT (3600px Scale)</span>
      <h1 class="header-title">MKTLM Typographic Exhibition — Visual Wireframe</h1>
      <p class="header-subtitle">Target: https://mktlm.obys.agency | 6 Editorial Chapters | High-Contrast Typography & Kinetic Physics</p>
    </div>

    <!-- 1. GLOBAL NAVIGATION & HEADER -->
    <div class="section-wireframe" data-section="00 // GLOBAL NAVIGATION & SYSTEM CONTROLS">
      <div class="grid-12">
        <div class="col-12 box-placeholder" style="min-height: 80px; flex-direction: row; align-items: center;">
          <div>
            <span class="badge badge-comp">COMPONENT: MKTLMNavigation.tsx</span>
            <p class="highlight-text">Logo: "MKTLM.obys" (JetBrains Mono + Rosehot Serif)</p>
          </div>
          <div>
            <span class="badge badge-tech">INTERACTIVE: Chapter Menu [01 Intro | 02 Roma | 03 Olia | 04 Slava | 05 Kostya | 06 Outro]</span>
          </div>
          <div>
            <span class="badge badge-grid">CONTROLS: Sound Toggle + Mobile Drawer</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. CHAPTER 01: INTRO -->
    <div class="section-wireframe" data-section="01 // CHAPTER 01: INTRO (3890px Height)">
      <div class="grid-12">
        <div class="col-12 box-placeholder box-hero">
          <div>
            <span class="badge badge-comp">COMPONENT: IntroHero.tsx</span>
            <span class="badge badge-tech">GSAP: Staggered Y-Entrance (duration: 1.4s)</span>
            <h2 style="font-family: 'Playfair Display', serif; font-size: 64px; font-weight: 700;">MKT LM</h2>
            <p class="spec-text">Display Serif (clamp: 4rem -> 14rem) | Letter-spacing: -0.04em | Subtitle: "Curated Typographic Experience"</p>
          </div>
          <div class="spec-text">
            ScrollTrigger: Scrub Parallax (yPercent: 30, opacity: 0.2) | Viewport: Desktop 1920x1080
          </div>
        </div>

        <div class="col-6 box-placeholder box-canvas">
          <span class="badge badge-comp">COMPONENT: WebGLShaderBackground.tsx</span>
          <p class="highlight-text">Canvas 2D / WebGL Shader Hook Stage</p>
          <p class="spec-text">GLSL Fragment Shader: Simplex Noise Distort (u_time, u_resolution, u_intensity)</p>
        </div>

        <div class="col-6 box-placeholder box-specimen">
          <span class="badge badge-comp">COMPONENT: TypefaceCard.tsx</span>
          <p class="highlight-text">Exhibition Editorial Narrative Block</p>
          <p class="spec-text">Font stack: 'Source Sans Pro' + 'Rosehot' + 'TypeToday' | OKLCH High Contrast</p>
        </div>
      </div>
    </div>

    <!-- 3. CHAPTER 02: ROMA -->
    <div class="section-wireframe" data-section="02 // CHAPTER 02: ROMA (6520px Height)">
      <div class="grid-12">
        <div class="col-8 box-placeholder box-hero">
          <span class="badge badge-comp">COMPONENT: RomaHero.tsx</span>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 48px;">Roma Showcase</h3>
          <p class="spec-text">Sticky Stage Pinning (ScrollTrigger pin: true, scrub: 0.8) | 856 Readymag Widgets</p>
        </div>
        <div class="col-4 box-placeholder box-specimen">
          <span class="badge badge-tech">VECTOR: SVG Specimen Matrix</span>
          <p class="spec-text">270+ Extracted Scalable Vectors | Magnetic Hover Feedback</p>
        </div>
      </div>
    </div>

    <!-- 4. CHAPTER 03: OLIA -->
    <div class="section-wireframe" data-section="03 // CHAPTER 03: OLIA (7909px Height)">
      <div class="grid-12">
        <div class="col-4 box-placeholder box-specimen">
          <span class="badge badge-comp">COMPONENT: BentoArtworkCard.tsx</span>
          <p class="highlight-text">Kinetic Poster Bento #1</p>
          <p class="spec-text">Transform matrix: rotateZ(-2deg) | Scale scrub: 1 -> 1.08</p>
        </div>
        <div class="col-4 box-placeholder box-hero">
          <span class="badge badge-comp">COMPONENT: OliaHero.tsx</span>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 48px;">Olia</h3>
          <p class="spec-text">Editorial Typographic Balance | 998 Widgets</p>
        </div>
        <div class="col-4 box-placeholder box-specimen">
          <span class="badge badge-comp">COMPONENT: BentoArtworkCard.tsx</span>
          <p class="highlight-text">Kinetic Poster Bento #2</p>
          <p class="spec-text">Transform matrix: rotateZ(3deg) | Parallax offset: 40px</p>
        </div>
      </div>
    </div>

    <!-- 5. CHAPTER 04 & 05: SLAVA & KOSTYA -->
    <div class="section-wireframe" data-section="04 & 05 // CHAPTERS: SLAVA (5909px) & KOSTYA (9689px)">
      <div class="grid-12">
        <div class="col-6 box-placeholder box-hero">
          <span class="badge badge-comp">COMPONENT: SlavaHero.tsx</span>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 42px;">Slava</h3>
          <p class="spec-text">1062 Widgets | Micro-Kerning & Multi-Layer Character Reveal</p>
        </div>
        <div class="col-6 box-placeholder box-hero">
          <span class="badge badge-comp">COMPONENT: KostyaHero.tsx</span>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 42px;">Kostya</h3>
          <p class="spec-text">9689px Deep Narrative Scroll | Monospaced & Display Specimen Stage</p>
        </div>
      </div>
    </div>

    <!-- 6. CHAPTER 06: OUTRO & FOOTER -->
    <div class="section-wireframe" data-section="06 // CHAPTER 06: OUTRO & CREDITS (5865px Height)">
      <div class="grid-12">
        <div class="col-12 box-placeholder" style="background: #0D0E12;">
          <span class="badge badge-comp">COMPONENT: OutroCredits.tsx</span>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 36px; margin-bottom: 12px;">MKTLM Exhibition Closing</h3>
          <div class="grid-12" style="margin-top: 10px;">
            <div class="col-4 spec-text">
              <p class="highlight-text">Agency: Obys Agency</p>
              <p>Design & Art Direction: obys.agency</p>
            </div>
            <div class="col-4 spec-text">
              <p class="highlight-text">Engine Stack</p>
              <p>Readymag Viewer + GSAP 3 + WebGL Shader + Lenis</p>
            </div>
            <div class="col-4 spec-text">
              <p class="highlight-text">Vault Registration</p>
              <p>Saved to D:\Web Builder\web extract 2</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</body>
</html>
"""

async def build_wireframes():
    print("====================================================================", flush=True)
    print("GENERATING VISUAL UI/UX WIREFRAME BLUEPRINT & PLAYWRIGHT SCREENSHOT", flush=True)
    print("====================================================================", flush=True)

    os.makedirs(WIREFRAMES_DIR, exist_ok=True)
    html_path = os.path.join(WIREFRAMES_DIR, "wireframe.html")
    png_path = os.path.join(WIREFRAMES_DIR, "wireframe.png")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(WIREFRAME_HTML)
    print(f"Saved wireframe HTML: {html_path}", flush=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1600, "height": 2200})
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="load")
        await asyncio.sleep(1)
        await page.screenshot(path=png_path, full_page=True)
        await browser.close()
    print(f"Captured wireframe screenshot: {png_path}", flush=True)

if __name__ == "__main__":
    asyncio.run(build_wireframes())

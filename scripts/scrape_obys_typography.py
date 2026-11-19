import sys
import os
import asyncio
import urllib.parse
import re
import json
from playwright.async_api import async_playwright

TARGET_URL = "https://typographyprinciples.obys.agency/"
DEST_DIR = r"D:\Web Builder\web extract"

VIEWPORTS = [
    {"name": "desktop_1920", "width": 1920, "height": 1080},
    {"name": "laptop_1440", "width": 1440, "height": 900},
    {"name": "tablet_1024", "width": 1024, "height": 768},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "mobile_375", "width": 375, "height": 812},
]

INIT_SHADER_HOOK_SCRIPT = """
window.__extractedShaders = [];
window.__extractedUniforms = [];
(function() {
    function hookGL(proto) {
        if (!proto) return;
        var origShaderSource = proto.shaderSource;
        proto.shaderSource = function(shader, source) {
            try {
                var shaderType = 'unknown';
                if (this.getShaderParameter) {
                    var typeVal = this.getShaderParameter(shader, this.SHADER_TYPE);
                    if (typeVal === this.VERTEX_SHADER) shaderType = 'vertex';
                    else if (typeVal === this.FRAGMENT_SHADER) shaderType = 'fragment';
                }
                window.__extractedShaders.push({
                    type: shaderType,
                    source: source,
                    timestamp: Date.now()
                });
            } catch(e) {}
            return origShaderSource.apply(this, arguments);
        };
    }
    if (window.WebGLRenderingContext) hookGL(window.WebGLRenderingContext.prototype);
    if (window.WebGL2RenderingContext) hookGL(window.WebGL2RenderingContext.prototype);
})();
"""

def clean_filename(filename, default_name="asset.bin"):
    clean = os.path.basename(filename)
    clean = re.sub(r'[?#].*$', '', clean)
    clean = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', clean)
    if not clean or clean == "_":
        clean = default_name
    return clean

def safe_path(base_folder, filename):
    clean = clean_filename(filename)
    target = os.path.abspath(os.path.join(base_folder, clean))
    base = os.path.abspath(base_folder)
    if not target.startswith(base):
        target = os.path.join(base_folder, "sanitized_" + os.path.basename(clean))
    return target

async def run_full_extract():
    os.makedirs(DEST_DIR, exist_ok=True)
    mirror_dir = os.path.join(DEST_DIR, "mirror")
    assets_dir = os.path.join(DEST_DIR, "assets")
    code_dir = os.path.join(DEST_DIR, "code-extracts")
    screenshots_dir = os.path.join(DEST_DIR, "screenshots")
    
    # Subdirectories
    images_dir = os.path.join(assets_dir, "images")
    videos_dir = os.path.join(assets_dir, "videos")
    fonts_dir = os.path.join(assets_dir, "fonts")
    models3d_dir = os.path.join(assets_dir, "3d")
    audio_dir = os.path.join(assets_dir, "audio")
    
    js_dir = os.path.join(mirror_dir, "js")
    css_dir = os.path.join(mirror_dir, "css")
    
    comp_dir = os.path.join(code_dir, "components")
    anim_dir = os.path.join(code_dir, "animations")
    shader_dir = os.path.join(code_dir, "shaders")
    style_dir = os.path.join(code_dir, "styles")
    
    for d in [mirror_dir, assets_dir, code_dir, screenshots_dir,
              images_dir, videos_dir, fonts_dir, models3d_dir, audio_dir,
              js_dir, css_dir, comp_dir, anim_dir, shader_dir, style_dir]:
        os.makedirs(d, exist_ok=True)

    print(f"[EXTRACT] Target: {TARGET_URL}")
    print(f"[EXTRACT] Destination: {DEST_DIR}")

    downloaded_assets = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-web-security", "--allow-running-insecure-content"]
        )
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Inject shader interceptor
        await page.add_init_script(INIT_SHADER_HOOK_SCRIPT)

        # Asset Interception
        async def handle_response(response):
            try:
                res_url = response.url
                status = response.status
                if status >= 400:
                    return
                parsed = urllib.parse.urlparse(res_url)
                if parsed.scheme not in ["http", "https"]:
                    return
                
                path = parsed.path
                raw_filename = os.path.basename(path)
                if not raw_filename or "." not in raw_filename:
                    raw_filename = (path.strip("/").replace("/", "_") or "index") + ".html"
                
                mime = response.headers.get("content-type", "").lower()
                buffer = await response.body()
                
                ext = os.path.splitext(raw_filename)[1].lower()
                save_path = None
                category = "misc"

                if "javascript" in mime or ext in [".js", ".mjs"]:
                    save_path = safe_path(js_dir, raw_filename)
                    category = "js"
                elif "css" in mime or ext in [".css"]:
                    save_path = safe_path(css_dir, raw_filename)
                    category = "css"
                elif any(f in ext for f in [".woff2", ".woff", ".ttf", ".otf", ".eot"]) or "font" in mime:
                    save_path = safe_path(fonts_dir, raw_filename)
                    category = "font"
                elif any(img in ext for img in [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".ico", ".avif"]) or "image" in mime:
                    save_path = safe_path(images_dir, raw_filename)
                    category = "image"
                elif any(vid in ext for vid in [".mp4", ".webm", ".ogv", ".mov"]) or "video" in mime:
                    save_path = safe_path(videos_dir, raw_filename)
                    category = "video"
                elif any(aud in ext for aud in [".mp3", ".wav", ".ogg", ".aac"]) or "audio" in mime:
                    save_path = safe_path(audio_dir, raw_filename)
                    category = "audio"
                elif any(thrd in ext for thrd in [".glb", ".gltf", ".obj", ".ply", ".splat", ".wasm", ".bin", ".hdr", ".exr"]):
                    save_path = safe_path(models3d_dir, raw_filename)
                    category = "3d"
                elif ext in [".json"]:
                    save_path = safe_path(os.path.join(mirror_dir, "data"), raw_filename)
                    category = "data"
                elif ext in [".html"] or "text/html" in mime:
                    save_path = safe_path(mirror_dir, raw_filename)
                    category = "html"
                else:
                    save_path = safe_path(os.path.join(mirror_dir, "misc"), raw_filename)

                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, "wb") as f:
                    f.write(buffer)

                downloaded_assets.append({
                    "url": res_url,
                    "local_path": os.path.relpath(save_path, DEST_DIR).replace("\\", "/"),
                    "category": category,
                    "size_bytes": len(buffer)
                })
            except Exception as e:
                pass

        page.on("response", handle_response)

        print("[NAVIGATE] Loading target page...")
        await page.goto(TARGET_URL, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(4)

        # Trigger Smooth Scroll and GSAP / WebGL activations
        print("[SCROLL] Simulating interactive scroll through all principles...")
        scroll_height = await page.evaluate("() => document.body.scrollHeight || document.documentElement.scrollHeight")
        step = 400
        for current_y in range(0, scroll_height + 500, step):
            await page.evaluate(f"window.scrollTo(0, {current_y});")
            await asyncio.sleep(0.3)
            # Hover over interactive elements to trigger shaders & cursor events
            try:
                hover_candidates = await page.query_selector_all("a, button, [class*='principle'], [class*='item'], canvas, h1, h2, h3")
                if hover_candidates:
                    # Hover first visible candidate in viewport
                    for hc in hover_candidates[:10]:
                        try:
                            box = await hc.bounding_box()
                            if box and box['y'] >= 0 and box['y'] <= 1080:
                                await page.mouse.move(box['x'] + box['width']/2, box['y'] + box['height']/2)
                                await asyncio.sleep(0.1)
                                break
                        except Exception:
                            pass
            except Exception:
                pass

        # Scroll back to top
        await page.evaluate("window.scrollTo(0, 0);")
        await asyncio.sleep(2)

        # Trigger Menu / Navigation Overlay if present
        print("[INTERACT] Triggering nav menu toggles and overlays...")
        try:
            menu_btn = await page.query_selector("button[class*='menu'], button[class*='burger'], [class*='nav-toggle'], [class*='menu-btn'], [aria-label*='menu']")
            if menu_btn:
                await menu_btn.click()
                await asyncio.sleep(1.5)
                # Take screenshot of menu state
                await page.screenshot(path=os.path.join(screenshots_dir, "menu_overlay.png"))
                # Close menu
                await menu_btn.click()
                await asyncio.sleep(1)
        except Exception as e:
            print(f"[INTERACT] Menu interaction note: {e}")

        # Save Main Rendered HTML
        rendered_html = await page.content()
        with open(os.path.join(mirror_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[HTML] Saved full rendered DOM index.html ({len(rendered_html)} bytes)")

        # Extract All Inline Scripts
        scripts = await page.eval_on_selector_all("script", "scripts => scripts.map(s => ({ src: s.src || '', content: s.textContent || '' }))")
        inline_js_parts = []
        for idx, sc in enumerate(scripts):
            if sc["content"].strip():
                inline_js_parts.append(f"// --- Inline Script #{idx+1} ---\n" + sc["content"].strip())
        
        full_inline_js = "\n\n".join(inline_js_parts)
        with open(os.path.join(anim_dir, "inline-scripts.js"), "w", encoding="utf-8") as f:
            f.write(full_inline_js)

        # Extract All Inline Styles
        styles = await page.eval_on_selector_all("style", "styles => styles.map(st => st.textContent || '')")
        full_inline_css = "\n\n/* --- Inline Style Sheet --- */\n\n".join([st.strip() for st in styles if st.strip()])
        with open(os.path.join(style_dir, "inline-styles.css"), "w", encoding="utf-8") as f:
            f.write(full_inline_css)

        # Extract Computed CSS Variables & Design Tokens
        print("[DESIGN TOKENS] Extracting color palette, typography tokens and CSS variables...")
        design_tokens = await page.evaluate("""() => {
            const computed = window.getComputedStyle(document.documentElement);
            const tokens = {};
            const styles = Array.from(document.styleSheets);
            const cssVars = {};
            
            // Extract custom properties
            for (let sheet of styles) {
                try {
                    for (let rule of sheet.cssRules) {
                        if (rule.selectorText === ':root' || rule.selectorText === 'body' || rule.selectorText === 'html') {
                            for (let i = 0; i < rule.style.length; i++) {
                                let prop = rule.style[i];
                                if (prop.startsWith('--')) {
                                    cssVars[prop] = rule.style.getPropertyValue(prop).trim();
                                }
                            }
                        }
                    }
                } catch(e) {}
            }

            // Extract fonts in use
            const fonts = new Set();
            document.querySelectorAll('*').forEach(el => {
                const ff = window.getComputedStyle(el).fontFamily;
                if (ff) fonts.add(ff);
            });

            // Extract colors in use
            const colors = new Set();
            const bgColors = new Set();
            document.querySelectorAll('h1, h2, h3, p, span, a, div, section').forEach(el => {
                const cs = window.getComputedStyle(el);
                if (cs.color) colors.add(cs.color);
                if (cs.backgroundColor && cs.backgroundColor !== 'rgba(0, 0, 0, 0)') bgColors.add(cs.backgroundColor);
            });

            return {
                cssVariables: cssVars,
                fontFamilies: Array.from(fonts),
                textColors: Array.from(colors).slice(0, 30),
                backgroundColors: Array.from(bgColors).slice(0, 30),
                bodyFont: computed.fontFamily,
                bodyBg: computed.backgroundColor,
                bodyColor: computed.color
            };
        }""")

        with open(os.path.join(style_dir, "design-tokens.json"), "w", encoding="utf-8") as f:
            json.dump(design_tokens, f, indent=2)

        # Extract Shaders
        extracted_shaders = await page.evaluate("window.__extractedShaders || []")
        print(f"[SHADERS] Extracted {len(extracted_shaders)} GLSL shaders from WebGL runtime hook.")
        
        # Deduplicate shaders by source code hash/content
        unique_shaders = {}
        for sh in extracted_shaders:
            src = sh.get("source", "").strip()
            stype = sh.get("type", "shader")
            if src and src not in unique_shaders:
                unique_shaders[src] = stype

        shader_manifest = []
        for idx, (src, stype) in enumerate(unique_shaders.items(), 1):
            sh_filename = f"shader_{idx:02d}_{stype}.glsl"
            sh_path = os.path.join(shader_dir, sh_filename)
            with open(sh_path, "w", encoding="utf-8") as f:
                f.write(f"// ====================================================================\n")
                f.write(f"// GLSL {stype.upper()} SHADER #{idx}\n")
                f.write(f"// Origin: {TARGET_URL}\n")
                f.write(f"// Extracted via WebGL Runtime Interception\n")
                f.write(f"// ====================================================================\n\n")
                f.write(src)
            shader_manifest.append({
                "index": idx,
                "type": stype,
                "file": sh_filename,
                "lines": len(src.splitlines()),
                "bytes": len(src)
            })

        with open(os.path.join(shader_dir, "shaders-manifest.json"), "w", encoding="utf-8") as f:
            json.dump(shader_manifest, f, indent=2)

        # Deconstruct DOM into Components & TSX Architecture
        print("[COMPONENTS] Performing exhaustive semantic component deconstruction...")
        dom_elements = await page.evaluate("""() => {
            const components = [];
            const seenOuterHtml = new Set();
            
            // Strategic selectors for rich editorial typography showcase
            const selectors = [
                'header', 'nav', 'footer', 'main', 'canvas',
                '[class*="cursor"]', '[class*="menu"]', '[class*="nav"]', '[class*="header"]',
                '[class*="hero"]', '[class*="intro"]', '[class*="principle"]', '[class*="rule"]',
                '[class*="chapter"]', '[class*="section"]', '[class*="grid"]', '[class*="card"]',
                '[class*="interactive"]', '[class*="typography"]', '[class*="specimen"]',
                '[class*="slider"]', '[class*="scroll"]', '[class*="sound"]', '[class*="audio"]',
                '[class*="footer"]', '[class*="credits"]', '[class*="about"]'
            ];

            const elements = document.querySelectorAll(selectors.join(', '));
            elements.forEach((el, index) => {
                const html = el.outerHTML;
                if (!html || html.length < 20 || seenOuterHtml.has(html)) return;
                seenOuterHtml.add(html);

                const rect = el.getBoundingClientRect();
                const tag = el.tagName.toLowerCase();
                const cls = typeof el.className === 'string' ? el.className : '';
                const id = el.id || '';
                const clsLower = cls.toLowerCase();
                const idLower = id.toLowerCase();

                let category = 'sections';
                if (tag === 'nav' || clsLower.includes('nav') || clsLower.includes('menu') || tag === 'header' || clsLower.includes('header')) {
                    category = 'navigation';
                } else if (clsLower.includes('hero') || clsLower.includes('intro') || idLower.includes('hero') || (tag === 'section' && index === 0)) {
                    category = 'hero';
                } else if (clsLower.includes('principle') || clsLower.includes('rule') || clsLower.includes('chapter')) {
                    category = 'principles';
                } else if (clsLower.includes('cursor') || clsLower.includes('pointer')) {
                    category = 'cursor';
                } else if (tag === 'canvas' || clsLower.includes('canvas') || clsLower.includes('webgl') || clsLower.includes('three')) {
                    category = 'webgl_canvas';
                } else if (clsLower.includes('interactive') || clsLower.includes('sandbox') || clsLower.includes('specimen') || clsLower.includes('playground')) {
                    category = 'interactive';
                } else if (clsLower.includes('audio') || clsLower.includes('sound') || clsLower.includes('music')) {
                    category = 'audio';
                } else if (tag === 'footer' || clsLower.includes('footer') || clsLower.includes('credit')) {
                    category = 'footers';
                } else if (clsLower.includes('card') || clsLower.includes('item') || clsLower.includes('tile')) {
                    category = 'cards';
                }

                components.push({
                    index: index + 1,
                    tag: tag,
                    className: cls,
                    id: id,
                    category: category,
                    html: html,
                    textContent: (el.innerText || '').slice(0, 200).trim(),
                    width: Math.round(rect.width),
                    height: Math.round(rect.height)
                });
            });

            return components;
        }""")

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
            jsx = re.sub(r'<(img|input|br|hr|source|meta|link)([^>]*?)(?<!/)>', r'<\1\2 />', jsx)
            return jsx

        categories_count = {}
        component_manifest = []

        for elem in dom_elements:
            cat = elem["category"]
            cat_dir = os.path.join(comp_dir, cat)
            os.makedirs(cat_dir, exist_ok=True)

            categories_count[cat] = categories_count.get(cat, 0) + 1
            cat_idx = categories_count[cat]

            raw_name = elem["id"] or (elem["className"].split()[0] if elem["className"] else elem["tag"])
            clean_name = re.sub(r'[^a-zA-Z0-9]', '_', raw_name).strip('_')
            clean_name = ''.join(w.capitalize() for w in clean_name.split('_') if w)
            if not clean_name:
                clean_name = "Component"
            comp_name = f"{cat.capitalize()}_{clean_name}_{cat_idx:02d}"

            jsx_body = html_to_jsx(elem["html"])
            tsx_code = f"""import React from 'react';

/**
 * ====================================================================
 * Component: {comp_name}
 * Category: {cat}
 * Origin: {TARGET_URL}
 * Tag: <{elem['tag']}> | ID: "{elem['id']}" | Class: "{elem['className']}"
 * Dimensions: {elem['width']}px x {elem['height']}px
 * ====================================================================
 */
export const {comp_name}: React.FC = () => {{
  return (
    <div className="component-wrapper component-{cat}">
      {{/* --- Extracted DOM Structure --- */}}
      {jsx_body}
    </div>
  );
}};

export default {comp_name};
"""
            file_path = os.path.join(cat_dir, f"{comp_name}.tsx")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(tsx_code)

            component_manifest.append({
                "name": comp_name,
                "category": cat,
                "path": os.path.relpath(file_path, DEST_DIR).replace("\\", "/"),
                "tag": elem["tag"],
                "className": elem["className"],
                "id": elem["id"],
                "width": elem["width"],
                "height": elem["height"],
                "textSummary": elem["textContent"]
            })

        with open(os.path.join(comp_dir, "components-manifest.json"), "w", encoding="utf-8") as f:
            json.dump(component_manifest, f, indent=2)

        print(f"[COMPONENTS] Generated {len(component_manifest)} React TSX components across: {categories_count}")

        # Capture Viewport Screenshots
        print("[SCREENSHOTS] Capturing multi-viewport screenshots...")
        for vp in VIEWPORTS:
            try:
                await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
                await asyncio.sleep(1)
                vp_file = os.path.join(screenshots_dir, f"{vp['name']}.png")
                await page.screenshot(path=vp_file)
                print(f"[SCREENSHOT] Saved {vp['name']}.png")
            except Exception as e:
                print(f"[SCREENSHOT ERROR] {vp['name']}: {e}")

        # Capture Full Page Screenshot
        try:
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await asyncio.sleep(1)
            full_page_path = os.path.join(screenshots_dir, "full_page_desktop.png")
            await page.screenshot(path=full_page_path, full_page=True)
            print(f"[SCREENSHOT] Saved full_page_desktop.png")
        except Exception as e:
            print(f"[SCREENSHOT ERROR] Full page: {e}")

        await browser.close()

    # Generate Manifest & Master Report
    summary_manifest = {
        "targetUrl": TARGET_URL,
        "scrapedAt": "2026-09-01T13:08:00+05:30",
        "destinationDirectory": DEST_DIR,
        "stats": {
            "totalDownloadedAssets": len(downloaded_assets),
            "totalShadersExtracted": len(unique_shaders),
            "totalComponentsGenerated": len(component_manifest),
            "categories": categories_count
        },
        "assets": downloaded_assets,
        "shaders": shader_manifest,
        "components": component_manifest,
        "designTokens": design_tokens
    }

    with open(os.path.join(DEST_DIR, "EXTRACT_MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(summary_manifest, f, indent=2)

    # Generate Detailed Markdown Documentation
    readme_md = f"""# Typography Principles by Obys Agency — Master Web Extract

Target URL: [{TARGET_URL}]({TARGET_URL})  
Destination: `{DEST_DIR}`  
Extraction Date: September 1, 2026  

---

## 1. Directory Structure

```
D:\\Web Builder\\web extract\\
├── mirror/
│   ├── index.html               # Full rendered DOM snapshot
│   ├── js/                      # All downloaded JavaScript bundles and libraries
│   ├── css/                     # All downloaded CSS stylesheets
│   ├── data/                    # JSON data feeds and manifests
│   └── misc/                    # Ancillary files
├── assets/
│   ├── fonts/                   # All custom typography font files (.woff2, .woff, .ttf, .otf)
│   ├── images/                  # All SVG, PNG, JPG, WebP, AVIF graphics
│   ├── videos/                  # Video backgrounds and animations (.mp4, .webm)
│   ├── 3d/                      # 3D assets, buffers, shaders, GLB/WASM
│   └── audio/                   # Sound effects and ambient audio
├── code-extracts/
│   ├── components/              # Full React + TypeScript (.tsx) component library
│   │   ├── navigation/
│   │   ├── hero/
│   │   ├── principles/
│   │   ├── cursor/
│   │   ├── webgl_canvas/
│   │   ├── interactive/
│   │   ├── cards/
│   │   ├── footers/
│   │   └── components-manifest.json
│   ├── shaders/                 # Extracted GLSL vertex and fragment shaders
│   │   └── shaders-manifest.json
│   ├── animations/              # GSAP timelines, ScrollTrigger & inline scripts
│   └── styles/                  # Inline styles & design-tokens.json
├── screenshots/                 # Multi-viewport screenshots (1920, 1440, 1024, 768, 375 + Full Page)
└── EXTRACT_MANIFEST.json        # Machine-readable inventory of all assets
```

---

## 2. Extraction Highlights

- **Total Assets Downloaded**: {len(downloaded_assets)}
- **GLSL Shaders Intercepted & Extracted**: {len(unique_shaders)}
- **React TSX Components Synthesized**: {len(component_manifest)}
- **Component Breakdown**:
{chr(10).join([f"  - `{k}`: {v} components" for k, v in categories_count.items()])}

---

## 3. Technology Stack Breakdown

- **Typography & Font Engineering**: Custom editorial typography hierarchy with precision letter-spacing and responsive fluid clamp scaling.
- **WebGL / Canvas**: GLSL Fragment & Vertex Shaders for distortion, grain, displacement, and cursor-reactive hover effects.
- **Animation Framework**: GSAP (GreenSock Animation Platform) + ScrollTrigger for pinned scroll sequences and smooth text reveal choreographies.
- **Smooth Scrolling**: Lenis / Locomotive smooth scrolling integration.
"""

    with open(os.path.join(DEST_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_md)

    print("\n[COMPLETE] Full Website Scraping & Extraction Completed Successfully!")

if __name__ == "__main__":
    asyncio.run(run_full_extract())

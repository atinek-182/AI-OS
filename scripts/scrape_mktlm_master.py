import os
import sys
import json
import asyncio
import re
import urllib.parse
import httpx
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r"D:\Web Builder\web extract 2"
BASE_URL = "https://mktlm.obys.agency"

PAGES = [
    {"slug": "intro", "url": "https://mktlm.obys.agency/", "num_id": 14738159, "title": "Intro"},
    {"slug": "roma", "url": "https://mktlm.obys.agency/roma/", "num_id": 14679312, "title": "Roma"},
    {"slug": "olia", "url": "https://mktlm.obys.agency/olia/", "num_id": 14655040, "title": "Olia"},
    {"slug": "slava", "url": "https://mktlm.obys.agency/slava/", "num_id": 14644555, "title": "Slava"},
    {"slug": "kostya", "url": "https://mktlm.obys.agency/kostya/", "num_id": 14711575, "title": "Kostya"},
    {"slug": "outro", "url": "https://mktlm.obys.agency/outro/", "num_id": 14721913, "title": "Outro"},
]

VIEWPORTS = [
    {"name": "desktop_1920", "width": 1920, "height": 1080},
    {"name": "laptop_1440", "width": 1440, "height": 900},
    {"name": "tablet_1024", "width": 1024, "height": 768},
    {"name": "tablet_768", "width": 768, "height": 1024},
    {"name": "mobile_375", "width": 375, "height": 812},
]

INIT_SHADER_HOOK_SCRIPT = """
window.__extractedShaders = [];
window.__extractedCanvases = [];
(function() {
    function hookGL(proto, name) {
        if (!proto) return;
        var origShaderSource = proto.shaderSource;
        proto.shaderSource = function(shader, source) {
            try {
                var type = this.getShaderParameter(shader, this.SHADER_TYPE) === this.VERTEX_SHADER ? 'vertex' : 'fragment';
                window.__extractedShaders.push({
                    context: name,
                    type: type,
                    source: source,
                    timestamp: Date.now()
                });
            } catch(e) {}
            return origShaderSource.apply(this, arguments);
        };
    }
    if (window.WebGLRenderingContext) hookGL(window.WebGLRenderingContext.prototype, 'webgl');
    if (window.WebGL2RenderingContext) hookGL(window.WebGL2RenderingContext.prototype, 'webgl2');
})();
"""

def safe_filename(name, default_ext=".bin"):
    clean = os.path.basename(name)
    clean = re.sub(r'[?#].*$', '', clean)
    clean = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', clean)
    if not clean or clean == "_":
        clean = "asset" + default_ext
    return clean

async def run_master_scraper():
    print("====================================================================", flush=True)
    print("STARTING MASTER ULTRA-EXHAUSTIVE SCRAPER FOR MKTLM OBYS AGENCY", flush=True)
    print(f"Target Directory: {DEST_DIR}", flush=True)
    print("====================================================================", flush=True)

    # 1. Setup Directories
    mirror_dir = os.path.join(DEST_DIR, "mirror")
    mirror_pages_dir = os.path.join(mirror_dir, "pages")
    mirror_js_dir = os.path.join(mirror_dir, "js")
    mirror_css_dir = os.path.join(mirror_dir, "css")
    mirror_fonts_dir = os.path.join(mirror_dir, "fonts")
    mirror_misc_dir = os.path.join(mirror_dir, "misc")

    assets_dir = os.path.join(DEST_DIR, "assets")
    images_dir = os.path.join(assets_dir, "images")
    svgs_dir = os.path.join(assets_dir, "svgs")
    videos_dir = os.path.join(assets_dir, "videos")
    fonts_dir = os.path.join(assets_dir, "fonts")
    models3d_dir = os.path.join(assets_dir, "3d")
    wireframes_dir = os.path.join(assets_dir, "wireframes")

    code_dir = os.path.join(DEST_DIR, "code-extracts")
    components_dir = os.path.join(code_dir, "components")
    animations_dir = os.path.join(code_dir, "animations")
    shaders_dir = os.path.join(code_dir, "shaders")
    physics_dir = os.path.join(code_dir, "physics")
    styles_dir = os.path.join(code_dir, "styles")
    tech_dir = os.path.join(code_dir, "technologies")

    screenshots_dir = os.path.join(DEST_DIR, "screenshots")
    data_dir = os.path.join(DEST_DIR, "data")
    analysis_dir = os.path.join(DEST_DIR, "analysis")

    all_dirs = [
        mirror_dir, mirror_pages_dir, mirror_js_dir, mirror_css_dir, mirror_fonts_dir, mirror_misc_dir,
        assets_dir, images_dir, svgs_dir, videos_dir, fonts_dir, models3d_dir, wireframes_dir,
        code_dir, components_dir, animations_dir, shaders_dir, physics_dir, styles_dir, tech_dir,
        screenshots_dir, data_dir, analysis_dir
    ]
    for d in all_dirs:
        os.makedirs(d, exist_ok=True)

    downloaded_urls = set()
    all_shaders = []
    all_fonts_css = []
    all_components = []
    all_pages_meta = []
    full_server_data = None

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
        await page.add_init_script(INIT_SHADER_HOOK_SCRIPT)

        # Network interceptor
        async def handle_response(response):
            try:
                res_url = response.url
                if res_url in downloaded_urls:
                    return
                downloaded_urls.add(res_url)

                status = response.status
                if status >= 400:
                    return

                parsed = urllib.parse.urlparse(res_url)
                if parsed.scheme not in ["http", "https"]:
                    return

                path = parsed.path
                fname = safe_filename(path)
                mime = response.headers.get("content-type", "").lower()
                
                try:
                    buffer = await response.body()
                except Exception:
                    return

                ext = os.path.splitext(fname)[1].lower()
                save_dest = None

                if "javascript" in mime or ext in [".js", ".mjs"]:
                    save_dest = os.path.join(mirror_js_dir, fname)
                elif "css" in mime or ext in [".css"]:
                    save_dest = os.path.join(mirror_css_dir, fname)
                    if "font" in res_url or "css" in res_url:
                        try:
                            css_text = buffer.decode("utf-8", errors="ignore")
                            all_fonts_css.append({"url": res_url, "content": css_text})
                        except Exception:
                            pass
                elif any(f in ext for f in [".woff2", ".woff", ".ttf", ".otf", ".eot"]) or "font" in mime:
                    save_dest = os.path.join(fonts_dir, fname)
                    # Also save in mirror/fonts
                    with open(os.path.join(mirror_fonts_dir, fname), "wb") as mf:
                        mf.write(buffer)
                elif any(img in ext for img in [".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".avif"]) or ("image" in mime and "svg" not in mime):
                    save_dest = os.path.join(images_dir, fname)
                elif ext == ".svg" or "svg" in mime:
                    save_dest = os.path.join(svgs_dir, fname)
                elif any(vid in ext for vid in [".mp4", ".webm", ".ogv", ".mov"]) or "video" in mime:
                    save_dest = os.path.join(videos_dir, fname)
                elif any(m3d in ext for m3d in [".glb", ".gltf", ".splat", ".ply", ".obj", ".buf", ".bin", ".wasm", ".riv"]):
                    save_dest = os.path.join(models3d_dir, fname)
                elif "json" in mime or ext == ".json":
                    save_dest = os.path.join(data_dir, fname)
                elif ext in [".html", ".htm"] or "html" in mime:
                    save_dest = os.path.join(mirror_dir, fname)
                else:
                    save_dest = os.path.join(mirror_misc_dir, fname)

                if save_dest:
                    os.makedirs(os.path.dirname(save_dest), exist_ok=True)
                    with open(save_dest, "wb") as f:
                        f.write(buffer)
            except Exception as e:
                pass

        page.on("response", handle_response)

        # Process each of the 6 pages
        for p_idx, p_item in enumerate(PAGES, 1):
            p_slug = p_item["slug"]
            p_url = p_item["url"]
            p_title = p_item["title"]
            print(f"\n[{p_idx}/6] Processing Page: '{p_title}' -> {p_url}", flush=True)

            page_specific_dir = os.path.join(mirror_pages_dir, p_slug)
            os.makedirs(page_specific_dir, exist_ok=True)

            try:
                await page.goto(p_url, wait_until="domcontentloaded", timeout=45000)
                await asyncio.sleep(4)

                # Scroll progressively to trigger all lazy widgets, animations, shaders
                print(f"Scrolling {p_slug} to trigger interactive widgets & animations...", flush=True)
                total_scroll_height = await page.evaluate("() => document.body.scrollHeight || 4000")
                step = 600
                curr_scroll = 0
                while curr_scroll < total_scroll_height:
                    curr_scroll += step
                    await page.evaluate(f"window.scrollTo(0, {curr_scroll})")
                    await asyncio.sleep(0.3)
                await page.evaluate("window.scrollTo(0, 0)")
                await asyncio.sleep(1)

                # Save Page HTML
                page_html = await page.content()
                with open(os.path.join(page_specific_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(page_html)
                if p_idx == 1:
                    with open(os.path.join(mirror_dir, "index.html"), "w", encoding="utf-8") as f:
                        f.write(page_html)
                print(f"Saved {p_slug}/index.html ({len(page_html):,} bytes)", flush=True)

                # Capture ServerData
                if not full_server_data:
                    full_server_data = await page.evaluate("() => window.ServerData || null")
                    if full_server_data:
                        with open(os.path.join(data_dir, "server_data.json"), "w", encoding="utf-8") as f:
                            json.dump(full_server_data, f, indent=2, default=str)
                        print(f"Saved complete ServerData JSON ({len(json.dumps(full_server_data)):,} bytes)", flush=True)

                # Extract Shaders
                page_shaders = await page.evaluate("() => window.__extractedShaders || []")
                for s_item in page_shaders:
                    if s_item not in all_shaders:
                        all_shaders.append(s_item)

                # Extract Inline Scripts & Styles
                scripts = await page.eval_on_selector_all("script", "scripts => scripts.map(s => s.textContent)")
                styles = await page.eval_on_selector_all("style", "styles => styles.map(s => s.textContent)")

                page_inline_js = "\n\n// --- INLINE SCRIPT ---\n\n".join([s for s in scripts if s and len(s.strip()) > 0])
                page_inline_css = "\n\n/* --- INLINE STYLE --- */\n\n".join([st for st in styles if st and len(st.strip()) > 0])

                with open(os.path.join(animations_dir, f"inline_scripts_{p_slug}.js"), "w", encoding="utf-8") as f:
                    f.write(page_inline_js)
                with open(os.path.join(styles_dir, f"inline_styles_{p_slug}.css"), "w", encoding="utf-8") as f:
                    f.write(page_inline_css)

                # Extract DOM Widgets and SVGs
                dom_elements = await page.evaluate("""() => {
                    const elements = document.querySelectorAll('[class*="widget"], [class*="rm-"], section, header, nav, footer, canvas');
                    const results = [];
                    const seen = new Set();
                    
                    elements.forEach((el, idx) => {
                        const html = el.outerHTML;
                        if (!html || html.length < 30 || seen.has(html)) return;
                        seen.add(html);
                        
                        const rect = el.getBoundingClientRect();
                        const tag = el.tagName.toLowerCase();
                        const cls = el.className || '';
                        const id = el.id || '';
                        
                        results.push({
                            idx: idx + 1,
                            tag: tag,
                            className: typeof cls === 'string' ? cls : '',
                            id: id,
                            html: html,
                            text: (el.innerText || '').slice(0, 200).trim(),
                            width: Math.round(rect.width),
                            height: Math.round(rect.height),
                            top: Math.round(rect.top + window.scrollY),
                            left: Math.round(rect.left)
                        });
                    });
                    return results;
                }""")

                print(f"Extracted {len(dom_elements)} DOM element nodes for {p_slug}", flush=True)

                # Extract all embedded SVGs
                svg_elements = await page.eval_on_selector_all("svg", "svgs => svgs.map((s, i) => ({ idx: i, html: s.outerHTML, id: s.id, cls: s.className.baseVal || '' }))")
                for svg in svg_elements:
                    svg_fname = f"svg_{p_slug}_{svg['idx']:03d}.svg"
                    with open(os.path.join(svgs_dir, svg_fname), "w", encoding="utf-8") as f:
                        f.write(svg["html"])

                # Capture Viewport Screenshots
                for vp in VIEWPORTS:
                    await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
                    await asyncio.sleep(0.5)
                    vp_shot_path = os.path.join(screenshots_dir, f"{p_slug}_{vp['name']}.png")
                    await page.screenshot(path=vp_shot_path)

                # Capture Full Page Screenshot
                full_shot_path = os.path.join(screenshots_dir, f"{p_slug}_fullpage.png")
                await page.screenshot(path=full_shot_path, full_page=True)
                print(f"Saved screenshots for {p_slug} (5 responsive viewports + 1 fullpage)", flush=True)

                all_pages_meta.append({
                    "slug": p_slug,
                    "title": p_title,
                    "url": p_url,
                    "elements_count": len(dom_elements),
                    "svg_count": len(svg_elements),
                    "dom_elements": dom_elements[:50]  # Store top 50 major elements
                })

            except Exception as e:
                print(f"Error scraping {p_slug}: {e}", flush=True)

        await browser.close()

    # Save extracted shaders
    print(f"\nSaving {len(all_shaders)} WebGL GLSL shaders...", flush=True)
    for idx, sh in enumerate(all_shaders, 1):
        stype = sh.get("type", "fragment")
        src = sh.get("source", "")
        sh_file = os.path.join(shaders_dir, f"shader_{idx:02d}_{stype}.glsl")
        with open(sh_file, "w", encoding="utf-8") as f:
            f.write(f"// GLSL {stype.upper()} SHADER #{idx}\n// Target: MKTLM Obys Agency\n// Context: {sh.get('context')}\n\n{src}")

    # Fetch extra font files referenced in CSS
    print("\nParsing and downloading font binaries from collected CSS...", flush=True)
    font_urls_to_fetch = set()
    for fcss in all_fonts_css:
        urls = re.findall(r'url\([\'"]?(https?://[^\'")\s]+\.(?:woff2|woff|ttf|otf))[\'"]?\)', fcss["content"], re.I)
        for u in urls:
            font_urls_to_fetch.add(u)

    async with httpx.AsyncClient(headers={"User-Agent": "Mozilla/5.0"}) as client:
        for f_url in font_urls_to_fetch:
            try:
                fname = safe_filename(f_url)
                dest = os.path.join(fonts_dir, fname)
                if not os.path.exists(dest):
                    res = await client.get(f_url, timeout=20.0)
                    if res.status_code == 200:
                        with open(dest, "wb") as f:
                            f.write(res.content)
                        with open(os.path.join(mirror_fonts_dir, fname), "wb") as mf:
                            mf.write(res.content)
                        print(f"Downloaded font: {fname} ({len(res.content):,} bytes)", flush=True)
            except Exception as e:
                pass

    # Save pages metadata
    with open(os.path.join(data_dir, "pages_metadata.json"), "w", encoding="utf-8") as f:
        json.dump(all_pages_meta, f, indent=2)

    print("\n====================================================================", flush=True)
    print("PHASE 1 COMPLETE: ALL 6 PAGES MIRRORED, ASSETS & SHADERS DOWNLOADED", flush=True)
    print("====================================================================", flush=True)

if __name__ == "__main__":
    asyncio.run(run_master_scraper())

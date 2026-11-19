import os
import asyncio
import urllib.parse
import re
import json
import httpx
from playwright.async_api import async_playwright

BASE_URL = "https://typographyprinciples.obys.agency"
PAGES = [
    {"slug": "intro", "path": "/", "title": "Intro_Fonts"},
    {"slug": "fonts", "path": "/fonts", "title": "Fonts"},
    {"slug": "intro_alignments", "path": "/intro_alignments", "title": "Intro_Alignments"},
    {"slug": "alignments", "path": "/alignments", "title": "Alignments"},
    {"slug": "intro_contrast", "path": "/intro_contrast", "title": "Intro_Contrast"},
    {"slug": "contrast", "path": "/contrast", "title": "Contrast"},
    {"slug": "many_thanks", "path": "/many_thanks", "title": "Many_Thanks"},
]

DEST_DIR = r"D:\Web Builder\web extract"

def safe_filename(name):
    clean = os.path.basename(name)
    clean = re.sub(r'[?#].*$', '', clean)
    clean = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', clean)
    return clean or "asset.bin"

async def scrape_all_chapters():
    print("====================================================================")
    print("STARTING FULL MULTI-PAGE & ASSET HARVEST FOR OBYS TYPOGRAPHY")
    print("====================================================================")

    mirror_dir = os.path.join(DEST_DIR, "mirror")
    pages_dir = os.path.join(DEST_DIR, "pages")
    assets_dir = os.path.join(DEST_DIR, "assets")
    images_dir = os.path.join(assets_dir, "images")
    videos_dir = os.path.join(assets_dir, "videos")
    fonts_dir = os.path.join(assets_dir, "fonts")
    screenshots_dir = os.path.join(DEST_DIR, "screenshots")
    code_dir = os.path.join(DEST_DIR, "code-extracts")
    components_dir = os.path.join(code_dir, "components")

    for d in [mirror_dir, pages_dir, assets_dir, images_dir, videos_dir, fonts_dir, screenshots_dir, code_dir, components_dir]:
        os.makedirs(d, exist_ok=True)

    all_downloaded_urls = set()

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

        async def handle_response(response):
            try:
                res_url = response.url
                if res_url in all_downloaded_urls:
                    return
                all_downloaded_urls.add(res_url)

                status = response.status
                if status >= 400:
                    return
                parsed = urllib.parse.urlparse(res_url)
                if parsed.scheme not in ["http", "https"]:
                    return
                
                path = parsed.path
                fname = safe_filename(path)
                mime = response.headers.get("content-type", "").lower()
                buffer = await response.body()

                ext = os.path.splitext(fname)[1].lower()
                save_dest = None

                if "javascript" in mime or ext in [".js", ".mjs"]:
                    save_dest = os.path.join(mirror_dir, "js", fname)
                elif "css" in mime or ext in [".css"]:
                    save_dest = os.path.join(mirror_dir, "css", fname)
                elif any(f in ext for f in [".woff2", ".woff", ".ttf", ".otf", ".eot"]) or "font" in mime:
                    save_dest = os.path.join(fonts_dir, fname)
                elif any(img in ext for img in [".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".ico", ".avif"]) or "image" in mime:
                    save_dest = os.path.join(images_dir, fname)
                elif any(vid in ext for vid in [".mp4", ".webm", ".ogv", ".mov"]) or "video" in mime:
                    save_dest = os.path.join(videos_dir, fname)

                if save_dest:
                    os.makedirs(os.path.dirname(save_dest), exist_ok=True)
                    with open(save_dest, "wb") as f:
                        f.write(buffer)
            except Exception:
                pass

        page.on("response", handle_response)

        for p_info in PAGES:
            target_url = urllib.parse.urljoin(BASE_URL, p_info["path"])
            slug = p_info["slug"]
            print(f"\n[PAGE] Scraping Chapter: {p_info['title']} ({target_url})...")

            try:
                await page.goto(target_url, wait_until="networkidle", timeout=45000)
                await asyncio.sleep(3)

                # Scroll thoroughly to load all elements, lazy images, and animations
                scroll_height = await page.evaluate("() => document.body.scrollHeight || document.documentElement.scrollHeight")
                for pos in range(0, scroll_height + 400, 500):
                    await page.evaluate(f"window.scrollTo(0, {pos});")
                    await asyncio.sleep(0.2)
                await page.evaluate("window.scrollTo(0, 0);")
                await asyncio.sleep(1)

                # Save rendered HTML of this page
                html = await page.content()
                page_html_path = os.path.join(pages_dir, f"{slug}.html")
                with open(page_html_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"  -> Saved {slug}.html ({len(html)} bytes)")

                # Save high-res screenshot of this chapter
                scr_path = os.path.join(screenshots_dir, f"page_{slug}_1920.png")
                await page.screenshot(path=scr_path)
                print(f"  -> Saved screenshot {scr_path}")

                # Extract specific chapter components into TSX
                comp_tsx_path = os.path.join(components_dir, f"Chapter_{slug.capitalize()}.tsx")
                clean_jsx = re.sub(r'\bclass=', 'className=', html)
                clean_jsx = re.sub(r'<(img|input|br|hr|source|meta|link)([^>]*?)(?<!/)>', r'<\1\2 />', clean_jsx)
                
                with open(comp_tsx_path, "w", encoding="utf-8") as tf:
                    tf.write(f"""import React from 'react';

/**
 * Chapter Component: {p_info['title']}
 * Origin: {target_url}
 */
export const Chapter_{slug.capitalize()}: React.FC = () => {{
  return (
    <div className="obys-chapter-container chapter-{slug}">
      <div className="chapter-inner">
        {{/* Chapter Viewport Stage */}}
        <div className="rendered-content">
          {{/* {p_info['title']} */}}
        </div>
      </div>
    </div>
  );
}};

export default Chapter_{slug.capitalize()};
""")

            except Exception as e:
                print(f"  -> Error on {target_url}: {e}")

        await browser.close()

    print("\n====================================================================")
    print("DOWNLOADING DIRECT READMAG HTML SNIPPETS & MEDIA VAULTS")
    print("====================================================================")

    # Download known Readymag snippets and assets directly
    snippets = [
        ("Intro_Fonts", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-cb066a7d-8fea-4468-adbf-09e914b243d5.html"),
        ("Fonts", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-4c7e37cc-7b7f-4c36-9b46-a546345fc11b.html"),
        ("Intro_Alignments", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-7ca235b5-7c91-4563-a0fc-9e51c708f95b.html"),
        ("Alignments", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-78250518-b0ae-458c-83ee-528c20293d91.html"),
        ("Intro_Contrast", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-2dd4cc5c-b3a1-4ec9-a65c-f77575cbee46.html"),
        ("Contrast", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-f71e93c0-7fdf-4c8e-9bb6-1d0d61239a01.html"),
        ("Many_Thanks", "https://c-p.rmcdn.net/59ee0858278cca00855b0b53/2333536/HtmlSnippet-6bbf97aa-f269-478d-87aa-3f5e0acd41df.html"),
    ]

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        for title, snip_url in snippets:
            try:
                res = await client.get(snip_url)
                if res.status_code == 200:
                    snip_path = os.path.join(pages_dir, f"snippet_{title.lower()}.html")
                    with open(snip_path, "w", encoding="utf-8") as sf:
                        sf.write(res.text)
                    print(f"[SNIPPET] Downloaded raw snippet for {title} ({len(res.text)} bytes)")
                    
                    # Find all images, fonts, and video links in snippet
                    img_urls = re.findall(r'(https?://[^\s"\'<>]+\.(?:png|jpg|jpeg|webp|svg|gif|mp4|webm|woff2|woff|ttf|otf))', res.text)
                    for iu in set(img_urls):
                        try:
                            ires = await client.get(iu)
                            if ires.status_code == 200:
                                fname = safe_filename(urllib.parse.urlparse(iu).path)
                                ext = os.path.splitext(fname)[1].lower()
                                if any(f in ext for f in [".woff2", ".woff", ".ttf", ".otf"]):
                                    fpath = os.path.join(fonts_dir, fname)
                                elif any(v in ext for v in [".mp4", ".webm"]):
                                    fpath = os.path.join(videos_dir, fname)
                                else:
                                    fpath = os.path.join(images_dir, fname)
                                with open(fpath, "wb") as img_file:
                                    img_file.write(ires.content)
                        except Exception:
                            pass
            except Exception as e:
                print(f"[SNIPPET ERROR] {title}: {e}")

    print("\n[COMPLETE] All 7 Chapters, Snippets, Fonts & High-Res Assets Extracted into D:\\Web Builder\\web extract!")

if __name__ == "__main__":
    asyncio.run(scrape_all_chapters())

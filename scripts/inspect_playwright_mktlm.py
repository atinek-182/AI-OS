import asyncio
import json
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def inspect():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        network_urls = []
        page.on("response", lambda res: network_urls.append({
            "url": res.url,
            "status": res.status,
            "mime": res.headers.get("content-type", "")
        }))

        print("Navigating to https://mktlm.obys.agency/ ...", flush=True)
        await page.goto("https://mktlm.obys.agency/", wait_until="domcontentloaded", timeout=45000)
        print("DOM content loaded. Waiting 5 seconds...", flush=True)
        await asyncio.sleep(5)

        # Inspect window objects
        globals_info = await page.evaluate("""() => {
            const keys = Object.keys(window).filter(k => 
                k.toLowerCase().includes('ready') || 
                k.toLowerCase().includes('project') || 
                k.toLowerCase().includes('page') || 
                k.toLowerCase().includes('data') || 
                k.toLowerCase().includes('rm') || 
                k.toLowerCase().includes('gsap') || 
                k.toLowerCase().includes('three') || 
                k.toLowerCase().includes('lenis') ||
                k.toLowerCase().includes('scroll')
            );
            
            const results = {};
            for (let k of keys) {
                try {
                    const val = window[k];
                    if (typeof val === 'object' && val !== null) {
                        results[k] = JSON.stringify(val).slice(0, 500);
                    } else {
                        results[k] = String(val);
                    }
                } catch(e) {
                    results[k] = '[Unserializable]';
                }
            }
            return {
                matchedKeys: keys,
                details: results,
                title: document.title,
                bodyClasses: document.body.className,
                numWidgets: document.querySelectorAll('[class*="widget"], [class*="rm-"]').length,
                canvasCount: document.querySelectorAll('canvas').length,
                videoCount: document.querySelectorAll('video').length,
                audioCount: document.querySelectorAll('audio').length,
                svgCount: document.querySelectorAll('svg').length,
                allClasses: Array.from(new Set(Array.from(document.querySelectorAll('*')).flatMap(el => Array.from(el.classList)))).slice(0, 50)
            };
        }""")

        print("GLOBALS & DOM INFO:", flush=True)
        print(json.dumps(globals_info, indent=2), flush=True)

        # Check Readymag internal project configuration
        rm_info = await page.evaluate("""() => {
            let res = {};
            if (window.rm) {
                res.hasRm = true;
                res.rmKeys = Object.keys(window.rm);
                if (window.rm.data) {
                    res.dataKeys = Object.keys(window.rm.data);
                    if (window.rm.data.project) {
                        res.project = window.rm.data.project;
                    }
                    if (window.rm.data.pages) {
                        res.pages = window.rm.data.pages;
                    }
                }
            }
            // Check scripts for embedded JSON
            const scripts = Array.from(document.querySelectorAll('script'));
            const embeddedData = [];
            scripts.forEach((s, idx) => {
                if (s.textContent && (s.textContent.includes('project') || s.textContent.includes('widgets') || s.textContent.includes('animation'))) {
                    embeddedData.push({
                        idx,
                        length: s.textContent.length,
                        preview: s.textContent.slice(0, 300)
                    });
                }
            });
            res.embeddedData = embeddedData;
            return res;
        }""")

        print("\nREADYMAG DETAILED INFO:", flush=True)
        print(json.dumps(rm_info, indent=2, default=str)[:3000], flush=True)

        print("\nNETWORK CAPTURED URLS (sample):", flush=True)
        for req in network_urls[:40]:
            print(f"[{req['status']}] {req['mime']} -> {req['url']}", flush=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect())

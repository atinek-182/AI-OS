import asyncio
import json
import sys
import os
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

PAGES = [
    {"num_id": 14738159, "title": "Intro", "paths": ["/", "/intro", "/14738159", "/1"]},
    {"num_id": 14679312, "title": "Roma", "paths": ["/roma", "/14679312", "/2"]},
    {"num_id": 14655040, "title": "Olia", "paths": ["/olia", "/14655040", "/3"]},
    {"num_id": 14644555, "title": "Slava", "paths": ["/slava", "/14644555", "/4"]},
    {"num_id": 14711575, "title": "Kostya", "paths": ["/kostya", "/14711575", "/5"]},
    {"num_id": 14721913, "title": "outro", "paths": ["/outro", "/14721913", "/6"]},
]

async def check_routes():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        # Go to root
        await page.goto("https://mktlm.obys.agency/", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(4)

        # Inspect navigation links or page switching mechanism in Readymag viewer
        nav_info = await page.evaluate("""() => {
            const mag = window.ServerData?.mags?.mag;
            const pages = mag?.pages || [];
            
            // Check if RM viewer has navigation methods
            const rmViewer = window.RM;
            
            // Check all anchor links on DOM
            const anchors = Array.from(document.querySelectorAll('a')).map(a => ({
                href: a.href,
                text: a.innerText.trim(),
                target: a.target
            }));
            
            return {
                pages: pages.map(p => ({
                    num_id: p.num_id,
                    title: p.title,
                    url: p.url,
                    alias: p.alias,
                    name: p.name,
                    order: p.order,
                    height: p.height
                })),
                anchors: anchors.slice(0, 30)
            };
        }""")

        print("PAGES DETAILED METADATA:", flush=True)
        print(json.dumps(nav_info, indent=2), flush=True)

        # Test each route in browser
        for p_item in PAGES:
            for path in p_item["paths"]:
                test_url = f"https://mktlm.obys.agency{path}"
                try:
                    res = await page.goto(test_url, wait_until="domcontentloaded", timeout=15000)
                    await asyncio.sleep(2)
                    status = res.status if res else 0
                    doc_title = await page.title()
                    current_url = page.url
                    num_widgets = await page.evaluate("() => document.querySelectorAll('[class*=\"widget\"]').length")
                    print(f"Path: {path:<12} -> Status: {status} | Final URL: {current_url} | Title: {doc_title} | Widgets: {num_widgets}", flush=True)
                except Exception as e:
                    print(f"Path: {path:<12} -> Error: {e}", flush=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(check_routes())

import asyncio
import json
import sys
import os
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

async def extract_server_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        
        await page.goto("https://mktlm.obys.agency/", wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(5)

        server_data = await page.evaluate("() => window.ServerData || null")
        
        if server_data:
            print("ServerData found! Keys:", list(server_data.keys()), flush=True)
            mag = server_data.get("mags", {}).get("mag", {})
            pages = mag.get("pages", [])
            print(f"Total Pages: {len(pages)}", flush=True)
            for idx, p_info in enumerate(pages):
                print(f"--- PAGE #{idx+1} ---", flush=True)
                print(f"ID: {p_info.get('id')} | Num ID: {p_info.get('num_id')}", flush=True)
                print(f"URL: {p_info.get('url')} | Title: {p_info.get('title')} | Name: {p_info.get('name')}", flush=True)
                print(f"Height: {p_info.get('height')} | Mobile Height: {p_info.get('phoneHeight')}", flush=True)
                widgets = p_info.get("widgets", {})
                if isinstance(widgets, dict):
                    print(f"Widgets count: {len(widgets)}", flush=True)
                elif isinstance(widgets, list):
                    print(f"Widgets list count: {len(widgets)}", flush=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(extract_server_data())

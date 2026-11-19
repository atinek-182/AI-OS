import os
import sys
import json
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def inspect_codrops():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto("https://tympanus.net/codrops/tag/case-study/", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(3000)
        
        info = page.evaluate('''() => {
            let links = Array.from(document.querySelectorAll('a')).map(a => ({
                href: a.href,
                text: a.innerText.trim(),
                className: a.className,
                parentClass: a.parentElement ? a.parentElement.className : ''
            }));
            
            let headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, .ct-card__title, .entry-title')).map(h => ({
                tag: h.tagName,
                text: h.innerText.trim(),
                className: h.className
            }));
            
            return { links: links.slice(0, 100), headings: headings.slice(0, 100) };
        }''')
        
        with open(r"d:\AI-OS\scratch\codrops_dom_debug.json", "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2)
            
        print("[SUCCESS] Dumped Codrops DOM debug to d:\\AI-OS\\scratch\\codrops_dom_debug.json")
        browser.close()

if __name__ == "__main__":
    inspect_codrops()

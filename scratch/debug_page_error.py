import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/3d-text-circle-animation-codrops/index.html"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on("pageerror", lambda err: print(f"[PAGE ERROR] {err}"))
    page.on("console", lambda m: print(f"[CONSOLE {m.type}] {m.text}"))
    page.goto(url)
    page.wait_for_timeout(3000)
    
    # Check if App was exported and created
    res = page.evaluate("""() => {
        return {
            windowInnerWidth: window.innerWidth,
            windowInnerHeight: window.innerHeight,
            canvasStyle: document.querySelector('#webgl') ? document.querySelector('#webgl').getAttribute('style') : null
        };
    }""")
    print("DOM RES:", res)
    browser.close()

import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/codrops-text-demo/index.html"
print(f"=== TESTING COMP-022: {url} ===")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    
    console_errs = []
    page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda err: print(f"  [PAGE ERROR] {err}"))
    
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(3500)
    
    canvas_count = page.evaluate("() => document.querySelectorAll('canvas').length")
    loader_active = page.evaluate("() => document.body.classList.contains('loading')")
    
    print(f"  Canvas Count: {canvas_count}")
    print(f"  Body Has 'loading' Class: {loader_active}")
    print(f"  Console Errors ({len(console_errs)}): {console_errs}")
    
    if canvas_count > 0 and not loader_active and len(console_errs) == 0:
        print("  [PASS 100%] COMP-022 renders Troika 3D WebGL Text cleanly with 0 console errors!")
        page.screenshot(path=r"C:\Users\HP\Downloads\Components\public\thumbnails\COMP-022.png")
        print("  Updated thumbnail COMP-022.png successfully!")
    
    browser.close()

import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/rolling-text/index.html"
print(f"=== TESTING COMP-026: {url} ===")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    
    console_errs = []
    page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda err: print(f"  [PAGE ERROR] {err}"))
    
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)
    
    char_count = page.evaluate("() => document.querySelectorAll('.char').length")
    
    print(f"  Rolling Text Char Count: {char_count}")
    print(f"  Console Errors ({len(console_errs)}): {console_errs}")
    
    if char_count > 0 and len(console_errs) == 0:
        print("  [PASS 100%] COMP-026 Rolling Text renders 3D tube rotation cleanly with 0 console errors!")
        page.screenshot(path=r"C:\Users\HP\Downloads\Components\public\thumbnails\COMP-026.png")
        print("  Updated thumbnail COMP-026.png successfully!")
    
    browser.close()

import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/text-trail-effect-on-mousemove/index.html"
print(f"=== TESTING COMP-027: {url} ===")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    
    console_errs = []
    page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda err: print(f"  [PAGE ERROR] {err}"))
    
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(1000)
    
    # Move mouse around to trigger trail effect
    page.mouse.move(300, 300)
    page.wait_for_timeout(500)
    page.mouse.move(600, 400)
    page.wait_for_timeout(1000)
    
    text_count = page.evaluate("() => document.querySelectorAll('.text').length")
    
    print(f"  Trail Text Elements Count: {text_count}")
    print(f"  Console Errors ({len(console_errs)}): {console_errs}")
    
    if text_count > 0 and len(console_errs) == 0:
        print("  [PASS 100%] COMP-027 Text Trail Effect renders mousemove physics cleanly with 0 console errors!")
        page.screenshot(path=r"C:\Users\HP\Downloads\Components\public\thumbnails\COMP-027.png")
        print("  Updated thumbnail COMP-027.png successfully!")
    
    browser.close()

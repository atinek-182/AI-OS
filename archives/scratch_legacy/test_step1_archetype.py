import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TEST_URLS = [
    ("COMP-023", "http://127.0.0.1:8080/01-text-and-typography/codrops-tutorial-text-animation/index.html"),
    ("COMP-086", "http://127.0.0.1:8080/04-images-galleries-and-sliders/horizontal-parallax-gallery-codrops/index.html")
]

print("=== STEP 1 ARCHETYPE VERIFICATION (Server MIME & Public Asset Fallback) ===")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    for comp_id, url in TEST_URLS:
        console_errs = []
        network_404s = []

        page.on("console", lambda m: console_errs.append(m.text) if m.type == "error" else None)
        page.on("response", lambda r: network_404s.append(r.url) if r.status >= 404 else None)

        print(f"\nTesting {comp_id}: {url}")
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(2500)

        loader_visible = page.evaluate("() => document.body.classList.contains('loading')")
        canvas_count = page.evaluate("() => document.querySelectorAll('canvas').length")

        print(f"  Body Still Has 'loading' Class: {loader_visible}")
        print(f"  Canvas Count: {canvas_count}")
        print(f"  Console Errors ({len(console_errs)}): {console_errs[:2]}")
        print(f"  Network 404s ({len(network_404s)}): {network_404s[:2]}")

        if not loader_visible and len(network_404s) == 0:
            print(f"  [SUCCESS] {comp_id} loaded 100% cleanly without loader deadlock or 404s!")
        else:
            print(f"  [PENDING] Needs next archetype fix.")

    browser.close()

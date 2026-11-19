import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/3d-text-circle-animation-codrops/index.html"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on("console", lambda m: print(f"[CONSOLE {m.type}] {m.text}"))
    page.on("response", lambda r: print(f"[HTTP {r.status}] {r.url}") if r.status >= 400 else None)
    page.goto(url)
    page.wait_for_timeout(3000)
    browser.close()

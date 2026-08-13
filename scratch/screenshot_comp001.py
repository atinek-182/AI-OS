import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/3d-text-circle-animation-codrops/index.html"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    page.goto(url)
    page.wait_for_timeout(3000)
    page.screenshot(path=r"C:\Users\HP\Downloads\Components\public\thumbnails\COMP-001.png")
    print("Screenshot saved to COMP-001.png successfully!")
    browser.close()

import os
import sys
import json
from playwright.sync_api import sync_playwright

# Standard UTF-8 output encoding for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\HP\Downloads\Components"
REGISTRY_PATH = os.path.join(BASE_DIR, "components_ai_registry.json")

TARGET_COMPS = [
    "COMP-023", "COMP-024", "COMP-025", "COMP-067", "COMP-080", "COMP-081",
    "COMP-086", "COMP-093", "COMP-110", "COMP-111", "COMP-121", "COMP-130",
    "COMP-137", "COMP-146", "COMP-151", "COMP-154", "COMP-174"
]

with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    registry = json.load(f)

comp_map = {item["id"]: item for item in registry}

print("==================================================")
print("INDIVIDUAL COMPONENT DEEP PLAYWRIGHT DIAGNOSTIC")
print("==================================================")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    for comp_id in TARGET_COMPS:
        comp = comp_map.get(comp_id)
        if not comp or not comp.get("entry_url"):
            print(f"\n[{comp_id}] NO ENTRY URL FOUND")
            continue

        url = f"http://127.0.0.1:8080/{comp['entry_url']}"
        console_logs = []
        network_errors = []

        def handle_console(msg):
            if msg.type in ("error", "warning"):
                console_logs.append(f"[{msg.type.upper()}] {msg.text}")

        def handle_response(response):
            if response.status >= 400:
                network_errors.append(f"[{response.status}] {response.url}")

        page.on("console", handle_console)
        page.on("response", handle_response)

        print(f"\n--------------------------------------------------")
        print(f"DIAGNOSING {comp_id}: {comp['name']}")
        print(f"URL: {url}")

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=10000)
            page.wait_for_timeout(2000)

            # DOM Inspection
            body_class = page.evaluate("document.body ? document.body.className : ''")
            canvas_count = page.evaluate("document.querySelectorAll('canvas').length")
            has_webgl = page.evaluate("""() => {
                const c = document.createElement('canvas');
                return !!(window.WebGLRenderingContext && (c.getContext('webgl') || c.getContext('experimental-webgl')));
            }""")
            
            # Check visible text / loader elements
            loader_elements = page.evaluate("""() => {
                const els = document.querySelectorAll('.loading, .preloader, .loader, #loader, #preloader');
                return Array.from(els).map(e => ({
                    tag: e.tagName,
                    class: e.className,
                    display: getComputedStyle(e).display,
                    opacity: getComputedStyle(e).opacity,
                    visibility: getComputedStyle(e).visibility
                }));
            }""")

            print(f"  Body Class: '{body_class}'")
            print(f"  Canvas Elements in DOM: {canvas_count}")
            print(f"  WebGL Supported: {has_webgl}")
            print(f"  Loader Elements Info: {json.dumps(loader_elements)}")

            if console_logs:
                print("  Console Errors/Warnings:")
                for log in console_logs[:5]:
                    print(f"    └─ {log[:120]}")
            else:
                print("  Console Errors: None")

            if network_errors:
                print("  Network 404/Failures:")
                for net in network_errors[:5]:
                    print(f"    └─ {net}")
            else:
                print("  Network Failures: None")

        except Exception as e:
            print(f"  [PAGE LOAD FAILED] {str(e)[:150]}")

        page.remove_listener("console", handle_console)
        page.remove_listener("response", handle_response)

    browser.close()

print("\n==================================================")
print("DIAGNOSTIC SWEEP COMPLETE")
print("==================================================")

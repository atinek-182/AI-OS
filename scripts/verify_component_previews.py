import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

# Standard UTF-8 output encoding for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\HP\Downloads\Components"
REGISTRY_PATH = os.path.join(BASE_DIR, "components_ai_registry.json")
THUMBNAILS_DIR = os.path.join(BASE_DIR, "public", "thumbnails")

os.makedirs(THUMBNAILS_DIR, exist_ok=True)

def verify_and_capture():
    if not os.path.exists(REGISTRY_PATH):
        print("[ERROR] components_ai_registry.json not found!")
        sys.exit(1)
        
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)
        
    print(f"[PLAYWRIGHT VERIFIER] Loaded {len(registry)} components from registry.")
    print("[PLAYWRIGHT VERIFIER] Starting Chromium headless browser sweep...")
    
    clean_count = 0
    warning_count = 0
    skipped_count = 0
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        
        for idx, comp in enumerate(registry, 1):
            comp_id = comp["id"]
            entry_url = comp["entry_url"]
            name = comp["name"]
            thumbnail_path = os.path.join(THUMBNAILS_DIR, f"{comp_id}.png")
            
            if not entry_url:
                print(f"[{idx}/{len(registry)}] [SKIP {comp_id}] {name} — Requires NPM Build.")
                comp["health_status"] = "NPM BUILD REQD"
                comp["health_note"] = "Build-dependent repository. Requires npm install & dev server."
                skipped_count += 1
                continue
                
            full_url = f"http://127.0.0.1:8080/{entry_url}"
            page_errors = []
            console_errors = []
            
            page.on("pageerror", lambda err: page_errors.append(str(err)))
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            
            try:
                print(f"[{idx}/{len(registry)}] [CHECKING {comp_id}] {name} -> http://127.0.0.1:8080/{entry_url}")
                page.goto(full_url, wait_until="domcontentloaded", timeout=12000)
                
                # User Requirement Q3: Explicit 3.0-second delay for WebGL / Canvas / GSAP animation initialization
                page.wait_for_timeout(3000)
                
                # Capture PNG screenshot
                page.screenshot(path=thumbnail_path, full_page=False)
                
                if page_errors:
                    err_msg = page_errors[0][:120].replace("\n", " ")
                    print(f"   └─ [JS WARNING] {err_msg}")
                    comp["health_status"] = "WARN"
                    comp["health_note"] = f"JS Warning: {err_msg}"
                    warning_count += 1
                else:
                    comp["health_status"] = "PASS 100%"
                    comp["health_note"] = "100% Clean Load (3.0s visual sweep verification)"
                    clean_count += 1
                    
            except Exception as e:
                err_str = str(e)[:120].replace("\n", " ")
                print(f"   └─ [LOAD FAILURE] {err_str}")
                comp["health_status"] = "FAIL"
                comp["health_note"] = f"Load Failed: {err_str}"
                warning_count += 1
                
        browser.close()
        
    # Save updated registry with health notes
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
        
    print("\n==================================================")
    print(f"[VERIFICATION SWEEP COMPLETE]")
    print(f"Total Components: {len(registry)}")
    print(f"Clean 100% Passes: {clean_count}")
    print(f"JS Warnings / Load Failures: {warning_count}")
    print(f"Build-Dependent Skipped (NPM Reqd): {skipped_count}")
    print(f"Thumbnails Directory: {THUMBNAILS_DIR}")
    print("==================================================\n")

if __name__ == "__main__":
    verify_and_capture()

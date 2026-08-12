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

TARGET_IDS = [
    "COMP-001", "COMP-021", "COMP-022", "COMP-023", "COMP-024", "COMP-025", "COMP-029",
    "COMP-044", "COMP-054", "COMP-055", "COMP-056", "COMP-067", "COMP-080", "COMP-081",
    "COMP-082", "COMP-083", "COMP-084", "COMP-086", "COMP-089", "COMP-092", "COMP-093",
    "COMP-095", "COMP-096", "COMP-109", "COMP-110", "COMP-111", "COMP-117", "COMP-121",
    "COMP-122", "COMP-128", "COMP-130", "COMP-132", "COMP-133", "COMP-135", "COMP-137",
    "COMP-138", "COMP-140", "COMP-141", "COMP-142", "COMP-144", "COMP-146", "COMP-147",
    "COMP-148", "COMP-149", "COMP-150", "COMP-151", "COMP-154", "COMP-158", "COMP-160",
    "COMP-163", "COMP-166", "COMP-173", "COMP-174"
]

def capture_target_screenshots():
    if not os.path.exists(REGISTRY_PATH):
        print("[ERROR] components_ai_registry.json missing!")
        sys.exit(1)
        
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)
        
    target_items = [comp for comp in registry if comp["id"] in TARGET_IDS]
    print(f"[PLAYWRIGHT TARGET SWEEP] Loaded {len(target_items)} target components for screenshot capture.")
    
    clean_pass = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()
        
        for idx, comp in enumerate(target_items, 1):
            comp_id = comp["id"]
            entry_url = comp["entry_url"]
            name = comp["name"]
            thumbnail_path = os.path.join(THUMBNAILS_DIR, f"{comp_id}.png")
            
            if not entry_url:
                print(f"[{idx}/{len(target_items)}] [{comp_id}] {name} — Skipped (No Static Entry).")
                continue
                
            full_url = f"http://127.0.0.1:8080/{entry_url}"
            try:
                print(f"[{idx}/{len(target_items)}] [{comp_id}] Navigating to http://127.0.0.1:8080/{entry_url}")
                page.goto(full_url, wait_until="domcontentloaded", timeout=12000)
                
                # Explicit 3.0s render delay
                page.wait_for_timeout(3000)
                
                page.screenshot(path=thumbnail_path, full_page=False)
                print(f"  └─ Captured PNG thumbnail for {comp_id}")
                clean_pass += 1
            except Exception as e:
                print(f"  └─ [ERROR {comp_id}] {str(e)[:100]}")
                
        browser.close()
        
    print(f"\n==================================================")
    print(f"[TARGET SCREENSHOT SWEEP COMPLETE] Captures: {clean_pass}/{len(target_items)}")
    print("==================================================\n")

if __name__ == "__main__":
    capture_target_screenshots()

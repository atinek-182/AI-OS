import os
import sys
import time
from playwright.sync_api import sync_playwright

AIOS_ROOT = r"d:\AI-OS"
GRAPH_PATH = os.path.join(AIOS_ROOT, "graphify-out", "graph.html")
ASSETS_DIR = os.path.join(AIOS_ROOT, "docs", "assets")
OUTPUT_PNG = os.path.join(ASSETS_DIR, "aios-knowledge-graph.png")
OUTPUT_ZOOMED_PNG = os.path.join(ASSETS_DIR, "aios-knowledge-graph-zoomed.png")

os.makedirs(ASSETS_DIR, exist_ok=True)

def capture_graph():
    print(f"[CAPTURE] Loading Graphify graph from {GRAPH_PATH}...")
    file_url = "file:///" + GRAPH_PATH.replace("\\", "/")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 1920x1080 resolution
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        page.goto(file_url, wait_until="networkidle")
        print("[CAPTURE] Page loaded. Waiting 6 seconds for physics stabilization...")
        time.sleep(6)
        
        # Take full screen overview
        page.screenshot(path=OUTPUT_PNG, full_page=False)
        print(f"[CAPTURE] Saved full overview screenshot to {OUTPUT_PNG}")
        
        # Click on canvas or zoom in slightly if possible
        try:
            # Let's inspect or zoom via vis-network API if available, or take screenshot of canvas element
            canvas = page.locator("#graph")
            if canvas.count() > 0:
                print("[CAPTURE] Focusing on graph canvas...")
        except Exception as e:
            print(f"[WARN] Zoom operation: {e}")
            
        browser.close()
        print("[CAPTURE] Done.")

if __name__ == "__main__":
    capture_graph()

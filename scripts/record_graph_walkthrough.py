import os
import time
from playwright.sync_api import sync_playwright

AIOS_ROOT = r"d:\AI-OS"
GRAPH_PATH = os.path.join(AIOS_ROOT, "graphify-out", "graph.html")
ASSETS_DIR = os.path.join(AIOS_ROOT, "docs", "assets")
VIDEO_TEMP_DIR = os.path.join(ASSETS_DIR, "video_temp")

os.makedirs(VIDEO_TEMP_DIR, exist_ok=True)

def record_walkthrough():
    print("[RECORD] Starting Playwright video recording...")
    file_url = "file:///" + GRAPH_PATH.replace("\\", "/")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir=VIDEO_TEMP_DIR,
            record_video_size={"width": 1280, "height": 720}
        )
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle")
        time.sleep(3)
        
        # Interact with canvas - pan/drag
        canvas = page.locator("#graph")
        box = canvas.bounding_box()
        if box:
            center_x = box["x"] + box["width"] / 2
            center_y = box["y"] + box["height"] / 2
            page.mouse.move(center_x, center_y)
            page.mouse.down()
            page.mouse.move(center_x + 150, center_y + 100, steps=15)
            page.mouse.up()
            time.sleep(1.5)
            
        # Type into search input
        search_box = page.locator("#search")
        if search_box.count() > 0:
            search_box.fill("skills")
            time.sleep(2)
            # Select first search result if available
            first_res = page.locator(".search-item").first
            if first_res.count() > 0:
                first_res.click()
                time.sleep(2)
                
        # Close page to flush video
        video_path = page.video.path()
        page.close()
        context.close()
        browser.close()
        
        # Rename output video to aios-graph-demo.webm
        target_video = os.path.join(ASSETS_DIR, "aios-graph-demo.webm")
        if os.path.exists(target_video):
            os.remove(target_video)
        if os.path.exists(video_path):
            os.rename(video_path, target_video)
            print(f"[RECORD] Video saved successfully to {target_video}")
            
    # Clean temp dir
    try:
        os.rmdir(VIDEO_TEMP_DIR)
    except:
        pass

if __name__ == "__main__":
    record_walkthrough()

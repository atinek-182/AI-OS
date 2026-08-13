import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = "http://127.0.0.1:8080/01-text-and-typography/3d-text-circle-animation-codrops/index.html"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.on("console", lambda m: print(f"[CONSOLE {m.type}] {m.text}"))
    page.goto(url)
    page.wait_for_timeout(3000)
    
    # Inspect window.App or Three.js scene
    info = page.evaluate("""() => {
        const canvas = document.querySelector('#webgl');
        const gl = canvas ? canvas.getContext('webgl') || canvas.getContext('experimental-webgl') : null;
        return {
            canvasExists: !!canvas,
            canvasWidth: canvas ? canvas.width : 0,
            canvasHeight: canvas ? canvas.height : 0,
            webglContext: !!gl,
            glError: gl ? gl.getError() : null
        };
    }""")
    print("INSPECT INFO:", info)
    browser.close()

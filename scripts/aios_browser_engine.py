"""ZORIXEL AIOS Unified Browser Engine & Playwright Helpers.

Extracted & adapted architectural patterns from browser-use/browser-harness:
1. fill_framework_input: React/Vue controlled input value prototype setter + synthetic event dispatch.
2. get_domain_skills: Hostname-based domain skill auto-resolution.
3. capture_debug_click: Visual click target crosshair/circle overlay on Playwright screenshot artifacts.
4. setup_dialog_handler: Non-blocking CDP JavaScript dialog interceptor.
"""

import sys
import os
import json
import urllib.parse
from pathlib import Path

# Ensure UTF-8 output encoding on Windows OS
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Base workspace directory
WORKSPACE_DIR = Path(__file__).resolve().parent.parent
DOMAIN_SKILLS_DIR = WORKSPACE_DIR / ".agents" / "skills" / "domain-skills"


def fill_framework_input_js(selector: str, text: str, clear_first: bool = True) -> str:
    """Generates pure JS to inject text into React/Vue/Ember controlled input elements

    and dispatch synthetic input+change events so internal framework state updates.
    """
    clean_selector = json.dumps(selector)
    clean_text = json.dumps(text)
    clear_code = "el.value = '';" if clear_first else ""

    return f"""
    (() => {{
        const el = document.querySelector({clean_selector});
        if (!el) return false;

        el.focus();
        {clear_code}

        const valueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value')?.set
            || Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value')?.set;

        if (valueSetter) {{
            valueSetter.call(el, {clean_text});
        }} else {{
            el.value = {clean_text};
        }}

        el.dispatchEvent(new Event('input', {{ bubbles: true }}));
        el.dispatchEvent(new Event('change', {{ bubbles: true }}));
        el.dispatchEvent(new KeyboardEvent('keydown', {{ bubbles: true, key: 'Enter' }}));
        el.dispatchEvent(new KeyboardEvent('keyup', {{ bubbles: true, key: 'Enter' }}));
        return true;
    }})()
    """


def get_domain_skills(url: str) -> list[dict]:
    """Scans .agents/skills/domain-skills/<hostname>/ for pre-recorded site SOPs

    and CSS selector maps based on target URL domain.
    """
    parsed = urllib.parse.urlparse(url)
    hostname = (parsed.hostname or "").lower().removeprefix("www.")
    if not hostname:
        return []

    domain_parts = hostname.split(".")
    domain_slug = domain_parts[0] if len(domain_parts) > 1 else hostname

    matched_skills = []
    target_dir = DOMAIN_SKILLS_DIR / domain_slug

    if target_dir.is_dir():
        for skill_file in target_dir.glob("*.md"):
            try:
                content = skill_file.read_text(encoding="utf-8")
                matched_skills.append({
                    "domain": domain_slug,
                    "filename": skill_file.name,
                    "path": str(skill_file),
                    "content": content
                })
            except Exception as e:
                sys.stderr.write(f"[WARN] Failed to read domain skill {skill_file}: {e}\n")

    return matched_skills


def setup_dialog_handler(page) -> list[dict]:
    """Attaches a non-blocking dialog handler to Playwright page context to record

    and handle native alert/confirm/prompt popups without freezing execution threads.
    """
    recorded_dialogs = []

    def on_dialog(dialog):
        recorded_dialogs.append({
            "type": dialog.type,
            "message": dialog.message,
            "default_value": dialog.default_value
        })
        dialog.accept()

    page.on("dialog", on_dialog)
    return recorded_dialogs


def capture_debug_click(image_path: str, x: int, y: int, output_path: str = None) -> str:
    """Draws a red crosshair and target circle at (x, y) coordinates on screenshot image."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        sys.stderr.write("[WARN] PIL/Pillow not installed. Skipping visual debug click overlay.\n")
        return image_path

    if not output_path:
        output_path = image_path

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    r = 15
    draw.ellipse([x - r, y - r, x + r, y + r], outline="red", width=3)
    draw.line([x - r - 5, y, x + r + 5, y], fill="red", width=2)
    draw.line([x, y - r - 5, x, y + r + 5], fill="red", width=2)

    img.save(output_path)
    return output_path


def run_tests():
    """Empirical verification test suite for AI-OS Browser Engine."""
    print("=== AIOS BROWSER ENGINE EMPIRICAL TESTS ===")

    # Test 1: JS Input Code Generation
    js_code = fill_framework_input_js("#search-bar", "zorixel ai agency")
    assert "Object.getOwnPropertyDescriptor" in js_code
    assert "zorixel ai agency" in js_code
    print("[OK] Test 1 Passed: Framework input JS snippet generated cleanly.")

    # Test 2: Domain Skills Lookup
    dummy_dir = DOMAIN_SKILLS_DIR / "example"
    dummy_dir.mkdir(parents=True, exist_ok=True)
    dummy_file = dummy_dir / "SOP.md"
    dummy_file.write_text("# Example Site SOP\nUse #login-btn for authorization.", encoding="utf-8")

    skills = get_domain_skills("https://example.com/dashboard")
    assert len(skills) > 0
    assert skills[0]["domain"] == "example"
    assert "login-btn" in skills[0]["content"]
    print("[OK] Test 2 Passed: Domain skill resolution successfully matched domain.")

    # Clean up test file
    dummy_file.unlink()
    dummy_dir.rmdir()

    print("[SUCCESS] All AI-OS Browser Engine unit tests passed successfully!")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        print("AIOS Browser Engine Utility loaded. Run with --test to verify.")

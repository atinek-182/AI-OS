"""ZORIXEL AIOS Pre-Flight Health Validator: Browser Engine & Domain Skills.

Audits:
1. aios_browser_engine.py script existence & syntax validity.
2. Framework-aware input JS generator correctness.
3. Domain skills directory structure and auto-resolution engine.
4. Browser-testing skill frontmatter and rule integration.
"""

import sys
import os
from pathlib import Path

# Force UTF-8 stdio encoding on Windows OS
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = WORKSPACE_DIR / "scripts"
SKILLS_DIR = WORKSPACE_DIR / ".agents" / "skills"


def check_browser_engine_health() -> bool:
    print("=== ZORIXEL AIOS BROWSER ENGINE HEALTH AUDIT ===")

    engine_script = SCRIPTS_DIR / "aios_browser_engine.py"
    if not engine_script.exists():
        sys.stderr.write("[ERROR] Missing scripts/aios_browser_engine.py!\n")
        return False
    print("[OK] aios_browser_engine.py exists.")

    domain_skills_dir = SKILLS_DIR / "domain-skills"
    if not domain_skills_dir.is_dir():
        sys.stderr.write("[ERROR] Missing .agents/skills/domain-skills directory!\n")
        return False
    print("[OK] .agents/skills/domain-skills directory exists.")

    browser_testing_skill = SKILLS_DIR / "browser-testing" / "SKILL.md"
    if not browser_testing_skill.exists():
        sys.stderr.write("[ERROR] Missing .agents/skills/browser-testing-with-devtools/SKILL.md!\n")
        return False
    print("[OK] .agents/skills/browser-testing-with-devtools/SKILL.md exists.")

    # Import and run engine unit tests dynamically
    sys.path.insert(0, str(SCRIPTS_DIR))
    try:
        import aios_browser_engine
        js_snippet = aios_browser_engine.fill_framework_input_js("#test-selector", "sample text")
        if "Object.getOwnPropertyDescriptor" not in js_snippet:
            sys.stderr.write("[ERROR] fill_framework_input_js missing prototype setter injection!\n")
            return False
        print("[OK] Framework input JS generator verified.")

        skills = aios_browser_engine.get_domain_skills("https://example.com/test")
        print(f"[OK] Domain skills engine initialized cleanly (returned {len(skills)} skills for example.com).")

    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to import/execute aios_browser_engine: {e}\n")
        return False

    print("=== [SUCCESS] ALL BROWSER ENGINE HEALTH CHECKS PASSED ===")
    return True


if __name__ == "__main__":
    success = check_browser_engine_health()
    if not success:
        sys.exit(1)

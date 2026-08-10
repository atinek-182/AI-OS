import os
import sys
import json

# Ensure UTF-8 output encoding for Windows compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_PATH = os.path.join(WORKSPACE_ROOT, ".agents", "skills", "loop-engine", "SKILL.md")
LOOPS_PATH = os.path.join(WORKSPACE_ROOT, "LOOPS.md")
AWWWARDS_SKILL_PATH = os.path.join(WORKSPACE_ROOT, ".agents", "skills", "website-design-engine", "SKILL.md")
AWWWARDS_GUIDE_PATH = os.path.join(WORKSPACE_ROOT, "references", "AWWWARDS-MASTER-CREATION-GUIDE.md")
RESEARCH_VAULT_DIR = os.path.join(WORKSPACE_ROOT, "references", "awwwards-research-vault")

def test_loop_engine_health():
    print("=== ZORIXEL AIOS LOOP ENGINE PRE-FLIGHT HEALTH TEST ===")
    errors = []
    
    # 1. Test Loop Engine Skill Existence
    if not os.path.exists(SKILL_PATH):
        errors.append(f"Missing skill file: {SKILL_PATH}")
    else:
        with open(SKILL_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            if "Observe" not in content or "Verify" not in content or "--dynamic" not in content:
                errors.append("Loop Engine SKILL.md missing core 6-phase cycle or --dynamic flag.")
            else:
                print("[OK] Loop Engine skill file validated (.agents/skills/loop-engine/SKILL.md).")
                
    # 2. Test LOOPS.md Registry
    if not os.path.exists(LOOPS_PATH):
        errors.append(f"Missing master registry: {LOOPS_PATH}")
    else:
        with open(LOOPS_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            if "tdd-sweep" not in content or "visual-qa" not in content:
                errors.append("LOOPS.md missing baseline playbooks.")
            else:
                print("[OK] Workspace LOOPS.md master registry validated.")

    # 3. Test Website Design Engine v5.1 Skill
    if not os.path.exists(AWWWARDS_SKILL_PATH):
        errors.append(f"Missing website design engine skill file: {AWWWARDS_SKILL_PATH}")
    else:
        with open(AWWWARDS_SKILL_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            if "C:\\Users\\HP\\Downloads\\Components" not in content or "Human-in-the-Loop" not in content:
                errors.append("Website Design Engine SKILL.md missing Awwwards vault index or Human-in-the-Loop gate.")
            else:
                print("[OK] Website Design Engine v5.1 skill file validated.")

    # 4. Test Awwwards Master Creation Guide
    if not os.path.exists(AWWWARDS_GUIDE_PATH):
        errors.append(f"Missing Awwwards Master Guide: {AWWWARDS_GUIDE_PATH}")
    else:
        print("[OK] Awwwards Master Creation Guide validated.")

    # 5. Test Research Vault Documents
    if not os.path.exists(RESEARCH_VAULT_DIR):
        errors.append(f"Missing research vault directory: {RESEARCH_VAULT_DIR}")
    else:
        vault_files = os.listdir(RESEARCH_VAULT_DIR)
        if len(vault_files) < 7:
            errors.append(f"Research vault incomplete: expected 7 files, found {len(vault_files)}")
        else:
            print(f"[OK] Awwwards Research Vault validated ({len(vault_files)} files present).")

    # Output Final Test Results
    if errors:
        print("\n[ERROR] Health Check Failed with the following errors:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n[SUCCESS] ALL LOOP ENGINE & AWWWARDS VAULT HEALTH TESTS PASSED 100%!")
        return True

if __name__ == "__main__":
    success = test_loop_engine_health()
    if not success:
        sys.exit(1)

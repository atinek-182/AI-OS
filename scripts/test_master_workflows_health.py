import os
import sys
from pathlib import Path

# Force UTF-8 stdio encoding for Windows console output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def run_health_checks():
    print("========================================================")
    print("ZORIXEL AIOS: Master Workflows & n8n Health Validator")
    print("========================================================")
    
    workspace_root = Path(r"d:\AI-OS")
    errors = []

    # 1. Verify MW01 Master Blueprint File
    mw01_blueprint = workspace_root / ".agents" / "skills" / "domain-skills" / "workflows" / "MW01_zero_subscription_client_os.md"
    if not mw01_blueprint.exists():
        errors.append(f"MISSING: MW01 Master Blueprint at {mw01_blueprint}")
    else:
        content = mw01_blueprint.read_text(encoding='utf-8')
        if "MANDATORY GRILL-ME GATE" not in content:
            errors.append("MW01 Blueprint missing MANDATORY GRILL-ME GATE directive")
        if "MANDATORY ROAST GATE" not in content:
            errors.append("MW01 Blueprint missing MANDATORY ROAST GATE directive")
        if "MANDATORY BOOTUP CONTEXT READ" not in content:
            errors.append("MW01 Blueprint missing MANDATORY BOOTUP CONTEXT READ directive")
        print(f"[OK] Verified MW01 Master Blueprint ({len(content.splitlines())} lines)")

    # 2. Verify n8n Skill & Reference Files
    n8n_skill = workspace_root / ".agents" / "skills" / "n8n" / "SKILL.md"
    n8n_ref = workspace_root / ".agents" / "skills" / "n8n" / "references" / "n8n-nodes-guide.md"
    if not n8n_skill.exists():
        errors.append(f"MISSING: n8n Skill file at {n8n_skill}")
    else:
        print("[OK] Verified n8n Skill file")

    if not n8n_ref.exists():
        errors.append(f"MISSING: n8n Node Reference guide at {n8n_ref}")
    else:
        print("[OK] Verified n8n Node Reference guide")

    # 3. Verify LOOPS.md Master Registry Registration
    loops_file = workspace_root / "LOOPS.md"
    if not loops_file.exists():
        errors.append(f"MISSING: LOOPS.md at {loops_file}")
    else:
        loops_content = loops_file.read_text(encoding='utf-8')
        if "MW01-zero-subscription-client-os" not in loops_content:
            errors.append("LOOPS.md missing MW01-zero-subscription-client-os entry")
        print("[OK] Verified LOOPS.md Master Registry")

    # 4. Verify Master Brainstorm Log
    brainstorm_log = workspace_root / "brainstorms" / "2026-08-10-dynamic-skill-workflows-integration.md"
    if not brainstorm_log.exists():
        errors.append(f"MISSING: Brainstorm Log at {brainstorm_log}")
    else:
        print(f"[OK] Verified Brainstorm Log ({len(brainstorm_log.read_text(encoding='utf-8').splitlines())} lines)")

    print("========================================================")
    if errors:
        print(f"[FAIL] Health check failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("[SUCCESS] All Master Workflows & n8n Health Checks Passed (0 Errors)!")
        print("========================================================")

if __name__ == "__main__":
    run_health_checks()

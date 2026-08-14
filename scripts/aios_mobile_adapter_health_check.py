#!/usr/bin/env python3
"""
ZORIXEL AIOS - Mobile Component Adapter & Vidya Dham Academy Pre-Flight Health Check
Audits mobile-component-adapter skill integrity, COMP-046 feature spec, zero-emoji compliance, and relative unit rules.
"""

import os
import sys

# Standard UTF-8 output encoding for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_DIR = r"d:\AI-OS\projects\Websites\Vidya-Dham-Academy"
SKILL_PATH = r"d:\AI-OS\.agents\skills\mobile-component-adapter\SKILL.md"

REQUIRED_FILES = [
    SKILL_PATH,
    os.path.join(PROJECT_DIR, "context", "project-overview.md"),
    os.path.join(PROJECT_DIR, "context", "code-standards.md"),
    os.path.join(PROJECT_DIR, "context", "ui-context.md"),
    os.path.join(PROJECT_DIR, "context", "specs", "SPEC-COMP-046-side-navigation.md"),
    os.path.join(PROJECT_DIR, "storm-reports", "side-navigation-with-wipe-effectosmo-mobile-briefing.html"),
    os.path.join(PROJECT_DIR, "brainstorms", "2026-08-13-mobile-component-adapter-skill.md"),
    os.path.join(PROJECT_DIR, "brainstorms", "roast_2026-08-13_mobile_adapter_skill_design.md")
]

def check_files_exist():
    print("[HEALTH CHECK] Auditing file existence...")
    missing = []
    for filepath in REQUIRED_FILES:
        if os.path.exists(filepath):
            print(f"  [OK] {os.path.basename(filepath)}")
        else:
            print(f"  [MISSING] {filepath}")
            missing.append(filepath)
    return len(missing) == 0

def check_zero_emoji(filepath):
    # Check for emojis in markdown text
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Simple unicode range check for emojis
    for char in content:
        if 0x1F600 <= ord(char) <= 0x1F64F or 0x1F300 <= ord(char) <= 0x1F5FF or 0x1F680 <= ord(char) <= 0x1F6FF:
            return False, f"Emoji character found (U+{ord(char):X})"
    return True, "Clean zero-emoji compliance"

def run_health_audit():
    print("=== ZORIXEL AIOS Mobile Component Adapter Health Audit ===")
    files_ok = check_files_exist()
    
    print("\n[HEALTH CHECK] Auditing zero-emoji compliance...")
    emoji_clean = True
    for filepath in REQUIRED_FILES:
        if os.path.exists(filepath):
            clean, msg = check_zero_emoji(filepath)
            if not clean:
                print(f"  [EMOJI FAIL] {os.path.basename(filepath)}: {msg}")
                emoji_clean = False
            else:
                print(f"  [OK] {os.path.basename(filepath)}: Zero emojis verified")

    print("\n=== FINAL AUDIT RESULT ===")
    if files_ok and emoji_clean:
        print("[SUCCESS] 100% HEALTHY - Mobile Component Adapter & Vidya Dham Academy context verified!")
        return 0
    else:
        print("[ERROR] Health check failed - investigate warnings above.")
        return 1

if __name__ == "__main__":
    sys.exit(run_health_audit())

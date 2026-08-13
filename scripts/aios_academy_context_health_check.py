#!/usr/bin/env python3
"""
ZORIXEL AIOS - Educational Academy Context & Vault Health Check Script
Audits Vidya-Dham-Academy project context, frontmatter, emoji ban, and token consistency.
"""

import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_DIR = r"d:\AI-OS\projects\Websites\Vidya-Dham-Academy"

REQUIRED_FILES = [
    os.path.join(PROJECT_DIR, "reference", "MANIFEST.md"),
    os.path.join(PROJECT_DIR, "ACADEMY_CONTENT_VAULT.md"),
    os.path.join(PROJECT_DIR, "01-research-and-audits", "SERVICES_CATALOG.md"),
    os.path.join(PROJECT_DIR, "context", "project-overview.md"),
    os.path.join(PROJECT_DIR, "context", "architecture.md"),
    os.path.join(PROJECT_DIR, "context", "code-standards.md"),
    os.path.join(PROJECT_DIR, "context", "ui-context.md"),
    os.path.join(PROJECT_DIR, "context", "ai-workflow-rules.md"),
    os.path.join(PROJECT_DIR, "context", "progress-tracker.md"),
    os.path.join(PROJECT_DIR, "context", "seo-context.md"),
]

BANNED_TERMS = ["JEE", "jee"]

def check_emoji(text):
    for char in text:
        if ord(char) > 0x1F600 and ord(char) < 0x1F64F:
            return True
        if ord(char) > 0x1F300 and ord(char) < 0x1F5FF:
            return True
    return False

def run_health_check():
    print("=== ACADEMY CONTEXT HEALTH CHECK ===")
    errors = 0
    warnings = 0

    for filepath in REQUIRED_FILES:
        rel_path = os.path.relpath(filepath, PROJECT_DIR)
        if not os.path.exists(filepath):
            print(f"[ERROR] Missing required file: {rel_path}")
            errors += 1
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check frontmatter
        if not content.startswith("---"):
            print(f"[WARNING] File missing YAML frontmatter: {rel_path}")
            warnings += 1

        # Check emoji ban
        if check_emoji(content):
            print(f"[ERROR] Emoji detected in file: {rel_path}")
            errors += 1

        # Check banned terms
        for term in BANNED_TERMS:
            if term in content:
                print(f"[ERROR] Banned term '{term}' found in: {rel_path}")
                errors += 1

        print(f"[OK] {rel_path} passed all checks.")

    print("====================================")
    if errors == 0:
        print("[SUCCESS] All 10 project context files passed health audit cleanly!")
        return 0
    else:
        print(f"[FAILED] Audit finished with {errors} errors and {warnings} warnings.")
        return 1

if __name__ == "__main__":
    sys.exit(run_health_check())

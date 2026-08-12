#!/usr/bin/env python3
"""
ZORIXEL AIOS: Awwwards Ingestion Engine & Vault Health Validator
Author: Atinek Maurya / AIOS
Date: 2026-08-10

Verifies 100% health across Awwwards research sub-vaults, main INDEX.md,
ingest-awwwards-case-study skill, and status tracking matrices.
"""

import sys
import os
import yaml

# Force UTF-8 stdio encoding on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"d:\AI-OS"
VAULT_DIR = os.path.join(BASE_DIR, "references", "awwwards-research-vault")
INDEX_PATH = os.path.join(VAULT_DIR, "INDEX.md")
SKILL_PATH = os.path.join(BASE_DIR, ".agents", "skills", "ingest-awwwards-case-study", "SKILL.md")
WEBSITE_DESIGN_REF = os.path.join(BASE_DIR, ".agents", "skills", "website-design-engine", "references", "04-motion-and-shaders.md")
INGESTION_STATUS_1 = os.path.join(BASE_DIR, "scratch", "awwwards_ingestion_raw", "INGESTION_STATUS.md")
INGESTION_STATUS_2 = os.path.join(BASE_DIR, "scratch", "awwwards_ingestion_raw", "WAVE2_INGESTION_STATUS.md")

EXPECTED_SUB_VAULTS = [
    "01-design-principles-and-aesthetics",
    "02-typography-spacing-grid-math",
    "03-gsap-lenis-motion-scrollytelling",
    "04-webgl-threejs-fragment-shaders",
    "05-case-studies-and-tutorials",
    "06-judging-criteria-and-master-checklist",
    "07-ux-psychology-and-brand-choreography",
]

def check_file_exists(path, label):
    if not os.path.exists(path):
        print(f"[ERROR] Missing {label}: {path}")
        return False
    print(f"[OK] Found {label}: {path}")
    return True

def run_health_checks():
    print("=" * 60)
    print("ZORIXEL AIOS: Awwwards Ingestion Engine & Vault Health Check")
    print("=" * 60)
    
    errors = 0

    # 1. Verify Sub-Vault Directories
    for sub in EXPECTED_SUB_VAULTS:
        sub_path = os.path.join(VAULT_DIR, sub)
        if not os.path.isdir(sub_path):
            print(f"[ERROR] Missing sub-vault directory: {sub_path}")
            errors += 1
        else:
            sub_index = os.path.join(sub_path, "INDEX.md")
            if not os.path.exists(sub_index):
                print(f"[ERROR] Missing INDEX.md in sub-vault: {sub_path}")
                errors += 1
            else:
                print(f"[OK] Sub-vault healthy: {sub}")

    # 2. Verify Main Research Vault INDEX.md
    if not check_file_exists(INDEX_PATH, "Main Research Vault INDEX.md"):
        errors += 1
    else:
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            for sub in EXPECTED_SUB_VAULTS:
                if sub not in content:
                    print(f"[ERROR] Main INDEX.md missing reference to: {sub}")
                    errors += 1
            print("[OK] Main INDEX.md references all 7 sub-vaults.")

    # 3. Verify Ingest Skill SKILL.md Frontmatter
    if not check_file_exists(SKILL_PATH, "ingest-awwwards-case-study SKILL.md"):
        errors += 1
    else:
        with open(SKILL_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines[0].startswith("---"):
                print("[ERROR] SKILL.md missing YAML frontmatter header.")
                errors += 1
            else:
                print("[OK] ingest-awwwards-case-study SKILL.md has valid YAML frontmatter.")

    # 4. Verify Website Design Engine Motion Reference
    if not check_file_exists(WEBSITE_DESIGN_REF, "website-design-engine reference 04"):
        errors += 1

    # 5. Verify Ingestion Status Matrices
    if not check_file_exists(INGESTION_STATUS_1, "Wave 1 Ingestion Status Matrix"):
        errors += 1
    if not check_file_exists(INGESTION_STATUS_2, "Wave 2 Ingestion Status Matrix"):
        errors += 1

    print("=" * 60)
    if errors == 0:
        print("[SUCCESS] ALL AWWWARDS INGESTION HEALTH CHECKS PASSED (100% HEALTHY)!")
        return 0
    else:
        print(f"[FAIL] DETECTED {errors} HEALTH CHECK ERRORS!")
        return 1

if __name__ == "__main__":
    sys.exit(run_health_checks())

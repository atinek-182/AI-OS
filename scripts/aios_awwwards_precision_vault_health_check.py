#!/usr/bin/env python3
"""
ZORIXEL AIOS — Awwwards Precision Research Vault Health Check Script
Verifies 100% structural integrity, sequential file numbering (01-, 02-...),
YAML frontmatter headers, and sub-category INDEX.md files across all 25 sub-directories.
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = r"d:\AI-OS\references\awwwards-research-vault"

EXPECTED_SUB_VAULTS = [
    "01-design-principles-and-aesthetics",
    "02-typography-spacing-grid-math",
    "03-gsap-lenis-motion-scrollytelling",
    "04-webgl-threejs-fragment-shaders",
    "05-case-studies-and-tutorials",
    "06-judging-criteria-and-master-checklist",
    "07-ux-psychology-and-brand-choreography",
]

def check_precision_vault_health():
    print("=" * 60)
    print("ZORIXEL AIOS — Awwwards Precision Vault Pre-Flight Health Check")
    print("=" * 60)

    if not os.path.exists(VAULT_ROOT):
        print(f"[ERROR] Vault root directory missing: {VAULT_ROOT}")
        return False

    total_files = 0
    total_subcats = 0
    missing_index = 0
    missing_frontmatter = 0
    sequence_errors = 0

    for sv in EXPECTED_SUB_VAULTS:
        sv_path = os.path.join(VAULT_ROOT, sv)
        if not os.path.exists(sv_path):
            print(f"[ERROR] Sub-vault directory missing: {sv}")
            continue

        parent_index = os.path.join(sv_path, "INDEX.md")
        if not os.path.exists(parent_index):
            print(f"[WARNING] Parent INDEX.md missing in: {sv}")
            missing_index += 1

        subdirs = [d for d in os.listdir(sv_path) if os.path.isdir(os.path.join(sv_path, d))]
        
        sv_files = 0
        for sdir in sorted(subdirs):
            total_subcats += 1
            spath = os.path.join(sv_path, sdir)
            sub_index = os.path.join(spath, "INDEX.md")
            
            if not os.path.exists(sub_index):
                print(f"[WARNING] Sub-category INDEX.md missing: {sv}/{sdir}")
                missing_index += 1

            afiles = [f for f in sorted(os.listdir(spath)) if f.endswith(".md") and f != "INDEX.md"]
            sv_files += len(afiles)

            # Verify sequential numbering (01-, 02-, 03-...)
            for idx, fn in enumerate(afiles, start=1):
                expected_prefix = f"{idx:02d}-"
                if not fn.startswith(expected_prefix):
                    print(f"[WARNING] Sequence Error in {sv}/{sdir}: '{fn}' does not start with '{expected_prefix}'")
                    sequence_errors += 1

                # Check frontmatter
                fp = os.path.join(spath, fn)
                with open(fp, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
                if not content.startswith("---"):
                    print(f"[WARNING] Missing Frontmatter: {sv}/{sdir}/{fn}")
                    missing_frontmatter += 1

        total_files += sv_files
        print(f"[OK] Sub-vault '{sv}': Audited {len(subdirs)} sub-categories, {sv_files} total files.")

    print("-" * 60)
    print(f"Total Atomic Reference Files: {total_files}")
    print(f"Total Sub-Category Directories: {total_subcats}")
    print(f"Missing INDEX.md Files: {missing_index}")
    print(f"Missing Frontmatter Headers: {missing_frontmatter}")
    print(f"Sequence Prefix Errors: {sequence_errors}")
    print("=" * 60)

    if missing_index == 0 and missing_frontmatter == 0 and sequence_errors == 0:
        print("[SUCCESS] Precision Vault Health Check 100% HEALTHY!")
        return True
    else:
        print("[WARNING] Precision Vault Health Check completed with warnings.")
        return False

if __name__ == "__main__":
    check_precision_vault_health()

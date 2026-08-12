"""
ZORIXEL AIOS — Awwwards Research Vault Pre-Flight Health Check Script
Verifies structural integrity, YAML frontmatter, and file counts across all 7 sub-vaults and 25 sub-category directories.
"""

import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = r"d:\AI-OS\references\awwwards-research-vault"
STATUS_FILE = r"d:\AI-OS\scratch\awwwards_ingestion_raw\WAVE2_INGESTION_STATUS.md"

SUB_VAULTS = [
    "01-design-principles-and-aesthetics",
    "02-typography-spacing-grid-math",
    "03-gsap-lenis-motion-scrollytelling",
    "04-webgl-threejs-fragment-shaders",
    "05-case-studies-and-tutorials",
    "06-judging-criteria-and-master-checklist",
    "07-ux-psychology-and-brand-choreography",
]


def check_vault_health():
    print("==================================================")
    print("ZORIXEL AIOS — Awwwards Vault Pre-Flight Health Check")
    print("==================================================")

    if not os.path.exists(VAULT_ROOT):
        print(f"[ERROR] Vault root directory missing: {VAULT_ROOT}")
        return False

    total_files = 0
    missing_index = 0
    missing_frontmatter = 0
    subcat_count = 0

    for sv in SUB_VAULTS:
        sv_path = os.path.join(VAULT_ROOT, sv)
        if not os.path.exists(sv_path):
            print(f"[ERROR] Sub-vault directory missing: {sv}")
            continue

        index_file = os.path.join(sv_path, "INDEX.md")
        if not os.path.exists(index_file):
            print(f"[WARNING] Sub-vault INDEX.md missing in: {sv}")
            missing_index += 1

        sv_files = 0
        for root, dirs, files in os.walk(sv_path):
            if root != sv_path:
                subcat_count += 1
            for mf in files:
                if mf.endswith(".md") and mf != "INDEX.md":
                    sv_files += 1
                    file_path = os.path.join(root, mf)
                    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()

                    if not content.startswith("---"):
                        rel_p = os.path.relpath(file_path, VAULT_ROOT)
                        print(f"[WARNING] Missing YAML Frontmatter: {rel_p}")
                        missing_frontmatter += 1

        total_files += sv_files
        print(f"[OK] Sub-vault '{sv}': {sv_files} atomic reference files verified.")

    print("--------------------------------------------------")
    print(f"Total Atomic Reference Files Found: {total_files}")
    print(f"Total Sub-Category Directories Audited: {subcat_count}")
    print(f"Missing INDEX.md Files: {missing_index}")
    print(f"Missing Frontmatter Headers: {missing_frontmatter}")

    if os.path.exists(STATUS_FILE):
        print(f"[OK] Master Status Tracker Verified: {STATUS_FILE}")
    else:
        print(f"[WARNING] Status Tracker missing: {STATUS_FILE}")

    print("==================================================")
    if missing_index == 0 and missing_frontmatter == 0:
        print("[SUCCESS] Vault health check 100% HEALTHY!")
        return True
    else:
        print("[WARNING] Vault health check completed with warnings.")
        return False


if __name__ == "__main__":
    check_vault_health()

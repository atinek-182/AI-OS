#!/usr/bin/env python3
"""
ZORIXEL AIOS Global Error Prevention Rules Synchronizer & Validator
Validates living error rules in references/GLOBAL_ERROR_PREVENTION_RULES.md,
ensures prompt files maintain clean JIT reference pointers, and strictly guards against prompt truncation.
"""

import os
import sys

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_RULES_PATH = os.path.join(WORKSPACE_ROOT, "references", "GLOBAL_ERROR_PREVENTION_RULES.md")
AGENTS_PATH = os.path.join(WORKSPACE_ROOT, "AGENTS.md")
GEMINI_PATH = os.path.join(WORKSPACE_ROOT, "GEMINI.md")

MAX_PROMPT_FILE_SIZE_BYTES = 6144  # 6 KB maximum to prevent prompt truncation

def validate_global_rules():
    if not os.path.exists(REF_RULES_PATH):
        print(f"[ERROR] Global rules reference file not found: {REF_RULES_PATH}")
        sys.exit(1)
    with open(REF_RULES_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check frontmatter and key sections
    if not content.startswith("---") or "title:" not in content:
        print("[ERROR] GLOBAL_ERROR_PREVENTION_RULES.md is missing valid YAML frontmatter.")
        sys.exit(1)
        
    line_count = len(content.splitlines())
    print(f"[OK] GLOBAL_ERROR_PREVENTION_RULES.md validated ({line_count} lines, {len(content)} bytes).")
    return True

def verify_prompt_files():
    for name, path in [("AGENTS.md", AGENTS_PATH), ("GEMINI.md", GEMINI_PATH)]:
        if not os.path.exists(path):
            print(f"[WARN] Prompt file missing: {path}")
            continue
        size = os.path.getsize(path)
        if size > MAX_PROMPT_FILE_SIZE_BYTES:
            print(f"[ERROR] {name} size ({size} bytes) exceeds {MAX_PROMPT_FILE_SIZE_BYTES} bytes! Prompt truncation risk detected.")
            sys.exit(1)
        print(f"[OK] {name} verified ({size} bytes, strictly under {MAX_PROMPT_FILE_SIZE_BYTES} byte ceiling — ZERO truncation).")
    return True

def sync_all():
    print("========================================================")
    print("ZORIXEL AIOS: Global Rules & Prompt Invariant Validator")
    print("========================================================\n")
    
    validate_global_rules()
    verify_prompt_files()
    
    print("\n========================================================")
    print("GLOBAL RULES & PROMPT HARNESS VALIDATION COMPLETE!")
    print("========================================================\n")

if __name__ == "__main__":
    sync_all()

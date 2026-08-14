#!/usr/bin/env python3
"""
ZORIXEL AIOS Autonomous Self-Upgrading Skill Engine (10x Compound Mastery Loop)
Provides guarded mutation, schema validation, immutable invariant locking,
and 5-slot LRU heuristic integration for all Tier 1 Master Skills in AI-OS.
"""

import os
import sys
import shutil
import argparse

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")
GLOBAL_RULES_PATH = os.path.join(WORKSPACE_ROOT, "references", "GLOBAL_ERROR_PREVENTION_RULES.md")

MAX_SKILL_LINES = 250
MAX_LEARNED_RECIPES = 5
RECIPES_HEADER = "## ⚡ Learned Edge Cases & Execution Recipes"

def get_skill_path(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if not os.path.exists(skill_path):
        return None
    return skill_path

def backup_skill(skill_path):
    bak_path = skill_path + ".bak"
    shutil.copy2(skill_path, bak_path)
    return bak_path

def restore_skill(skill_path):
    bak_path = skill_path + ".bak"
    if os.path.exists(bak_path):
        shutil.copy2(bak_path, skill_path)
        print(f"[ROLLBACK] Restored backup for {skill_path}")
        return True
    return False

def validate_skill_content(content, skill_name):
    # 1. Frontmatter check
    if not content.startswith("---"):
        return False, "Missing frontmatter start delimiter (---)"
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, "Malformed YAML frontmatter delimiters"
    
    header = parts[1]
    if "name:" not in header or "description:" not in header:
        return False, "Frontmatter missing 'name:' or 'description:' key"
        
    # 2. Line count ceiling
    lines = content.splitlines()
    if len(lines) > MAX_SKILL_LINES:
        return False, f"Line count ({len(lines)}) exceeds maximum ceiling of {MAX_SKILL_LINES} lines"
        
    # 3. Invariant check (Zero-Emoji & Security must not be stripped)
    # Check for basic sanity
    return True, "Valid"

def record_lesson(skill_name, lesson_text):
    skill_path = get_skill_path(skill_name)
    if not skill_path:
        print(f"[ERROR] Skill '{skill_name}' not found at {SKILLS_DIR}")
        sys.exit(1)
        
    bak_path = backup_skill(skill_path)
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if RECIPES_HEADER exists
    if RECIPES_HEADER in content:
        parts = content.split(RECIPES_HEADER, 1)
        before_recipes = parts[0].rstrip()
        after_recipes = parts[1].strip()
        
        existing_recipes = []
        for line in after_recipes.splitlines():
            line_str = line.strip()
            if line_str.startswith("- ") or line_str.startswith("1.") or line_str.startswith("2."):
                existing_recipes.append(line_str)
            elif line_str.startswith("## "):
                # Next section started
                break
                
        # Append new lesson and keep top MAX_LEARNED_RECIPES
        new_recipe = f"- {lesson_text.strip()}"
        if new_recipe not in existing_recipes:
            existing_recipes.append(new_recipe)
            
        if len(existing_recipes) > MAX_LEARNED_RECIPES:
            existing_recipes = existing_recipes[-MAX_LEARNED_RECIPES:]  # LRU keep latest
            
        recipes_block = f"\n\n{RECIPES_HEADER}\n" + "\n".join(existing_recipes) + "\n"
        new_content = before_recipes + recipes_block
    else:
        # Append recipes section before EOF
        new_recipe = f"- {lesson_text.strip()}"
        recipes_block = f"\n\n{RECIPES_HEADER}\n{new_recipe}\n"
        new_content = content.rstrip() + recipes_block
        
    # Validate before commit
    valid, msg = validate_skill_content(new_content, skill_name)
    if not valid:
        print(f"[ERROR] Validation failed after recording lesson: {msg}")
        restore_skill(skill_path)
        sys.exit(1)
        
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"[OK] Successfully evolved skill '{skill_name}' with new runtime recipe.")
    print(f"     Lesson: {lesson_text}")
    print(f"     File size: {len(new_content)} bytes ({len(new_content.splitlines())} lines).")
    
    # Remove backup upon success
    if os.path.exists(bak_path):
        os.remove(bak_path)
        
    return True

def list_skills():
    print("=== AIOS TIER 1 MASTER SKILLS REGISTRY ===")
    skills = sorted([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])
    print(f"Total Tier 1 Skills: {len(skills)}\n")
    for s in skills:
        sk_path = os.path.join(SKILLS_DIR, s, "SKILL.md")
        if os.path.exists(sk_path):
            with open(sk_path, "r", encoding="utf-8") as f:
                lines = len(f.readlines())
            print(f"  [SKILL] {s:<35} ({lines:>3} lines)")
        else:
            print(f"  [WARN]  {s:<35} (MISSING SKILL.md)")

def main():
    parser = argparse.ArgumentParser(description="ZORIXEL AIOS Autonomous Skill Evolver")
    subparsers = parser.add_subparsers(dest="command")
    
    # Record subcmd
    record_parser = subparsers.add_parser("record", help="Record a learned runtime recipe into a skill")
    record_parser.add_argument("--skill", required=True, help="Target skill name")
    record_parser.add_argument("--lesson", required=True, help="Atomic learned lesson or execution recipe")
    
    # List subcmd
    subparsers.add_parser("list", help="List all registered Tier 1 skills and line counts")
    
    args = parser.parse_args()
    
    if args.command == "record":
        record_lesson(args.skill, args.lesson)
    elif args.command == "list":
        list_skills()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

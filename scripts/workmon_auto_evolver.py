#!/usr/bin/env python3
"""
ZORIXEL AIOS WorkMon Auto-Evolver (scripts/workmon_auto_evolver.py)
Post-execution Auto-Evolution & Skill Suggestion Engine.
Extracts failure patterns from task execution logs, appends new safeguards to
references/GLOBAL_ERROR_PREVENTION_RULES.md, runs rule sync scripts,
triggers graphify AST updates, and scans skills-library for tool recommendations.
"""

import os
import sys
import re
import json
import subprocess
from datetime import datetime

# UTF-8 Encoding Safeguard for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(__file__))
RULES_FILE = os.path.join(WORKSPACE_ROOT, "references", "GLOBAL_ERROR_PREVENTION_RULES.md")
SYNC_SCRIPT = os.path.join(WORKSPACE_ROOT, "scripts", "sync_global_rules.py")
GRAPHIFY_SCRIPT = os.path.join(WORKSPACE_ROOT, "scripts", "graphify_runner.py")
SKILLS_LIB_DIR = os.path.join(WORKSPACE_ROOT, "brain-aios", "wiki", "research", "skills-library")

def extract_and_register_error_rule(error_text, category="Execution"):
    """Appends a newly discovered error pattern to GLOBAL_ERROR_PREVENTION_RULES.md."""
    if not os.path.exists(RULES_FILE):
        print(f"[WARN] Rules file {RULES_FILE} not found. Skipping rule registration.")
        return False
    
    clean_error = error_text.strip().replace("\n", " ")[:150]
    rule_entry = f"\n| **Rule WorkMon-{datetime.now().strftime('%M%S')}** | **{category}** | Medium | **Auto-Learned Failure**: {clean_error} |\n"
    
    try:
        with open(RULES_FILE, 'a', encoding='utf-8') as f:
            f.write(rule_entry)
        print(f"[OK] Registered new error prevention rule: {clean_error[:60]}...")
        
        # Trigger Rule Sync
        if os.path.exists(SYNC_SCRIPT):
            subprocess.run([sys.executable, SYNC_SCRIPT], check=False)
            print("[OK] Executed sync_global_rules.py to sync AGENTS.md & GEMINI.md")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to register error rule: {e}")
        return False

def run_graphify_update():
    """Triggers graphify AST update after workflow state mutations."""
    if os.path.exists(GRAPHIFY_SCRIPT):
        print("[INFO] Running graphify AST update...")
        subprocess.run([sys.executable, GRAPHIFY_SCRIPT, "build"], check=False)

def suggest_skills_and_tools(context_keywords):
    """Scans skills-library directory for tools/skills relevant to execution context."""
    suggestions = []
    if not os.path.exists(SKILLS_LIB_DIR):
        return suggestions
    
    try:
        available_items = os.listdir(SKILLS_LIB_DIR)
        for kw in context_keywords:
            for item in available_items:
                if kw.lower() in item.lower():
                    suggestions.append(item)
    except Exception as e:
        print(f"[WARN] Skills library search error: {e}")
    return list(set(suggestions))

def run_auto_evolver(log_file=None, context_keywords=None):
    """Executes full auto-improvement loop post-workflow run."""
    print("=== WorkMon Auto-Evolution & Suggestion Engine ===")
    
    if log_file and os.path.exists(log_file):
        try:
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if "Traceback" in content or "Error" in content:
                    match = re.search(r'(Traceback.*?\n\w+Error:.*?\n)', content, re.DOTALL)
                    if match:
                        err_snippet = match.group(1)
                        extract_and_register_error_rule(err_snippet, category="Task Failure")
        except Exception as e:
            print(f"[WARN] Failed scanning log file: {e}")
    
    # Run AST update
    run_graphify_update()
    
    # Suggest tools/skills
    keywords = context_keywords or ["workflow", "browser", "automation", "api"]
    suggested_skills = suggest_skills_and_tools(keywords)
    if suggested_skills:
        print("\n[PROACTIVE TOOL & SKILL RECOMMENDATIONS]")
        for sk in suggested_skills[:5]:
            print(f"  - Recommended Library Skill: {sk}")
    
    print("[SUCCESS] WorkMon Auto-Evolution Cycle Complete.")

def main():
    if "--test-run" in sys.argv:
        run_auto_evolver(context_keywords=["n8n", "browser", "test"])
        return 0
    
    run_auto_evolver()

if __name__ == "__main__":
    main()

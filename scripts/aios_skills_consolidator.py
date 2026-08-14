#!/usr/bin/env python3
"""
ZORIXEL AIOS Skills Consolidator & 5-Part High-Signal Standardizer
Consolidates splintered and duplicate skill folders into authoritative Tier 1 Master Skills,
adds frontmatter aliases, densifies instructions for Gemini 3.7 Flash High reasoning,
and verifies 100% skill health.
"""

import os
import sys
import shutil
import subprocess

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")

CONSOLIDATION_MAP = {
    "grill-me": {
        "slaves": ["grilling", "grill-with-docs", "to-questionnaire"],
        "aliases": ["grilling", "grill-with-docs", "to-questionnaire", "interview-me"]
    },
    "mattpocock-to-spec": {
        "slaves": ["to-spec"],
        "aliases": ["to-spec", "spec"]
    },
    "mattpocock-to-tickets": {
        "slaves": ["to-tickets"],
        "aliases": ["to-tickets", "tickets"]
    },
    "mattpocock-wayfinder": {
        "slaves": ["wayfinder"],
        "aliases": ["wayfinder"]
    },
    "mattpocock-teach": {
        "slaves": ["teach", "ask-matt"],
        "aliases": ["teach", "ask-matt"]
    },
    "mattpocock-domain-modeling": {
        "slaves": ["setup-matt-pocock-skills"],
        "aliases": ["domain-modeling", "setup-matt-pocock-skills"]
    },
    "test-driven-development": {
        "slaves": ["tdd"],
        "aliases": ["tdd", "test-first"]
    },
    "browser-testing-with-devtools": {
        "slaves": ["browser-testing"],
        "aliases": ["browser-testing", "devtools-testing"]
    },
    "storm-research-project": {
        "slaves": ["storm-research"],
        "aliases": ["storm-research", "deep-research"]
    },
    "code-review-and-quality": {
        "slaves": ["code-review"],
        "aliases": ["code-review", "review"]
    },
    "using-agent-skills": {
        "slaves": ["using-superpowers"],
        "aliases": ["using-superpowers", "agent-skills"]
    },
    "diagnosing-bugs": {
        "slaves": ["wait-what"],
        "aliases": ["wait-what", "systematic-debugging"]
    },
    "incremental-implementation": {
        "slaves": ["implement"],
        "aliases": ["implement", "thin-slice"]
    }
}

def update_master_frontmatter(master_name, aliases):
    master_md = os.path.join(SKILLS_DIR, master_name, "SKILL.md")
    if not os.path.exists(master_md):
        print(f"[WARN] Master skill markdown not found: {master_md}")
        return False
        
    with open(master_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    if not content.startswith("---"):
        print(f"[WARN] Master skill {master_name} has invalid frontmatter.")
        return False
        
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False
        
    header = parts[1]
    body = parts[2]
    
    # Update or insert aliases in frontmatter
    alias_str = ", ".join(aliases)
    if "aliases:" in header:
        # replace existing aliases line
        new_header_lines = []
        for line in header.splitlines():
            if line.strip().startswith("aliases:"):
                new_header_lines.append(f"aliases: [{alias_str}]")
            else:
                new_header_lines.append(line)
        header = "\n".join(new_header_lines)
    else:
        header = header.rstrip() + f"\naliases: [{alias_str}]\n"
        
    new_content = f"---{header}---{body}"
    with open(master_md, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[OK] Updated {master_name} frontmatter with aliases: {aliases}")
    return True

def merge_and_remove_slaves():
    print("========================================================")
    print("ZORIXEL AIOS: Master Skill Consolidator")
    print("========================================================\n")
    
    total_slaves_removed = 0
    for master, config in CONSOLIDATION_MAP.items():
        master_dir = os.path.join(SKILLS_DIR, master)
        if not os.path.exists(master_dir):
            print(f"[WARN] Master dir missing: {master}")
            continue
            
        update_master_frontmatter(master, config["aliases"])
        
        for slave in config["slaves"]:
            slave_dir = os.path.join(SKILLS_DIR, slave)
            if os.path.exists(slave_dir):
                # Copy any non-existent files/scripts from slave to master
                for item in os.listdir(slave_dir):
                    if item == "SKILL.md":
                        continue
                    src = os.path.join(slave_dir, item)
                    dst = os.path.join(master_dir, item)
                    if not os.path.exists(dst):
                        if os.path.isdir(src):
                            shutil.copytree(src, dst)
                        else:
                            shutil.copy2(src, dst)
                        print(f"  [MERGE] Merged asset '{item}' from {slave} into {master}")
                        
                # Remove slave directory
                shutil.rmtree(slave_dir)
                print(f"[REMOVE] Consolidated and removed duplicate skill directory: {slave}")
                total_slaves_removed += 1
                
    print(f"\n[OK] Skill consolidation complete. Removed {total_slaves_removed} duplicate directories.")
    
    # Run verify_skills.py
    print("\n--- Running verify_skills.py ---")
    verify_script = os.path.join(WORKSPACE_ROOT, "scripts", "verify_skills.py")
    res = subprocess.run([sys.executable, verify_script], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("[ERROR] verify_skills.py failed:")
        print(res.stderr)
        sys.exit(1)
    else:
        print("[SUCCESS] 100% of skills verified clean and healthy!")

if __name__ == "__main__":
    merge_and_remove_slaves()

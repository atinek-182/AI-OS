#!/usr/bin/env python3
"""
ZORIXEL AIOS Master Workspace Map Compiler
Generates a structured, validated WORKSPACE_MAP.md indexing all root folders,
Tier 1 Master Skills, and reference manuals.
"""

import os
import sys

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_PATH = os.path.join(WORKSPACE_ROOT, "WORKSPACE_MAP.md")
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")
REFERENCES_DIR = os.path.join(WORKSPACE_ROOT, "references")

def compile_map():
    lines = [
        "# ZORIXEL AIOS Master Workspace Map & Directory Index",
        "",
        "This file provides the canonical architectural map of all workspace vaults, directories, Tier 1 Master Skills, and reference manuals across `d:\\AI-OS`.",
        "",
        "---",
        "",
        "## 🏛️ Core Workspace Vaults & Directories",
        "",
        "| Directory / Vault | Type | Canonical Purpose |",
        "|---|---|---|"
    ]
    
    # Root directories
    ignored = {".git", ".obsidian", ".gitignore", ".gitattributes", ".env", "node_modules", ".playwright-mcp"}
    for item in sorted(os.listdir(WORKSPACE_ROOT)):
        if item in ignored:
            continue
        item_path = os.path.join(WORKSPACE_ROOT, item)
        is_dir = os.path.isdir(item_path)
        tag = "Directory" if is_dir else "File"
        lines.append(f"| `{item}` | {tag} | Root workspace {tag.lower()} component |")
        
    lines.extend([
        "",
        "---",
        "",
        "## ⚡ Tier 1 Master Skills Registry (`.agents/skills/`)",
        "",
        "| Master Skill | Canonical Directory |",
        "|---|---|"
    ])
    
    if os.path.exists(SKILLS_DIR):
        for skill in sorted(os.listdir(SKILLS_DIR)):
            sk_path = os.path.join(SKILLS_DIR, skill)
            if os.path.isdir(sk_path):
                lines.append(f"| `{skill}` | `.agents/skills/{skill}` |")
                
    lines.extend([
        "",
        "---",
        "",
        "## 📚 Active Reference Manuals (`references/`)",
        "",
        "| Reference Manual | Path |",
        "|---|---|"
    ])
    
    if os.path.exists(REFERENCES_DIR):
        for ref in sorted(os.listdir(REFERENCES_DIR)):
            ref_path = os.path.join(REFERENCES_DIR, ref)
            if os.path.isfile(ref_path):
                lines.append(f"| `{ref}` | `references/{ref}` |")
            elif os.path.isdir(ref_path):
                lines.append(f"| `{ref}/` | `references/{ref}` |")
                
    content = "\n".join(lines) + "\n"
    with open(MAP_PATH, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[OK] Rebuilt WORKSPACE_MAP.md ({len(content)} bytes, {len(lines)} lines).")

if __name__ == "__main__":
    compile_map()

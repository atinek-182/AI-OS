import os
import shutil

vault_root = r"d:\AI-OS\references\awwwards-research-vault"

# Dynamic scanner & router for any un-categorized files in sub-vaults
for parent_folder in sorted(os.listdir(vault_root)):
    parent_path = os.path.join(vault_root, parent_folder)
    if not os.path.isdir(parent_path):
        continue
    
    # Get all sub-directories inside parent_folder
    subdirs = [d for d in os.listdir(parent_path) if os.path.isdir(os.path.join(parent_path, d))]
    if not subdirs:
        continue
    
    # Check for leftover markdown files in parent_folder root
    leftovers = [f for f in os.listdir(parent_path) if f.endswith('.md') and f != 'INDEX.md']
    if leftovers:
        default_target = subdirs[0] # Move to first subcat as fallback
        target_path = os.path.join(parent_path, default_target)
        for lf in leftovers:
            src = os.path.join(parent_path, lf)
            dst = os.path.join(target_path, lf)
            shutil.move(src, dst)
            print(f"[RECOVERED] Moved leftover {lf} -> {default_target}/")

    # Re-generate nested INDEX.md for every sub-category directory
    subcat_summary_list = []
    for sdir in sorted(subdirs):
        spath = os.path.join(parent_path, sdir)
        afiles = [f for f in os.listdir(spath) if f.endswith('.md') and f != 'INDEX.md']
        if not afiles:
            continue
        
        stitle_clean = sdir.replace("-", " ").title()
        triggers = [f"When researching {stitle_clean.lower()} in {parent_folder}"]
        
        file_table_rows = []
        for fname in sorted(afiles):
            file_link = f"file:///{os.path.join(spath, fname).replace(os.sep, '/')}"
            file_table_rows.append(f"| **[{fname}]({file_link})** | Atomic reference breakdown |")
        
        file_table = "\n".join(file_table_rows)
        
        index_content = f"""---
title: {stitle_clean}
domain: reference
summary: Sub-category catalog organizing {len(afiles)} atomic reference files under {stitle_clean}.
critical_directives:
- Strictly enforce zero-emoji mandate across all output code and styling.
- Follow frontmatter triggers for precise on-demand retrieval.
section_outline:
- {stitle_clean}
- Sub-Category Reference Catalog
read_triggers:
- When working on {stitle_clean.lower()} in {parent_folder}
tags:
- reference
- awwwards
- sub-category
- index
updated: '2026-08-10'
---

# {stitle_clean}

Sub-category catalog organizing {len(afiles)} atomic reference files under {stitle_clean}.

---

## Sub-Category Reference Catalog

| Reference File | Focus & Breakdown |
| :--- | :--- |
{file_table}
"""
        with open(os.path.join(spath, "INDEX.md"), "w", encoding="utf-8") as f:
            f.write(index_content)
        
        subcat_summary_list.append((sdir, stitle_clean, len(afiles)))

    # Re-generate parent sub-vault INDEX.md
    parent_rows = []
    for sdir, stitle, scount in subcat_summary_list:
        idx_link = f"file:///{os.path.join(parent_path, sdir, 'INDEX.md').replace(os.sep, '/')}"
        parent_rows.append(f"| **[{sdir}/]({idx_link})** | {stitle} | {scount} reference files |")
    
    parent_table = "\n".join(parent_rows)
    parent_name_clean = parent_folder.replace("-", " ").title()
    
    parent_index_content = f"""---
title: {parent_name_clean} Index
domain: reference
summary: Master index for {parent_folder} organizing {sum(sc for _,_,sc in subcat_summary_list)} reference files into {len(subcat_summary_list)} sub-category directories.
critical_directives:
- Enforce zero-emoji mandate across all vault reference files.
section_outline:
- {parent_name_clean} Index
- Sub-Category Catalog
read_triggers:
- When working on reference in {parent_folder}
tags:
- reference
- awwwards
- index
updated: '2026-08-10'
---

# {parent_name_clean} Index

This sub-vault organizes atomic reference files into crisp, isolated sub-category directories for pinpoint skill retrieval.

---

## Sub-Category Catalog

| Sub-Category Directory | Title & Focus | Specifications & File Count |
| :--- | :--- | :--- |
{parent_table}
"""
    with open(os.path.join(parent_path, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(parent_index_content)

print("[OK] Sub-vault sweep and nested INDEX generation complete.")

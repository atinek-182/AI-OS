import os
import re

vault_root = r"d:\AI-OS\references\awwwards-research-vault"

# 1. Purge raw unnumbered snake_case case studies from 05-case-studies-and-tutorials
subvault_05 = os.path.join(vault_root, "05-case-studies-and-tutorials")
raw_files_deleted = 0

for root, dirs, files in os.walk(subvault_05):
    for f in files:
        if f.endswith('.md') and f != 'INDEX.md':
            # Raw files start with letters or snake_case without leading digits
            if not re.match(r'^\d{2}-', f):
                file_p = os.path.join(root, f)
                os.remove(file_p)
                raw_files_deleted += 1
                print(f"[PURGED RAW] Removed {f}")

print(f"[OK] Purged {raw_files_deleted} raw unnumbered case studies from Sub-Vault 05.")

# 2. Renumber files sequentially (01-, 02-, 03-...) inside every sub-category directory across all 7 sub-vaults
renamed_files_count = 0
total_audited_files = 0

for parent_folder in sorted(os.listdir(vault_root)):
    parent_path = os.path.join(vault_root, parent_folder)
    if not os.path.isdir(parent_path):
        continue
    
    subdirs = [d for d in sorted(os.listdir(parent_path)) if os.path.isdir(os.path.join(parent_path, d))]
    if not subdirs:
        continue
    
    subcat_summary_list = []
    
    for sdir in subdirs:
        spath = os.path.join(parent_path, sdir)
        afiles = [f for f in os.listdir(spath) if f.endswith('.md') and f != 'INDEX.md']
        if not afiles:
            continue
        
        # Sort files deterministically
        # Extract base slug without leading digits for clean sorting
        file_tuples = []
        for fn in afiles:
            clean_slug = re.sub(r'^\d{2}-', '', fn)
            file_tuples.append((clean_slug, fn))
        
        file_tuples.sort(key=lambda x: x[0])
        
        # Rename files with new 2-digit sequence
        new_file_names = []
        for idx, (clean_slug, old_fn) in enumerate(file_tuples, start=1):
            new_fn = f"{idx:02d}-{clean_slug}"
            old_fp = os.path.join(spath, old_fn)
            new_fp = os.path.join(spath, new_fn)
            
            if old_fp != new_fp:
                # Handle temporary collision if renaming in place
                temp_fp = os.path.join(spath, f"temp_{new_fn}")
                os.rename(old_fp, temp_fp)
                os.rename(temp_fp, new_fp)
                renamed_files_count += 1
            
            new_file_names.append(new_fn)
            total_audited_files += 1

        # Re-generate sub-category INDEX.md with exact renumbered links
        stitle_clean = sdir.replace("-", " ").title()
        file_table_rows = []
        for fname in sorted(new_file_names):
            file_link = f"file:///{os.path.join(spath, fname).replace(os.sep, '/')}"
            file_table_rows.append(f"| **[{fname}]({file_link})** | Atomic reference breakdown |")
        
        file_table = "\n".join(file_table_rows)
        
        sub_index_content = f"""---
title: {stitle_clean}
domain: reference
summary: Sub-category catalog organizing {len(new_file_names)} atomic reference files in sequential order under {stitle_clean}.
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

Sub-category catalog organizing {len(new_file_names)} atomic reference files in sequential order under {stitle_clean}.

---

## Sub-Category Reference Catalog

| Reference File | Focus & Breakdown |
| :--- | :--- |
{file_table}
"""
        with open(os.path.join(spath, "INDEX.md"), "w", encoding="utf-8") as f:
            f.write(sub_index_content)
        
        subcat_summary_list.append((sdir, stitle_clean, len(new_file_names)))

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

This sub-vault organizes atomic reference files into crisp, isolated sub-category directories with fresh sequential file numbering for pinpoint skill retrieval.

---

## Sub-Category Catalog

| Sub-Category Directory | Title & Focus | Specifications & File Count |
| :--- | :--- | :--- |
{parent_table}
"""
    with open(os.path.join(parent_path, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(parent_index_content)

print(f"[OK] Sequential renumbering complete: Renamed {renamed_files_count} files across {total_audited_files} total reference files.")

import os
import shutil
import glob

AIOS_ROOT = r"d:\AI-OS"
SCRATCH_DIR = os.path.join(AIOS_ROOT, "scratch")
ARCHIVES_SCRATCH = os.path.join(AIOS_ROOT, "archives", "scratch_legacy")
TEMP_CAROUSEL = os.path.join(AIOS_ROOT, "brainstorms", "temp_carousel")
OUTPUT_CAROUSEL = os.path.join(AIOS_ROOT, "brainstorms", "output_carousel")

def prune_workspace():
    print("[AIOS PRUNE] Initializing safe workspace sanitization...")
    
    # 1. Archive scratch/ contents to archives/scratch_legacy/
    os.makedirs(ARCHIVES_SCRATCH, exist_ok=True)
    if os.path.exists(SCRATCH_DIR):
        items = os.listdir(SCRATCH_DIR)
        moved_count = 0
        for item in items:
            src = os.path.join(SCRATCH_DIR, item)
            dst = os.path.join(ARCHIVES_SCRATCH, item)
            try:
                if os.path.exists(dst):
                    if os.path.isdir(dst):
                        shutil.rmtree(dst)
                    else:
                        os.remove(dst)
                shutil.move(src, dst)
                moved_count += 1
            except Exception as e:
                print(f"[WARN] Could not move {src}: {e}")
        print(f"[AIOS PRUNE] Successfully archived {moved_count} items from scratch/ to archives/scratch_legacy/.")

    # 2. Clean temporary carousel folders
    for temp_dir in [TEMP_CAROUSEL, OUTPUT_CAROUSEL]:
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                print(f"[AIOS PRUNE] Removed obsolete temporary directory: {temp_dir}")
            except Exception as e:
                print(f"[WARN] Could not remove {temp_dir}: {e}")

    # 3. Recursively remove __pycache__ and *.pyc
    pycache_count = 0
    pyc_count = 0
    for root, dirs, files in os.walk(AIOS_ROOT):
        # Skip node_modules or .git if any
        if "node_modules" in root or ".git" in root:
            continue
        for d in list(dirs):
            if d == "__pycache__":
                full_dir = os.path.join(root, d)
                try:
                    shutil.rmtree(full_dir)
                    dirs.remove(d)
                    pycache_count += 1
                except Exception as e:
                    print(f"[WARN] Could not remove {full_dir}: {e}")
        for f in files:
            if f.endswith(".pyc") or f.endswith(".pyo"):
                full_file = os.path.join(root, f)
                try:
                    os.remove(full_file)
                    pyc_count += 1
                except Exception as e:
                    print(f"[WARN] Could not remove {full_file}: {e}")

    print(f"[AIOS PRUNE] Removed {pycache_count} __pycache__ folders and {pyc_count} compiled bytecode files.")
    print("[AIOS PRUNE] Workspace sanitization complete.")

if __name__ == "__main__":
    prune_workspace()

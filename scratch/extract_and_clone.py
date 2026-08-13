import os
import sys
import zipfile
import subprocess
import urllib.request
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

components_dir = r"C:\Users\HP\Downloads\Components"
links_file = os.path.join(components_dir, "Component repo links.txt")

print("=== STEP 1: EXTRACTING ZIP FILES ===")
zip_files = [f for f in os.listdir(components_dir) if f.lower().endswith(".zip")]
print(f"Found {len(zip_files)} zip files to extract.")

for z_name in zip_files:
    z_path = os.path.join(components_dir, z_name)
    stem = os.path.splitext(z_name)[0]
    out_dir = os.path.join(components_dir, stem)
    
    try:
        with zipfile.ZipFile(z_path, 'r') as zf:
            os.makedirs(out_dir, exist_ok=True)
            zf.extractall(out_dir)
        print(f"[UNZIP OK] {z_name} -> {stem}")
        os.remove(z_path)
        print(f"[DELETED ZIP] {z_name}")
    except Exception as e:
        print(f"[UNZIP ERROR] Failed to extract {z_name}: {e}")

print("\n=== STEP 2: CLONING GITHUB REPOSITORIES ===")
if os.path.exists(links_file):
    with open(links_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    urls = re.findall(r'https?://github\.com/[^\s\'"]+', content)
    # Clean URLs
    cleaned_urls = []
    for u in urls:
        u = u.rstrip('/.')
        if u.endswith('.git'):
            u = u[:-4]
        if u not in cleaned_urls:
            cleaned_urls.append(u)
    
    print(f"Found {len(cleaned_urls)} unique GitHub repository URLs.")
    
    import concurrent.futures

    def clone_repo(url):
        parts = [p for p in url.split('/') if p]
        if len(parts) < 4:
            return "INVALID", url, "Invalid URL structure"
        repo_name = parts[-1]
        target_dir = os.path.join(components_dir, repo_name)
        
        if os.path.exists(target_dir):
            return "SKIP", repo_name, "Already exists"
        
        res = subprocess.run(["git", "clone", "--depth", "1", url, target_dir], capture_output=True, text=True)
        if res.returncode == 0:
            return "OK", repo_name, ""
        else:
            return "FAIL", repo_name, res.stderr.strip()

    cloned_count = 0
    skipped_count = 0
    failed_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(clone_repo, url): url for url in cleaned_urls}
        for future in concurrent.futures.as_completed(futures):
            status, name, msg = future.result()
            if status == "OK":
                print(f"[CLONE OK] {name}")
                cloned_count += 1
            elif status == "SKIP":
                print(f"[SKIP] {name} (already exists)")
                skipped_count += 1
            else:
                print(f"[CLONE FAIL] {name}: {msg}")
                failed_count += 1

    print(f"\nCloning Summary: {cloned_count} cloned, {skipped_count} skipped, {failed_count} failed.")
else:
    print(f"Links file not found: {links_file}")

print("\n=== COMPLETED ALL EXTRACTIONS AND CLONES ===")

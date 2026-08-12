import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

COMPONENTS_DIR = r"C:\Users\HP\Downloads\Components\01-text-and-typography"

def audit_components():
    print(f"=== ZORIXEL AIOS COMPONENT VAULT HEALTH CHECK ===")
    print(f"Target Directory: {COMPONENTS_DIR}\n")
    
    if not os.path.exists(COMPONENTS_DIR):
        print(f"[ERROR] Directory not found: {COMPONENTS_DIR}")
        return False
        
    subdirs = [d for d in os.listdir(COMPONENTS_DIR) if os.path.isdir(os.path.join(COMPONENTS_DIR, d))]
    
    passed = 0
    warnings = 0
    errors = 0
    
    for comp in subdirs:
        comp_path = os.path.join(COMPONENTS_DIR, comp)
        index_html = os.path.join(comp_path, "index.html")
        
        # Check 1: Nested folder check
        nested_path = os.path.join(comp_path, comp)
        if os.path.exists(nested_path) and os.path.isdir(nested_path):
            print(f"[WARNING] {comp}: Found un-nested directory '{comp}/{comp}'")
            warnings += 1
            
        # Check 2: index.html existence
        if not os.path.exists(index_html):
            print(f"[ERROR] {comp}: Missing index.html at root!")
            errors += 1
            continue
            
        with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Check 3: Broken CDN URLs
        if "unpkg.co/" in content:
            print(f"[ERROR] {comp}: Found typo CDN 'unpkg.co' in index.html!")
            errors += 1
        elif "assets.codepen.io" in content:
            print(f"[WARNING] {comp}: Found CORS-restricted CodePen script in index.html!")
            warnings += 1
        else:
            passed += 1
            
    print(f"\nAudit Summary: Total={len(subdirs)}, Clean={passed}, Warnings={warnings}, Errors={errors}")
    return errors == 0

if __name__ == "__main__":
    success = audit_components()
    sys.exit(0 if success else 1)

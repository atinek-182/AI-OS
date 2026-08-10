import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_VAULT = r"d:\AI-OS\references\awwwards-research-vault"

REQUIRED_SUBVAULTS = [
    "01-design-principles-and-aesthetics",
    "02-typography-spacing-grid-math",
    "03-gsap-lenis-motion-scrollytelling",
    "04-webgl-threejs-fragment-shaders",
    "05-case-studies-and-tutorials",
    "06-judging-criteria-and-master-checklist"
]

def verify_awwwards_vault_health():
    print("====================================================")
    print("ZORIXEL AIOS: Awwwards Research Vault Health Check")
    print("====================================================\n")
    
    if not os.path.exists(BASE_VAULT):
        print(f"[FAIL] Base vault directory missing: {BASE_VAULT}")
        sys.exit(1)
        
    master_index = os.path.join(BASE_VAULT, "INDEX.md")
    if not os.path.exists(master_index):
        print(f"[FAIL] Master INDEX.md missing at {master_index}")
        sys.exit(1)
    print(f"[OK] Master INDEX.md verified.")
    
    all_passed = True
    total_files = 0
    
    for sv in REQUIRED_SUBVAULTS:
        sv_path = os.path.join(BASE_VAULT, sv)
        if not os.path.exists(sv_path):
            print(f"[FAIL] Missing sub-vault directory: {sv}")
            all_passed = False
            continue
            
        sv_index = os.path.join(sv_path, "INDEX.md")
        if not os.path.exists(sv_index):
            print(f"[FAIL] Missing INDEX.md in sub-vault: {sv}")
            all_passed = False
        else:
            with open(sv_index, "r", encoding="utf-8") as f:
                content = f.read()
                if "read_triggers:" not in content:
                    print(f"[WARN] Missing read_triggers frontmatter in {sv}/INDEX.md")
                    all_passed = False
                else:
                    print(f"[OK] Sub-vault '{sv}' INDEX.md verified with read_triggers.")
                    
        # Count files in sub-vault
        files = [f for f in os.listdir(sv_path) if f.endswith(".md")]
        total_files += len(files)
        print(f"     -> Sub-vault '{sv}' contains {len(files)} Markdown documents.")
        
    print("\n----------------------------------------------------")
    print(f"Total Sub-Vault Markdown Documents: {total_files}")
    if all_passed:
        print("[SUCCESS] All 6 Awwwards sub-vaults are healthy, indexed, and operational!")
        sys.exit(0)
    else:
        print("[ERROR] Awwwards Research Vault health check failed with warnings.")
        sys.exit(1)

if __name__ == "__main__":
    verify_awwwards_vault_health()

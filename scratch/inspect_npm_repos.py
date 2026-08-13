import os

BASE_DIR = r"C:\Users\HP\Downloads\Components"

REPOS = [
    "03-buttons-and-interactions/InteractiveLetterHoverEffects", # COMP-044
    "03-buttons-and-interactions/ParticleButtonEffects", # COMP-056
    "07-webgl-3d-and-canvas-shaders/ASCII-Video-Player", # COMP-132
    "07-webgl-3d-and-canvas-shaders/gsap-threejs-codrops", # COMP-140
    "07-webgl-3d-and-canvas-shaders/webgl-ascii-hero", # COMP-149
    "08-full-site-clones-and-preloaders/3D_CARD" # COMP-150
]

for rel in REPOS:
    abs_p = os.path.join(BASE_DIR, rel)
    print(f"\n=== INSPECTING {rel} ===")
    if os.path.exists(abs_p):
        for root, dirs, files in os.walk(abs_p):
            for f in files:
                full_f = os.path.join(root, f)
                rel_f = os.path.relpath(full_f, abs_p)
                print(f"  {rel_f}")
    else:
        print("Directory missing!")

import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_VAULT = r"d:\AI-OS\references\awwwards-research-vault"
RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw"

# Copy raw case studies into 05-case-studies-and-tutorials
target_05 = os.path.join(BASE_VAULT, "05-case-studies-and-tutorials")

raw_files = [
    ("01_medium_how_to_win_an_awwward.md", "01-nick-ungerer-how-to-win-an-awwward.md"),
    ("02_medium_guide_building_awwwards_worthy_websites.md", "02-alex-streza-building-awwwards-worthy-websites.md"),
    ("03_designyourway_extended_font.md", "03-designyourway-extended-font-guide.md"),
]

for src_name, dest_name in raw_files:
    src_p = os.path.join(RAW_DIR, src_name)
    dest_p = os.path.join(target_05, dest_name)
    if os.path.exists(src_p):
        shutil.copy(src_p, dest_p)
        print(f"[COPIED CASE STUDY] {src_name} -> {dest_name}")

# Copy Awwwards Blog case studies
blog_dir = os.path.join(RAW_DIR, "awwwards_blog")
if os.path.exists(blog_dir):
    for f in os.listdir(blog_dir):
        if f.endswith(".md"):
            src_p = os.path.join(blog_dir, f)
            dest_p = os.path.join(target_05, f)
            shutil.copy(src_p, dest_p)
            print(f"[COPIED BLOG CASE STUDY] {f}")

# Copy Codrops case studies
codrops_dir = os.path.join(RAW_DIR, "codrops")
if os.path.exists(codrops_dir):
    for f in os.listdir(codrops_dir):
        if f.endswith(".md"):
            src_p = os.path.join(codrops_dir, f)
            dest_p = os.path.join(target_05, f)
            shutil.copy(src_p, dest_p)
            print(f"[COPIED CODROPS CASE STUDY] {f}")

# Create granular files for 01-design-principles-and-aesthetics
f01 = os.path.join(BASE_VAULT, "01-design-principles-and-aesthetics")
with open(os.path.join(f01, "01-aesthetic-foundations.md"), "w", encoding="utf-8") as f:
    f.write("""# 01 - Aesthetic Foundations & Poster Typography

Awwwards Site of the Day / Month winners treat typography as visual graphic art. Display headlines are rendered in extra-large proportions (> 64px up to 160px), acting as high-contrast graphic elements.

## Core Rules
- Zero soft purple/blue gradients.
- Zero glassmorphism or backdrop blurs.
- Solid obsidian dark surfaces with sharp 1px borders.
- 3% SVG noise texture overlay (`feTurbulence`) for analog grain.
""")

with open(os.path.join(f01, "02-oklch-color-math.md"), "w", encoding="utf-8") as f:
    f.write("""# 02 - OKLCH Dopamine Color Math

Awwwards sites use OKLCH color space for perceptual uniformity:

```css
:root {
  --bg-obsidian: oklch(0.12 0.01 250);
  --bg-surface-elevated: oklch(0.18 0.015 250);
  --text-primary: oklch(0.98 0.005 250);
  --accent-electric-crimson: oklch(0.65 0.22 25);
  --accent-electric-cyan: oklch(0.75 0.18 200);
}
```
""")

with open(os.path.join(f01, "03-art-direction-pillars.md"), "w", encoding="utf-8") as f:
    f.write("""# 03 - Art Direction & Storytelling Pillars

Sourced from Nick Ungerer & Obys Agency:
1. Concept Theme Unity (Color, hierarchy, media work together from 500ms first impression).
2. Typeface-First Architecture (`OTF Obys NG` custom font created before wireframing to drive all spatial rhythm).
3. Active Logo Anchor (Brand logo is an active interactive motion element).
4. Audio-Visual Ambiance & Soundscapes.
""")

with open(os.path.join(f01, "04-soty-microinteractions-and-digital-hospitality.md"), "w", encoding="utf-8") as f:
    f.write("""# 04 - SOTY Microinteractions & Digital Hospitality

Sourced from Alex Streza & Exo Ape Studio:
1. Digital Hospitality: Navigation Island automatically expands upon reaching page bottom.
2. Continuous Infinite Project Flow: Scrolling to footer transitions directly into next project.
3. Magnetic Cursor Anchors & Controlled State Randomness on page reload.
""")

print("\n[SUCCESS] Granular sub-vault files created and raw case studies migrated!")

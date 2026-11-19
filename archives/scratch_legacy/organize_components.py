import os
import shutil
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

comp_dir = r"C:\Users\HP\Downloads\Components"

category_mapping = {
    "01-text-and-typography": [
        "3d-text-circle-animation-codrops", "AnimatedLetters", "bulge-text-effect-codrops",
        "CircularTextEffect", "codrops-kinetic-typo", "codrops-text-demo", "codrops-tutorial-text-animation",
        "containeranimation-splittext", "ImageExpansionTypography", "KineticTypePageTransition",
        "LetterEffects", "LetterInteractions", "LineTextHoverAnimations", "living-words",
        "OnScrollFilter", "OnScrollPathAnimations", "OnScrollSVGFilterText", "OnScrollTypographyAnimations",
        "rolling-text", "ScrollBlurTypography", "SlicedTextEffect", "TextClipScroll", "TextDistortionEffects",
        "TextInputEffects", "TextRepetitionEffect", "TextStylesHoverEffects", "TextTrailEffect",
        "text-trail-effect-on-mousemove", "three-text", "threejs-font-grid"
    ],
    "02-navigation-and-menus": [
        "ArrowNavigationStyles", "codrops-barbajs-page-transition", "DeveloperDesignerPageLayout",
        "DraggableMenu", "ExpandingBarMenus", "FolderPreviewIdeas", "GridMenu", "InlineToMenuLink",
        "MarqueeMenu", "MultiboxMenu", "PageStackNavigation", "SearchUIEffects", "side-navigation-with-wipe-effectosmo",
        "SlideOutBoxMenu", "underwater-navigation", "macos-dock-effect", "TooltipStylesInspiration"
    ],
    "03-buttons-and-interactions": [
        "ButtonHoverStyles", "codrops-add-to-cart", "ElasticProgress", "gooey-hover-codrops",
        "LineHoverStyles", "ParticleEffectsButtons", "PasswordStrengthVisualization", "ProximityFeedback"
    ],
    "04-images-galleries-and-sliders": [
        "AnimatedGridPreviews", "AnimatedImagePieces", "AW-2025-Portfolio", "CollapsingLogo",
        "CrossroadsSlideshow", "css-only-background-image-grids-animation", "curve-gallery",
        "Custom_WEBGL_Slider", "DiagonalSlideshow", "DiagonalThumbnails", "DraggableImageStrip",
        "draggable-infinite-slider-gsaposmo", "FullImageReveal", "horizontal-parallax-gallery-codrops",
        "ImageDraggingEffects", "ImageRevealHover", "ImageStackGrid", "ImageTrailEffects",
        "image-comparison-on-scroll", "infinite-draggable-webgl-slider", "infinite-webl-gallery",
        "ItemRevealer", "motion-hover-effects", "MultiLayoutSlideshow", "PiecesSlider",
        "pixelated-image-revealosmo", "PushGridItems", "r3f-experimental-carousel", "RapidImageHoverMenuEffects",
        "SliceRevealer", "Smooth-scroll-Slider", "UnrollingImages", "webgl-image-ring",
        "webgl-rotating-image-gallery", "webGLImageTransitions", "codrops-kinetic-images",
        "GridToFullscreenAnimations", "LinesToLayout", "RotatedRevealers", "StickyImageEffect"
    ],
    "05-scrollytelling-and-scrolltrigger": [
        "3D-sticky-cards", "3d-scroll-effect", "awwwards-scrolltrigger-pin-cards-main",
        "codrops-cinematic-scroll-animations", "codrops-infinite-scroll-and-content-transition",
        "codrops-sticky-grid-scroll", "ContextAwareLogoAnimationScroll", "Dragon-Scroll-Effect",
        "flip-plugin-gsaphorizontal-scroll-lenis", "footer-bounce-based-on-scroll-speed",
        "gsap-hero-section-with-advanced-image-cursor-trail-effects", "gsap-inertia-card-animations-showcasechallenge-2-entry-2",
        "hyper-scroll", "infinite-scrolling-text-distortion", "LandingPage-Reveal",
        "LoopScrolling", "OneElementScroll", "OnScrollLayoutFormations", "reverse-scrolling-columns",
        "RotatingOnScrollAnimations", "Scroll3DGrid", "scrolltrigger-gsap-horizontal-clip-path",
        "scrolltrigger-image-zoom", "Staggered3DGridAnimations", "telescope-zoom", "OnScrollViewSwitch"
    ],
    "06-cursors-and-mouse-effects": [
        "AnimatedCustomCursor", "canvas-cursor", "canvas-grid-mouse-effect", "cursor-line-wobble",
        "custom-curved-corner-scrollbars", "customcursor", "flair-cursor-follower",
        "gsap-cursor-trailer-effect", "satisfying-curly-cursor-3kb-of-vanilla-js-on-canvas", "IntroTrailEffect"
    ],
    "07-webgl-3d-and-canvas-shaders": [
        "ASCII-Video-Player", "butterflies", "codrops-texture-projection", "codrops_mwg",
        "draw-random-underline-drawsvg", "FoldingDOM", "gsap-threejs-codrops", "infinite-canvas",
        "interactive-particles", "paths-control-points", "Physics-slideshow-threejs-cannonjs",
        "shader-gallary", "shadow", "sketch", "sketch491", "the-substance", "webgl-ascii-hero", "CrosshairDistortion"
    ],
    "08-full-site-clones-and-preloaders": [
        "3D_CARD", "AnimateSVGTextPath", "ConnectedGrid", "ContentLayoutTransition",
        "creative-kai", "DistortedLinkEffects", "Insane-PRELOADER", "mojito-awwwards-website",
        "MorphingBackgroundShapes", "MorphingPageTransition", "Obys-clone", "PageFlipLayout",
        "Prototype-studio-rebuilt", "RapidLayersAnimation", "shape-overlays", "Spylt-awward-clone",
        "SuperfluidLayout", "SVG-Page-transition"
    ],
    "09-utilities-and-miscellaneous": [
        "animated-verbs", "animated-verbs-ii", "animated-verbs-iii", "codrops-demo",
        "codrops-sketches", "InlineLayoutSwitch", "PixelTransition", "soothe"
    ]
}

# 1. Identify category directory names
category_dir_names = set(category_mapping.keys())

# 2. Get list of existing component folders
all_entries = os.listdir(comp_dir)
folders_to_move = []
for entry in all_entries:
    entry_path = os.path.join(comp_dir, entry)
    if os.path.isdir(entry_path) and entry not in category_dir_names:
        folders_to_move.append(entry)

print(f"Total existing component folders to organize: {len(folders_to_move)}")

# Invert mapping to find target category for each folder
folder_to_cat = {}
for cat, folder_list in category_mapping.items():
    for fol in folder_list:
        folder_to_cat[fol] = cat

# 3. Create category folders and move components
manifest = {}
moved_count = 0

for cat in category_mapping.keys():
    cat_path = os.path.join(comp_dir, cat)
    os.makedirs(cat_path, exist_ok=True)

for fol in folders_to_move:
    target_cat = folder_to_cat.get(fol, "09-utilities-and-miscellaneous")
    src_path = os.path.join(comp_dir, fol)
    dest_cat_dir = os.path.join(comp_dir, target_cat)
    dest_path = os.path.join(dest_cat_dir, fol)
    
    try:
        if not os.path.exists(dest_path):
            shutil.move(src_path, dest_path)
            moved_count += 1
            print(f"[MOVED] {fol} -> {target_cat}/{fol}")
        else:
            print(f"[EXISTS] {fol} already in {target_cat}")
        
        manifest[fol] = {
            "name": fol,
            "category": target_cat,
            "rel_path": f"{target_cat}/{fol}",
            "abs_path": dest_path.replace("\\", "/")
        }
    except Exception as e:
        print(f"[MOVE ERROR] Failed {fol}: {e}")

print(f"\nCompleted moving {moved_count} component folders.")

# 4. Generate JSON Manifest
manifest_file = os.path.join(comp_dir, "component_manifest.json")
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)
print(f"[MANIFEST CREATED] {manifest_file}")

# 5. Generate COMPONENTS_TAXONOMY_INDEX.md
index_md_path = os.path.join(comp_dir, "COMPONENTS_TAXONOMY_INDEX.md")
md_lines = [
    "# ZORIXEL AIOS Component Vault Master Index (`COMPONENTS_TAXONOMY_INDEX.md`)",
    "Date: 2026-08-12 · Vault Path: `C:\\Users\\HP\\Downloads\\Components` · Total Repositories: 175",
    "",
    "## Category Overview & Repo Directory",
    ""
]

for cat, f_list in category_mapping.items():
    md_lines.append(f"### {cat.upper()} ({len(f_list)} Repositories)")
    for fol in sorted(f_list):
        rel = f"{cat}/{fol}"
        md_lines.append(f"- **[{fol}]({rel})** — `{rel}`")
    md_lines.append("")

with open(index_md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"[TAXONOMY INDEX CREATED] {index_md_path}")
print("=== COMPONENT ORGANIZATION COMPLETE ===")

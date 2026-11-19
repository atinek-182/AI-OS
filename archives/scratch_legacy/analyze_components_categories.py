import os
import json

comp_dir = r"C:\Users\HP\Downloads\Components"
folders = [f for f in os.listdir(comp_dir) if os.path.isdir(os.path.join(comp_dir, f))]

categories = {
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
        "SlideOutBoxMenu", "underwater-navigation"
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
        "webgl-rotating-image-gallery", "webGLImageTransitions"
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
        "scrolltrigger-image-zoom", "Staggered3DGridAnimations", "telescope-zoom"
    ],
    "06-cursors-and-mouse-effects": [
        "AnimatedCustomCursor", "canvas-cursor", "canvas-grid-mouse-effect", "cursor-line-wobble",
        "custom-curved-corner-scrollbars", "customcursor", "flair-cursor-follower",
        "gsap-cursor-trailer-effect", "satisfying-curly-cursor-3kb-of-vanilla-js-on-canvas"
    ],
    "07-webgl-3d-and-canvas-shaders": [
        "ASCII-Video-Player", "butterflies", "codrops-texture-projection", "codrops_mwg",
        "draw-random-underline-drawsvg", "FoldingDOM", "gsap-threejs-codrops", "infinite-canvas",
        "interactive-particles", "paths-control-points", "Physics-slideshow-threejs-cannonjs",
        "shader-gallary", "shadow", "sketch", "sketch491", "the-substance", "webgl-ascii-hero"
    ],
    "08-full-site-clones-and-preloaders": [
        "3D_CARD", "AnimateSVGTextPath", "butterflies", "ConnectedGrid", "ContentLayoutTransition",
        "creative-kai", "DistortedLinkEffects", "Insane-PRELOADER", "mojito-awwwards-website",
        "MorphingBackgroundShapes", "MorphingPageTransition", "Obys-clone", "PageFlipLayout",
        "Prototype-studio-rebuilt", "RapidLayersAnimation", "shape-overlays", "Spylt-awward-clone",
        "SuperfluidLayout", "SVG-Page-transition"
    ]
}

categorized_set = set()
for cat, folder_list in categories.items():
    for fol in folder_list:
        categorized_set.add(fol)

uncategorized = [f for f in folders if f not in categorized_set]

print(f"Total Folders: {len(folders)}")
print(f"Categorized: {len(categorized_set)}")
print(f"Uncategorized ({len(uncategorized)}): {uncategorized}")

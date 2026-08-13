# Universal Adversarial Roast Council Report: Component Studio Failures Audit & Recovery Spec
Date: 2026-08-12 · Target: 52 Non-Working Component Repositories & Dashboard Copy Button · Operator: Atinek Maurya

## THE VERDICT: RESHAPE (Surgical Root-Cause Repair & Zero-Interference Policy)
Confidence: High · Operator: Atinek Maurya · Domain: code

**The Call in One Line:** All 52 non-working components can be cleanly repaired and launched natively over `http://127.0.0.1:8080` without touching or interfering with any of the 123 working components.

**Why:** The failures stem from 6 distinct technical root causes:
1. Missing `<script type="module">` tags causing `Cannot use import statement outside a module`.
2. Stuck image preloader overlays (`imagesLoaded` blocking DOM display on missing/slow images).
3. GSAP trial version CustomEase deprecation banners.
4. Incorrect entry point paths in `components_ai_registry.json` (pointing to `__MACOSX` or raw `package.json` instead of actual static HTML files inside `dist/`, `public/`, `src/`, or root).
5. Escaped string single-quote syntax errors in `index.html` inline `onclick="copyPrompt(...)"` handlers.
6. Missing pagination navigation links on multi-page sketch archives (COMP-174).

**4-Axis Risk Matrix:**
- Security / Failure Risk: 2/10 (Surgical repairs isolated strictly to target folders)
- Implementation Friction: 3/10 (Automated diagnosis script + precise targeted file edits)
- Value & ROI: 10/10 (Achieves 100% working rate across all 175 components)
- System Simplicity: 9/10 (Eliminates NPM dev server dependencies for static gallery browsing)

**Council Scores:**
- Contrarian: 8/10 ("Do NOT modify global scripts or touched working components. Target strictly the 52 bad folders.")
- Logician: 9/10 ("Group components by technical failure archetype and apply exact surgical patches.")
- Researcher: 9/10 ("All Codrops repos have static HTML entry points either in root, dist/, or src/.")
- UX Specialist: 10/10 ("Fix Copy for AI using data-prompt attributes and event delegation instead of broken inline onclick quotes.")

## ROAST_REFINEMENT_SPEC (Surgical Repair Plan)

### Archetype 1: Dashboard UI Fix (Copy for AI Button)
- [ ] **Fix**: Update `index.html` button generator to use `data-prompt="..."` attributes with HTML entity encoding and a single global click listener using `navigator.clipboard.writeText()` with `document.execCommand('copy')` fallback.

### Archetype 2: Stuck Preloader / Image Overlay (COMP-023, 024, 067, 081, 086, 110, 111, 121, 151, 080, 093, 130)
- [ ] **Fix**: Inject defensive CSS/JS preloader timeout in `index.html` forcing `.loading`, `.preloader`, `#loader` to set `opacity: 0; display: none;` after 600ms if `imagesLoaded` or image network requests stall.

### Archetype 3: GSAP Trial Deprecation Notice (COMP-025)
- [ ] **Fix**: Remove deprecated `CustomEase3.min.js` trial banner script and replace with standard GSAP CustomEase script or inline ease curve.

### Archetype 4: Entry Point Path & NPM Build Fixes (COMP-044, 056, 132, 138, 140, 149, 150)
- [ ] **Fix**: Point `entry_url` to the actual `index.html` inside `dist/`, `public/`, `src/`, or build static HTML entry point. Fix COMP-138 to point to `codrops_mwg/index.html` (stripping `__MACOSX`).

### Archetype 5: ES Module & Script Tag Fixes (COMP-001, 021, 022, 029, 054, 055, 082, 083, 084, 089, 092, 095, 096, 109, 117, 122, 128, 133, 135, 137, 141, 142, 144, 146, 147, 148, 154, 158, 160, 163, 166, 173)
- [ ] **Fix**: Add `type="module"` to main script tags or fix relative CDN script paths for Three.js/GSAP.

### Archetype 6: Multi-Page Navigation Links (COMP-174)
- [ ] **Fix**: Inject a floating navigation bar into COMP-174 pages allowing 1-click navigation between all 29 sketch variants (`001` through `029`).

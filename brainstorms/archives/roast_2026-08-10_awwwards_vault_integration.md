# ZORIXEL AIOS Universal Adversarial Roast Council (`/roast`)
Date: 2026-08-10 · Target: Awwwards Research Vault Ingestion & Web Design Loop Architecture · Operator: Atinek Maurya

## THE VERDICT: RESHAPE (With 3-Stage Token-Safe Vault Routing)
Confidence: High · Operator: Atinek Maurya · Domain: workflow & code

**The Call in One Line:** The overall plan to unify all Awwwards research, 23 site granularity masters, and component vaults is high-value, but needs explicit 3-Stage Token-Safe Vault Routing to prevent token exhaustion and accidental deletion of raw sources.

**Why:** Loading 50+ sub-vault files or 23 site breakdowns simultaneously into an LLM context window will cause severe latency and token blowouts. Furthermore, deleting raw source files in `scratch` before verifying 100% extraction creates data loss risk. The system must use a 3-stage hierarchical lookup (Master Index -> Archetype Match -> 2 Target Files Max).

**Biggest Risk:** Context token explosion and greedy `read_triggers` firing on generic queries, causing the LLM to load 100k+ tokens of raw GSAP/WebGL code for simple web edits.
**Biggest Upside:** A 100% deterministic, award-winning web design engine that transforms raw project briefs into Awwwards SOTD-grade UI architectures with exact GSAP timelines and GLSL shaders.

**4-Axis Risk Matrix:**
- Security / Failure Risk: 3/10 (No security vulnerabilities; main risk is token budget explosion)
- Implementation Friction: 6/10 (Requires reading 20+ raw files line-by-line and writing atomic sub-vault markdowns)
- Value & ROI: 10/10 (Gives ZORIXEL an unmatchable Awwwards web creation engine)
- System Simplicity: 7/10 (Clean 3-stage hierarchy prevents vault clutter)

**Council Scores:**
- Contrarian: 4/10 (Warning: Strict token cap required; do not load all 23 sites at once)
- Expansionist: 10/10 (Huge competitive moat for ZORIXEL AI Agency)
- Logician: 8/10 (3-stage lookup solves context limits mathematically)
- Researcher: 9/10 (23 sites are top-tier award winners with proven GLSL/GSAP code)
- Buyer: 9/10 (Atinek Maurya gets 1-click Awwwards-grade site generation)

**The Cheapest 48-Hour Test:**
Perform line-by-line reading of the first 3 raw case study files (Trionn, ZERO, Obys), create their atomic sub-vault files in `03` and `04`, and test `website-design-engine` Phase 0 matching to verify token consumption stays under 8k tokens.

## ROAST_REFINEMENT_SPEC (Required Fixes Before Execution)
- [ ] **Fix 1: 3-Stage Hierarchical Vault Discovery**: Enforce a strict 3-Stage Lookup Rule in `website-design-engine/SKILL.md` and `loop-engine/SKILL.md`:
  - Stage 1: Read `references/AWWWARDS_MASTER_INTELLIGENCE_INDEX.md` (~2k tokens).
  - Stage 2: Match brief to 1 of 5 Archetype Clusters (Editorial, GSAP Motion, 3D WebGL, Dark Modern, Minimal Luxury).
  - Stage 3: Load ONLY the matching 2-3 site granularity master files + 1 relevant sub-vault topic file (~8k tokens max).
- [ ] **Fix 2: Precision `read_triggers` Guard**: Scope YAML frontmatter `read_triggers` tightly with explicit multi-word triggers (e.g. `"When building Awwwards-grade websites with GSAP Lenis"` instead of `"CSS"`) so non-web tasks never trigger vault loading.
- [ ] **Fix 3: Non-Lossy Verification Before Scratch Cleanup**: Never delete any raw markdown in `scratch/awwwards_ingestion_raw/` until 100% of its GSAP code, GLSL shaders, typography rules, and spatial math are verified as present in `references/awwwards-research-vault/`.
- [ ] **Fix 4: Checklist & Skill Reference Upgrade**: Update `06-awwwards-judging-criteria-and-master-checklist` and `website-design-engine/references/05-anti-slop-quality-gates.md` with the 57 Awwwards Scoring Standards and 23-site quality rules.

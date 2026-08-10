---
title: Awwwards Research Vault 02 - Typography, Spacing & Grid Math
domain: reference
summary: Technical reference specification defining Obys spatial padding math (140px-160px), 12-column asymmetric bento grids, typography golden ratio scale (1.618), line-height rules, and 8px modular spacing systems for Awwwards web creation.
critical_directives:
- Desktop vertical section padding MUST be 140px to 160px (Obys Spatial Rhythm).
- Display headlines larger than 64px MUST specify line-height: 1.28 and margin-bottom: 28px.
- Use 12-column asymmetric bento grids with 24px column gaps.
- Follow zero-emoji mandate across all CSS, tokens, and docs.
section_outline:
- Awwwards Research Vault 02 - Typography, Spacing & Grid Math
- Obys Spatial Padding & Vertical Rhythm Ratios
- The 12-Column Asymmetric Bento Grid Math
- Typography Scale & Line-Height Math Rules
- The 8px Modular Spacing System
read_triggers:
- When working on reference in references/awwwards-research-vault/02-awwwards-typography-spacing-grid-math.md
- When reading context for Awwwards Typography, Spacing & Grid Math
tags:
- reference
- awwwards
- typography
- grid-math
- spacing
updated: '2026-08-09'
---

# Awwwards Research Vault 02 - Typography, Spacing & Grid Math

## Overview

Precision in spacing and typography scale is the signature trait separating amateur websites from Awwwards Site of the Day winners. This technical specification details the mathematical formulas, grid configurations, and vertical rhythm ratios required for Awwwards-grade layout composition.

---

## Obys Spatial Padding & Vertical Rhythm Ratios

Obys Agency spatial rhythm enforces generous vertical breathing room to convey luxury and editorial polish:

| Viewport Category | Screen Width Range | Section Vertical Padding | Container Max Width |
|---|---|---|---|
| **Ultra-Wide Desktop** | `>= 1440px` | `160px` top / bottom | `1400px` |
| **Standard Desktop** | `1024px - 1439px` | `140px` top / bottom | `1200px` |
| **Tablet Landscape** | `768px - 1023px` | `96px` top / bottom | `90%` |
| **Mobile Screen** | `< 768px` | `64px` to `80px` top / bottom | `92%` |

---

## The 12-Column Asymmetric Bento Grid Math

The 12-column grid is the standard because 12 is cleanly divisible by 2, 3, 4, and 6. Awwwards layouts start with this 12-column skeleton and intentionally create asymmetric bento compositions:

```css
/* Awwwards 12-Column Bento Grid Container */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 24px;
  width: 100%;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

/* Asymmetric Bento Span Ratios */
.bento-hero-card   { grid-column: span 8 / span 8; }
.bento-side-card   { grid-column: span 4 / span 4; }
.bento-full-width  { grid-column: span 12 / span 12; }
.bento-tri-card    { grid-column: span 4 / span 4; }

@media (max-width: 768px) {
  .bento-grid {
    grid-template-columns: repeat(1, minmax(0, 1fr));
    gap: 16px;
  }
  .bento-hero-card,
  .bento-side-card,
  .bento-tri-card {
    grid-column: span 1 / span 1;
  }
}
```

---

## Typography Scale & Line-Height Math Rules

### Typography Scale (Golden Ratio 1.618)
- `Display Title XL`: `120px` (7.5rem)
- `Display Title L`: `80px` (5rem)
- `Headline H1`: `64px` (4rem)
- `Headline H2`: `40px` (2.5rem)
- `Subheading H3`: `28px` (1.75rem)
- `Body Large`: `20px` (1.25rem)
- `Body Regular`: `16px` (1rem)
- `Caption / Tag`: `13px` (0.8125rem)

### Line-Height & Margin Rules
- **Display Headlines (`> 64px`)**: `line-height: 1.28` (prevents multi-line headline overlap) and minimum `margin-bottom: 28px`.
- **Subheadings (`24px - 40px`)**: `line-height: 1.35`, `margin-bottom: 16px`.
- **Body Text (`16px - 20px`)**: `line-height: 1.6`, `margin-bottom: 12px`.

---

## Extended Font & Variable Font Width Specification

Extended fonts feature wider character proportions designed by type artisans, commanding hero presence on display headlines.

### Extended vs. Artificial Distortion (`scaleX`) Rule
- **True Extended Variant**: Designed in font glyph geometry. Bowls, counter spaces, and crossbars stretch in balance without distorting vertical stroke weights.
- **Artificial Scale (`transform: scaleX(1.3)`)**: Strictly banned. Artificial stretching corrupts stroke thickness and fails visual audit gates.

### CSS `font-stretch` & Variable Font `wdth` Settings
```css
/* Modern Extended Display Typography Specification */
.awwwards-extended-title {
  font-family: 'Barlow Variable', 'Trade Gothic Extended', sans-serif;
  font-variation-settings: "wdth" 125, "wght" 800; /* Expanded width axis */
  font-stretch: expanded; /* Full modern browser support fallback */
  font-size: clamp(48px, 6vw, 110px);
  line-height: 1.15;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  margin-bottom: 28px;
}
```

### Approved Extended Font Families
1. **Barlow Expanded**: High-performance open-source variable font family with `wdth` axis range `75% - 125%`.
2. **Trade Gothic Extended**: Premium editorial display typeface for high-end digital agency flagships.
3. **Akira Expanded**: Ultra-bold display font for brutalist headers and poster section titles.

- **Body Text (`16px - 20px`)**: `line-height: 1.6`, `max-width: 65ch` for optimal reading baseline.

---

## The 8px Modular Spacing System

All internal padding, margins, and gaps strictly align to an 8px modular grid:
- `8px` - Micro gap / icon padding
- `16px` - Compact element spacing / button padding
- `24px` - Grid column gap / card internal padding (mobile)
- `32px` - Card internal padding (desktop)
- `48px` - Group spacing / header bottom margin
- `64px` - Component block separation
- `140px` - Section vertical padding

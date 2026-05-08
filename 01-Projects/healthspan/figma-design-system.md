# Figma Design System: Healthspan
Phase: 0 — Visual Brand Profile (Extension of Phase 0)
Date: 2026-05-07
Agent: Primary Agent
Status: File created — design system pages pending (Figma Starter plan MCP limit)

---

## Figma File

**File name:** Healthspan — Design Foundation
**File key:** `wj0P7v1prSF6VyJGkJkTS1`
**File URL:** https://www.figma.com/design/wj0P7v1prSF6VyJGkJkTS1
**Location:** Personal drafts (Starter plan — View seat in team)

**Pages to build (pending MCP limit reset or plan upgrade):**
1. Design System — color palette, typography scale, spacing tokens
2. Homepage Reference — full page screenshot + 17-section annotation
3. Social Templates — 5 blank brand-ready frames

---

## Design Tokens (Extracted from Live CSS)

All values extracted directly from `gethealthspan.com` production CSS.
Source: `/_next/static/css/399b41114f71e48c.css`, `094ae032cfba8f5f.css`, `74aaee6d67408879.css`

---

### Typography

| Variable | Value |
|----------|-------|
| `--font-default` | `"Suisse Intl"` — primary UI and display font |
| `--font-decorative` | `"Soehne Mono"` — monospace accent font |

**Suisse Intl weights in use:**
- 400 (Regular) — `SuisseIntl-Regular.woff2`
- 500 (Medium) — `SuisseIntl-Medium.woff2`
- 700 (Semibold) — `SuisseIntl-Semibold.woff2`

**Soehne Mono weights in use:**
- 400 (Regular) — `soehne-mono-buch.woff2`
- 400 Italic — `soehne-mono-buch-kursiv.woff2`

**Font Size Scale:**
| Token | Value | Use case |
|-------|-------|----------|
| `--font-size-xxxs` | 8px | Micro labels |
| `--font-size-xxs` | 10px | |
| `--font-size-xs` | 12px | Captions |
| `--font-size-sm` | 14px | Body small |
| `--font-size-md` | 16px | Body regular |
| `--font-size-lg` | 18px | Body large |
| `--font-size-xl` | 20px | |
| `--font-size-xxl` | 24px | |
| `--font-size-heading-xxs` | 18px | |
| `--font-size-heading-xs` | 20px | |
| `--font-size-heading-sm` | 24px | |
| `--font-size-heading-md` | 28px | |
| `--font-size-heading-lg` | 32px | |
| `--font-size-heading-xl` | 40px | |
| `--font-size-display-xs` | 48px | |
| `--font-size-display-sm` | 56px | |
| `--font-size-display-md` | 64px | |
| `--font-size-display-lg` | 96px | |
| `--font-size-display-xl` | 120px | Hero headline |

**Font Weight Scale:**
- 300 — light
- 400 — regular
- 500 — medium
- 700 — bold

---

### Color System

#### Base
| Token | Hex | Use |
|-------|-----|-----|
| `--color-black` | `#000000` | Text primary |
| `--color-white` | `#ffffff` | Background, text inverted |

#### Neutral (Gray)
| Token | Hex |
|-------|-----|
| `--color-neutral-100` | `#f7f7f7` |
| `--color-neutral-200` | `#e5e5e5` |
| `--color-neutral-300` | `#adadad` |
| `--color-neutral-400` | `#888888` |
| `--color-neutral-500` | `#676767` |
| `--color-neutral-900` | `#1a1a1a` |

#### Indigo (Brand Primary — Blue)
| Token | Hex |
|-------|-----|
| `--color-indigo-50` | `#eaf2fa` |
| `--color-indigo-100` | `#cadff3` |
| `--color-indigo-200` | `#81b1e2` |
| `--color-indigo-300` | `#5999d9` |
| `--color-indigo-400` | `#2666a6` |
| `--color-indigo-500` | `#133353` |

#### Powder Blue (Brand Secondary — Accent Blue)
| Token | Hex |
|-------|-----|
| `--color-powder-blue-100` | `#deecfa` |
| `--color-powder-blue-200` | `#c4e0f8` |
| `--color-powder-blue-300` | `#5a9bea` |
| `--color-powder-blue-400` | `#3375dc` |
| `--color-powder-blue-500` | `#264582` |

#### Orchre (Warm Accent)
| Token | Hex |
|-------|-----|
| `--color-orchre-50` | `#fff5e6` |
| `--color-orchre-100` | `#feeacd` |
| `--color-orchre-200` | `#fcc169` |
| `--color-orchre-300` | `#fba626` |
| `--color-orchre-400` | `#c87a04` |
| `--color-orchre-500` | `#643d02` |

#### Solar (Gold Accent)
| Token | Hex |
|-------|-----|
| `--color-solar-50` | `#fffce6` |
| `--color-solar-100` | `#fffacc` |
| `--color-solar-200` | `#fef38e` |
| `--color-solar-300` | `#feef67` |
| `--color-solar-400` | `#cab602` |
| `--color-solar-500` | `#655b01` |

#### Sage (Green Accent)
| Token | Hex |
|-------|-----|
| `--color-sage-50` | `#f1f8ed` |
| `--color-sage-100` | `#e3f1da` |
| `--color-sage-200` | `#a5d088` |
| `--color-sage-300` | `#90c56d` |
| `--color-sage-400` | `#5d923a` |
| `--color-sage-500` | `#2f491d` |

#### Lilac (Purple Accent)
| Token | Hex |
|-------|-----|
| `--color-lilac-50` | `#d6cefb` |
| `--color-lilac-100` | `#bdb0f8` |
| `--color-lilac-200` | `#b0a4e8` |
| `--color-lilac-300` | `#625793` |
| `--color-lilac-400` | `#4e4879` |
| `--color-lilac-500` | `#0a151c` |

#### Status Colors
| Name | 100 | 300 | 500 |
|------|-----|-----|-----|
| Calm Green (success) | `#e1f7e6` | `#56d391` | `#084b2e` |
| Urgent Red (error) | `#ffe2e1` | `#ff5850` | `#841d18` |
| Heal Yellow (warning) | `#fff8c8` | `#f6c64f` | `#733b10` |
| Cell Pink (supportive) | `#fee5f1` | `#ff81b8` | `#8d0e37` |

---

### Semantic Color Mappings

| Semantic Token | Maps to |
|----------------|---------|
| `--color-bg-fill-primary` | Black (`#000000`) |
| `--color-bg-base-light` | White (`#ffffff`) |
| `--color-text-primary` | Black (`#000000`) |
| `--color-text-primary-inverted` | White (`#ffffff`) |
| `--color-text-secondary` | Neutral 500 (`#676767`) |
| `--border-color-light` | Neutral 200 (`#e5e5e5`) |

---

## Homepage Sections (17 total — for Page 2 annotation)

1. Navigation header
2. Hero — "Transform your quality of living through the science of aging"
3. Key features / trust badges (Trustpilot, HSA/FSA, 12K patients, 70+ biomarkers)
4. Personalized care section
5. Trust metrics (1st digital longevity clinic, 4.9★, 20+ years, 150+ publications)
6. Programs section (Longevity, Men's Hormones, Women's Hormones, GLP-1)
7. Treatments showcase (tabbed: Medications, Supplements, Labs — 17 products)
8. MySpan platform section
9. Care team section
10. Media recognition (Washington Post, WSJ, USA Today, Business Insider)
11. Patient journey (4-step process)
12. Testimonials
13. Differentiator comparison table
14. Research section (featured articles)
15. Mission statement
16. Newsletter signup
17. Footer

---

## Social Template Frames (for Page 3)

| Format | Dimensions | Platform |
|--------|-----------|----------|
| Instagram Square | 1080 × 1080 px | Feed |
| Instagram Portrait | 1080 × 1350 px | Feed (portrait) |
| Instagram Story | 1080 × 1920 px | Stories / Reels |
| LinkedIn Landscape | 1200 × 627 px | LinkedIn |
| Twitter/X Banner | 1600 × 900 px | Twitter/X posts |

---

## Status

- [x] Figma file created
- [x] Design tokens extracted from production CSS
- [x] Design System page built — Color Palette (55 swatches, 12 groups) + Typography Scale (19 sizes)
- [x] Homepage Reference page built — 17 annotated section cards
- [x] Social Templates page built — 5 frames at exact export dimensions
- [x] creative-prompter.md updated with Figma reference

# Correction Log: GLP-1 Ad Figma — CEO Manual Corrections
Date: 2026-05-07
Agent: Primary Agent (Tier 1) — documenting CEO correction
Phase: 1 — Test Creative

---

## What Was Corrected

CEO reviewed the AI-built Figma ad layout and made manual corrections to typography scale, scrim approach, and overall visual hierarchy. The corrected version is the source of truth going forward.

---

## Original State (AI-built) vs Corrected State (CEO)

| Element | AI Original | CEO Correction | Reason |
|---------|------------|----------------|--------|
| HEALTHSPAN wordmark | 20px Bold, white | **40px Bold, white** | Too small — not legible as brand anchor |
| LONGEVITY PROTOCOL eyebrow | 13px Bold, #81b1e2 | **24px Bold, white** | Illegible at feed scale; color lacked hierarchy |
| Headline | 58px Bold, white | **55px Bold, white** | Minor tightening |
| Sub-headline | 22px Regular, #cadff3 | **22px Medium, white** | Bumped weight; changed to white for cleaner tone |
| Social proof | 15px Regular, #81b1e2 | **Unchanged** | Correct as accent/supporting copy |
| CTA Button | 256×60px, r=30 | **303×71px, r=30** | Larger pill for stronger CTA presence |
| CTA Label | 18px Bold, #133353 | **32px Bold, #133353** | Far too small — nearly unreadable |
| Gradient scrim | 5 stacked bands (5%→25%→55%→80%→100%) | **Single gradient rect y=675, h=410** | Simpler, cleaner, native Figma gradient |
| Image node | MCP-imported blurry 400×400 JPEG | **Full-res CEO drag-and-drop, 1080×1080** | MCP import quality insufficient for production |

---

## Final Frame State After CEO Corrections

**Figma File:** `wj0P7v1prSF6VyJGkJkTS1` — Social Templates page — node 1:179

Layer stack (bottom → top):
| Node | Name | Position | Size | Style |
|------|------|----------|------|-------|
| 1:212 | ChatGPT Image | (0,0) | 1080×1080 | Full-res portrait, fill frame |
| 1:214 | Scrim (gradient) | (0,675) | 1080×410 | Gradient: transparent → #133353 |
| 1:202 | HEALTHSPAN | (60,56) | — | 40px Bold, white |
| 1:203 | LONGEVITY PROTOCOL | (60,700) | — | 24px Bold, white |
| 1:204 | Headline | (60,729) | — | 55px Bold, white |
| 1:205 | Sub-headline | (60,810) | — | 22px Medium, white |
| 1:206 | Social proof | (60,862) | — | 15px Regular, #81b1e2 |
| 1:207 | CTA Button | (60,918) | 303×71, r=30 | Fill: white |
| 1:208 | CTA Label | (98,934) | — | 32px Bold, #133353 |

---

## Root Cause of Original Errors

1. **Typography under-scaled** — applied UI/web sizing conventions to ad creative. Ad creative requires much heavier typography to survive mobile feed at thumb-scroll speed.
2. **Scrim over-engineered** — attempted to simulate a gradient with stacked semi-transparent bands because MCP `set_fills` doesn't support gradient fills. This is noisy and inferior. Correct solution: set gradient in Figma UI directly.
3. **MCP image import impractical** — base64 token limits force heavy compression. Production hero images must be imported manually via Figma drag-and-drop.

---

## Knowledge Applied Forward

See `08-Logs/knowledge-checks/2026-05-07-ad-creative-design-lessons.md` for the full lesson distillation.

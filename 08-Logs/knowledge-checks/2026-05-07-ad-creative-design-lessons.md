# Knowledge Check: Ad Creative Design — Lessons from Phase 1 Test Creative
Date: 2026-05-07
Agent: Primary Agent (Tier 1)
Source: CEO corrections to Healthspan GLP-1 Instagram ad

---

## Gap Closed

Did not have internalized standards for ad creative typography, scrim architecture, or image import workflows before this session. Applied web/UI conventions to ad creative — which CEO correctly identified as wrong.

---

## Lessons

### 1. Ad Typography Scale Is Completely Different from Web/UI Scale

Web UI elements can survive at 13–16px because users zoom in, click, and interact. Ad creatives are consumed at thumb-scroll speed on mobile. Everything must be readable in under a second.

**Rule:** When in doubt, go bigger. Doubled or near-doubled sizes were correct (18px → 32px CTA, 13px → 24px eyebrow, 20px → 40px wordmark).

Minimum viable sizes for 1080×1080 Instagram ads:
- Brand wordmark: 36px+ Bold
- Category eyebrow: 22px+ Bold
- Primary headline: 52–62px Bold
- Sub-headline: 20–24px Medium
- CTA: 28–36px Bold inside 280×65px+ pill

### 2. Color Hierarchy in Ads: White = Signal, Brand Color = Accent Only

Original approach: used brand blue (#81b1e2, #cadff3) on sub-copy and eyebrows. This created too many competing tones and no clear reading hierarchy.

CEO corrected to: **all primary copy = white, brand blue = social proof / trust badges only.**

This is a standard ad design principle: the image provides color; the copy should be white (maximum legibility on dark scrims). Brand color is reserved for the element that needs to be noticed second — not first.

### 3. Gradient Scrims — One Clean Layer, Not Stacked Bands

Stacked semi-transparent rectangles simulating a gradient look noisy and produce visible banding in the actual render. Figma's native gradient fill on a single rectangle produces a smoother result.

**MCP limitation:** `set_fills` only supports solid hex colors. Cannot set gradient fills via MCP. Must use Figma UI for any gradient.

Scrim positioning for portrait-dominant ads:
- Start at roughly 60–65% of the frame height (y=650–700 in a 1080px frame)
- Cover from there to bottom of frame
- Gradient: transparent at top → solid brand dark at bottom

### 4. Hero Images — CEO Drag-and-Drop, Not MCP Import

MCP `import_image` requires base64 passed inline. Token limits cap the usable resolution at ~400×400 JPEG Q60. At that compression level, stretched to 1080px, the image is an unrecognizable blurry blob.

**Workflow:** Use MCP for layout scaffolding (placeholders, text, buttons). For final hero image, tell CEO to drag-and-drop directly in Figma. Full quality, no compression, no pipeline overhead.

### 5. Full-Frame Portrait > Cropped Hero Zone

Original layout: hero image cropped to 680px height (top zone only), then dark panel below for text.

CEO corrected to: full 1080×1080 portrait filling the entire frame. Gradient scrim handles the transition. This looks more premium — the subject bleeds to all edges, the scrim creates depth rather than a hard panel split.

### 6. Simpler Is Always Better

Each time the AI added complexity (5-band scrim, multiple placeholder layers, template labels), the CEO simplified it. The final design had fewer nodes, cleaner naming, and a more professional result.

**Rule:** When building Figma layouts via MCP, prioritize the minimum number of nodes needed. Every layer that isn't necessary is something the CEO has to clean up.

---

## Applied To

- Memory: `feedback_ad_creative_standards.md`
- Memory: `feedback_figma_mcp_limitations.md`
- Correction log: `08-Logs/corrections/2026-05-07-glp1-ad-figma-ceo-corrections.md`

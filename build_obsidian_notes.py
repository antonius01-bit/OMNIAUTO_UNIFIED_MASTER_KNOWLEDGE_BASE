import json
import os

with open(r'C:\Users\antoni\Dola\parsed_visual_shortcuts.json', 'r', encoding='utf-8') as f:
    shortcuts = json.load(f)

# 1. THE_VISUAL_PROMPT_BOOK_200_SHORTCUTS.md
content = """---
title: "The Visual Prompt Book — 200 Image & Video Shortcuts (2026 Edition)"
created: 2026-09-25
tags: [dola, agy, prompt-master, visual-prompts, midjourney, flux, higgsfield, chatgpt]
type: reference
---

# 🎨 The Visual Prompt Book: 200 Image & Video Shortcuts (2026 Edition)
*Master Prompt Shorthands for ChatGPT, Midjourney v6+, FLUX.1, Ideogram 4.0, Recraft 4.1, and Higgsfield AI.*

---

## ⚡ The 5-Part Universal Brief Anatomy
Always format image/video requests using this exact formula:
```text
[Shortcut] for [subject].
Use [references].
Keep [fixed details].
Change [specific elements].
Style: [look, lighting, color palette, camera lens].
Include this exact text: "[words]".
Format: [aspect ratio / shape / dimensions].
```

---

## 🔗 The 3 Connected Production Workflows

### 1. Product Launch
`[[/productshot]]` ➔ `[[/colorways]]` ➔ `[[/staticad]]` ➔ `[[/productreel]]`  
*Rule*: Approve product geometry and packaging in `/productshot` first, then reuse that reference at every subsequent stage.

### 2. Executive & Personal Brand Suite
`[[/headshot]]` ➔ `[[/linkedinbanner]]` ➔ `[[/quotecard]]`  
*Rule*: Maintain the exact same facial landmarks, skin tones, color grading, and typography styling across all three assets.

### 3. Technical & Explainer Narrative
`[[/processdiagram]]` ➔ `[[/slidevisual]]` ➔ `[[/explainerclip]]`  
*Rule*: Verify factual accuracy, label hierarchy, and logic flow before adapting the concept into motion.

---

## 📚 Complete Catalog of 200 Shortcuts
"""

collections = [
    ('01 Six Ways to Begin', 1, 6),
    ('02 People & Portraits', 7, 26),
    ('03 Products in Focus', 27, 46),
    ('04 Form, Parts & Dimension', 47, 66),
    ('05 Campaigns & Conversion', 67, 86),
    ('06 Identity & Brand Systems', 87, 106),
    ('07 Made for the Feed', 107, 126),
    ('08 Design in Context', 127, 146),
    ('09 Food, Rooms & Places', 147, 166),
    ('10 Style Experiments', 167, 186),
    ('11 Ideas Made Clear & Personal Projects', 187, 195),
    ('12 Pictures into Motion', 196, 200)
]

for col_name, start_idx, end_idx in collections:
    content += f"\n### {col_name}\n"
    items = [x for x in shortcuts if start_idx <= int(x['num']) <= end_idx]
    for item in items:
        content += f"- **`{item['num']} {item['command']}`**: {item['description']}\n"

target_file = r'C:\Users\antoni\Dola\obsidian_vault\01_PROMPT_ENGINEERING\THE_VISUAL_PROMPT_BOOK_200_SHORTCUTS.md'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {target_file}")

# 2. HIGGSFIELD_AI_VIDEO_MULTIMODAL_API.md
higgs_content = """---
title: "Higgsfield AI Video & Multimodal API Architecture"
created: 2026-09-25
tags: [dola, agy, higgsfield, video-ai, genjutsu, seedance, kling]
type: deliverable
---

# 🎬 Higgsfield AI Video & Multimodal API Architecture

## 🚀 Overview
The Higgsfield AI API Platform (`https://open.higgsfield.ai`) provides production-grade endpoints for video synthesis, video-to-video motion transfer, character consistency, and multimodal scene direction.

## 📊 Core Model Catalog
1. **`bytedance/Seedance 2.5`**: 30-second multi-reference video generation with native audio.
2. **`higgsfield/Genjutsu`**: Groundbreaking **Motion Transfer** engine that replaces characters/styles while 100% preserving camera motion, speed, physics, and actor timing.
3. **`kling/Kling 3.0`**: 4K Ultra-HD multi-shot sequences with start/end frames.
4. **`higgsfield/Cinema Studio 4.0`**: Cinematic videos with automatic scene direction.
5. **`alibaba/Wan 3.0 Prime`**: Rapid 30s video rendering with native audio.
6. **`lightricks/LTX 2.5 Pro`**: Full 6-axis camera motion control (pan, tilt, zoom, dolly, roll).
7. **`higgsfield/Soul 2`**: High-end fashion and editorial photography with realistic skin texture.
8. **`ideogram/Ideogram 4.0`**: Flawless typography and signage rendering.

## 🔄 Integration with The Visual Prompt Book (S238)
Pair `/animated`, `/productreel`, `/360orbit`, or `/unboxingvideo` directly with Higgsfield API calls for automated clip rendering.
"""

higgs_file = r'C:\Users\antoni\Dola\obsidian_vault\09_AI_WORKFLOW\HIGGSFIELD_AI_VIDEO_MULTIMODAL_API.md'
with open(higgs_file, 'w', encoding='utf-8') as f:
    f.write(higgs_content)
print(f"Created {higgs_file}")

# 3. PAYOUTVAULT_5DAY_TRADER_RESET_FRAMEWORK.md
payout_content = """---
title: "PayoutVault 5-Day Systematic Trader Reset & Risk Engine"
created: 2026-09-25
tags: [dola, agy, finance, trading, risk-management, prop-firms, payoutvault]
type: deliverable
---

# 📈 PayoutVault 5-Day Trader Reset & Risk Architecture
*Standard Reference: Filip Gajko / Effata Core (payoutvault.one)*

## 🛡️ The 5-Day Reset Protocol
1. **Day 1: Bias Before The Open**
   - Identify Draw on Liquidity (DOL).
   - Write directional bias AND exact invalidation level before session opens. If invalidated, stop trading.
2. **Day 2: Levels & Liquidity (The 3-Line Rule)**
   - Line 1: Primary Draw on Liquidity.
   - Line 2: Major opposing HTF zone.
   - Line 3: Internal range liquidity pool.
3. **Day 3: One Frozen Trigger**
   - Freeze one single mechanical trigger (e.g. 5m body close confirmation). Zero intuition, zero wick-chasing.
4. **Day 4: Risk First**
   - Stop distance strictly dictates position size.
   - Hard cap on daily loss limit (DLL).
5. **Day 5: The Forensic Audit**
   - Log all trades into unified schema. Eradicate repeat behavioral leaks.

## 🛠️ Integrated Tool Suite
- CRT Engine (Candle Range Theory)
- VWAP Suite
- SMT Autopilot (Smart Money Technique Divergence)
"""

payout_file = r'C:\Users\antoni\Dola\obsidian_vault\06_FINANCE\PAYOUTVAULT_5DAY_TRADER_RESET_FRAMEWORK.md'
with open(payout_file, 'w', encoding='utf-8') as f:
    f.write(payout_content)
print(f"Created {payout_file}")

# 4. MINDFUL_AGENTIC_ENGINEERING_MANIFESTO.md
mindful_content = """---
title: "Mindful Agentic Engineering Manifesto (Anti-Churn Discipline)"
created: 2026-09-25
tags: [dola, agy, engineering, architecture, code-quality, ponytail-discipline, tdd]
type: concept
---

# 🧠 Mindful Agentic Engineering Manifesto (Anti-Churn Architecture)
*Countering the "Talk to Claude. Generate. Ship. Repeat. Nobody is thinking anymore." trap.*

## 🚫 The Problem: The AI Code Churn Hamster Wheel
Recent engineering reports highlight an emerging dysfunction:
- Developers feel miserable supervising endless streams of unreviewed, AI-generated code.
- Pressure to ship 10x more volume replaces architectural contemplation.
- Unverified code creates catastrophic technical debt and fragile architectures.

## 💎 The Dola AI / AGY Solution: Mindful Craftsmanship
1. **The 30-Second Comprehension Rule**: Never accept an AI diff unless you can explain every line, edge case, and failure mode within 30 seconds.
2. **Surgical Diffs**: Reject 300-line rewrites when a 5-line diff solves the issue (`senior-dev-ponytail-discipline`).
3. **TDD-First Safety Guard**: Write the test that proves the bug *before* invoking the AI.
4. **Zero-Slop Standard**: Strip boilerplate, hallucinated imports, and unnecessary dependencies.
5. **Reclaiming Cognitive Time**: Use AI efficiency to think 10x deeper about system architecture, performance, and security.
"""

mindful_file = r'C:\Users\antoni\Dola\obsidian_vault\05_OPERATIONS\MINDFUL_AGENTIC_ENGINEERING_MANIFESTO.md'
with open(mindful_file, 'w', encoding='utf-8') as f:
    f.write(mindful_content)
print(f"Created {mindful_file}")

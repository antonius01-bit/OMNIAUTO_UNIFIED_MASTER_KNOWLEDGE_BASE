---
name: diagram-design-academic-visualizer
description: Editorial-quality, publication-ready SVG and standalone HTML diagram generator based on cathrynlavery diagram-design and GitHub advanced formatting. Replaces generic AI Mermaid slop with polished, zero-dependency visual diagrams including architecture views, sequence flows, state machines, Wardley maps, quadrants, and timelines across 3 themes.
---

# 📊 S132 — Diagram Design Academic Visualizer (`diagram-design-academic-visualizer`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories**:
  - [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) (Editorial-quality diagram suite designed for AI coding assistants: Claude Code, Codex, Pi, and Antigravity).
  - [GitHub Advanced Diagramming](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) (GitHub Markdown diagram standards).
  - [GitHub Topics: Academic Diagrams](https://github.com/topics/academic-diagrams) (Vector graphics for academic journals and technical whitepapers).
- **Core Philosophy**: **Anti-Slop Visual Craftsmanship**. Standard LLMs routinely generate primitive, cluttered Mermaid.js diagrams with broken layouts, unreadable labels, and harsh default palettes. This super-skill generates clean, bespoke, self-contained SVG and responsive HTML diagrams that look handcrafted by an elite publication designer.

---

## 🏛️ Supported Diagram Catalog (Dozens of Types)

| Category | Diagram Types Included | Primary Use Cases |
|---|---|---|
| **System Architecture** | Multi-tier cloud, distributed agent mesh, microservices, pipeline topology | Technical specifications, RFCs, system architecture documents |
| **Process & Flow** | Flowcharts, swimming-lane workflows, user journeys, decision trees | Business runbooks, SOPs, algorithm explanations |
| **Interaction & Protocol** | UML sequence diagrams, handshake flows, API call choreographies | Security protocol audits, multi-agent communication traces |
| **Behavior & State** | Finite state machines (FSM), statecharts, lifecycle diagrams | Agent execution harnesses, transaction lifecycles |
| **Strategy & Analysis** | Wardley maps, 2x2 quadrant matrices, Eisenhower matrix, SWOT grids | Competitive analysis, strategic planning, risk modeling |
| **Temporal & Roadmaps** | Milestone timelines, sprint Gantt flows, phase roadmaps | Project proposals, grant applications, executive summaries |
| **Operational & Task** | Kanban boards, funnel flows, RACI matrix visualizations | Sprint reviews, team organization, product telemetry |

---

## 🎨 Design System & Theming Heuristics

Every generated visual artifact adheres strictly to professional design heuristics:
1. **Zero External Dependencies**: Self-contained SVG or pure inline HTML/CSS. Renders perfectly offline without external font CDN or script tags.
2. **3 Cohesive Variants**:
   - **Minimal Light**: Clean white background (`#ffffff`), slate borders (`#e2e8f0`), charcoal text (`#1e293b`). Ideal for print and IEEE/ACM PDFs.
   - **Minimal Dark**: Deep navy/slate background (`#0f172a`), muted grid lines (`#1e293b`), crisp white typography (`#f8fafc`). Ideal for modern developer portals.
   - **Full Editorial**: Refined typography scales, subtle accent gradients, card drop-shadows, and elegant badge tags. Ideal for executive presentations.
3. **Typography Precision**: Clean system sans-serif font stack (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`). Minimum text size $\ge 12\text{px}$ for perfect legibility.
4. **Accessible Contrast**: All text-to-background combinations maintain WCAG AAA compliance ($\ge 7:1$). Colorblind-safe palette mappings.

---

## 💻 SVG Generation Template (Architecture Pattern)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <style>
      .card { fill: #ffffff; stroke: #e2e8f0; stroke-width: 1.5; rx: 8; }
      .header { font-family: system-ui, sans-serif; font-size: 14px; font-weight: 600; fill: #0f172a; }
      .body { font-family: system-ui, sans-serif; font-size: 12px; fill: #64748b; }
      .badge { fill: #eff6ff; stroke: #bfdbfe; rx: 4; }
      .badge-text { font-family: system-ui, sans-serif; font-size: 11px; fill: #1d4ed8; font-weight: 500; }
      .arrow { stroke: #94a3b8; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#94a3b8" />
    </marker>
  </defs>
  <!-- Rendered Cards, Nodes, and Connected Connectors -->
</svg>
```

---

## 🚀 Triggers & Operational Commands
- `/omni-auto diagram: Generate editorial-quality [architecture/sequence/state/wardley] diagram for [system_description] in [minimal_light/minimal_dark/editorial] theme.`
- `/omni-auto diagram-academic: Render publication-ready vector figure for [manuscript_section] matching ACM/IEEE journal standards.`
- `/omni-auto diagram-replace: Convert messy Mermaid diagram in [file.md] into a pristine, high-taste SVG visual.`
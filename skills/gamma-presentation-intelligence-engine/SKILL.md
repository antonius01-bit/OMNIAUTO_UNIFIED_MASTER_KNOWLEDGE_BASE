---
name: gamma-presentation-intelligence-engine
description: Enterprise AI presentation design and browser-native slide rendering engine powered by Gamma App open-source components and PPTX renderers. Automates outline-to-slide generation, card-based layouts, responsive presentation streaming, and n8n workflow triggers.
---

# S110: Gamma Presentation Intelligence Engine (gamma-presentation-intelligence-engine)

## ⚡ Overview & Presentation Architecture
Synthesized from Gamma App open-source components (`gamma-app/pptx-renderer`, `n8n-nodes-gamma`, `aijsx`):
1. **Browser-Native High-Fidelity PPTX Renderer (`gamma-app/pptx-renderer`)**:
   - Parses raw Office Open XML (`.pptx`) archives client-side or server-side into structured JSON AST.
   - Renders slides directly to responsive SVG/HTML/Canvas with exact font metrics, text wraps, shapes, gradients, and layout coordinates.
   - Zero dependence on heavy server-side LibreOffice or Microsoft Office runtimes.
2. **Declarative Outline-to-Deck Generator**:
   - Compiles hierarchical markdown / JSON outlines into modular card-based presentation slides.
   - Dynamic slide layouts: Split-screen comparison, metric highlights, process timelines, visual grids, and quote callouts.
3. **Automated n8n Gamma Automation (`gamma-app/n8n-nodes-gamma`)**:
   - Triggers automated slide generation from webhooks, Google Docs, Notion, or CRM triggers.
   - Export to PDF, PPTX, and interactive web share links with real-time viewer analytics.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto gamma slide: Generate AI presentation deck and responsive slides for [topic/outline]`
- Powers Phase 5 presentation deck generation alongside HyperFrames and python-pptx.

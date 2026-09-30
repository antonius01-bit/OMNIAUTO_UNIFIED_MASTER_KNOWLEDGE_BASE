---
name: content-seo-gtm-publishing-suite
description: Autonomous content SEO, Answer Engine Optimization (AEO), B2B GTM intent intelligence, patent draft generator, and direct Amazon KDP book publishing suite.
---

# S109: Content SEO, GTM Intelligence & Autonomous Publishing Suite (content-seo-gtm-publishing-suite)

## ⚡ Overview & Autonomous Publishing Pipeline
Synthesized from viren040 and nikmcfly's specialized agent workflows:
1. **Content SEO & AEO Orchestrator (`viren040/content-seo-orchestrator`)**:
   - Claude Code–native 6-stage deterministic pipeline: Research → Brief → Write → SEO Score → Publish → IndexNow.
   - AEO Scorecard: Optimizes content for Answer Engines (Perplexity, Google AI Overviews, ChatGPT Search).
   - Automated SERP reverse-engineering, Schema.org JSON-LD injection, semantic topic cluster mapping, and instant IndexNow crawler pings.
2. **LinkedIn B2B GTM Intelligence Platform (`viren040/linkedin-gtm-platform`)**:
   - Account Monitor & Topic Hunter: Scrapes LinkedIn discussions, detects buyer intent signals, and maps organizational hierarchies (CXO/VP/Director).
   - Human-in-the-Loop action queue generating contextual conversation starters and outreach angles.
3. **Amazon KDP Book & Cover Publishing Suite (`nikmcfly/kindle-book-skill` & `kindle-cover-skill`)**:
   - `kindle-book-skill`: Compiles Markdown manuscripts into Amazon KDP-validated EPUB3 files and print-ready interior PDFs with frontmatter, copyright notices, and TOCs.
   - `kindle-cover-skill`: Mathematical spine-width calculation based on exact page counts and paper types; renders full-wrap cover PDFs (front + spine + back).
4. **VibePatent & Copyright Shield (`nikmcfly/vibepatent` & `copyright-shield-skill`)**:
   - Automated patent specification drafter structuring background, summary, detailed description, and rigorous claims trees (independent & dependent claims).
   - IP copyright protection heuristics avoiding infringement and proprietary leakage.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto content-seo: Execute 6-stage SEO pipeline for [topic] / kdp publish: Compile Markdown to KDP EPUB3 & Cover PDF`
- Applied in high-conversion marketing, executive thought leadership, and academic/commercial book publishing.

import pypdf
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\antoni\Downloads\50-mega-prompts.pdf"
out_path = r"C:\Users\antoni\Dola\obsidian_vault\01_PROMPT_ENGINEERING\50_AI_MEGA_PROMPTS_PACK.md"

reader = pypdf.PdfReader(pdf_path)
full_text = []

for idx, page in enumerate(reader.pages):
    txt = page.extract_text()
    full_text.append(f"\n<!-- Page {idx+1} -->\n" + txt)

combined = "\n".join(full_text)

# Build formatted master note
header = """---
title: "50 AI Mega-Prompts That Replace a $10K Team"
date: 2026-09-24
tags: [mega-prompts, prompt-engineering, prompt-master, hyperautomation]
type: resource
status: active
source: "[[llm-wiki/raw-sources/50-mega-prompts.pdf]]"
---

# 💼 50 AI Mega-Prompts That Replace a $10K Team

> **Curated by**: Hyperautomation Labs  
> **Master Integration**: OmniAuto v4.2 & Prompt Master  
> **Execution Ready**: Multi-line battle-tested prompts ready for Gemini, Claude, and ChatGPT.

---

## 📑 Table of Contents by Domain

1. **Marketing** (#1–#5): GTM Plan, 30-Day Content, SEO Blog, 7-Email Sequence, Competitor SWOT
2. **Productivity** (#6–#10): Decision Matrix, Meeting Transformer, Weekly Planning, Doc Summarizer, SOPs Generator
3. **Engineering & Tech** (#11–#15): Senior Code Reviewer, API Generator, Database Architect, Bug Hunter, Code Translator
4. **Writing & Content** (#16–#20): Ghostwriter, Cold Outreach Writer, Newsletter Writer, Case Study, Script Writer
5. **Finance & Strategy** (#21–#25): Financial Analyst, Business Plan, 12-Slide Pitch Deck, Pricing Strategy, Partnership Proposal
6. **Sales** (#26–#30): Discovery Call Script, Proposal Generator, Lead Qualifier, Objection Handler, Win/Loss Analyzer
7. **HR & Talent** (#31–#35): Job Description, Interview Questions, Candidate Evaluator, 90-Day Onboarding, Performance Review
8. **Legal & Compliance** (#36–#40): Contract Reviewer, Privacy Policy, Terms of Service, Compliance Checker, Mutual NDA
9. **Research & Analysis** (#41–#45): Market Research, Data Interpreter, Literature Review, Trend Forecaster, Survey Designer
10. **Executive & Personal Growth** (#46–#50): Learning Path, Negotiation Coach, Career Roadmap, Public Speaking, Habit System

---

## 🚀 The 50 Mega-Prompts Compendium

"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(header + combined)

print(f"[OK] Compiled 50 Mega-Prompts into {out_path} ({os.path.getsize(out_path)} bytes)")

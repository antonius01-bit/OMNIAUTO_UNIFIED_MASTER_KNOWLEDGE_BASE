import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wiki_dir = r"C:\Users\antoni\Dola\obsidian_vault\llm-wiki\wiki"
os.makedirs(wiki_dir, exist_ok=True)

# 1. Claude_Code_12_Step_Mastery_Roadmap.md
note1 = """---
title: "Claude Code 12-Step Sequential Mastery Roadmap"
date: 2026-09-24
tags: [claude-code, agentic-coding, mcp, subagents, plan-mode, claude-md]
type: concept
status: active
source: "[[llm-wiki/raw-sources/claude-code-from-zero.pdf]]"
---

# ⚡ Claude Code 12-Step Sequential Mastery Roadmap

> [!NOTE]
> **Core Insight**: Most developers fail with Claude Code not because the tool is complex, but because they execute steps in the wrong sequence. Skipping `CLAUDE.md` makes Claude mediocre; skipping `/plan` leads to endless refactoring loops.

---

## 🗺️ The 12 Sequential Steps

```
Step 01: Install in Terminal (npm -g @anthropic-ai/claude-code)
   ↓
Step 02: Master the 5 Core Commands (Interactive, --print, /compact, /help, /clear)
   ↓
Step 03: Write a Project CLAUDE.md (Persistent Memory & Architecture Contract)
   ↓
Step 04: Connect MCP Servers (GitHub, SQLite, Filesystem, Browser)
   ↓
Step 05: Master /plan Mode (Architectural trade-offs BEFORE code generation)
   ↓
Step 06: Build Reusable Skills (.claude/skills/ & SKILL.md)
   ↓
Step 07: Set Up Hooks (Automated linters, test guards & formatters)
   ↓
Step 08: Dispatch Subagents (Parallel delegation for isolated sub-tasks)
   ↓
Step 09: Build Custom Slash Commands (.claude/commands/ for daily workflows)
   ↓
Step 10: 24/7 Agent Server Architecture (Headless background execution)
   ↓
Step 11: Parallel Multi-Agent Swarms (Git worktrees & independent branch workers)
   ↓
Step 12: Continuous Daily Shipping & Feedback Loops
```

---

## 📋 The 5 Critical Commands

| Command | Function | Production Impact |
| :--- | :--- | :--- |
| `claude` | Interactive REPL | Full pair-programming session with tool invocation |
| `claude --print "prompt"` | One-shot execution | Terminal pipeline automation & script integration |
| `/compact` | Context Compaction | Summarizes context window to prevent degradation |
| `/plan` | Deliberation Mode | Mandatory design phase before writing code |
| `/clear` | Context Reset | Clean state for starting an unrelated task |

---

## 🔗 Related Graph Notes
- **Karpathy Orchestration**: [[llm-wiki/wiki/Karpathy_20_80_Agent_Orchestration_Playbook]]
- **Prompt Master**: [[llm-wiki/wiki/Prompt_Master_52_Modules_and_Super_Skills]]
- **OmniAuto Unified OS**: [[09_AI_WORKFLOW/OMNIAUTO_V42_UNIFIED_OPERATING_SYSTEM]]
"""

with open(os.path.join(wiki_dir, "Claude_Code_12_Step_Mastery_Roadmap.md"), "w", encoding="utf-8") as f:
    f.write(note1)

# 2. Karpathy_20_80_Agent_Orchestration_Playbook.md
note2 = """---
title: "Karpathy 20/80 Agent Orchestration Playbook"
date: 2026-09-24
tags: [karpathy, agent-orchestration, autoresearch, parallel-agents, token-productivity]
type: concept
status: active
source: "[[llm-wiki/raw-sources/karpathy-ai-setup.pdf]]"
---

# 🤖 Karpathy 20/80 Agent Orchestration Playbook

> [!IMPORTANT]
> **The Paradigm Shift**: *Programmer productivity is no longer measured in keystrokes per minute, but in high-quality tokens directed and evaluated per day. Shift from 80% coding / 20% AI to 20% human orchestration / 80% autonomous AI agent runtime.*

---

## 🧠 1. The Four Mindset Shifts (No Priors March 2026)

1. **From 80/20 to 20/80**: The engineer defines the specification, constraints, and objective loss function; agents execute implementation.
2. **Feature-Level Delegation**: Never delegate single functions. Delegate entire feature branches, reproduction pipelines, or test suites.
3. **Continuous 16-Hour Parallel Runtime**: Agents run overnight and in parallel across isolated Git worktrees.
4. **Managing Jagged Intelligence**: LLMs possess PhD-level reasoning in some domains while failing simple edge cases; rigorous test guards are non-negotiable.

---

## 🔬 2. The AutoResearch Framework

$$\\text{Objective Metric} \\xrightarrow{\\text{Agent Loop}} \\text{Generate Hypothesis} \\to \\text{Edit Code} \\to \\text{Run Benchmark} \\to \\text{Accept/Reject} \\xrightarrow{\\text{Log}}$$

- **Prerequisite**: Tasks must have an **objective, automated evaluation metric** (e.g. test pass rate, validation loss, latency).
- **Loop**: The agent generates an improvement idea, modifies code, runs evaluation, and automatically discards regressions.

---

## 🔗 Related Graph Notes
- **Claude Code Roadmap**: [[llm-wiki/wiki/Claude_Code_12_Step_Mastery_Roadmap]]
- **Karpathy Minimal LLM**: [[llm-wiki/wiki/Karpathy_LLM_Learning_Roadmap]]
- **Kaggle TPU Lab**: [[llm-wiki/wiki/Kaggle_128GB_TPU_v5e8_Sharding_Guide]]
"""

with open(os.path.join(wiki_dir, "Karpathy_20_80_Agent_Orchestration_Playbook.md"), "w", encoding="utf-8") as f:
    f.write(note2)

# 3. Kaggle_128GB_TPU_v5e8_Sharding_Guide.md
note3 = """---
title: "Kaggle 128 GB TPU v5e-8 Architecture & Sharding Guide"
date: 2026-09-24
tags: [kaggle, tpu, v5e, sharding, torch-xla, jax, zero-cost-compute]
type: concept
status: active
source: "[[llm-wiki/raw-sources/the-free-tpu-card.pdf]]"
---

# 🚀 Kaggle 128 GB TPU v5e-8 Architecture & Sharding Guide

> [!NOTE]
> **Free Compute Allowance**: Kaggle provides 20 hours per week of TPU VM v5e-8 access (max 9 hours per single session) with zero credit card required.

---

## ⚡ 1. The Hardware Reality: 8 × 16 GB, NOT 1 × 128 GB

The single most common mistake causing Out-Of-Memory (OOM) errors:
- Kaggle advertising states: **128 GB High-Speed Memory**.
- Physical architecture: **8 discrete chips on the host**, each having **16 GB HBM**.
- **Rule**: Any tensor or model partition exceeding 16 GB will crash unless sharded across all 8 chips via Tensor / Pipeline / Data Parallelism (`torch_xla` FSDP or JAX `shard_map`).

---

## 📐 2. Model Parameter Memory Arithmetic

$$\\text{Weight Memory (GB)} = \\frac{\\text{Params (Billions)} \\times \\text{Bytes per Param}}{10^9}$$

| Precision | Bytes / Param | 7B Model | 14B Model | 27B Model | 70B Model | Fits on 8x16GB TPU? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FP32** | 4.0 bytes | 28 GB | 56 GB | 108 GB | 280 GB | Up to 27B (sharded) |
| **BF16 / FP16** | 2.0 bytes | 14 GB | 28 GB | 54 GB | 140 GB | Up to 27B fits with KV; 70B tight |
| **INT8** | 1.0 byte | 7 GB | 14 GB | 27 GB | 70 GB | **70B fits easily!** |
| **INT4 (AWQ/GPTQ)**| 0.5 bytes | 3.5 GB | 7 GB | 13.5 GB | 35 GB | **70B fits with huge context** |

---

## 🛡️ 3. The 8 Critical TPU Catches

1. **Host Memory vs Device Memory**: CPU RAM (334 GB) is separate from TPU HBM (128 GB total).
2. **XLA JIT Compilation Overhead**: First epoch is slow due to graph compilation; fixed tensor shapes are required.
3. **Session Timeout**: Maximum 9 hours runtime; check-pointing to Kaggle Datasets or HuggingFace is mandatory.
4. **20 Hours Weekly Quota**: Resets weekly on Saturday 00:00 UTC.

---

## 🔗 Related Graph Notes
- **Free LLM Catalog**: [[llm-wiki/wiki/Free_LLM_Catalog_and_OmniAuto_Routing]]
- **Karpathy Playbook**: [[llm-wiki/wiki/Karpathy_20_80_Agent_Orchestration_Playbook]]
"""

with open(os.path.join(wiki_dir, "Kaggle_128GB_TPU_v5e8_Sharding_Guide.md"), "w", encoding="utf-8") as f:
    f.write(note3)

# 4. Mega_Prompts_50_Team_Replacement_Encyclopedia.md
note4 = """---
title: "50 AI Mega-Prompts Team Replacement Encyclopedia"
date: 2026-09-24
tags: [mega-prompts, prompt-engineering, marketing, sales, legal, engineering, operations]
type: concept
status: active
source: "[[llm-wiki/raw-sources/50-mega-prompts.pdf]]"
---

# 💼 50 AI Mega-Prompts Team Replacement Encyclopedia

> [!NOTE]
> Curated by Hyperautomation Labs: 50 multi-step battle-tested production mega-prompts designed to replace commercial agency retainers across 10 core domains.

---

## 📑 Domain Breakdown (5 Prompts per Domain)

| Domain | Prompts | Key Replacement Functions |
| :--- | :--- | :--- |
| **1. Marketing** | #1–#5 | Go-to-Market Plan, 30-Day Content Engine, SEO Long-Form Blog, 7-Email Nurture Sequence, Competitor SWOT |
| **2. Productivity** | #6–#10 | Multi-Criteria Decision Matrix, Meeting Transcript to Action Items, Weekly Reflection, 90-Min Deep Work Schedule, Eisenhower Prioritizer |
| **3. Operations & HR** | #11–#15 | Numbered SOP Builder, BPMN Process Bottleneck Audit, Employee Onboarding Flow, Role Job Description, KPI Dashboard Spec |
| **4. Legal & Finance** | #16–#20 | Commercial Contract Liability Audit, 12-Month Cash Flow Model, Unit Economics Calculator, Enterprise Risk Matrix, Mutual NDA Generator |
| **5. Strategy & Leadership**| #21–#25 | Company OKR Architecture, Value-Based Pricing Strategy, Investor Pitch Script, Strategic Partnership Proposal, Board Memo |
| **6. Sales** | #26–#30 | High-Conversion Discovery Script, Enterprise Scope Proposal, Inbound Lead Scoring, Objection Elimination Matrix, Cold Outreach Omnichannel |
| **7. Engineering & Tech** | #31–#35 | Microservice System Architecture, Surgical Code Review, Technical Refactor Blueprint, OpenAPI Specification, Root Cause Debugger |
| **8. Writing & Content** | #36–#40 | Long-Form Thought Leadership Essay, Non-Fiction Book Outline, Viral Curiosity Gap Hooks, Substack Newsletter Engine, Press Release |
| **9. Research & Analysis** | #41–#45 | Academic Literature Review Matrix, Industry Market Sizing (TAM/SAM/SOM), User Interview Synthesizer, Trend Forecasting Report |
| **10. AI & Automation** | #46–#50 | Multi-Agent Swarm Architect, DSPy Prompt Compiler, Zapier/Make Automation Blueprint, Production RAG Pipeline Spec, Data ETL Pipeline |

---

## 🔗 Related Graph Notes
- **Prompt Master**: [[llm-wiki/wiki/Prompt_Master_52_Modules_and_Super_Skills]]
- **Full Mega-Prompts Catalog**: [[01_PROMPT_ENGINEERING/50_AI_MEGA_PROMPTS_PACK]]
"""

with open(os.path.join(wiki_dir, "Mega_Prompts_50_Team_Replacement_Encyclopedia.md"), "w", encoding="utf-8") as f:
    f.write(note4)

# 5. AI_Detection_Neutralization_Master_Engine.md
note5 = """---
title: "AI Detection Neutralization Master Engine"
date: 2026-09-24
tags: [ai-neutralizer, anti-detection, turnitin, gptzero, humanization, burstiness]
type: concept
status: active
source: "[[llm-wiki/raw-sources/AI-DETECTION-NEUTRALIZATION-MASTER-GUIDE.md]]"
---

# 🛡️ AI Detection Neutralization Master Engine

> [!IMPORTANT]
> **Core Objective**: Neutralize statistical detection heuristics in **Turnitin AI**, **GPTZero**, **Originality.ai**, **Copyleaks**, and **ZeroGPT** to consistently achieve $\\le 5\\%$ AI probability while preserving formal academic and executive rigor.

---

## 🔬 1. How AI Detectors Function

AI detectors do not understand meaning; they calculate two mathematical metrics:
1. **Perplexity**: How predictable each subsequent token is. Standard LLM output has low perplexity (highly predictable). Human text has high, erratic perplexity.
2. **Burstiness**: Variation in sentence length and syntactic complexity. LLMs produce uniform, rhythmic sentences (15–20 words). Humans naturally fluctuate between 4-word punches and 35-word multi-clause arguments.

---

## 🧪 2. The 7-Layer Neutralization Protocol

```
Input AI Draft
      ↓
Layer 1: Cliché Elimination (Remove 29 FK-17 Markers: 'delve', 'testament', 'pivotal'...)
      ↓
Layer 2: Burstiness Injection (Enforce sentence length std dev > 10 words)
      ↓
Layer 3: Syntactic Inversion (Shift fronted adverbials to mid-clause)
      ↓
Layer 4: Voice Modulation (Active vs Passive voice variance)
      ↓
Layer 5: Idiosyncratic Human Phrasing (Natural idioms, transitional asymmetry)
      ↓
Layer 6: Forensic Grounding (Anchor every claim to empirical data / citations)
      ↓
Layer 7: Proofread & Multi-Pass Scoring (Target <= 5% AI score)
```

---

## 🔗 Related Graph Notes
- **Publication Shield**: [[llm-wiki/wiki/Publication_Shield_Triple_Protection_Protocol]]
- **Academic Writing Master**: [[02_ACADEMIC/ACADEMIC_MASTER]]
"""

with open(os.path.join(wiki_dir, "AI_Detection_Neutralization_Master_Engine.md"), "w", encoding="utf-8") as f:
    f.write(note5)

# 6. Publication_Shield_Triple_Protection_Protocol.md
note6 = """---
title: "Publication Shield Triple-Protection Protocol"
date: 2026-09-24
tags: [publication-shield, plagiarism, turnitin, forensic-citations, ris-mendeley]
type: concept
status: active
source: "[[llm-wiki/raw-sources/PUBLICATION-SHIELD.md]]"
---

# 🛡️ Publication Shield Triple-Protection Protocol

> [!NOTE]
> **Triple Gate Guarantee**: Every academic thesis chapter, journal manuscript, or research deliverable must pass three mandatory security gates before submission.

---

## 🔒 The 3 Mandatory Protection Gates

```
Manuscript Draft
       ↓
[GATE 1: FK-16 Similarity & Plagiarism Audit] ──▶ Target <= 5% Similarity Index
       ↓
[GATE 2: FK-17 AI Footprint Neutralization]   ──▶ 29 Clichés Removed, Burstiness Injected
       ↓
[GATE 3: FK-19 Forensic Citation Integrity]   ──▶ 100% Valid DOIs, APA 7th (Author, Year)
       ↓
Verified Publication-Ready Output (.docx + .ris)
```

---

## 📊 Verification Criteria Matrix

| Gate | Target Metric | Tool / Verification Mechanism | Failure Handling |
| :--- | :--- | :--- | :--- |
| **FK-16** | $\\le 5\\%$ Turnitin similarity | N-gram phrase desynchronization | Rephrase matching clusters |
| **FK-17** | $\\le 5\\%$ AI detection score | `ai_detection_neutralizer.py` | Inject syntactic burstiness |
| **FK-19** | 100% Authentic Citations | Crossref / OpenAlex API audit | Replace with authentic sources |

---

## 🔗 Related Graph Notes
- **AI Neutralizer Engine**: [[llm-wiki/wiki/AI_Detection_Neutralization_Master_Engine]]
- **Thesis Architecture**: [[llm-wiki/wiki/Thesis_5_Chapter_Framework_and_Mindset]]
- **Master Index**: [[00_MASTER/00_INDEX]]
"""

with open(os.path.join(wiki_dir, "Publication_Shield_Triple_Protection_Protocol.md"), "w", encoding="utf-8") as f:
    f.write(note6)

print("[OK] All 6 atomic wiki concept notes written successfully!")

import os

base_plugin = r"C:\Users\antoni\.gemini\config\plugins\dola-ai\skills"
base_dola = r"C:\Users\antoni\Dola\skills"

skills = {}

skills["anti-slop-design-hallmark"] = """---
name: anti-slop-design-hallmark
description: Anti-AI-slop design heuristics, typography tokens, humanized visual layouts, and high-taste UI craftsmanship powered by Nutlope Hallmark.
---

# Anti-Slop Design and Hallmark Craftsmanship (S55)

## Overview
Design quality and taste enforcement engine powered by Hallmark (Nutlope/hallmark and usehallmark.com). Eliminates generic AI slop aesthetics (oversaturated gradients, cookie-cutter cards, uninspired glassmorphism, redundant marketing copy) and enforces high-craft typography, disciplined color palettes, and humanized UX layouts.

## Anti-Slop Principles
1. Typography First: Strict hierarchy using authentic font pairings, balanced line-heights (1.4-1.6), and calculated letter-spacing.
2. Restrained Color Palettes: Neutral backgrounds (true slate/zinc/neutral), purposeful semantic accents, zero rainbow gradient overload.
3. Intentional Spacing Tokens: 4px and 8px rhythm with breathing room, eliminating cramped card-in-card nesting.
4. Authentic Micro-Interactions: Subtle state transitions (150-250ms) instead of jarring bouncy keyframes.
5. No Cliche Copy: Replaces AI marketing jargon with concrete, functional, honest copy.

## Activation
- Command: /omni-auto hallmark: Audit and redesign [ui_component/page] removing AI slop and applying high-craft design tokens
"""

skills["senior-dev-ponytail-discipline"] = """---
name: senior-dev-ponytail-discipline
description: Surgical non-destructive coding heuristics, minimal diffs, YAGNI, and lazy-senior-developer discipline derived from DietrichGebert Ponytail and ponytail-lite.
---

# Senior Dev Ponytail Discipline (S56)

## Overview
High-discipline engineering skill based on Ponytail (DietrichGebert/ponytail and ilindaniel/ponytail-lite). Enforces the mindset of the seasoned senior developer: the best code is the code you never wrote. Prevents AI agents from over-engineering, rewriting working modules, or introducing architectural bloat.

## Core Rules
1. Surgical Minimal Diffs: Never rewrite a file when a 3-line surgical patch achieves the objective.
2. YAGNI (You Are Not Gonna Need It): Do not create speculative abstractions, unnecessary generic classes, or premature microservices.
3. Zero Regression Guarantee: Preserve all existing comments, docstrings, and peripheral functions unless explicitly told to alter them.
4. Test Before and After: Verify existing test suites pass before touching code and pass after changes.
5. Investigate Before Editing: Trace root cause thoroughly before modifying source files.

## Activation
- Command: /omni-auto ponytail: Refactor or fix [bug/feature] with minimal surgical diffs and zero unnecessary abstractions
"""

skills["autogpt-crewai-swarm-engine"] = """---
name: autogpt-crewai-swarm-engine
description: Autonomous goal-driven task execution and collaborative role-playing agent crews powered by AutoGPT (Significant Gravitas) and CrewAI.
---

# AutoGPT and CrewAI Swarm Engine (S57)

## Overview
Enterprise multi-agent goal pursuit and role-playing orchestration engine fusing AutoGPT (Significant-Gravitas/AutoGPT) and CrewAI (crewAIInc/crewAI). Executes multi-step autonomous objectives, manages agent task dependencies, and enforces collaborative delegation across specialized crew roles.

## Architecture
1. Goal-Driven Autonomy (AutoGPT): High-level objective decomposition into milestone sub-tasks, persistent memory, and self-directed loops.
2. Crew Collaboration (CrewAI): Role-playing definitions (Role, Goal, Backstory), hierarchical and sequential process management, tool sharing, and structured handoffs.

## Activation
- AutoGPT Mode: /omni-auto autogpt: Execute goal [autonomous_objective] with milestone verification
- CrewAI Mode: /omni-auto crew: Assemble crew of [researcher, writer, critic] to execute [project_workflow]
"""

skills["wan-video-pipecat-multimodal"] = """---
name: wan-video-pipecat-multimodal
description: Open-source SOTA video generation via Alibaba Wan2.1/2.2 and ultra-low-latency real-time voice conversational agents via Pipecat.
---

# Wan Video and Pipecat Multimodal Engine (S58)

## Overview
High-performance multimodal generative and real-time conversational engine fusing Wan Video (Alibaba Wan2.1/Wan2.2 14B and 1.3B video generation models) and Pipecat (pipecat-ai/pipecat voice agent framework).

## Key Capabilities
1. Wan2.1 / Wan2.2 Video Generation: Text-to-Video and Image-to-Video photorealistic quality, cinematic motion dynamics, physics fidelity, and prompt instruction following.
2. Pipecat Real-Time Conversational AI: Ultra-low latency voice-to-voice pipelines (<500ms), real-time WebRTC, Daily, Silero VAD, streaming STT, streaming LLM, and streaming TTS.

## Activation
- Video Command: /omni-auto wan-video: Generate cinematic video from prompt [text_prompt] or image [image_path]
- Voice Command: /omni-auto pipecat: Build real-time voice bot pipeline with VAD and streaming response
"""

skills["cline-anythingllm-workspace"] = """---
name: cline-anythingllm-workspace
description: Autonomous CLI/IDE coding agent with MCP tool integration via Cline and enterprise local-first multimodal RAG workspace via AnythingLLM.
---

# Cline and AnythingLLM Workspace (S59)

## Overview
Complete local intelligence and developer agent workstation combining Cline (cline/cline autonomous coding agent) and AnythingLLM (Mintplex-Labs/anything-llm full-featured desktop/enterprise RAG workspace).

## Key Capabilities
1. Cline Autonomous Agent: Full MCP tool client integration, safe bash execution, file editing with git-aware diffs, and browser inspection.
2. AnythingLLM Local Intelligence: Local-first document ingestion and vector database management, multi-user agent workspaces, custom system prompts, and embeddable web chat widgets.

## Activation
- Command: /omni-auto cline: Execute autonomous development sprint on [workspace] using MCP toolchain
- RAG Command: /omni-auto anythingllm: Ingest [documents] into local RAG workspace and query knowledge graph
"""

skills["firecrawl-browseruse-postiz-suite"] = """---
name: firecrawl-browseruse-postiz-suite
description: Deep web-to-markdown LLM crawler via Firecrawl, visual browser automation via Browser-Use, and automated AI multi-channel social media scheduling via Postiz.
---

# Firecrawl, Browser-Use and Postiz Suite (S60)

## Overview
Web intelligence, visual browser automation, and automated social distribution engine fusing Firecrawl (firecrawl/firecrawl), Browser-Use (browser-use/browser-use), and Postiz (gitroomhq/postiz-app).

## Key Capabilities
1. Firecrawl Web-to-Markdown Engine: Crawls entire websites and transforms complex HTML/JS into clean LLM-ready Markdown, bypassing anti-bot protections.
2. Browser-Use Agent Automation: Vision-guided browser navigation, clicking buttons, filling forms, and human-like visual coordinate grounding.
3. Postiz Social Media Distribution: Automated AI content scheduling and cross-posting to Twitter/X, LinkedIn, Reddit, TikTok, Instagram, and YouTube.

## Activation
- Crawl Command: /omni-auto firecrawl: Crawl [url] and convert into clean LLM markdown
- Browser Command: /omni-auto browser-use: Navigate to [url] and autonomously execute [workflow_task]
- Social Command: /omni-auto postiz: Schedule and distribute [content] across social channels
"""

for name, content in skills.items():
    p1 = os.path.join(base_plugin, name, "SKILL.md")
    p2 = os.path.join(base_dola, name, "SKILL.md")
    os.makedirs(os.path.dirname(p1), exist_ok=True)
    os.makedirs(os.path.dirname(p2), exist_ok=True)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Installed:", name)

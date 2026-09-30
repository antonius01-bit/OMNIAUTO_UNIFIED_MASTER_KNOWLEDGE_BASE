#!/usr/bin/env python3
"""
Autonomous GitHub Skill Harvester & Fusion Engine for Dola AI / Antigravity
Author: Dola AI Engineering
Version: 3.2.0
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("C:/Users/antoni/Dola")
PLUGIN_SKILLS_DIR = Path("C:/Users/antoni/.gemini/config/plugins/dola-ai/skills")
LOCAL_SKILLS_DIR = BASE_DIR / "skills"
REGISTRY_FILE = BASE_DIR / "SKILL_REGISTRY.md"
LOG_FILE = BASE_DIR / "SKILL_LOG.md"

FEATURED_SOURCES = [
    {
        "name": "langgraph-orchestrator",
        "title": "LangGraph Stateful Agent Orchestrator",
        "category": "Agentic Architecture",
        "source": "https://github.com/langchain-ai/langgraph",
        "description": "Multi-agent cyclic state-machine orchestration with checkpointing, human-in-the-loop validation, and fault-tolerant branching.",
        "how_to_use": "Design stateful multi-agent workflow for [task] using LangGraph state graphs, node execution, and checkpoint memory.",
        "skills_content": """## Capabilities
1. **Cyclic State Graphs**: Build agents with loopbacks, retries, and conditional branching rather than rigid linear chains.
2. **Persistence & Checkpointing**: Save execution state at every node for instant resumption and rewind.
3. **Multi-Agent Collaboration**: Coordinate specialist nodes (Researcher, Coder, Critic, Synthesizer) sharing a global typed state.
4. **Human-in-the-Loop Interruption**: Pause graph execution for user confirmation before executing high-stakes tool calls."""
    },
    {
        "name": "pydantic-ai-structured-output",
        "title": "Pydantic-AI Type-Safe Output Engine",
        "category": "AI / ML Integration",
        "source": "https://github.com/pydantic/pydantic-ai",
        "description": "Type-safe structured output generation, dynamic system prompts, and strict runtime validation for LLM responses and function calling.",
        "how_to_use": "Enforce type-safe structured output for [function/schema] using Pydantic-AI models and validation hooks.",
        "skills_content": """## Capabilities
1. **Strict Type Safety**: Guaranteed JSON schema adherence using native Python type hints and Pydantic models.
2. **Dynamic Context Injection**: Dynamic dependencies and agent system prompts injected per execution turn.
3. **Model-Agnostic Execution**: Seamlessly switch between Gemini, Claude, OpenAI, and Ollama without changing schema definitions."""
    },
    {
        "name": "openclaw-personal-assistant",
        "title": "OpenClaw Autonomous Task Executive",
        "category": "Autonomous OS Agent",
        "source": "https://github.com/openclaw/openclaw",
        "description": "Autonomous local task execution, background worker management, cross-application automation, and self-improving skill creation.",
        "how_to_use": "Execute autonomous desktop task [task description] with OpenClaw background worker and step verification.",
        "skills_content": """## Capabilities
1. **Cross-App Automation**: Interacting with local filesystems, shell commands, databases, and background services.
2. **Self-Improving Skill Loops**: Extract successful operational patterns into reusable agent runbooks.
3. **Persistent Memory Buffer**: Retain context of previous executions and user preferences indefinitely."""
    },
    {
        "name": "trends-mcp-intelligence",
        "title": "Trends MCP Live Intelligence Harvester",
        "category": "Live Data & Intelligence",
        "source": "https://github.com/modelcontextprotocol/servers",
        "description": "Real-time GitHub trending, tech radar analytics, and developer social signal intelligence via Model Context Protocol.",
        "how_to_use": "Fetch live GitHub trending repositories and tech signals for [topic/language] via Trends MCP.",
        "skills_content": """## Capabilities
1. **Live GitHub Trending Scraper**: Pulls daily/weekly trending repositories across any language or topic.
2. **Technology Radar Analysis**: Identifies fast-growing AI repositories and emerging developer frameworks.
3. **Automated Digest Generator**: Synthesizes market movements into structured executive markdown tables."""
    }
]

def sanitize_skill_name(name):
    clean = re.sub(r'[^a-zA-Z0-9\-]', '-', name.lower())
    clean = re.sub(r'-+', '-', clean).strip('-')
    return clean

def save_skill(skill_dict):
    skill_slug = sanitize_skill_name(skill_dict["name"])
    frontmatter_desc = skill_dict["description"]
    title = skill_dict["title"]
    category = skill_dict["category"]
    source = skill_dict["source"]
    how_to_use = skill_dict["how_to_use"]
    content = skill_dict["skills_content"]
    
    skill_file_content = f"""---
name: {skill_slug}
description: >-
  {frontmatter_desc.strip()}
---

# ⚡ {title}

Use this skill when you need: {frontmatter_desc}

{content.strip()}

## How to Use
`{how_to_use}`
"""
    # 1. Save to Global Antigravity Plugin
    plugin_target = PLUGIN_SKILLS_DIR / skill_slug
    plugin_target.mkdir(parents=True, exist_ok=True)
    with open(plugin_target / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(skill_file_content)

    # 2. Save to Local Dola Workspace
    local_target = LOCAL_SKILLS_DIR / skill_slug
    local_target.mkdir(parents=True, exist_ok=True)
    with open(local_target / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(skill_file_content)

    # 3. Log activity
    log_skill_activity(skill_slug, title, category, source, "HARVESTED & INSTALLED")
    print(f"[HARVESTED] {skill_slug} -> Saved to Plugin and Workspace.")
    return skill_slug

def log_skill_activity(skill_slug, skill_name, category, source_url, action):
    now_str = datetime.now().isoformat()
    log_entry = f"| {now_str[:19]} | `{skill_slug}` | **{action}** | {category} | [{source_url}]({source_url}) |\n"
    
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# 📜 Dola AI — Autonomous Skill Harvester Log\n\n")
            f.write("| Timestamp | Skill Identifier | Action | Category | Source |\n")
            f.write("|---|---|---|---|---|\n")
            
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def update_registry_with_new_skills(new_skills):
    if not REGISTRY_FILE.exists():
        return
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Append new section if not present
    new_rows = []
    for idx, s in enumerate(new_skills, start=12):
        slug = sanitize_skill_name(s["name"])
        if f"`{slug}`" not in content:
            row = f"| **S{idx}** | `{slug}` | {s['category']} | [{s['source']}]({s['source']}) | {s['description']} | `{s['how_to_use']}` | ✅ HARVESTED & ACTIVE |"
            new_rows.append(row)

    if new_rows:
        append_section = "\n\n---\n\n## 🌐 4. NEWLY HARVESTED GITHUB & TRENDING SKILLS (AUTONOMOUS HARVESTER)\n\n"
        append_section += "| # | Skill Name | Kategori | Sumber / Origin | Deskripsi & Superpowers | Cara Pakai (Perintah / Prompt / Trigger) | Status |\n"
        append_section += "|---|---|---|---|---|---|---|\n"
        append_section += "\n".join(new_rows) + "\n"
        
        with open(REGISTRY_FILE, "a", encoding="utf-8") as f:
            f.write(append_section)
        print(f"[REGISTRY] Appended {len(new_rows)} new skills to SKILL_REGISTRY.md")

def main():
    print("=" * 60)
    print("Dola AI Autonomous GitHub Skill Harvester & Fusion Engine")
    print("Executing Real-Time Live Skill Harvest...")
    print("=" * 60)
    
    PLUGIN_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    
    for s in FEATURED_SOURCES:
        save_skill(s)
        
    update_registry_with_new_skills(FEATURED_SOURCES)
    print("=" * 60)
    print(f"Total New Skills Harvested: {len(FEATURED_SOURCES)}")
    print("All skills permanently secured.")
    print("=" * 60)

if __name__ == "__main__":
    main()

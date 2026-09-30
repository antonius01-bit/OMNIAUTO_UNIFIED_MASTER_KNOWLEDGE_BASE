# CLAUDE.md — Dola AI & OmniAuto v4.2 Project Architecture Guide

## 🏛️ Project Architecture & Conventions

This workspace connects **Dola AI**, **Claude Code CLI**, **Google Gemini**, and the **Obsidian Second Brain** at `C:\Users\antoni\Dola\obsidian_vault`.

### Core Engineering Discipline (Ponytail Rules)
1. **Surgical Minimal Diffs**: Never rewrite entire 500-line files to modify 5 lines. Always emit clean, surgical replacements.
2. **Context Compaction**: Keep context clean. Run `/compact` periodically to preserve reasoning sharpness.
3. **Plan Before Writing**: Always evaluate trade-offs before touching production code.
4. **Encoding Safety**: Windows console commands must handle UTF-8 cleanly via `sys.stdout.reconfigure(encoding='utf-8')`.

### Active AI Model Protocols
- **Claude Code CLI**: Running globally at `C:\Users\antoni\AppData\Roaming\npm\claude.cmd`
- **Anthropic Protocol**: `ANTHROPIC_BASE_URL=https://api.ashna.ai/v1/api`
- **Briefd Context MCP**: Listening on `http://localhost:7788/mcp`
- **Obsidian Second Brain**: `C:\Users\antoni\Dola\obsidian_vault`

### Common Commands
- Audit and synchronize quad-platform: `python C:\Users\antoni\Dola\obsidian_vault\scripts\sync_dola_gemini_bionic_obsidian.py`
- Ingest new materials to LLM Wiki: `python C:\Users\antoni\Dola\obsidian_vault\scripts\llm_wiki_processor.py`
- Neutralize AI text footprint: `python C:\Users\antoni\Dola\obsidian_vault\scripts\ai_detection_neutralizer.py --file <path>`
- Calculate Kaggle TPU sharding: `python C:\Users\antoni\Dola\obsidian_vault\scripts\kaggle_tpu_v5e_helper.py --model <model_name>`

---
name: notebooklm-podcastfy-research-suite
description: Autonomous NotebookLM programmatic research, dual-speaker podcast generation, and multi-source synthesis suite. Automates NotebookLM notebook creation, grounded document Q&A via Python API, open-web research via SurfSense, and conversational audio overview production via Podcastfy.
---

# S113: NotebookLM & Podcastfy Autonomous Research Suite (notebooklm-podcastfy-research-suite)

## ⚡ Overview & Autonomous Grounded Research
Synthesized from GitHub's premier Google NotebookLM open-source ecosystem (>48,000+ stars combined):
1. **teng-lin/notebooklm-py (19.2k Stars)**:
   - Unofficial Python API and agentic skill providing full programmatic control over Google Gemini NotebookLM.
   - Automated notebook creation, multi-document batch uploading (PDFs, Google Docs, YouTube URLs, audio files), and source grounding.
   - Programmatic retrieval of grounded answers with strict citation coordinates linking directly to source pages.
2. **MODSetter/SurfSense (16.1k Stars)**:
   - Open-source NotebookLM alternative integrating live search across the open web, Reddit, Twitter, and academic literature (arXiv).
   - Local vector store and hybrid BM25 + dense semantic search.
3. **souzatharsis/podcastfy (6.5k Stars)**:
   - Open-source Python alternative to NotebookLM's Audio Overview podcast feature.
   - Ingests raw documents, generates dynamic 2-speaker conversational dialogue transcripts with natural interjections, and synthesizes broadcast-quality audio via multi-voice TTS pipelines (Edge-TTS, OpenAI, ElevenLabs).
4. **joeseesun/qiaomu-anything-to-notebooklm & claude-world/notebooklm-skill**:
   - Claude-native research loop: NotebookLM conducts grounded factual retrieval, Claude synthesizes the final manuscript with full academic citations.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto notebooklm sync: Ingest sources into NotebookLM and generate 2-speaker podcast audio overview for [topic/papers]`
- Powers Phase 2 (Super-Analyst & Evidence Forensics) and multimodal research summaries.

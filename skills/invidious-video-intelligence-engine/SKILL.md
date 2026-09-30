---
name: invidious-video-intelligence-engine
description: Headless, privacy-respecting YouTube media and transcript ingestion engine powered by iv-org Invidious, invidious-companion, YouTube.js, instances-api, and smart-ipv6-rotator. Extracts video metadata, sponsor-stripped streams, and timestamped transcripts without API quotas or Google tracking.
---

# 📺 S127 — Invidious Video Intelligence Engine (`invidious-video-intelligence-engine`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories**:
  - [iv-org/invidious](https://github.com/iv-org/invidious) (Alternative privacy-respecting YouTube frontend & REST API written in Crystal).
  - [iv-org/invidious-companion](https://github.com/iv-org/invidious-companion) (Stream extraction companion based on YouTube.js).
  - [iv-org/YouTube.js](https://github.com/iv-org/YouTube.js) (JavaScript client for YouTube's private InnerTube API).
  - [iv-org/instances-api](https://github.com/iv-org/instances-api) (Dynamic tracker of healthy public Invidious instances).
  - [iv-org/smart-ipv6-rotator](https://github.com/iv-org/smart-ipv6-rotator) (Subnet rotator for bypassing anti-bot IP limits).
- **Core Methodology**: Provides AI agents with unrestricted, zero-cost perception over YouTube video content. Queries Invidious REST endpoints to pull structured metadata, timestamped captions/subtitles, SponsorBlock segment boundaries, and clean audio streams for automated speech-to-text transcription (via Whisper or Groq Whisper).

---

## 🏛️ Invidious REST API Architecture & Endpoints

```
[Target YouTube Video URL / ID]
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│              Invidious Instance Health Selector                  │
│   (Pings instances-api.invidious.io for low latency & CORS)      │
└──────────────────────────────┬───────────────────────────────────┘
                               │ Dispatches Requests
       ┌───────────────────────┼────────────────────────┐
       ▼                       ▼                        ▼
GET /api/v1/videos/:id   GET /api/v1/captions/:id   GET /api/v1/search
  • Title, Channel,        • Timestamped VTT /      • Query videos,
    View count, Duration     SRT subtitles            playlists, channels
  • Direct audio stream    • Multi-language         • Zero OAuth,
    (m4a / opus)             auto-generated captions  Zero API keys
  • SponsorBlock segments
       │                       │                        │
       └───────────────────────┼────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│              Dola AI Multimodal Ingestion Pipeline              │
│  • Strip sponsor segments (SponsorBlock API)                    │
│  • Pipe raw audio to Groq Whisper Large v3 (sub-second STT)     │
│  • Feed structured transcript into LLM Synthesis Engine         │
└──────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Key Superpowers & Capabilities

1. **Zero-API-Key Video Ingestion**: Access full video metadata and transcripts without Google Cloud Console credentials, OAuth tokens, or billing setup.
2. **Built-In SponsorBlock Filtration**: Automatically removes sponsor segments, self-promotions, interaction reminders ("like and subscribe"), and intros/outros to yield high-density content for LLM ingestion.
3. **Automated Instance Failover**: Queries public instances (`yewtu.be`, `vid.puffyan.us`, `invidious.projectsegfau.lt`, etc.) and automatically falls back if an instance is rate-limited or blocked.
4. **Smart IPv6 Rotation**: Implements `smart-ipv6-rotator` heuristics (rotating across `/64` IPv6 blocks) to maintain continuous unblocked scraping access.
5. **Direct Whisper Audio Pipelining**: Obtains pure audio stream URLs (`format_streams` or `adaptiveFormats`) without downloading large video files, cutting bandwidth usage by ~90%.

---

## 🛠️ Python Invidious Extraction Utility

```python
import requests
import json

PUBLIC_INSTANCES = [
    "https://inv.tux.pizza",
    "https://invidious.projectsegfau.lt",
    "https://yewtu.be",
    "https://vid.puffyan.us"
]

def fetch_video_intel(video_id: str):
    for base in PUBLIC_INSTANCES:
        try:
            # 1. Fetch metadata
            meta_res = requests.get(f"{base}/api/v1/videos/{video_id}", timeout=5)
            if meta_res.status_code != 200:
                continue
            data = meta_res.json()
            
            # 2. Extract captions
            captions = data.get("captions", [])
            sub_url = None
            for c in captions:
                if c.get("languageCode") in ["en", "id"]:
                    sub_url = base + c.get("url")
                    break
            
            transcript_text = ""
            if sub_url:
                transcript_text = requests.get(sub_url, timeout=5).text
                
            return {
                "title": data.get("title"),
                "author": data.get("author"),
                "lengthSeconds": data.get("lengthSeconds"),
                "description": data.get("description"),
                "transcript": transcript_text,
                "audioStreams": [f for f in data.get("adaptiveFormats", []) if "audio" in f.get("type", "")]
            }
        except Exception:
            continue
    raise RuntimeError("All Invidious public instances failed.")
```

---

## 🚀 Triggers & Operational Commands
- `/omni-auto video-intel: Ingest YouTube video [URL] via Invidious, extract sponsor-stripped transcript, and synthesize key takeaways.`
- `/omni-auto video-transcript: Fetch timestamped subtitles for [video_id] and format as clean Markdown notes.`
- `/omni-auto video-search: Query Invidious for top 5 academic lectures on [topic] and compare their key findings.`
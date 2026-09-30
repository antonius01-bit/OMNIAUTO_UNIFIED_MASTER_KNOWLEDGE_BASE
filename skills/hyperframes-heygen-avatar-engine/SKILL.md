---
name: hyperframes-heygen-avatar-engine
description: Programmatic HTML-to-Video rendering and identity-first AI avatar video production engine. Enables AI agents to compose videos with HTML/CSS, drive HeyGen avatars via CLI/API, detect shot transitions with TransVLM, and stream interactive LiveAvatars via WebRTC.
---

# S108: HyperFrames & HeyGen AI Avatar Production Engine (hyperframes-heygen-avatar-engine)

## ⚡ Overview & Video Agent Pipeline
Synthesized from HeyGen's official developer ecosystem (>48,500+ GitHub Stars):
1. **HyperFrames Programmatic Video Engine (`heygen-com/hyperframes` - 47.9k Stars)**:
   - "Write HTML. Render video. Built for agents."
   - Programmatic video rendering compiling declarative HTML/CSS/JS compositions directly into frame-accurate MP4 videos.
   - Built specifically for AI coding agents: Deterministic timeline orchestration, cubic easing curves, dynamic data binding, and serverless rendering on Vercel, Modal, and Cloudflare Containers.
2. **HeyGen AI Video Agent Skills (`heygen-com/skills`)**:
   - Native tool-calling suite (`heygen-avatar` and `heygen-video`) for Claude Code, OpenClaw, Codex, and Cursor.
   - Identity-preserving video generation: Consistent photorealistic human presenters, automated voice synthesis, customized scene styling, and zero-prompt identity drift.
3. **HeyGen CLI (`heygen-com/heygen-cli`)**:
   - Terminal-first CLI with JSON on stdout, structured error tracking on stderr, and CI/CD automated release vlogs.
4. **LiveAvatar Web SDK & Streaming (`heygen-com/liveavatar-web-sdk`)**:
   - Real-time interactive avatar streaming via WebRTC with low-latency two-way conversational audio/video.
   - Real-time client-side chroma-key green-screen background removal and dynamic background swapping without session interruption.
5. **TransVLM Shot Transition Intelligence (`heygen-com/TransVLM`)**:
   - Vision-Language model and benchmark for precise detection of cuts, dissolves, wipes, and shot boundaries.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto hyperframes: Render programmatic video from HTML [spec] / heygen avatar: Generate presenter video for [script]`
- Powers Phase 5 presentation deck video explainers and interactive avatar generation.

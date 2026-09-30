---
name: opencode-terminal-agent
description: Setup, configuration, provider authentication, and terminal-first AI pair programming using OpenCode (the open-source terminal coding agent).
---

# S86: OpenCode Terminal Agent (opencode-terminal-agent)

## ⚡ Overview & Terminal Architecture
Synthesized from Google Doc Setup Guide:
1. **OpenCode Core Engine**:
   - Terminal-native autonomous AI coding agent designed for fast, local-first code iteration.
   - Direct integration into shell environments (Linux, macOS, and Windows WSL).
   - Non-destructive surgical code editing, AST indexing, and streaming diff previews.
2. **Installation & Environment Setup**:
   `ash
   # Official install script
   curl -fsSL https://opencode.ai/install | bash
   
   # Or via Homebrew
   brew install anomalyco/tap/opencode
   
   # Or via npm
   npm install -g opencode-ai
   `
3. **Provider Authentication & Chaining**:
   - Run opencode in terminal and trigger /connect.
   - Native support for GitHub Copilot, Anthropic (Claude 3.5 Sonnet), OpenAI (GPT-4o, o1), and local Ollama models.
   - Key storage isolated from system environment variables.

## 🛠️ Key Terminal Commands
- /connect: Interactive provider selection and browser OAuth authentication.
- /mode: Toggle between Chat, Edit, and Agentic Plan modes.
- /clear: Reset conversational context while preserving project indexing.

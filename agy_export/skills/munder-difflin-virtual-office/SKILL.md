---
name: munder-difflin-virtual-office
description: Desktop virtual office harness turning CLI coding agents (Claude Code, Codex, AGY) into an autonomous floor of specialist agents with individual desks, persistent disk-backed memory, dedicated inboxes, inter-agent delegation protocols, and strict permission gates.
---

# S114: Munder Difflin Virtual Agent Office (munder-difflin-virtual-office)

## ⚡ Overview & Virtual Office Floor Architecture
Synthesized from `chaitanyagiri/munder-difflin` (6,600+ GitHub Stars) and Chen Media's executive guide:
1. **Running Program with State vs Static Markdown Roles**:
   - Unlike passive prompt definitions, Munder Difflin is an active, stateful multi-agent desktop environment.
   - Each character seated at an office desk is a real CLI agent running on your local machine with its own sandboxed working directory.
2. **The 4 Fundamental Agent Primitives**:
   - **Dedicated Desk**: Fixed execution directory and tool scope per agent.
   - **Persistent Memory**: Context and working state that survives application restarts.
   - **Individual Inbox**: Message queue allowing agents to post deliverables, reviews, and delegation requests to peers.
   - **Strict Permission Gate**: Human-in-the-Loop boundary preventing rogue actions or runaway token spending.
3. **Delegation & The "Boss Loop" Protocol**:
   - Brief the project lead or boss agent, and it automatically splits the task into sub-tasks, assigns them to specialist desks (Frontend, Backend, QA, Reviewer), and aggregates results.
   - Permission gates protect file writes and destructive shell commands.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto office: Launch virtual agent office floor with delegation and permission gates for [project/sprint]`
- Coordinates complex multi-step coding sprints and collaborative research workflows.

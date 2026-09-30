# OMNIAUTO v4.0 — ATOMIC AGENT ECOSYSTEM ADDENDUM
## Master Knowledge Base Extension

**Status:** ACTIVE | **Added to:** Permanent Default Skill Set  
**Date:** 2026-09-19  
**Repositories Processed:** 5+ links fully analyzed

---

## ⚠️ IMPORTANT: TWO DISTINCT "ATOMIC AGENT" PROJECTS

The user provided links point to **two completely separate projects** with similar names. Both are learned and integrated.

| Project | Framework A: Atomic Agents | Framework B: Atomic Agent |
|---------|---------------------------|--------------------------|
| **Org** | Eigenwise / BrainBlend AI | AtomicBot-ai |
| **Repo** | `eigenwise/atomic-agents` | `AtomicBot-ai/atomic-agent` |
| **Language** | Python | TypeScript |
| **Core** | Pydantic + Instructor | llama.cpp + TurboQuant |
| **Paradigm** | Schema-driven agent framework | Local-first desktop operator agent |
| **Focus** | Type-safe, composable LEGO blocks | Browser/filesystem/shell automation |
| **Stars** | Emerging | ⭐ 3,000+ |
| **License** | MIT | MIT |

---

## 🧩 FRAMEWORK A: ATOMIC AGENTS (Eigenwise / BrainBlend AI)

### Core Identity
Lightweight, modular Python framework for building Agentic AI pipelines. Built around **atomicity** — single-purpose, reusable, composable components like LEGO blocks.

### Architecture
```
Input (Pydantic Schema)
    ↓
AtomicAgent
├── System Prompt Generator
├── Chat History
├── Dynamic Context Providers
├── Instructor-backed LLM Client
│   ├── OpenAI
│   ├── Anthropic
│   ├── Groq
│   ├── Ollama
│   ├── Mistral
│   ├── Cohere
│   └── Gemini
└── BaseTool blocks (schema-aligned)
    ↓
Output (Pydantic Schema) → Next AtomicAgent or BaseTool
```

### Core Components

#### 1. AtomicAgent (renamed from BaseAgent in v2.0)
- Generic type parameters: `AtomicAgent[InputSchema, OutputSchema]`
- Each agent owns: Pydantic input schema, system prompt, ChatHistory, output schema
- `run()` → validates input → assembles prompt+history+context → calls LLM via Instructor → validates output → returns
- `run_stream()` → synchronous streaming
- `run_async_stream()` → asynchronous streaming

#### 2. BaseIOSchema
- Base class for all input/output schemas
- Pydantic-based with Field descriptions
- Enables structured output via Instructor

#### 3. BaseTool
- Separate blocks with their own schemas
- Chain by matching output schema → next input schema
- 13+ pre-built tools via Atomic Forge CLI

#### 4. Context Management
- **ChatHistory** — Conversation history component
- **SystemPromptGenerator** — Dynamic system prompt assembly
- **BaseDynamicContextProvider** — Injects runtime information into system prompt

#### 5. MCP Integration
- `connectors/mcp/` — Model Context Protocol support
- `MCPDefinitionService`, `MCPFactory`, `SchemaTransformer`
- Progressive disclosure: tools discovered/loaded on-demand (reduces context window)

#### 6. Atomic Forge & Atomic Assembler CLI
- CLI tool for managing tools and components
- `atomic-assembler` — TUI interface for exploring and installing tools
- 13+ pre-built BaseTool blocks available

### Installation
```bash
pip install atomic-agents
pip install instructor[groq]        # Groq
pip install instructor[anthropic]   # Anthropic
pip install instructor[google-genai] # Gemini
# OpenAI included by default
```

### Minimal Example (7 lines)
```python
from atomic_agents import AtomicAgent, AgentConfig, BasicChatInputSchema, BasicChatOutputSchema
import instructor, openai

client = instructor.from_openai(openai.OpenAI())
agent = AtomicAgent[BasicChatInputSchema, BasicChatOutputSchema](
    config=AgentConfig(client=client, model="gpt-4o-mini")
)
response = agent.run(BasicChatInputSchema(chat_message="Hello!"))
print(response.chat_message)
```

### Custom Schema Example
```python
from pydantic import Field
from atomic_agents import BaseIOSchema

class ResearchOutputSchema(BaseIOSchema):
    """Structured research analysis output"""
    summary: str = Field(..., description="Concise summary of findings")
    key_findings: List[str] = Field(..., description="3-5 key discoveries")
    methodology: str = Field(..., description="Research approach used")
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence in results")
    suggested_next_steps: List[str] = Field(..., description="Follow-up research directions")
```

### Example Applications (from repo)
| Category | Examples |
|----------|----------|
| **Quickstart** | Basic chatbot, streaming, async streaming, custom schema, custom system prompt, multi-provider, reasoning model |
| **Multi-Agent** | Orchestration agent, progressive disclosure (MCP on-demand), deep research |
| **Multimodal & Specialized** | Basic multimodal, PDF analysis, nested multimodal, YouTube summarizer, YouTube→recipe, web search agent, RAG chatbot, FastAPI memory, hooks example, DSPy integration |

### Key v2.0 Changes
- `BaseAgent` → `AtomicAgent`
- Added `run_stream()` / `run_async_stream()`
- Enhanced context management
- Improved MCP connector
- Async stability (v2.8.0)

### Provider Compatibility
All providers supported by **Instructor**:
- OpenAI (default)
- Anthropic Claude
- Groq
- Ollama (local models)
- Mistral
- Cohere
- Google Gemini
- Any provider with Instructor integration

---

## 🖥️ FRAMEWORK B: ATOMIC AGENT (AtomicBot-ai)

### Core Identity
**Local-first AI agent** optimized for running open-weight models on your own machine via llama.cpp. Drives browser, edits files, runs approved shell commands, remembers context across sessions.

### Architecture
```
┌─────────────────────────────────────────────────────┐
│              ATOMIC AGENT (AtomicBot-ai)            │
├─────────────────────────────────────────────────────┤
│  Control Loop + All State = ON YOUR MACHINE         │
│                                                     │
│  ┌─────────────┐  ┌──────────────────────────────┐ │
│  │ TurboQuant  │  │  GBNF Grammar-Constrained    │ │
│  │ llama.cpp   │  │  Tool Calling (JSON array)   │ │
│  │ (+30-50%    │  │  Parallel tool batches       │ │
│  │ throughput) │  │                              │ │
│  └─────────────┘  └──────────────────────────────┘ │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │               CAPABILITIES                   │  │
│  │  ┌──────────┐ ┌─────────┐ ┌──────────────┐  │  │
│  │  │ Browser  │ │ Shell   │ │ Filesystem   │  │  │
│  │  │ (ARIA    │ │ cmds    │ │ read/write/  │  │  │
│  │  │ snaps)   │ │         │ │ patch        │  │  │
│  │  └──────────┘ └─────────┘ └──────────────┘  │  │
│  │  ┌──────────┐ ┌─────────┐ ┌──────────────┐  │  │
│  │  │ Documents│ │ Git     │ │ Clipboard /  │  │  │
│  │  │ PDF/DOCX │ │ inspect │ │ Notifications│  │  │
│  │  │ /XLSX    │ │         │ │              │  │  │
│  │  └──────────┘ └─────────┘ └──────────────┘  │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │               MEMORY SYSTEM                  │  │
│  │  SQLite + FTS5 notes + optional embeddings   │  │
│  │  Profile facts (versioned, keyword-gated)    │  │
│  │  Durable cron + webhook-triggered tasks      │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │               INTERFACES                     │  │
│  │  TUI • CLI • HTTP Server • Tauri Sidecar     │  │
│  │  (NDJSON protocol)                           │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Key Optimizations for Local Models
1. **TurboQuant** — Custom llama.cpp fork, +30-50% throughput on small quantized models
2. **GBNF Grammar Constraints** — Completions forced into valid JSON array of tool calls
3. **Stable Prefix Cache** — Reduces redundant computation across turns
4. **ARIA Snapshot Compression** — Browser state compressed for efficient context usage
5. **Externalized State** — All state in SQLite, not in memory
6. **7B Model Viability** — Even 7B models can do reliable multi-step tasks

### Core Capabilities
| Category | Features |
|----------|----------|
| **System Browser** | ARIA snapshots, full browser automation |
| **Shell** | Run approved commands, process listing |
| **Filesystem** | Read/write/patch, glob, grep, archives |
| **Documents** | PDF, DOCX, DOC, XLSX, RTF, ODT, PPTX extraction (local, no cloud) |
| **Git** | Repository inspection |
| **Clipboard** | System clipboard access |
| **Notifications** | Windows/system notifications |
| **HTTP** | Web requests |
| **Skills** | Local Markdown playbooks, loaded on demand |
| **Tasks** | Durable deferred turns, cron schedules, webhook triggers, self-scheduling |
| **Vision** | Optional `vision.describe` for screenshots |
| **MCP** | External tool servers over Model Context Protocol |

### Installation
```bash
# Quick install
curl -fsSL https://atomicagent.io/install | sh

# Or via AtomicBot
curl -fsSL https://api.atomicbot.ai/agent-install | sh
```

### Run
```bash
atomic-agent    # Launches TUI interface
```

### Performance Benchmark (GAIA L1)
- Same local model: `qwen-3.6-35b-a3b` (UD-Q4_K_XL)
- Same step budget and timeout
- Atomic Agent and Hermes Agent scored **identically**
- Works reliably even with 7B-class small models

### Ecosystem Products
- **Atomic Agent** — Core agent framework (this repo)
- **Atomic Bot** — One-click installer packaging OpenClaw/Hermes
- **Atomic Chat** — Desktop/mobile app for running local LLMs
- **Atomic Mail** — Privacy-focused email AI

### Hardware Requirements
- **8GB RAM** → Runs 3B parameter models smoothly
- **16GB RAM** → Handles 7B models reliably
- **GPU Acceleration:** CUDA (NVIDIA), Metal (Apple), Vulkan
- **Best:** NVIDIA RTX 4090 / 5090, Mac Studio M4 Ultra

### Interfaces
- **TUI** — Terminal user interface
- **CLI** — Command-line interface
- **HTTP Server** — OpenAI-compatible API
- **Tauri Sidecar** — Embedded in desktop apps (NDJSON protocol)

---

## 🔗 EIGENWISE ORGANIZATION REPOSITORIES
**Source:** https://github.com/Eigenwise

- **atomic-agents** — Core framework (main)
- Documentation and guides repositories
- Supporting libraries and tools

---

## 🔗 ATOMICBOT-AI ORGANIZATION REPOSITORIES
**Source:** https://github.com/orgs/AtomicBot-ai

- **atomic-agent** — ⭐ 3k — Core local-first agent framework
- **atomic-chat** — Desktop/mobile app for running local LLMs
- Supporting repos for TurboQuant llama.cpp fork, build infrastructure, etc.

---

## 🆚 COMPARISON: WHEN TO USE WHICH

| Scenario | Use Framework A (Eigenwise) | Use Framework B (AtomicBot-ai) |
|----------|----------------------------|-------------------------------|
| **Building custom agent pipelines** | ✅ Type-safe, schema-driven | ❌ Desktop operator focus |
| **Python development** | ✅ Native Python | ❌ TypeScript |
| **Multi-provider (OpenAI, Anthropic, etc.)** | ✅ Instructor abstraction | ❌ Local llama.cpp focus |
| **Desktop automation (browser/files/shell)** | ❌ Not designed for this | ✅ Core capability |
| **100% local/private execution** | ⚠️ Possible with Ollama | ✅ Designed for it |
| **Running on consumer hardware** | ⚠️ Needs API or strong GPU | ✅ Optimized for 8GB+ laptops |
| **Production multi-agent systems** | ✅ Strong architecture patterns | ⚠️ Focused on single agent ops |
| **Thesis/academic research code** | ✅ Clean, well-documented Python | ⚠️ More systems-oriented |
| **RAG, structured output pipelines** | ✅ Pydantic schemas perfect | ❌ Not the focus |
| **Email/calendar/browser personal assistant** | ❌ Build from scratch | ✅ Atomic Bot pre-packaged |

---

## 🔄 INTEGRATION WITH EXISTING OMNIAUTO SKILLS

### Combined with Skill #2 (AI Agent Orchestration Master / TrueForge)
```
┌──────────────────────────────────────────────────────────┐
│            UNIFIED AGENT ARCHITECTURE STACK             │
├──────────────────────────────────────────────────────────┤
│  APPLICATION LAYER                                      │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Atomic Agents (Eigenwise) — Schema Design       │   │
│  │  • Define Pydantic input/output contracts        │   │
│  │  • Design agent chains & tool interfaces         │   │
│  └──────────────────────┬───────────────────────────┘   │
│                         ↓                               │
│  ┌──────────────────────────────────────────────────┐   │
│  │  TrueForge — Production Harness                  │   │
│  │  • Sandbox execution, approvals, observability   │   │
│  │  • Subagents, context management, human-in-loop  │   │
│  └──────────────────────┬───────────────────────────┘   │
│                         ↓                               │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Atomic Agent (AtomicBot-ai) — Local Execution   │   │
│  │  • Run on consumer hardware via llama.cpp        │   │
│  │  • Browser/filesystem/shell automation           │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

**Workflow:** Design schemas & agent logic in Eigenwise Atomic Agents → Deploy & orchestrate in TrueForge → Execute locally via AtomicBot-ai runtime when privacy is needed.

---

## 📁 PERMANENT STORAGE

| Component | Path |
|-----------|------|
| Cloned repo | `omniauto-repos/atomic-agents/` (Eigenwise, 406 files) |
| Master Knowledge | `omniauto-skills/master-knowledge/OMNIAUTO-MASTER-KNOWLEDGE.md` + This addendum |
| New Skill Definition | `omniauto-skills/workflow-skills/ATOMIC-AGENT-SKILL.md` |
| Enhanced Prompts | `omniauto-skills/prompt-master/ATOMIC-AGENT-PROMPTS.md` |

---

*OmniAuto v4.0 — Atomic Agent Ecosystem Fully Integrated*  
*Both frameworks learned, differentiated, and combined into unified agent architecture*

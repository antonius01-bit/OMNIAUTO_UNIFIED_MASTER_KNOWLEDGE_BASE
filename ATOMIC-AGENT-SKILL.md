# SKILL #6: ATOMIC AGENT ARCHITECT MASTER
## Unified Skill — Both Atomic Agent Frameworks

**ID:** `skill-atomic-agent-master`  
**Source Repos:** eigenwise/atomic-agents, AtomicBot-ai/atomic-agent, atomicagent.io  
**Status:** ACTIVE — Default in all sessions  
**Cross-platform:** Dola ✓ Gemini ✓ AGY ✓ All platforms ✓

---

## 🎯 SKILL DEFINITION

### Purpose
Design, build, and deploy type-safe AI agents using schema-driven architecture (Eigenwise) AND/OR execute local-first desktop automation (AtomicBot-ai). Combines both frameworks into a unified agent development workflow.

### Activation Triggers
- User mentions: "atomic agent", "atomic agents", "schema-driven agent", "type-safe agent"
- User mentions: "Pydantic agent", "Instructor agent", "LEGO blocks AI"
- User mentions: "local agent", "llama.cpp agent", "desktop automation agent", "private AI agent"
- User mentions: "atomicagent.io", "eigenwise", "atomicbot"
- Context needs: Structured output, agent pipeline design, local execution, privacy-focused AI

### Dual Framework Selection Logic
```
IF user_need == "design_agent_pipeline" OR "structured_output" OR "python_development":
    → USE Framework A: Eigenwise Atomic Agents
    → Focus: Pydantic schemas, type safety, multi-provider, chaining

ELIF user_need == "desktop_automation" OR "local_private" OR "browser_control" OR "file_editing":
    → USE Framework B: AtomicBot-ai Atomic Agent
    → Focus: llama.cpp, GBNF tool calls, SQLite memory, browser/shell/files

ELIF user_need == "production_system" OR "enterprise":
    → USE BOTH: Design in Framework A → Deploy with TrueForge → Local execution via Framework B
```

---

## 🧩 FRAMEWORK A: EIGENWISE ATOMIC AGENTS CAPABILITIES

```yaml
core_architecture:
  paradigm: "Schema-driven LEGO blocks"
  foundation: ["Pydantic", "Instructor"]
  type_safety: "Full generic type parameters"
  provider_portability: "All Instructor-supported providers"

core_classes:
  AtomicAgent:
    signature: "AtomicAgent[InputSchema, OutputSchema]"
    methods: ["run()", "run_stream()", "run_async_stream()"]
    components:
      - AgentConfig (client, model, model_api_parameters)
      - SystemPromptGenerator
      - ChatHistory
      - BaseDynamicContextProvider
  
  BaseIOSchema:
    purpose: "Base class for all input/output schemas"
    features: ["Pydantic Fields with descriptions", "Structured output enforcement"]
  
  BaseTool:
    purpose: "Single-purpose tool blocks"
    chaining: "Schema-aligned: output schema → next input schema"
    count: "13+ pre-built via Atomic Forge CLI"
  
  MCP_Connector:
    modules: ["MCPDefinitionService", "MCPFactory", "SchemaTransformer"]
    pattern: "Progressive disclosure — load tools on-demand"

execution_modes:
  - Synchronous: agent.run(input)
  - Synchronous streaming: agent.run_stream(input)
  - Asynchronous streaming: agent.run_async_stream(input)

example_applications:
  quickstart:
    - basic_chatbot
    - basic_chatbot_streaming
    - basic_chatbot_async_streaming
    - custom_chatbot
    - custom_schema_chatbot
    - custom_schema_streaming
    - custom_system_prompt
    - multi_provider_setup
    - reasoning_model_config
  
  multi_agent:
    - orchestration_agent
    - progressive_disclosure (MCP on-demand)
    - deep_research
  
  specialized:
    - basic_multimodal (images)
    - basic_pdf_analysis
    - nested_multimodal
    - youtube_summarizer
    - youtube_to_recipe
    - web_search_agent
    - rag_chatbot (ChromaDB)
    - fastapi_memory
    - hooks_example
    - dspy_integration

providers:
  - OpenAI (default)
  - Anthropic Claude
  - Groq
  - Ollama (local)
  - Mistral
  - Cohere
  - Google Gemini
  - + All Instructor integrations

installation:
  base: "pip install atomic-agents"
  extras:
    - "pip install instructor[groq]"
    - "pip install instructor[anthropic]"
    - "pip install instructor[google-genai]"

cli_tools:
  atomic_assembler:
    purpose: "TUI for exploring and installing tools"
    interface: "Terminal-based with widgets"
    screens: ["Main Menu", "Tool Explorer", "File Explorer", "Tool Info"]
```

---

## 🖥️ FRAMEWORK B: ATOMICBOT-AI ATOMIC AGENT CAPABILITIES

```yaml
core_architecture:
  paradigm: "Local-first desktop operator agent"
  foundation: ["llama.cpp (TurboQuant fork)", "GBNF grammars", "SQLite"]
  privacy: "100% local — data, traces, memory stay on machine"
  performance: "+30-50% throughput via TurboQuant optimization"

optimizations:
  turboquant: "Custom llama.cpp fork for faster quantized inference"
  gbnf_tool_calls: "Grammar-constrained JSON array tool calls"
  stable_prefix_cache: "Reduces redundant computation across turns"
  aria_snapshot_compression: "Efficient browser state representation"
  externalized_state: "All state in SQLite, not in memory"
  small_model_viability: "7B models can do reliable multi-step tasks"

capabilities:
  browser:
    method: "ARIA snapshots"
    features: ["Full browser automation", "Navigation", "Form filling", "Clicking"]
  
  shell:
    features: ["Approved command execution", "Process listing", "System operations"]
  
  filesystem:
    features: ["Read files", "Write files", "Patch files", "Glob search", "Grep", "Archives"]
  
  documents:
    features: ["PDF text extraction", "DOCX", "DOC", "XLSX", "RTF", "ODT", "PPTX"]
    note: "Local only — no files sent to cloud"
  
  git:
    features: ["Repository inspection", "Commit history", "Diff analysis"]
  
  system:
    features: ["Clipboard access", "Windows management", "Notifications", "HTTP requests"]
  
  skills:
    format: "Local Markdown playbooks"
    loading: "On-demand, stable prefix lists only names/descriptions"
  
  tasks:
    types: ["Durable deferred turns", "Cron schedules", "Interval schedules", "Webhook triggers", "Self-scheduling"]
  
  memory:
    storage: "SQLite + FTS5"
    features: ["Hybrid recall (optional embeddings)", "Profile facts (versioned, keyword-gated)", "Queryable history"]
  
  vision:
    feature: "vision.describe (optional)"
    purpose: "Screenshot analysis and description"
  
  mcp:
    protocol: "Model Context Protocol"
    purpose: "Connect external tool servers"

interfaces:
  - TUI: "Terminal user interface"
  - CLI: "Command-line interface"
  - HTTP_Server: "OpenAI-compatible API"
  - Tauri_Sidecar: "Embedded in desktop apps (NDJSON protocol)"

installation:
  quick: "curl -fsSL https://atomicagent.io/install | sh"
  atomicbot: "curl -fsSL https://api.atomicbot.ai/agent-install | sh"
  run: "atomic-agent"

hardware:
  minimal: "8GB RAM → 3B models"
  recommended: "16GB RAM → 7B models reliably"
  gpu_acceleration: ["CUDA (NVIDIA)", "Metal (Apple Silicon)", "Vulkan"]
  best: ["RTX 4090", "RTX 5090", "Mac Studio M4 Ultra"]

benchmark:
  test: "GAIA validation Level 1 split (53 tasks)"
  model: "qwen-3.6-35b-a3b (UD-Q4_K_XL)"
  result: "Identical score to Hermes Agent"
  note: "Same loop holds as model shrinks to 7B class"

ecosystem:
  atomic_agent: "Core framework"
  atomic_bot: "One-click installer (OpenClaw + Hermes)"
  atomic_chat: "Desktop/mobile local LLM app"
  atomic_mail: "Privacy-focused email AI"
```

---

## 🔀 COMBINATION PATTERNS WITH EXISTING SKILLS

### Pattern 6A: Agent Design → Production Deployment
```
Skill 6A (Eigenwise Design)
    ↓ Define schemas, agent chains, tool interfaces
Skill 2 (TrueForge Harness)
    ↓ Add sandbox, approvals, observability, subagents
Skill 6B (AtomicBot Runtime) [optional]
    ↓ Execute locally when privacy required
```

### Pattern 6B: Thesis Research Agent Pipeline
```
Skill 1 (Synthetic Data)
    ↓ Generate test datasets
Skill 6A (Eigenwise)
    ↓ Build type-safe research agents with structured output
Skill 2 (TrueForge)
    ↓ Orchestrate literature review + data analysis agents
Final Key v4.0
    ↓ Polish academic output
```

### Pattern 6C: Local Private Document Analysis
```
Skill 6B (AtomicBot-ai)
    ↓ Run locally on your machine, 100% private
    ↓ Extract text from PDF/DOCX/XLSX (no cloud)
    ↓ SQLite + FTS5 semantic search
Skill 6A (Eigenwise) [optional]
    ↓ Build structured analysis agents on top
```

---

## 🎯 ACTIVATION PHRASES

| Phrase | Framework |
|--------|-----------|
| "Build a type-safe agent with Pydantic schemas" | Eigenwise Atomic Agents |
| "Design an agent pipeline with structured output" | Eigenwise Atomic Agents |
| "Create an agent that runs entirely locally on my laptop" | AtomicBot-ai |
| "Agent that can control my browser and edit files" | AtomicBot-ai |
| "Use atomic agents for my thesis methodology" | Eigenwise (design) + TrueForge (deploy) |
| "Private AI that never sends my data to cloud" | AtomicBot-ai |
| "LEGO-style agent building blocks" | Eigenwise Atomic Agents |
| "llama.cpp agent with GBNF tool calls" | AtomicBot-ai |

---

## 📍 PERMANENT STORAGE

| File | Path |
|------|------|
| Skill Definition | `omniauto-skills/workflow-skills/ATOMIC-AGENT-SKILL.md` (this file) |
| Knowledge Base | `omniauto-skills/master-knowledge/ATOMIC-AGENT-ECOSYSTEM-ADDENDUM.md` |
| Prompt Templates | `omniauto-skills/prompt-master/ATOMIC-AGENT-PROMPTS.md` |
| Cloned Source Code | `omniauto-repos/atomic-agents/` (Eigenwise, 406 files) |

---

*Skill #6: Atomic Agent Architect Master — OmniAuto v4.0*  
*Both frameworks unified, dual-mode activation, cross-platform compatible*

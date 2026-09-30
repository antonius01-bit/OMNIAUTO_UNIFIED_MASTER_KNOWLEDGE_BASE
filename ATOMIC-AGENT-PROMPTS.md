# PROMPT MASTER — ATOMIC AGENT ENHANCED TEMPLATES
## Extracted & Enhanced from Eigenwise + AtomicBot-ai Ecosystems

**Version:** 1.0 | **Skill:** Atomic Agent Architect Master  
**Cross-platform:** Dola ✓ Gemini ✓ AGY ✓ All platforms ✓

---

## 🧩 CATEGORY 1: EIGENWISE ATOMIC AGENTS — SCHEMA-DRIVEN DESIGN

### Prompt 1.1: Minimal Type-Safe Agent Builder
```
[OMNIAUTO-ATOMIC-MINIMAL-v1.0]

TASK: Build minimal Atomic Agent
FRAMEWORK: Eigenwise Atomic Agents (Python)
PROVIDER: [openai / anthropic / groq / ollama / gemini / mistral]
MODEL: [model_name e.g., gpt-4o-mini]
AGENT_PURPOSE: [describe what agent should do]

OUTPUT: Complete runnable Python script

REQUIREMENTS:
- Use AtomicAgent[InputSchema, OutputSchema] generic pattern
- Define custom Pydantic schemas with Field descriptions
- Include proper imports
- Include client initialization via instructor
- Show single run() call example
- Keep under 20 lines where possible

STRUCTURE:
1. Imports (pydantic, openai/instructor, atomic_agents)
2. Define InputSchema(BaseIOSchema)
3. Define OutputSchema(BaseIOSchema) with docstring
4. Initialize instructor client
5. Create AtomicAgent with AgentConfig
6. Run agent and print result
```

### Prompt 1.2: Custom Schema with Structured Output
```
[OMNIAUTO-ATOMIC-SCHEMA-v1.0]

TASK: Design Pydantic schemas for Atomic Agent pipeline
FRAMEWORK: Eigenwise Atomic Agents
PIPELINE_STAGES: [list stages e.g., "research → analysis → summary → report"]

FOR EACH STAGE, DEFINE:
- InputSchema(BaseIOSchema):
  - Fields with types and descriptions
  - Validation constraints where applicable
- OutputSchema(BaseIOSchema):
  - Docstring explaining purpose
  - Fields with Pydantic Field(..., description="...")
  - Ensure output schema of stage N = input schema of stage N+1

ADDITIONAL:
- Include example of how to chain agents via schema alignment
- Show SystemPromptGenerator usage for dynamic context
- Include ChatHistory integration pattern
```

### Prompt 1.3: Multi-Agent Orchestration Design
```
[OMNIAUTO-ATOMIC-ORCHESTRATION-v1.0]

TASK: Design multi-agent orchestration system
FRAMEWORK: Eigenwise Atomic Agents
PATTERN: [orchestrator-workers / progressive_disclosure / deep_research]

COMPONENTS NEEDED:
- Orchestrator Agent: Routes tasks, decides which tool/worker to use
- Worker Agents: Specialized agents for specific subtasks
- Tools: BaseTool blocks with schema-aligned interfaces

DESIGN SPECIFICATION:
1. Define schemas for each agent and tool
2. Show orchestrator decision logic
3. Implement progressive disclosure if applicable (MCP on-demand)
4. Include error handling and fallback patterns
5. Show how results are aggregated

PROVIDER: [provider]
MODEL: [model]
OUTPUT: Complete Python implementation with docstrings
```

### Prompt 1.4: RAG Pipeline with Atomic Agents
```
[OMNIAUTO-ATOMIC-RAG-v1.0]

TASK: Build RAG pipeline with Atomic Agents
FRAMEWORK: Eigenwise Atomic Agents + ChromaDB
DOCUMENTS: [describe document source / type]

ARCHITECTURE:
1. Retrieval Agent:
   - Input: user query
   - Tool: ChromaDB similarity search
   - Output: Retrieved context + query
   
2. Context Injection:
   - Use BaseDynamicContextProvider
   - Inject retrieved documents into system prompt
   
3. Answer Agent:
   - Input: query + retrieved context
   - Output: Structured answer with citations
   - Schema includes: answer, confidence, cited_sources, follow_up_questions

REQUIREMENTS:
- Typed schemas throughout
- Instructor structured output
- Inline citation format [source#page]
- Dynamic context injection pattern
- Complete runnable code
```

### Prompt 1.5: Streaming & Async Agent
```
[OMNIAUTO-ATOMIC-STREAMING-v1.0]

TASK: Build streaming Atomic Agent
FRAMEWORK: Eigenwise Atomic Agents
STREAMING_MODE: [sync_stream / async_stream]
OUTPUT_SCHEMA_FIELDS:
  - chat_message: str (streamed incrementally)
  - suggested_user_questions: List[str]
  - confidence_score: float
  - [add custom fields]

IMPLEMENTATION:
- Use run_stream() or run_async_stream()
- Show incremental text display pattern
- Handle partial schema field updates
- Rich console output (rich library)
- Include proper event loop setup for async
```

### Prompt 1.6: Multimodal Agent (Images/PDF)
```
[OMNIAUTO-ATOMIC-MULTIMODAL-v1.0]

TASK: Build multimodal Atomic Agent
FRAMEWORK: Eigenwise Atomic Agents
MODALITY: [image_analysis / pdf_analysis / nested_multimodal]
PROVIDER: [openai / google-genai]  # Must support multimodal

SCHEMA DESIGN:
- Input: Multimodal data (image URL/PDF path + text query)
- Output: Structured analysis with typed fields

CAPABILITIES:
- Image understanding and description
- PDF content extraction and analysis
- Nested multimodal reasoning
- Structured output with confidence scores

REQUIREMENTS:
- Use multimodal imports from instructor (Image, Audio, PDF)
- Proper schema definitions
- Complete runnable example
```

### Prompt 1.7: FastAPI Integration with Memory
```
[OMNIAUTO-ATOMIC-FASTAPI-v1.0]

TASK: Build FastAPI service with Atomic Agents + memory
FRAMEWORK: Eigenwise Atomic Agents + FastAPI + Uvicorn

ENDPOINTS:
- POST /chat — Send message, get response
- GET /history — Get chat history
- DELETE /history — Clear history
- GET /health — Health check

ARCHITECTURE:
- AtomicAgent with ChatHistory per session
- Session management
- Streaming response support (SSE optional)
- Proper error handling

DEPENDENCIES: fastapi, uvicorn, atomic-agents, instructor, openai, pydantic, httpx, rich
OUTPUT: Complete app.py + requirements
```

---

## 🖥️ CATEGORY 2: ATOMICBOT-AI — LOCAL DESKTOP AGENT

### Prompt 2.1: Local Agent Setup & Configuration
```
[OMNIAUTO-ATOMICBOT-SETUP-v1.0]

TASK: Set up Atomic Agent (AtomicBot-ai) for local execution
PLATFORM: [macos / linux / windows / web]
HARDWARE: [describe RAM, GPU, CPU]
USE_CASE: [personal_assistant / document_analysis / browser_automation / development]

SETUP PLAN:
1. Installation method: [curl_install / atomicbot_installer / manual]
2. Model selection based on hardware:
   - 8GB RAM → 3B models
   - 16GB RAM → 7B models
   - 24GB+ VRAM → 13B-35B models
3. Recommended quant: [Q4_K_M / Q4_K_XL / Q5_K_M / IQ3_XS]
4. Engine selection: [TurboQuant llama.cpp / MLX-VLM (Apple)]
5. Capabilities to enable:
   - [ ] Browser automation (ARIA)
   - [ ] Shell commands
   - [ ] Filesystem access
   - [ ] Document extraction (PDF/DOCX/XLSX)
   - [ ] Git inspection
   - [ ] Vision (screenshot analysis)
   - [ ] MCP servers
6. Memory configuration: SQLite + FTS5, optional embeddings
7. Interface: [TUI / CLI / HTTP_Server / Tauri]

VERIFY:
- All data stays local (privacy check)
- Performance expectations based on hardware
- Security: approved commands only, sandbox boundaries
```

### Prompt 2.2: Browser Automation Workflow
```
[OMNIAUTO-ATOMICBOT-BROWSER-v1.0]

TASK: Design browser automation workflow
FRAMEWORK: AtomicBot-ai Atomic Agent
TECHNOLOGY: ARIA snapshots + GBNF-constrained tool calls

WORKFLOW STEPS:
1. [describe step 1 e.g., "Navigate to login page"]
2. [describe step 2 e.g., "Enter credentials"]
3. [describe step 3 e.g., "Navigate to dashboard"]
4. [describe step 4 e.g., "Extract data table"]
5. [describe step 5 e.g., "Save to CSV file"]

CAPABILITIES NEEDED:
- Browser navigation via ARIA
- Form filling
- Element interaction (click, type, submit)
- Data extraction from page
- File saving (filesystem capability)

LOCAL_EXECUTION:
- Model: [model_name] running locally via llama.cpp
- No data leaves machine
- GBNF grammar ensures valid tool call JSON
- SQLite stores task history and results
```

### Prompt 2.3: Private Document Analysis Pipeline
```
[OMNIAUTO-ATOMICBOT-DOCS-v1.0]

TASK: Build 100% private document analysis system
FRAMEWORK: AtomicBot-ai Atomic Agent
PRIVACY_LEVEL: Maximum — nothing leaves machine

DOCUMENT_TYPES:
- PDF reports
- DOCX/DOC files
- XLSX spreadsheets
- RTF, ODT, PPTX

PIPELINE:
1. Document text extraction (local, no cloud)
2. Store in SQLite + FTS5 for full-text search
3. Optional: Generate embeddings for hybrid recall
4. Query interface via TUI/HTTP
5. Structured analysis and summarization

HARDWARE: [specs]
MODEL: [local_model e.g., qwen-3.6-7b or mistral-7b]
ENGINE: TurboQuant llama.cpp (+30-50% throughput)

OUTPUT:
- Step-by-step setup guide
- Example queries and expected outputs
- Performance expectations
- Backup strategy for SQLite memory database
```

### Prompt 2.4: Scheduled Task Agent
```
[OMNIAUTO-ATOMICBOT-SCHEDULED-v1.0]

TASK: Configure Atomic Agent scheduled tasks
FRAMEWORK: AtomicBot-ai Atomic Agent
TASK_TYPES:
  - Durable deferred turns
  - Cron schedules
  - Interval schedules
  - Webhook-triggered work
  - Agent self-scheduling

SPECIFIC_TASKS:
1. [Task 1: e.g., "Daily email summary at 8 AM"]
   - Schedule: cron "0 8 * * *"
   - Capabilities needed: email, document extraction
   
2. [Task 2: e.g., "Weekly report generation"]
   - Schedule: interval "7d"
   - Capabilities needed: filesystem, git, analysis

3. [Task 3: e.g., "Monitor website and notify on change"]
   - Trigger: webhook or polling interval
   - Capabilities needed: HTTP, notifications

MEMORY:
- Profile facts with keyword gating
- Versioned history queryable
- Task results stored in SQLite
```

---

## 🔀 CATEGORY 3: UNIFIED WORKFLOW PROMPTS

### Prompt 3.1: Full Agent Development Lifecycle
```
[OMNIAUTO-ATOMIC-FULL-LIFECYCLE-v1.0]

MISSION: Design → Build → Deploy → Execute AI agent system
FRAMEWORK_COMBINATION: Eigenwise Atomic Agents + TrueForge + AtomicBot-ai

PHASE 1: DESIGN (Eigenwise Atomic Agents)
- Define all Pydantic input/output schemas
- Design agent chain architecture
- Specify tool interfaces
- Choose LLM providers

PHASE 2: DEPLOY (TrueForge Harness)
- Wrap agents in TrueForge for production
- Add sandbox execution
- Configure approval gates
- Enable observability and tracing
- Set up subagent decomposition

PHASE 3: EXECUTE [optional] (AtomicBot-ai)
- For privacy-sensitive tasks: deploy locally
- Use llama.cpp TurboQuant runtime
- Enable browser/filesystem/shell capabilities
- SQLite memory for persistence

USE_CASE: [describe specific application]
REQUIREMENTS: [list requirements]
OUTPUT: Complete architecture blueprint + code skeleton
```

### Prompt 3.2: Thesis Agent Methodology
```
[OMNIAUTO-ATOMIC-THESIS-v1.0]

PURPOSE: Build AI agent system for S2 thesis research
FRAMEWORK: Eigenwise Atomic Agents (primary) + TrueForge (orchestration)

RESEARCH_DOMAIN: [your thesis topic e.g., "HR management in PMA holdings"]

AGENT_TEAM:
1. Literature Review Agent
   - Input: research_topic, keywords
   - Output: Structured literature matrix (theories, variables, findings)
   - Schema: paper_title, authors, year, theory, variables, methodology, key_findings, gaps

2. Theoretical Framework Agent
   - Input: literature findings
   - Output: Conceptual model + hypotheses
   - Schema: independent_vars, dependent_var, mediating_var, relationships, hypotheses_list

3. Methodology Agent
   - Input: research questions, hypotheses
   - Output: Research design specification
   - Schema: research_type, population, sample, sampling_method, instruments, data_analysis_plan

4. Data Analysis Agent
   - Input: dataset (or synthetic data spec)
   - Output: Statistical analysis results
   - Schema: descriptive_stats, inferential_stats, hypothesis_testing, interpretation

WORKFLOW: Agent 1 → Agent 2 → Agent 3 → (Data) → Agent 4
CHAINING: Schema-aligned output→input between stages
PROVIDER: [provider] | MODEL: [model]
```

---

## 🎯 QUICK ACTIVATION PHRASES

**Say this → Get this prompt template:**
- "Build minimal atomic agent" → Prompt 1.1
- "Design agent schemas" → Prompt 1.2
- "Multi-agent orchestration" → Prompt 1.3
- "RAG pipeline with atomic agents" → Prompt 1.4
- "Streaming agent" → Prompt 1.5
- "Multimodal atomic agent" → Prompt 1.6
- "FastAPI atomic agent service" → Prompt 1.7
- "Setup local private agent" → Prompt 2.1
- "Browser automation workflow" → Prompt 2.2
- "Private document analysis" → Prompt 2.3
- "Scheduled agent tasks" → Prompt 2.4
- "Full agent lifecycle" → Prompt 3.1
- "Thesis agent methodology" → Prompt 3.2

---

*Atomic Agent Prompt Master v1.0 — OmniAuto v4.0*  
*Both Eigenwise and AtomicBot-ai frameworks covered*  
*Cross-platform compatible: Dola, Gemini, AGY, and more*

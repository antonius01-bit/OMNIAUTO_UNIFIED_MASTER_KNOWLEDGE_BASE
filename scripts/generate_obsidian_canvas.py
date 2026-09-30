import json
import os

VAULT_DIR = r"C:\Users\antoni\Dola\obsidian_vault"
CANVAS_PATH = os.path.join(VAULT_DIR, "Dola_AI_Master_Workflow.canvas")

canvas_data = {
    "nodes": [
        # GROUP 1: HEAD ENGINE
        {
            "id": "group-head",
            "type": "group",
            "x": -900,
            "y": -350,
            "width": 520,
            "height": 720,
            "label": "👑 PHASE 0: HEAD PROMPT MASTER & TOKEN OPTIMIZER",
            "color": "4" # Green/Emerald
        },
        {
            "id": "node-raw-input",
            "type": "text",
            "x": -870,
            "y": -280,
            "width": 460,
            "height": 130,
            "text": "### 📥 Raw User Command / Intent\n- Captures any raw instruction, topic, or question.\n- Intercepted by **`/omni-auto` Head Engine** before execution.",
            "color": "6" # Purple
        },
        {
            "id": "node-token-compressor",
            "type": "text",
            "x": -870,
            "y": -110,
            "width": 460,
            "height": 190,
            "text": "### ⚡ Token & Credit Optimizer (Prompt Master Pack)\n- Strips conversational bloat while preserving 100% intent.\n- **Universal 8-Part Template**:\n  - **Role** & **Objective**\n  - **Context** & **Task**\n  - **Inputs** & **Constraints**\n  - **Method** & **Output Format**",
            "color": "4" # Green
        },
        {
            "id": "node-evidence-sep",
            "type": "text",
            "x": -870,
            "y": 120,
            "width": 460,
            "height": 180,
            "text": "### 🔍 Evidence Separation Protocol\n- **FACT**: Verified data from Scopus/WoS/files.\n- **INFERENCE**: Logical deductions derived from evidence.\n- **ASSUMPTION**: Explicitly labeled defaults.\n- **UNKNOWN**: Explicitly marked \"DATA TIDAK TERSEDIA\".",
            "color": "1" # Red/Amber
        },

        # GROUP 2: ROUTER & 32 SUPER-SKILLS
        {
            "id": "group-router",
            "type": "group",
            "x": -300,
            "y": -480,
            "width": 640,
            "height": 960,
            "label": "🧭 PHASE 1: MASTER SKILL ROUTER (32 SUPER-SKILLS DISPATCH)",
            "color": "5" # Cyan
        },
        {
            "id": "node-router-hub",
            "type": "text",
            "x": -270,
            "y": -420,
            "width": 580,
            "height": 110,
            "text": "### 🔀 Automated Intent Classification & Dispatcher\nDynamically routes tasks into the optimal combination of specialized sub-engines without manual prompt configuration.",
            "color": "5"
        },
        {
            "id": "node-cat-acad",
            "type": "text",
            "x": -270,
            "y": -280,
            "width": 580,
            "height": 160,
            "text": "### 🎓 1. Core Academic & Research (S1–S6, S20, S22)\n- `omni-auto` v4.0 · `publication-shield` · `mendeley-ris-linker`\n- `master-journal-tracking` · `markitdown-academic-parser`\n- `ai-research-deep-engine` · `autonomous-research-rubrics`",
            "color": "2" # Orange
        },
        {
            "id": "node-cat-eng",
            "type": "text",
            "x": -270,
            "y": -90,
            "width": 580,
            "height": 170,
            "text": "### ⚙️ 2. Engineering, Architecture & DeepSeek (S7–S14, S21, S25, S27, S28)\n- `agentic-engineering-suite` · `master-senior-software-engineer`\n- `deepseek-harness-optimizer` (Everything is a Plugin)\n- `langgraph-orchestrator` · `system-architecture-foundations`\n- `continuous-ai-workflow-orchestrator`",
            "color": "5" # Cyan
        },
        {
            "id": "node-cat-recsys",
            "type": "text",
            "x": -270,
            "y": 110,
            "width": 580,
            "height": 150,
            "text": "### 🤖 3. RecSys, AutoML & Deep Reasoning (S15–S17, S23, S24, S26)\n- `recommendation-systems-engine` · `job-career-recommender`\n- `cognitive-deep-thinking-strategies` · `automl-pipeline-optimizer`\n- `reasoning-multimodal-recsys` · `trends-mcp-intelligence`",
            "color": "3" # Yellow
        },
        {
            "id": "node-cat-pabrik",
            "type": "text",
            "x": -270,
            "y": 290,
            "width": 580,
            "height": 160,
            "text": "### 🏭 4. Pabrik AI Fused High-Conversion Suite (S29–S32)\n- `pabrik-ai-access-hub` (22 Cloned AI Tools & Direct Launch)\n- `hyper-copywriting-seo-suite` (Copymatic + FK-17 Humanizer)\n- `hyper-visual-pptx-orchestrator` (PPT from Text/Word + MomentsAI)\n- `enterprise-business-financial-analyzer` (Modal & Profit + Property)",
            "color": "4" # Green
        },

        # GROUP 3: VERIFICATION & PUBLICATION SHIELD
        {
            "id": "group-forensics",
            "type": "group",
            "x": 420,
            "y": -350,
            "width": 500,
            "height": 720,
            "label": "🛡️ PHASE 2-4: FORENSIC VERIFICATION & PUBLICATION SHIELD",
            "color": "1" # Red
        },
        {
            "id": "node-chain",
            "type": "text",
            "x": 450,
            "y": -280,
            "width": 440,
            "height": 140,
            "text": "### 🔗 Source-to-Claim Evidence Chain\n$$\\text{Claim} \\to \\text{Evidence} \\to \\text{Source} \\to \\text{Source Quality} \\to \\text{Limitation}$$\n- Zero fabricated statistics or imaginary claims.",
            "color": "2"
        },
        {
            "id": "node-triple-shield",
            "type": "text",
            "x": 450,
            "y": -110,
            "width": 440,
            "height": 220,
            "text": "### 🛡️ Triple Publication Shield Verification\n- **FK-16**: 4-Layer Plagiarism & Similarity Audit (Target $\\le 5\\%$).\n- **FK-17**: 29 AI Pattern Scanner with Natural Humanization.\n- **FK-19**: Strict Mendeley/Scopus Citation Authenticity Validator.",
            "color": "1"
        },
        {
            "id": "node-anti-bias",
            "type": "text",
            "x": 450,
            "y": 140,
            "width": 440,
            "height": 160,
            "text": "### ⚖️ Anti-Bias & Reproducibility Audit\n- Validates mathematical proofs and statistical formulas.\n- Cross-checks code against test suites and edge cases.",
            "color": "6"
        },

        # GROUP 4: 100% GUARANTEED OUTPUTS
        {
            "id": "group-outputs",
            "type": "group",
            "x": 1000,
            "y": -350,
            "width": 480,
            "height": 720,
            "label": "📦 PHASE 5: 100% RELIABLE WORKING DELIVERABLES",
            "color": "4" # Green
        },
        {
            "id": "node-docx",
            "type": "text",
            "x": 1030,
            "y": -280,
            "width": 420,
            "height": 130,
            "text": "### 📄 Dual-Language Academic Naskah (.docx)\n- `Naskah — Bahasa Indonesia.docx`\n- `Naskah — English Version.docx`\n- Synchronized `[N#E]` claims across both versions.",
            "color": "4"
        },
        {
            "id": "node-pptx",
            "type": "text",
            "x": 1030,
            "y": -120,
            "width": 420,
            "height": 120,
            "text": "### 📊 Formatted Slide Deck (.pptx)\n- `Presentasi — Proposal / Sidang.pptx`\n- High-impact visual slides with presenter notes.",
            "color": "3"
        },
        {
            "id": "node-ris",
            "type": "text",
            "x": 1030,
            "y": 30,
            "width": 420,
            "height": 120,
            "text": "### 📚 Synchronized Mendeley RIS (.ris)\n- `Daftar Pustaka — Mendeley.ris`\n- 1-Click Mendeley/Zotero import with matching `ID - N`.",
            "color": "5"
        },
        {
            "id": "node-code-biz",
            "type": "text",
            "x": 1030,
            "y": 180,
            "width": 420,
            "height": 120,
            "text": "### 💻 Working Code & Financial Models\n- Zero-regression executable software suites.\n- Financial models with BEP, COGS, and Cap Rate ROI.",
            "color": "6"
        }
    ],
    "edges": [
        # Head to Compressor
        {"id": "e1", "fromNode": "node-raw-input", "fromSide": "bottom", "toNode": "node-token-compressor", "toSide": "top"},
        {"id": "e2", "fromNode": "node-token-compressor", "fromSide": "bottom", "toNode": "node-evidence-sep", "toSide": "top"},
        
        # Compressor to Router
        {"id": "e3", "fromNode": "node-token-compressor", "fromSide": "right", "toNode": "node-router-hub", "toSide": "left", "label": "Optimized Prompt"},
        
        # Router Hub to Categories
        {"id": "e4", "fromNode": "node-router-hub", "fromSide": "bottom", "toNode": "node-cat-acad", "toSide": "top"},
        {"id": "e5", "fromNode": "node-cat-acad", "fromSide": "bottom", "toNode": "node-cat-eng", "toSide": "top"},
        {"id": "e6", "fromNode": "node-cat-eng", "fromSide": "bottom", "toNode": "node-cat-recsys", "toSide": "top"},
        {"id": "e7", "fromNode": "node-cat-recsys", "fromSide": "bottom", "toNode": "node-cat-pabrik", "toSide": "top"},

        # Categories to Forensics
        {"id": "e8", "fromNode": "node-cat-acad", "fromSide": "right", "toNode": "node-chain", "toSide": "left", "label": "Draft Synthesis"},
        {"id": "e9", "fromNode": "node-chain", "fromSide": "bottom", "toNode": "node-triple-shield", "toSide": "top"},
        {"id": "e10", "fromNode": "node-triple-shield", "fromSide": "bottom", "toNode": "node-anti-bias", "toSide": "top"},

        # Forensics to Deliverables
        {"id": "e11", "fromNode": "node-triple-shield", "fromSide": "right", "toNode": "node-docx", "toSide": "left", "label": "Verified Publication"},
        {"id": "e12", "fromNode": "node-docx", "fromSide": "bottom", "toNode": "node-pptx", "toSide": "top"},
        {"id": "e13", "fromNode": "node-pptx", "fromSide": "bottom", "toNode": "node-ris", "toSide": "top"},
        {"id": "e14", "fromNode": "node-ris", "fromSide": "bottom", "toNode": "node-code-biz", "toSide": "top"}
    ]
}

with open(CANVAS_PATH, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, indent=2)

print(f"Obsidian Canvas successfully generated at: {CANVAS_PATH}")

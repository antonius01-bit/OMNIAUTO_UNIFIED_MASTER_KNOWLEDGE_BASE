import os
import shutil

BASE_DIR = r"C:\Users\antoni\Dola"
VAULT_DIR = os.path.join(BASE_DIR, "obsidian_vault")

folders = [
    "00_MASTER",
    "01_PROMPT_ENGINEERING",
    "02_ACADEMIC",
    "03_RESEARCH",
    "04_DATA",
    "05_OPERATIONS",
    "06_FINANCE",
    "07_HR",
    "08_PRESENTATION",
    "09_AI_WORKFLOW",
    "10_OBSIDIAN",
    "11_TEMPLATES",
    "12_ARCHIVE"
]

for f in folders:
    os.makedirs(os.path.join(VAULT_DIR, f), exist_ok=True)

# Master Index Note
master_index = """---
title: Dola AI & Prompt Master Knowledge Hub
type: master_index
status: active
created: 2026-09-03
updated: 2026-09-03
tags:
  - master
  - dola-ai
  - prompt-engineering
  - omni-auto
---

# 🧠 Dola AI & Prompt Master Knowledge Hub

Welcome to your central Obsidian AI knowledge base.

## 🚀 Head Engine & Core Modules
- [[PROMPT_MASTER]]: Universal Cross-Platform Prompt Optimizer & Token Compressor.
- [[OMNI_AUTO_ROUTER]]: Head Meta-Router & 32 Super-Skills Dispatcher.
- [[ACADEMIC_MASTER]]: Graduate-Level Academic Writing & Evidence Forensics.
- [[THESIS_ENGINE]]: 5-Chapter Thesis Construction & Methodological Validation.
- [[PABRIK_AI_CATALOG]]: 22 Cloned Tools from DigitalProfitsNusantara.
- [[DEEPSEEK_HARNESS]]: DeepSeek R1/V3 Agent Runtime & Plugin Sandbox.

## 📁 Vault Structure
- **00_MASTER**: Master indexes and configuration rules.
- **01_PROMPT_ENGINEERING**: Universal templates and token optimizers.
- **02_ACADEMIC**: Academic drafting, Turnitin shield, Scopus journal trackers.
- **03_RESEARCH**: Literature search, research gap analysis, citation chains.
- **04_DATA**: Quantitative, qualitative, and mixed-methods engines.
- **05_OPERATIONS**: Operations management, RCA, and SOP builders.
- **06_FINANCE**: Breakdown modal & profit, financial models, property valuation.
- **07_HR**: Workforce analytics and recruitment matrices.
- **08_PRESENTATION**: PPTX deck generation, infographics, MomentsAI.
- **09_AI_WORKFLOW**: Multi-agent architectures, DeepSeek harness, n8n.
- **10_OBSIDIAN**: Obsidian system instructions and link maps.
- **11_TEMPLATES**: Standard note templates.
"""

with open(os.path.join(VAULT_DIR, "00_MASTER", "00_INDEX.md"), "w", encoding="utf-8") as f:
    f.write(master_index)

with open(os.path.join(VAULT_DIR, "00_MASTER", "PROMPT_MASTER.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Prompt Master Universal Framework
type: core_engine
status: active
tags:
  - prompt-master
  - token-optimization
---

# 👑 Prompt Master Universal Framework

## Template Structure
- **ROLE**: Expert system persona.
- **OBJECTIVE**: Specific intended outcome.
- **CONTEXT**: Background & environment.
- **TASK**: Actionable work definition.
- **INPUTS**: Files, datasets, variables, links.
- **CONSTRAINTS**: Word count, tone, language, format.
- **METHOD**: Step-by-step reasoning chain.
- **OUTPUT**: Exact deliverable structure.
- **QUALITY CONTROL**: Anti-hallucination, factual evidence chain.

Related: [[OMNI_AUTO_ROUTER]] | [[ACADEMIC_MASTER]]
""")

with open(os.path.join(VAULT_DIR, "02_ACADEMIC", "ACADEMIC_MASTER.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Academic Master & Publication Shield
type: academic_module
status: active
tags:
  - academic
  - thesis
  - scopus
  - mendeley
---

# 🎓 Academic Master & Publication Shield

## Standards
- Graduate level S2/Master tone (PUEBI / Formal English).
- **FK-16**: Plagiarism/similarity risk ≤ 5%.
- **FK-17**: 29 AI cliché removal with natural humanization.
- **FK-19**: Strict Mendeley RIS citation verification `[N#E]`.

Related: [[00_INDEX]] | [[THESIS_ENGINE]]
""")

with open(os.path.join(VAULT_DIR, "09_AI_WORKFLOW", "PABRIK_AI_CATALOG.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Pabrik AI Catalog & Direct Launcher
type: tool_catalog
status: active
tags:
  - pabrik-ai
  - gemini-studio
---

# 🏭 Pabrik AI (DigitalProfitsNusantara) 22 Tools

- **Passphrase**: `berjanji demi tuhan`
- **Admin Support**: `+6289512598090`

## Categories
1. **Copywriting & SEO**: Copymatic, Scriptwriter, SEO Optimizer, Konten Pro.
2. **Akademik & Edukasi**: AI Turnitin, Jurnal Refleksi, Scopus Kuliah, Materi Belajar, Asisten Tugas.
3. **Visual & PPT**: Pembuat PPT, PPT Word/txt, Presentation & Infographic, Studio Banner, Product Image, MomentsAI.
4. **Bisnis & Analisis**: Breakdown Modal & Profit, File Analyzer, Model Studio, Studio Pro, Property, ChatDigiPro.

Related: [[00_INDEX]] | [[PROMPT_MASTER]]
""")

# Copy Prompt Master and Pabrik AI Database into vault
shutil.copy2(os.path.join(BASE_DIR, "Prompt_Master_AI_Skills_Pack.md"), os.path.join(VAULT_DIR, "01_PROMPT_ENGINEERING", "Prompt_Master_AI_Skills_Pack.md"))
shutil.copy2(os.path.join(BASE_DIR, "PABRIK_AI_DATABASE.md"), os.path.join(VAULT_DIR, "09_AI_WORKFLOW", "PABRIK_AI_DATABASE.md"))

print(f"Obsidian Vault successfully populated at: {VAULT_DIR}")

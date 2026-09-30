import json
import os
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

VAULT_DIR = r"C:\Users\antoni\Dola\obsidian_vault"

def create_note_if_missing(folder, filename, title, tags, content):
    folder_path = os.path.join(VAULT_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        tag_str = ", ".join(tags)
        full_content = f"""---
title: "{title}"
created: 2026-09-28
tags: [{tag_str}]
type: concept
---

# {title}

{content}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"[+] Created note: {folder}/{filename}")

# 1. Ensure complementary notes in folders 14 to 20
create_note_if_missing(
    "14_AUTONOMOUS_LOOPS", "FIVE_MANDATORY_LOOP_EXITS.md",
    "Five Mandatory Loop Exit Criteria & Git Worktree Isolation",
    ["dola", "agy", "loop-engineering", "exit-criteria", "git-worktree"],
    """## 🎯 5 Gerbang Keluar Mandatori Loop
1. **Success Exit**: Semua pengujian deterministik lulus 100% dan verifikasi linter 0 error.
2. **Failure Exit**: Terdeteksi kesalahan fatal yang tidak dapat dipulihkan (*unrecoverable*).
3. **Budget Exit**: Mencapai batas maksimum putaran (*max_turns*) atau token budget.
4. **No-Progress Break**: Terdeteksi perulangan buntu jika hash state/kode identik dalam 2 turn berturut-turut.
5. **Human Escalation Gate**: Permintaan keputusan kritis kepada pengguna sebelum aksi irreversible.

## 🛡️ Git Worktree Sandboxing
- Agen selalu beroperasi di dalam branch `git worktree` sementara.
- Branch utama (`main`) tidak akan terpolusi oleh iterasi agen yang belum terverifikasi."""
)

create_note_if_missing(
    "15_HARVESTED_PROFILES", "CONTINUOUS_PROFILE_WATCHER_SPEC.md",
    "Continuous GitHub Profile Watcher Architecture",
    ["dola", "agy", "github-watcher", "profile-tracking", "re-learner"],
    """## 🛰️ Arsitektur Pemantau 173 Profil GitHub
- **Pola URL Target**: `https://github.com/{username}?tab=repositories`
- **Audit Git Remote**: Menggunakan `git ls-remote origin HEAD` non-destruktif untuk membandingkan commit remote dengan lokal.
- **Deteksi Repositori Baru**: Memindai rilis repositori publik terbaru dari 173 akun/organisasi terpantau.
- **Ekstraksi Otomatis**: Membedah markdown, skrip, dan file prompt untuk diserap ke dalam **Prompt Master**."""
)

create_note_if_missing(
    "16_META_LEARNING", "FOUR_HONESTY_TESTS_FRAMEWORK.md",
    "Four Honesty Tests Framework for Autonomous Agents",
    ["dola", "agy", "meta-learning", "honesty-tests", "anti-slop"],
    """## ⚖️ 4 Uji Kejujuran Sistem Agen
1. **Verification Honesty**: Apakah status 'selesai' diverifikasi oleh runner deterministik atau hanya penilaian sendiri? (Wajib independen).
2. **Maker != Checker**: Pembuat kode tidak boleh menjadi penguji kode miliknya sendiri.
3. **Anti-Slop Cleanliness**: Bebas dari 29 pola klise AI (FK-17) dan over-engineering.
4. **Permanent Persistence**: Semua perubahan disimpan secara permanen di NVMe lokal dan Obsidian vault."""
)

create_note_if_missing(
    "17_BROWSER_RPA", "AUTOMA_JSON_SCHEMA_WORKFLOWS.md",
    "Automa JSON Schema & Block-Based Workflows",
    ["dola", "agy", "automa", "browser-rpa", "json-schema"],
    """## 🌐 Arsitektur Alur Kerja Automa JSON
- **Blok Pemicu (*Trigger*)**: Manual, event URL, jadwal waktu, atau webhook.
- **Blok Interaksi DOM**: Click element, type text, scroll element, hover, select dropdown.
- **Blok Logika & Looping**: Repeat elements, conditions, wait for selector, javascript execution.
- **Blok Ekstraksi & Ekspor**: Get text/attribute, tables to dataset, export ke CSV/JSON."""
)

create_note_if_missing(
    "18_MODEL_CURRICULUM", "TWENTY_PHASE_ROADMAP_DETAILS.md",
    "Twenty Phase Roadmap Details: AI Engineering from Scratch",
    ["dola", "agy", "ai-engineering", "curriculum", "roadmap"],
    """## 🗺️ Rincian 20 Fase Rekayasa AI
- **Fase 1–3**: Python internals, OOP, Async, NumPy tensors, Micrograd autograd engine.
- **Fase 4–6**: PyTorch deep dive, backprop math, MLP, optimizers (AdamW, SGD).
- **Fase 7–9**: Tokenizers BPE, embeddings, self-attention, Multi-Head Attention, FlashAttention-2.
- **Fase 10–12**: Transformer architecture, RoPE / ALiBi positional encoding, scaling laws.
- **Fase 13–15**: Pretraining, mixed precision (FP16/BF16), DDP/FSDP, dataset curation.
- **Fase 16–18**: RLHF, DPO, PPO, Quantization (GGUF, AWQ, TurboQuant), vLLM / Ollama serving.
- **Fase 19–20**: Advanced RAG (CRAG, Graph RAG), agent tool use, LLM-as-a-Judge evals."""
)

create_note_if_missing(
    "19_TOOL_ECOSYSTEM", "MCP_ENTERPRISE_TOOL_GATEWAY.md",
    "Model Context Protocol & Enterprise Gateway Architecture",
    ["dola", "agy", "mcp", "tools", "gateway", "substrates"],
    """## 🛠️ Gerbang MCP & Substrat Sistem
- **Server MCP Aktif**:
  - `context7`: Dokumentasi langsung & anti-halusinasi Upstash.
  - `gemini-api-docs`: Dokumentasi resmi upstream Google Gemini API & SDK.
  - `obsidian` / `seekstone-obsidian`: Jembatan bi-directional vault lokal pada port 27124.
  - `memory`: Graf relasi entitas-pengetahuan persisten.
- **Substrat Lokal**:
  - Desktop Bridge HTTP server port 5050 (`agy_bridge_server.py`).
  - Stark OS HUD supervisor & status task telemetry."""
)

create_note_if_missing(
    "20_MULTI_AGENT_BRAIN", "SIX_PILLAR_AGENT_ALLIANCE.md",
    "Six-Pillar AI Agent Alliance & Orchestration Model",
    ["dola", "agy", "bionic", "gemini", "copilot", "obsidian", "alliance"],
    """## 🏛️ Aliansi 6 Pilar Kecerdasan Buatan
1. **👁️ Bionic**: Mesin persepsi web bebas biaya API (Twitter, Reddit, YouTube, GitHub).
2. **🌟 Gemini**: Penalaran multimodal mendalam, riset web, dan dekomposisi tingkat lanjut.
3. **⚡ AGY (Antigravity)**: Eksekusi kode bedah, pengujian deterministik, dan otomasi OS.
4. **🤖 Dola AI**: Head meta-router, orkestrator workflow, dan audit SOP multi-pass.
5. **💻 Copilot**: Asisten inline IDE dan percepatan penulisan kode harian.
6. **🧠 Obsidian**: Memori jangka panjang permanen, graf semantik, dan Zettelkasten Small Brain."""
)

# Folder meta definitions
NODE_METAS = {
    "14_AUTONOMOUS_LOOPS": {
        "icon": "🔄",
        "title": "14_AUTONOMOUS_LOOPS: Loop Engineering, Harness OS & Worktree Isolation",
        "desc": "Autonomous agent execution loops, deterministic verifiers (Maker != Checker), 5 exit gates & disposable git worktrees.",
        "color": "1" # Red/Amber
    },
    "15_HARVESTED_PROFILES": {
        "icon": "🛰️",
        "title": "15_HARVESTED_PROFILES: 173+ GitHub Authors & Orgs Watcher Registry",
        "desc": "Continuous monitoring of https://github.com/{username}?tab=repositories, remote commit audits, and auto-cloning.",
        "color": "5" # Blue/Cyan
    },
    "16_META_LEARNING": {
        "icon": "🧬",
        "title": "16_META_LEARNING: Self-Development, Recursive Loops & Skill Optimization",
        "desc": "Autonomous self-reflection, 4 honesty tests, anti-slop enforcement, runlog auditing, and permanent memory lock.",
        "color": "6" # Purple
    },
    "17_BROWSER_RPA": {
        "icon": "🌐",
        "title": "17_BROWSER_RPA: Automa Block Workflows & Zero-Cost Web Automation",
        "desc": "Visual & JSON browser automation (.automa.json), headless web scrapers, DOM manipulation, and dataset exports.",
        "color": "4" # Green
    },
    "18_MODEL_CURRICULUM": {
        "icon": "🧠",
        "title": "18_MODEL_CURRICULUM: AI Engineering from Scratch (523 Lessons, 20 Phases)",
        "desc": "Comprehensive technical mastery from Python internals to BPE tokenizers, FlashAttention-2, SFT/DPO, and RAG evaluation.",
        "color": "3" # Yellow/Gold
    },
    "19_TOOL_ECOSYSTEM": {
        "icon": "🛠️",
        "title": "19_TOOL_ECOSYSTEM: MCP Enterprise Gateway & OS Desktop Substrates",
        "desc": "Model Context Protocol servers (Context7, Gemini Docs, Obsidian REST API), Desktop Bridge 5050 & Stark OS HUD.",
        "color": "2" # Orange
    },
    "20_MULTI_AGENT_BRAIN": {
        "icon": "👑",
        "title": "20_MULTI_AGENT_BRAIN: 6-Pillar Alliance (Bionic + Gemini + AGY + Dola + Copilot + Obsidian)",
        "desc": "Unified apex multi-agent orchestration, 5-step knowledge compilation loop, and long-term persistent memory graph.",
        "color": "4" # Emerald
    }
}

# 2. Build folder-specific workflow canvases
for folder_name, meta in NODE_METAS.items():
    folder_path = os.path.join(VAULT_DIR, folder_name)
    canvas_path = os.path.join(folder_path, f"{folder_name}_workflow.canvas")
    
    # Get all markdown files in folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    md_files.sort()
    
    nodes = []
    edges = []
    
    # Hub Node
    hub_id = f"hub-{folder_name}"
    nodes.append({
        "id": hub_id,
        "type": "text",
        "x": 0,
        "y": 0,
        "width": 560,
        "height": 170,
        "text": f"### {meta['icon']} {meta['title']}\n{meta['desc']}\n\nInteractive navigation canvas connecting **{len(md_files)} Knowledge Nodes** in this domain.\n*Powered by Antigravity, Gemini 2.5 & Dola AI.*",
        "color": meta["color"]
    })
    
    # Distribute notes Left and Right
    left_notes = [f for i, f in enumerate(md_files) if i % 2 == 0]
    right_notes = [f for i, f in enumerate(md_files) if i % 2 != 0]
    
    y_spacing = 160
    
    # Left Nodes
    start_y_left = -((len(left_notes) - 1) * y_spacing) / 2.0
    for idx, f in enumerate(left_notes):
        note_id = f"node-{folder_name}-L{idx}"
        base_name = f[:-3]
        nodes.append({
            "id": note_id,
            "type": "text",
            "x": -680,
            "y": start_y_left + (idx * y_spacing),
            "width": 480,
            "height": 130,
            "text": f"### [[{f}]]\n**{base_name}**\nFile: `{folder_name}/{f}`",
            "color": "5" if idx % 2 == 0 else "2"
        })
        edges.append({
            "id": f"edge-L{idx}",
            "fromNode": hub_id,
            "fromSide": "left",
            "toNode": note_id,
            "toSide": "right"
        })
        
    # Right Nodes
    start_y_right = -((len(right_notes) - 1) * y_spacing) / 2.0
    for idx, f in enumerate(right_notes):
        note_id = f"node-{folder_name}-R{idx}"
        base_name = f[:-3]
        nodes.append({
            "id": note_id,
            "type": "text",
            "x": 780,
            "y": start_y_right + (idx * y_spacing),
            "width": 480,
            "height": 130,
            "text": f"### [[{f}]]\n**{base_name}**\nFile: `{folder_name}/{f}`",
            "color": "3" if idx % 2 == 0 else "6"
        })
        edges.append({
            "id": f"edge-R{idx}",
            "fromNode": hub_id,
            "fromSide": "right",
            "toNode": note_id,
            "toSide": "left"
        })
        
    canvas_json = {
        "nodes": nodes,
        "edges": edges
    }
    
    with open(canvas_path, "w", encoding="utf-8") as fp:
        json.dump(canvas_json, fp, indent=2, ensure_ascii=False)
    print(f"[✓] Created workflow canvas: {folder_name}/{folder_name}_workflow.canvas ({len(nodes)} nodes, {len(edges)} edges)")


# 3. Build the Grand Master Canvas in 00-Canvas
master_canvas_path = os.path.join(VAULT_DIR, "00-Canvas", "Obsidian_Small_Brain_Nodes_14_to_20.canvas")

master_nodes = []
master_edges = []

# Central Apex Node
master_apex_id = "node-apex-small-brain"
master_nodes.append({
    "id": master_apex_id,
    "type": "text",
    "x": 0,
    "y": -50,
    "width": 640,
    "height": 220,
    "text": "## 🧠 OBSIDIAN SMALL BRAIN APEX: NODES 14–20 ORCHESTRATION\n**Permanent Default Autonomous Learning & Execution Architecture (S243–S251)**\n- **Outer Loop**: 173+ GitHub Authors Watcher (`https://github.com/{username}?tab=repositories`)\n- **Inner Loop**: Autonomous Loop Harness, Maker != Checker, Prompt Master Ingestion\n- **Substrates**: Automa Web RPA, AI Engineering Curriculum, MCP Gateway\n- **Alliance**: Bionic + Gemini + AGY + Dola + Copilot + Obsidian\n*Powered by Antigravity OS & Dola AI v4.0*",
    "color": "4"
})

# Layout coordinates for the 7 satellite groups surrounding the apex
group_coords = [
    # (id, x, y, width, height, title, color)
    ("group-node-14", -1200, -600, 520, 480, "🔄 NODE 14: AUTONOMOUS LOOPS", "1"),
    ("group-node-15", -1200, 0, 520, 480, "🛰️ NODE 15: HARVESTED PROFILES (173 AUTHORS)", "5"),
    ("group-node-16", -1200, 600, 520, 480, "🧬 NODE 16: META LEARNING & RECURSIVE IMPROVEMENT", "6"),
    ("group-node-17", 800, -600, 520, 480, "🌐 NODE 17: BROWSER RPA & AUTOMA ENGINE", "4"),
    ("group-node-18", 800, 0, 520, 480, "🧠 NODE 18: MODEL CURRICULUM (523 LESSONS)", "3"),
    ("group-node-19", 800, 600, 520, 480, "🛠️ NODE 19: TOOL ECOSYSTEM & MCP GATEWAY", "2"),
    ("group-node-20", -260, 450, 640, 420, "👑 NODE 20: MULTI-AGENT BRAIN ALLIANCE", "4")
]

for gid, gx, gy, gw, gh, glabel, gcolor in group_coords:
    master_nodes.append({
        "id": gid,
        "type": "group",
        "x": gx,
        "y": gy,
        "width": gw,
        "height": gh,
        "label": glabel,
        "color": gcolor
    })

# Add detail cards inside each group
# Node 14 Card
master_nodes.append({
    "id": "card-14",
    "type": "text",
    "x": -1170,
    "y": -540,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_AUTONOMOUS_LOOPS]]\n- **Skill**: `S243` Loop Engineering Suite\n- **Files**: [[LOOP_ENGINEERING_MASTER_HARNESS]], [[FIVE_MANDATORY_LOOP_EXITS]]\n- **6 Loop Elements**: Trigger, Work Engine, Verifier, State, 5 Exits, Human Gate\n- **Discipline**: Maker != Checker, read-only test suites, git worktree sandboxing.",
    "color": "1"
})

# Node 15 Card
master_nodes.append({
    "id": "card-15",
    "type": "text",
    "x": -1170,
    "y": 60,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_HARVESTED_PROFILES]]\n- **Skill**: `S251` GitHub Profile Watcher Engine\n- **Registry**: [[GITHUB_USER_WATCHER_REGISTRY]]\n- **Spec**: [[CONTINUOUS_PROFILE_WATCHER_SPEC]]\n- **Target**: `https://github.com/{username}?tab=repositories`\n- **Scale**: 173 unique authors, 213 local NVMe repositories\n- **Audit**: Non-destructive `git ls-remote origin HEAD` checks.",
    "color": "5"
})

# Node 16 Card
master_nodes.append({
    "id": "card-16",
    "type": "text",
    "x": -1170,
    "y": 660,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_META_LEARNING]]\n- **Standards**: [[SELF_DEVELOPMENT_RECURSIVE_LOOP]]\n- **Audit Rules**: [[FOUR_HONESTY_TESTS_FRAMEWORK]]\n- **Runlog**: [[SELF_IMPROVEMENT_RUNLOG]]\n- **Mechanism**: Adversarial reflection, prompt master fusion, permanent Obsidian locking\n- **Principle**: Continuous self-development in every turn.",
    "color": "6"
})

# Node 17 Card
master_nodes.append({
    "id": "card-17",
    "type": "text",
    "x": 830,
    "y": -540,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_BROWSER_RPA]]\n- **Skill**: `S244` Automa Browser RPA Engine\n- **Blueprints**: [[AUTOMA_BROWSER_AUTOMATION_BLUEPRINT]], [[AUTOMA_JSON_SCHEMA_WORKFLOWS]]\n- **Capabilites**: Block workflows, multi-tab automation, DOM scraping, form-filling, CSV/JSON exports\n- **Advantage**: Zero cloud API fees using local Chromium extension.",
    "color": "4"
})

# Node 18 Card
master_nodes.append({
    "id": "card-18",
    "type": "text",
    "x": 830,
    "y": 60,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_MODEL_CURRICULUM]]\n- **Skill**: `S245` AI Engineering from Scratch\n- **Curriculum**: [[AI_ENGINEERING_FROM_SCRATCH_CURRICULUM]], [[TWENTY_PHASE_ROADMAP_DETAILS]]\n- **Scope**: 523 structured lessons across 20 phases\n- **Topics**: Micrograd, PyTorch, BPE, FlashAttention-2, SFT, DPO, Quantization (GGUF/AWQ), RAG.",
    "color": "3"
})

# Node 19 Card
master_nodes.append({
    "id": "card-19",
    "type": "text",
    "x": 830,
    "y": 660,
    "width": 460,
    "height": 380,
    "text": "### [[00_INDEX_TOOL_ECOSYSTEM]]\n- **Architecture**: [[MCP_ENTERPRISE_TOOL_GATEWAY]]\n- **MCP Integrations**: Context7, Gemini API Docs, Obsidian REST API (port 27124), Memory graph\n- **Desktop Substrates**: Stark OS HUD supervisor, Desktop Bridge port 5050, Acrylic taskbar styling.",
    "color": "2"
})

# Node 20 Card
master_nodes.append({
    "id": "card-20",
    "type": "text",
    "x": -230,
    "y": 510,
    "width": 580,
    "height": 320,
    "text": "### [[00_INDEX_MULTI_AGENT_BRAIN]]\n- **Alliance**: [[SIX_PILLAR_AGENT_ALLIANCE]]\n- **6 AI Pillars**: Bionic (Perception) + Gemini (Deep Reasoning) + AGY (Surgical Code) + Dola (Head Router) + Copilot (IDE Pairing) + Obsidian (Persistent Brain)\n- **L0 Compounding Loop**: Ingest -> Store (.md) -> Link [[...]] -> Query Dataview -> Graph Emergence.",
    "color": "4"
})

# Master Edges
edge_configs = [
    ("edge-m15-apex", "card-15", "right", master_apex_id, "left", "Git Commits & New Repos Stream"),
    ("edge-m14-apex", "card-14", "right", master_apex_id, "left", "Loop Verifier & Exit Guards"),
    ("edge-m16-apex", "card-16", "right", master_apex_id, "left", "Self-Improvement Reflexion"),
    ("edge-apex-m17", master_apex_id, "right", "card-17", "left", "Browser RPA Execution"),
    ("edge-apex-m18", master_apex_id, "right", "card-18", "left", "Model Curriculum & Evals"),
    ("edge-apex-m19", master_apex_id, "right", "card-19", "left", "MCP & Local Substrates"),
    ("edge-apex-m20", master_apex_id, "bottom", "card-20", "top", "6-Pillar Alliance Graph Persistence")
]

for eid, fn, fs, tn, ts, lbl in edge_configs:
    master_edges.append({
        "id": eid,
        "fromNode": fn,
        "fromSide": fs,
        "toNode": tn,
        "toSide": ts,
        "label": lbl
    })

master_canvas_json = {
    "nodes": master_nodes,
    "edges": master_edges
}

with open(master_canvas_path, "w", encoding="utf-8") as fp:
    json.dump(master_canvas_json, fp, indent=2, ensure_ascii=False)
print(f"[✓] Created master panoramic canvas: 00-Canvas/Obsidian_Small_Brain_Nodes_14_to_20.canvas ({len(master_nodes)} nodes, {len(master_edges)} edges)")
print("[🎉] All Small Brain Canvases successfully generated!")

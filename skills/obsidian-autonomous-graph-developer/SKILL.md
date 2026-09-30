---
name: obsidian-autonomous-graph-developer
description: Autonomous Second Brain graph densification, orphan note healing, MOC auto-sync, dynamic Dataview queries, and vault health auditing engine for Obsidian based on Dola AI and Antigravity.
---

# 🧠 S135 — Obsidian Autonomous Graph Developer (`obsidian-autonomous-graph-developer`)

## 📌 Overview & Architecture
- **Origin & Core Purpose**: Converts Obsidian from a passive note store into an active, self-healing, self-organizing Second Brain. Automatically detects orphan notes, weaves bidirectional `[[Wikilinks]]`, synchronizes category Maps of Content (MOCs) and `00_INDEX.md`, standardizes YAML frontmatter, and logs evolution metrics into `13_SELF_IMPROVEMENT/`.
- **Primary Tool**: `C:/Users/antoni/Dola/scripts/obsidian_self_developer.py`
- **Vault Root**: `C:/Users/antoni/Dola/obsidian_vault`
- **Execution Cadence**: On-demand via `/omni-auto obsidian-evolve` or nightly automated cron (`0 3 * * *`).

---

## 🏛️ Autonomous Vault Maintenance Topology

```
                         ┌─────────────────────────────┐
                         │   obsidian_self_developer   │
                         │      Autonomous Engine      │
                         └──────────────┬──────────────┘
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│  Graph Analysis  │          │  Orphan Healing  │          │ Master Sync & Log│
├──────────────────┤          ├──────────────────┤          ├──────────────────┤
│ • AST Regex Scan │          │ • MOC Weaving    │          │ • 00_INDEX.md    │
│ • In/Out Edges   │          │ • Context Links  │          │ • Health Log     │
│ • Topology State │          │ • Bidirectional  │          │ • Dataview Query │
└──────────────────┘          └──────────────────┘          └──────────────────┘
```

---

## 🛠️ The 5 Core Autonomic Operations

1. **Topology Discovery**:
   - Recursively traverses all 14 taxonomy directories (`00_MASTER` to `13_SELF_IMPROVEMENT`), parsing file contents for `[[wikilink]]` syntax.
2. **Strict Orphan Remediation**:
   - Identifies notes with zero incoming and zero outgoing links.
   - Automatically injects parent category breadcrumbs (`[[Category_MOC]]`) and master index link (`[[00_INDEX]]`).
3. **Master Index Auto-Sync**:
   - Updates `00_INDEX.md` header counts to reflect exact live Super-Skills and granular sub-skills totals.
4. **YAML Frontmatter Governance**:
   - Guarantees `title`, `created`, `tags`, and `type` fields exist and adhere to Obsidian Dola AI rules.
5. **Evolution Metrics Logging**:
   - Generates and appends audit logs to `13_SELF_IMPROVEMENT/VAULT_AUTONOMOUS_HEALTH_LOG.md`.

---

## 💻 CLI Operations & Triggers

### 1. On-Demand Vault Evolution
```bash
python C:/Users/antoni/Dola/scripts/obsidian_self_developer.py
```

### 2. Antigravity Scheduled Background Job
```bash
/schedule CronExpression="0 3 * * *" Prompt="Run python C:\Users\antoni\Dola\scripts\obsidian_self_developer.py and audit vault graph density" IsDaemon=true
```

### 3. Omni-Auto Chat Trigger
```text
/omni-auto obsidian-evolve: Execute autonomous vault self-developer engine, heal orphan links, and update graph density.
```
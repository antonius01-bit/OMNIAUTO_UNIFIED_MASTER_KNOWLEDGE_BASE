---
name: affine-open-workspace-os
description: Privacy-first open-source collaborative workspace, multi-modal canvas/doc hybrid editor, block-suite plugin architecture, and offline-first decentralized knowledge graphs.
---

# 📑 AFFiNE Open Workspace OS & Hybrid Canvas Engine (S140)

## 📌 Overview & Core Architecture
The `affine-open-workspace-os` Super-Skill provides complete mastery over AFFiNE (the next-generation open-source Notion + Miro alternative) and BlockSuite:
1. **True Hybrid Modality**: Flawless bi-directional switching between linear document mode (Page View) and infinite spatial whiteboard (Edgeless Canvas Mode).
2. **Local-First & Offline-Ready (OctoBase / Yjs)**: High-performance CRDT state management ensuring 100% data ownership, privacy, and real-time zero-conflict sync.
3. **BlockSuite Architecture**: Extensible, headless rich-text and block-level document infrastructure for building specialized AI agent interfaces and collaborative canvases.
4. **Self-Hosted Enterprise Deployment**: Docker Compose, PostgreSQL/SQLite backend, and decentralized storage federation.

---

## ⚡ Core Operational Modes & Commands
- `/affine canvas-create [title]`: Scaffolds a new spatial visual canvas with connected mind maps, shape blocks, and live markdown documents.
- `/workspace-os sync [doc_id]`: Synchronizes local markdown artifacts and Obsidian notes into AFFiNE native block hierarchies.
- `/blocksuite component [spec]`: Develops custom BlockSuite plugins, custom schema extensions, and interactive agent UI widgets.
- `/affine self-host init`: Generates production-ready Docker Compose stacks for enterprise private AFFiNE cloud.

---

## 🏗️ Technical Architecture & BlockSuite Contracts
- **Data Layer**: OctoBase embedded key-value store with native CRDT transactions and peer-to-peer sync protocols.
- **Editor Engine**: Headless BlockSuite editor with pluggable block models:
  - `affine:page`: Linear document container with rich typography, code blocks, and tables.
  - `affine:surface`: Infinite canvas surface rendering shapes, connectors, frames, and embedded notes.
  - `affine:database`: Inline relational databases with Kanban, Table, and Calendar views.

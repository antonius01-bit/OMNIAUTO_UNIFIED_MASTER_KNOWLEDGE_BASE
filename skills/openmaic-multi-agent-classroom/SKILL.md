---
name: openmaic-multi-agent-classroom
description: Multi-agent interactive classroom engine based on THU-MAIC (Tsinghua University & CogEvol) OpenMAIC, MAIC-UI, SimClass, and dsh-openmaic. Decomposes documents into Socratic scenes with coordinated teacher, TA, and student agents, live whiteboard rendering, and interactive quizzes.
---

# 🎓 S126 — OpenMAIC Multi-Agent Classroom (`openmaic-multi-agent-classroom`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories**:
  - [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (Flagship interactive multi-agent classroom framework).
  - [THU-MAIC/MAIC-UI](https://github.com/THU-MAIC/MAIC-UI) (Interactive pedagogical interfaces & courseware generator).
  - [THU-MAIC/MAIC-Core](https://github.com/THU-MAIC/MAIC-Core) (Core algorithms for multi-agent educational simulation).
  - [THU-MAIC/dsh-openmaic](https://github.com/THU-MAIC/dsh-openmaic) (DeepSeek Harness runtime plugin).
  - [THU-MAIC/SimClass](https://github.com/THU-MAIC/SimClass) (Research paper codebase on classroom simulation).
- **Core Methodology**: Transforms static academic papers, textbooks, and documentation into dynamic, multi-agent interactive learning environments. Operates via coordinated agent personas (Professor, TA, and diverse student archetypes), step-by-step whiteboard derivations with KaTeX/SVG, Socratic dialogue branching, and real-time comprehension evaluation.

---

## 🏛️ Multi-Agent Classroom Roles & Personas

```
                     ┌───────────────────────────────┐
                     │       User / Student          │
                     └───────────────▲───────────────┘
                                     │ Interacts
┌────────────────────────────────────▼────────────────────────────────────┐
│                  OpenMAIC Multi-Agent Classroom Engine                  │
├──────────────────────────────┬──────────────────────────────────────────┤
│ 👨‍🏫 Professor Agent          │ • Frames lesson objectives & overarching │
│   (Academic Lead)            │   theoretical principles.                │
│                              │ • Manages lecture progression & pacing.  │
├──────────────────────────────┼──────────────────────────────────────────┤
│ 👩‍🏫 Teaching Assistant (TA)  │ • Breaks down complex mathematical math. │
│   (Derivation & Assessment)  │ • Renders real-time whiteboard canvas.   │
│                              │ • Deploys diagnostic quizzes & checks.   │
├──────────────────────────────┼──────────────────────────────────────────┤
│ 🧑‍🎓 Student: Curious Novice │ • Asks foundational questions.           │
│   (Conceptual Bridging)      │ • Requests intuitive metaphors.          │
├──────────────────────────────┼──────────────────────────────────────────┤
│ 🧐 Student: Sharp Skeptic    │ • Challenges edge cases & assumptions.   │
│   (Critical Thinking)        │ • Demands empirical proofs & citations.  │
├──────────────────────────────┼──────────────────────────────────────────┤
│ 💻 Student: Practitioner     │ • Asks for implementation & code.        │
│   (Applied Engineering)      │ • Maps theoretical models to systems.    │
└──────────────────────────────┴──────────────────────────────────────────┘
```

---

## 🎨 Interactive Whiteboard Canvas Architecture

The whiteboard module (`MAIC-UI`) renders dynamic visual state snapshots synchronized with agent dialogues:
1. **Mathematical Equations**: Live formatted KaTeX blocks with step-by-step term highlighting (e.g. highlighting learning rate $\eta$ during gradient descent discussion).
2. **Architecture Diagrams**: Programmatic Mermaid and SVG flowcharts generated on-the-fly.
3. **Concept Mindmaps**: Dynamic hierarchical graphs of prerequisites and downstream topics.
4. **Formative Assessment Cards**: Interactive multiple-choice or short-answer cards with instant diagnostic feedback from the TA agent.

---

## ⚡ 5-Phase Pedagogical Pipeline

1. **Phase 1: Knowledge Ingestion & Deconstruction**:
   - Parses document (PDF, Markdown, Paper) via `markitdown-academic-parser`.
   - Extracts key theorems, definitions, empirical claims, and formulas into an ontological knowledge tree.
2. **Phase 2: Pedagogical Scripting & Scene Structuring**:
   - Breaks lesson into 4–6 thematic learning scenes: Introduction $\to$ Core Theorem $\to$ Edge-Case Critique $\to$ Hands-On Application $\to$ Summary Quiz.
3. **Phase 3: Multi-Agent Socratic Multilogue**:
   - Professor introduces the central concept.
   - Skeptic student raises a common misconception.
   - Professor guides the class through Socratic questioning.
   - TA updates the Whiteboard with mathematical formalisms.
   - Practitioner student demonstrates code implementation.
4. **Phase 4: User Interactive Intervention**:
   - The human learner can interrupt, ask questions, answer TA prompts, or request deeper derivations.
5. **Phase 5: Knowledge Artifact Generation**:
   - Generates comprehensive lesson recap document, annotated whiteboard SVG snapshot, and self-test question bank.

---

## 🛠️ DeepSeek Harness (`dsh-openmaic`) & CLI Contracts

### 1. Launch Classroom from Research Paper
```bash
/omni-auto classroom: Ingest [paper.pdf] and launch an interactive OpenMAIC classroom with Professor, TA, and 2 peer students. Focus on methodology and mathematical proofs.
```

### 2. Generate Interactive Teaching Slides & Whiteboard
```bash
/omni-auto classroom-whiteboard: Generate step-by-step whiteboard derivations and interactive Mermaid architecture for [topic/concept].
```

### 3. Run Socratic Peer-Review Defense Simulation
```bash
/omni-auto classroom-defense: Simulate a thesis defense classroom session for [thesis_draft.docx]. Professor acts as chief examiner, TA probes methodology, and skeptic student challenges sample size.
```
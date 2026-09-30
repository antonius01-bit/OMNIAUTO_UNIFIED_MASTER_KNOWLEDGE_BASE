---
name: scientific-agent-research-suite
description: Autonomous scientific research and laboratory workflow suite based on K-Dense-AI (MIT) scientific-agent-skills (165+ procedural skills, arXiv:2609.00065), Google DeepMind science-skills, and Shanghai AI Lab InternScience (ResearchClawBench). Equips AI agents with validated protocols for biology, chemistry, genomics, drug discovery, and automated experiment design.
---

# 🔬 S133 — Scientific Agent Research Suite (`scientific-agent-research-suite`)

## 📌 Overview & Upstream Origin
- **Upstream Repositories & Research Papers**:
  - [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (MIT spinoff library of 165+ procedural research skills for AI scientists; arXiv:2609.00065).
  - [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) (Google DeepMind authoritative procedural workflows in biomolecular modeling and scientific analysis).
  - [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) (Shanghai AI Laboratory "AI for Science" ecosystem & ResearchClawBench benchmarks).
- **Core Methodology**: Transforms general LLM agents into domain-expert **AI Scientists**. Replaces naive prompt generation with rigorously validated procedural playbooks combining specialized databases (PDB, ChEMBL, PubChem, Ensembl, UniProt, GTEx) with systematic hypothesis formulation, computational chemistry, structural biology, and empirical ablation protocols.

---

## 🏛️ 5 Specialized Scientific Domains (165+ Procedural Skills)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SCIENTIFIC AGENT RESEARCH SUITE                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Structural Biology & Macromolecular Modeling:                       │
│    • PDB 3D structure resolution & ligand binding pocket mapping       │
│    • AlphaFold / ESMFold confidence (pLDDT, PAE) assessment            │
│    • Protein-protein interaction (PPI) interface energy calculations   │
├────────────────────────────────────────────────────────────────────────┤
│ 2. Cheminformatics & Computational Drug Discovery:                     │
│    • SMILES / InChI chemical structure canonicalization                │
│    • Molecular docking simulation setup & binding affinity scoring     │
│    • ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) │
├────────────────────────────────────────────────────────────────────────┤
│ 3. Genomics, Transcriptomics & Precision Medicine:                     │
│    • Variant Effect Predictor (VEP) & ClinVar pathogenicity audits     │
│    • GTEx tissue-specific eQTL and RNA expression profiling            │
│    • Cis-Regulatory Elements (cCREs) & transcription factor binding    │
├────────────────────────────────────────────────────────────────────────┤
│ 4. Automated Experimentation & ResearchClawBench:                      │
│    • Multi-hypothesis generation with Bradford Hill causality checks   │
│    • Statistical power estimation & sample size calculation            │
│    • Full ablation matrix design with competing SOTA baselines         │
├────────────────────────────────────────────────────────────────────────┤
│ 5. Scientific Literature Mining & Knowledge Graphs:                   │
│    • Multi-database citation traversal (arXiv, PubMed, Europe PMC)     │
│    • Systematic review data extraction according to PRISMA 2020        │
│    • Cross-study meta-analytic effect size aggregation (Hedges' g)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ Core Procedural Workflows

### 1. Drug Target Discovery & In Silico Screening
1. **Target Identification**: Query Open Targets Platform & UniProt for disease-associated target genes.
2. **Structure Verification**: Retrieve high-resolution ($< 2.5\text{Å}$) PDB crystal structure or AlphaFold DB model.
3. **Candidate Screening**: Pull bioactive small molecules from ChEMBL ($\text{IC}_{50} \le 100\text{nM}$) and verify Lipinski's Rule of Five.
4. **Docking Simulation**: Script AutoDock Vina or gnina molecular docking runs; compute binding free energy ($\Delta G_{\text{bind}}$).

### 2. Genomic Variant Pathogenicity & Functional Impact
1. **Variant Resolution**: Resolve rsID via Ensembl or dbSNP.
2. **Pathogenicity Scoring**: Correlate ClinVar clinical records with AlphaGenome and CADD scores.
3. **Expression Impact**: Cross-reference tissue-specific GTEx expression to evaluate transcriptomic perturbation.

### 3. Empirical Machine Learning & AI for Science Benchmarking
1. **Dataset Hygiene**: Verify zero test-set leakage, stratified split integrity, and class imbalance mitigation.
2. **Ablation Protocol**: Design systematic factorial ablations isolating each architectural component.
3. **Statistical Significance**: Report paired bootstrap test or Wilcoxon signed-rank tests across $K \ge 5$ random seeds.

---

## 🛠️ Operational Workflows & Triggers

### 1. Execute Drug Target & Ligand Binding Analysis
```bash
/omni-auto science-target: Analyze target protein [UniProt_ID/PDB_ID] for disease [disease_name]. Extract known active inhibitors from ChEMBL and evaluate binding pockets.
```

### 2. Functional Genomics Variant Impact Assessment
```bash
/omni-auto science-variant: Investigate genomic variant [rsID / chr:pos:ref:alt]. Predict protein functional impact, ClinVar status, and GTEx tissue expression changes.
```

### 3. Design Empirical Scientific Experiment & Ablation
```bash
/omni-auto science-experiment: Design rigorous experimental methodology for [hypothesis]. Define baseline models, evaluation metrics, ablation table, and sample size requirements.
```
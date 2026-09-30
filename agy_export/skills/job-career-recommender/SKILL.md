---
name: job-career-recommender
description: >-
  Specialized AI recommendation engine for job matching, candidate ranking, resume ATS scoring, skill taxonomy normalization (O*NET/ESCO), and career trajectory prediction.
---

# 💼 Job & Career Recommendation Engine (ATS + Taxonomy + Two-Tower Matching)

Use this skill when building or optimizing job recommendation systems, candidate-job matching algorithms, resume parser & score matching, skill gap analysis, or career path forecasting.

## Architecture

```mermaid
flowchart TD
    subgraph Ingestion ["1. Multi-Modal Profile Ingestion"]
        R["Candidate Resume (PDF/DOCX)"] --> P["Skill & Experience Entity Extraction"]
        J["Job Description (JD)"] --> TE["Requirements & Seniority Parsing"]
    end

    subgraph Taxonomy ["2. Skill Taxonomy Normalization"]
        P & TE --> ON["Ontology Mapping (O*NET, ESCO, Lightcast)"]
        ON --> E["Vector & Graph Embeddings"]
    end

    subgraph Matching ["3. Multi-Stage Matching & Ranking"]
        E --> TT["Stage 1: Two-Tower Hard Matching (Skills, Location, Salary)"]
        TT --> RK["Stage 2: Semantic Experience & Culture Scoring (Cross-Encoder)"]
        RK --> SG["Stage 3: Skill Gap Analysis & Salary Fair Benchmark"]
    end

    subgraph Deliverable ["4. Output"]
        SG --> Out["Ranked Candidates / Matched Jobs + Match Explanations"]
    end
```

## Core Modules
1. **Skill Taxonomy Normalization**: Standardizes non-standard skill terms (e.g. "ReactJS", "React.js", "React 18" $\to$ `Skill:React`) against O*NET and ESCO taxonomies.
2. **Two-Tower Candidate-Job Matching**:
   - Candidate Tower: Encodes resume skills, years of experience, education, domain velocity.
   - Job Tower: Encodes requirements, responsibility vectors, seniority level, industry sector.
3. **Skill Gap & Trajectory Analytics**:
   - Identifies missing critical skills vs "nice-to-haves".
   - Suggests upskilling pathways and next-step career promotions.
4. **Fairness & Debiasing**: Filters protected attributes (gender, age, ethnicity) to ensure compliance with hiring regulations and unbiased scoring.

## How to Use
`Match resume [resume_text/file] against job description [job_desc] with skill taxonomy normalization, ATS score, and gap analysis.`

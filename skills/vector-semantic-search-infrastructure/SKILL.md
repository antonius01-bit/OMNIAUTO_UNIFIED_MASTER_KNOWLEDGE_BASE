---
name: vector-semantic-search-infrastructure
description: High-throughput semantic search and vector database infrastructure combining Weaviate, Typesense, and OpenSearch.
---

# 🔍 Vector & Semantic Search Infrastructure (Weaviate & Typesense) (S150)

## 📌 Overview & Core Architecture
The `vector-semantic-search-infrastructure` Super-Skill replaces expensive proprietary search SaaS (Pinecone, Algolia) with open-source high-throughput search engines:
1. **Weaviate Vector Database**: Cloud-native, real-time vector search engine with GraphQL/REST APIs, hybrid search, and multi-modal vectorizers.
2. **Typesense Fast Lexical Search**: Typo-tolerant, in-memory search engine optimized for sub-50ms instant search-as-you-type UI experiences.
3. **Hybrid Search Fusion (Reciprocal Rank Fusion - RRF)**: Combines dense vector similarity ($k$-NN) with sparse BM25 keyword matching for optimal recall.
4. **Self-Hosted Deployment**: Docker Compose architectures with persistent volume mounts, zero egress cost, and local data sovereignty.

---

## ⚡ Core Operational Modes & Commands
- `/vector-infra deploy`: Generates Docker Compose configurations for Weaviate and Typesense clusters.
- `/weaviate-db schema [spec]`: Defines vector classes, cross-references, and index parameters (HNSW / Flat).
- `/typesense-search index [docs]`: Creates typo-tolerant collections with faceted filtering and instant search schemas.
- `/hybrid-search query [text]`: Executes combined dense + sparse retrieval with dynamic alpha weighting.

---

## ⚡ Hybrid Retrieval Mathematics
$$\text{Score}_{\text{hybrid}} = \alpha \cdot \text{Score}_{\text{dense}} + (1 - \alpha) \cdot \text{Score}_{\text{sparse}}$$
Where $\alpha = 0.75$ prioritizes conceptual semantic depth while retaining exact keyword and ID precision.

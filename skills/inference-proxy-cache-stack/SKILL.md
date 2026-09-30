---
name: inference-proxy-cache-stack
description: High-throughput LLM serving via vLLM (PagedAttention), universal 100+ LLM proxy gateway & fallbacks via LiteLLM, and semantic vector caching via GPTCache.
---

# S67: Inference Proxy & Cache Stack (inference-proxy-cache-stack)

## ⚡ Overview & Architecture
The inference-proxy-cache-stack unites industry-standard high-throughput model inference, unified proxy routing across 100+ LLM providers, and semantic caching:
1. **vLLM Engine (llm-project/vllm)**:
   - High-throughput, low-latency LLM serving powered by PagedAttention (virtual memory management for KV cache).
   - Continuous batching, chunked prefill, speculative decoding, and native tensor parallelism across GPUs.
   - Compatible with OpenAI API endpoints (/v1/chat/completions, /v1/completions).
2. **LiteLLM Proxy & Gateway (BerriAI/litellm)**:
   - Universal abstraction layer calling OpenAI, Anthropic, Gemini, Vertex, Bedrock, Ollama, Groq, DeepSeek, and HuggingFace using a single standard format.
   - Built-in load balancing, auto-fallbacks (e.g. Gemini -> Groq -> DeepSeek -> Local vLLM), retry backoffs, and cost/spend tracking.
   - Proxy server mode with virtual keys, rate limiting, and team quotas.
3. **GPTCache Vector Caching (zilliztech/GPTCache, ilip-halt/gptcache)**:
   - Semantic exact and approximate caching layer for LLM responses.
   - Drastically cuts latency (from seconds to <10ms) and token spend by up to 80% for repetitive queries.
   - Integrates with Milvus, Faiss, Qdrant, Chroma, and Redis for embedding similarity retrieval.

## 🛠️ Usage & Key Recipes
- **vLLM CLI**: python -m vllm.entrypoints.openai.api_server --model <model_path> --port 8000
- **LiteLLM Fallback Matrix**: Seamless multi-provider failover chains with latency tracking.
- **GPTCache Embeddings**: Similarity thresholds for instant semantic hit caching.

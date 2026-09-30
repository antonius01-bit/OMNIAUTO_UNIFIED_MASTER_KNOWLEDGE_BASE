---
name: free-tier-open-software-replacements
description: >-
  Zero-cost enterprise stack replacing paid SaaS with 10 top-tier open-source tools (Fooocus, AppFlowy, yt-dlp, n8n, Cal.com, Plausible, Whisper, Listmonk, Bitwarden, Ollama) and free public/LLM API gateways.
---

# 🆓 Free-Tier Open-Source Software Replacements (Zero-Cost Enterprise Stack)

Use this skill when seeking zero-cost, self-hosted, or free API alternatives to commercial paid software for automation, creative generation, notes, analytics, scheduling, password management, and local LLM execution.

## The 10 Essential Open-Source Replacements

```mermaid
flowchart TD
    subgraph CreativeMedia ["1. Creative & Media"]
        F["Fooocus (lllyasviel/Fooocus)"] -->|Replaces| MJ["Midjourney / DALL-E ($30+/mo)"]
        W["Whisper (openai/whisper)"] -->|Replaces| OT["Otter.ai / Descript ($20+/mo)"]
        Y["yt-dlp (yt-dlp/yt-dlp)"] -->|Replaces| DL["Paid Video Downloaders"]
    end

    subgraph ProductivityOps ["2. Productivity & Operations"]
        AF["AppFlowy (AppFlowy-IO/AppFlowy)"] -->|Replaces| NO["Notion / Coda ($10+/mo)"]
        CAL["Cal.com (calcom/cal.com)"] -->|Replaces| CL["Calendly ($12+/mo)"]
        BW["Bitwarden (bitwarden/clients)"] -->|Replaces| OP["1Password / LastPass ($5+/mo)"]
    end

    subgraph AutomationData ["3. Automation, Marketing & AI"]
        N8N["n8n (n8n-io/n8n)"] -->|Replaces| ZP["Zapier / Make ($30+/mo)"]
        PL["Plausible (plausible/analytics)"] -->|Replaces| GA["Google Analytics / Mixpanel"]
        LM["Listmonk (knadh/listmonk)"] -->|Replaces| MC["Mailchimp / ConvertKit ($25+/mo)"]
        OL["Ollama (ollama/ollama)"] -->|Replaces| API["Paid Cloud LLM APIs ($$$)"]
    end
```

## Free API & Cloud Gateway Integrations
1. **Awesome Free LLM APIs** (`open-free-llm-api/awesome-freellm-apis`): Curated index of keyless and free-tier LLM endpoints (Groq, Together, Mistral, HuggingFace, Gemini Free Tier).
2. **Public APIs Directory** (`public-apis/public-apis`): 1400+ free public APIs for finance, weather, crypto, development, science, and social media data extraction.
3. **Tokenin AI** (`tokenin.my.id`): Low-latency Indonesian token-optimized AI model routing.

## How to Use
`Deploy zero-cost replacement for [software_name] using [Fooocus/n8n/AppFlowy/Ollama/Cal.com] with configuration guide.`

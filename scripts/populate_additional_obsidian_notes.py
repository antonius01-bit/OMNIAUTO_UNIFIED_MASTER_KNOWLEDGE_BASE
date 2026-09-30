import os

VAULT_DIR = r"C:\Users\antoni\Dola\obsidian_vault"

# 1. Cognitive Modes Matrix
with open(os.path.join(VAULT_DIR, "01_PROMPT_ENGINEERING", "COGNITIVE_MODES_MATRIX.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Cognitive Prompt Modes Matrix
type: cognitive_framework
status: active
tags:
  - mental-models
  - reasoning
  - prompt-master
---

# 🧠 10 Cognitive Reasoning & Prompt Modes Matrix

Use these modifiers with `/omni-auto` to instantly shape AI reasoning and depth:

1. **`TL;DR`**: *Ringkas jawaban panjang jadi inti saja.* Eliminates all filler narrative.
2. **`ELI10`**: *Jelaskan topik rumit pakai bahasa simpel.* Analogy-driven simplification for beginners.
3. **`LAYMAN'S TERMS`**: *Ubah bahasa teknis jadi bahasa awam.* Translates technical jargon into accessible terms.
4. **`BREAKDOWN STEPS`**: *Pecah jadi langkah satu per satu.* Step-by-step sequential execution roadmap.
5. **`PROS & CONS`**: *Kasih plus minus sebelum ambil keputusan.* Balanced multi-dimensional impact evaluation.
6. **`COMPARE / CONTRAST`**: *Bandingkan dua pilihan dengan jelas.* Feature-by-feature comparative matrix.
7. **`SOCRATIC METHOD`**: *Bimbing lewat pertanyaan, bukan langsung jawab.* Guided self-discovery via inquiry.
8. **`DEVIL'S ADVOCATE`**: *Cari sisi lawan dari ide kamu.* Stress-testing hypotheses with counter-arguments.
9. **`PARETO (80/20)`**: *Fokus hal kecil yang hasilnya paling besar.* Finding the 20% inputs producing 80% results.
10. **`REDTEAM`**: *Cari kelemahan ide dan blind spot.* Adversarial vulnerability & failure mode scan.

Related: [[PROMPT_MASTER]] | [[00_INDEX]]
""")

# 2. Free Tier Software Replacements
with open(os.path.join(VAULT_DIR, "05_OPERATIONS", "FREE_TIER_SOFTWARE_REPLACEMENTS.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Free-Tier Open-Source Enterprise Stack
type: software_replacements
status: active
tags:
  - open-source
  - cost-saving
  - self-hosted
---

# 🆓 10 Free Open-Source Replacements for Commercial SaaS

1. **Fooocus** (`lllyasviel/Fooocus`): Replaces Midjourney / DALL-E (Free local SDXL/Flux generation).
2. **AppFlowy** (`AppFlowy-IO/AppFlowy`): Replaces Notion & Coda (Privacy-first local workspace).
3. **yt-dlp** (`yt-dlp/yt-dlp`): Media & video streaming extraction.
4. **n8n** (`n8n-io/n8n`): Replaces Zapier & Make (Self-hosted node automation).
5. **Cal.com** (`calcom/cal.com`): Replaces Calendly (Scheduling infrastructure).
6. **Plausible** (`plausible/analytics`): Replaces Google Analytics (Lightweight, privacy-friendly).
7. **Whisper** (`openai/whisper`): Replaces Otter.ai & Descript (SOTA speech-to-text).
8. **Listmonk** (`knadh/listmonk`): Replaces Mailchimp & ConvertKit (High-volume newsletter engine).
9. **Bitwarden** (`bitwarden/clients`): Replaces 1Password & LastPass (Encrypted vault).
10. **Ollama** (`ollama/ollama`): Replaces paid cloud APIs for local LLM inference.

## Free API Gateways
- **Awesome Free LLM APIs**: `open-free-llm-api/awesome-freellm-apis`
- **Public APIs Directory**: `public-apis/public-apis` (1400+ free public endpoints)
- **Tokenin AI**: `tokenin.my.id` (Indonesian token-optimized routing)

Related: [[00_INDEX]]
""")

# 3. Expert Roles Library
with open(os.path.join(VAULT_DIR, "00_MASTER", "EXPERT_ROLES_LIBRARY_268.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: 268+ Expert System Roles & Personas
type: role_personas
status: active
tags:
  - personas
  - expert-roles
  - superman-prompts
---

# 🎭 268+ Expert System Roles & Executive Personas

Derived from Chen Media, Ultron, Knox, and ChatGPT Tricks Superman collection:

- **Technical & Architecture**: Principal Architect, Distributed Systems Engineer, Cryptographer, ML Scientist, Security Red Teamer.
- **Corporate & Financial**: Fractional CFO, M&A Due Diligence Specialist, Tax Strategist, IP Attorney, Risk Officer.
- **Academic & Scientific**: Scopus/WoS Editor, Bioinformatician, Econometrician, Clinical Trial Statistician.
- **Growth & Marketing**: Direct-Response Copywriting Legend, Viral Short-Form Director, Conversion Rate Optimizer.

Related: [[PROMPT_MASTER]] | [[00_INDEX]]
""")

# 4. Multimodal Creative Studio
with open(os.path.join(VAULT_DIR, "08_PRESENTATION", "MULTIMODAL_CREATIVE_STUDIO.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: Multimodal Creative Studio & Social Growth
type: creative_studio
status: active
tags:
  - voice-synthesis
  - image-prompting
  - instagram-audit
  - fish-audio
---

# 🎙️ Multimodal Creative Studio & Growth Frameworks

- **Fish Audio Voice Engine** (`fish.audio`): High-fidelity TTS, emotion tagging, and multilingual voice cloning.
- **Fooocus & Flux Prompt Craft**: Lens, camera angle, film stock, and lighting prompts.
- **Claude Instagram Account Auditor**: Bio positioning, hook retention, and monetization CTA.
- **Orbitagents & Ultron Swarms**: Multi-agent desktop automation.
- **Moonshot Kimi K2.6**: Long-context reasoning integration.

Related: [[00_INDEX]] | [[PABRIK_AI_CATALOG]]
""")

print("Obsidian notes successfully created!")

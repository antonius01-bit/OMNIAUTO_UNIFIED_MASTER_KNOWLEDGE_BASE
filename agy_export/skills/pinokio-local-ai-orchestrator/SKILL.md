---
name: pinokio-local-ai-orchestrator
description: >-
  Autonomous local AI application runner and professional generative studio combining Pinokio browser automations, InvokeAI canvas workflows, and LoRA visual training.
---

# 🎨 Pinokio Local AI Orchestrator & InvokeAI Studio

Use this skill when installing, scripting, or automating local open-source AI applications (ComfyUI, InvokeAI, Fooocus, Whisper, LLaMA), configuring LoRA training, or managing visual generative canvases.

## Architecture

```mermaid
flowchart LR
    subgraph Host ["1. Pinokio Autonomous Browser Engine (pinokio.co)"]
        PIN["Pinokio Script Runner (.json / .js)"] --> ENV["Virtual Environment & Dependency Sandbox"]
    end

    subgraph VisualStudio ["2. InvokeAI Generative Studio (invoke-ai/InvokeAI)"]
        ENV --> INV["Infinite Canvas (Inpainting / Outpainting)"]
        ENV --> CTL["ControlNet & IP-Adapter Visual Staging"]
        ENV --> TRN["Invoke-Training (LoRA / Textual Inversion)"]
    end

    subgraph Production ["3. Output Generation"]
        INV & CTL & TRN --> OUT["Production Visual Assets & Custom Fine-Tuned Weights"]
    end
```

## Key Capabilities
1. **Pinokio Automated Scripting**: Automates Git cloning, Python venv creation, CUDA dependency installation, and background server execution.
2. **InvokeAI Canvas Workflows**: Advanced visual compositing, regional prompting, inpainting, and outpainting for concept art.
3. **LoRA Visual Fine-Tuning**: Scripted workflows for training custom character, style, and object LoRAs with `invoke-training`.

## How to Use
`Deploy and run local AI app [app_name] via Pinokio script or configure InvokeAI visual workflow for [creative_task].`

---
name: fireflies-meeting-voice-intelligence
description: Meeting transcription, conversation intelligence, and automated action item extraction engine powered by Fireflies AI SDK and Podcastfy audio synthesis. Automates meeting notes, CRM logging, multi-speaker conversational summarization, and audio briefing generation.
---

# S111: Fireflies Meeting & Voice Intelligence Engine (fireflies-meeting-voice-intelligence)

## ⚡ Overview & Conversation Intelligence
Synthesized from official Fireflies.ai developer libraries (`firefliesai/fireflies-node-sdk`, `n8n-nodes-fireflies`, `schema-forge`):
1. **Automated Meeting Transcription & Multi-Speaker Diarization**:
   - Ingests audio/video recordings and generates speaker-attributed transcripts with millisecond timestamps.
   - Topic detection, sentiment trajectory tracking, and talk-time distribution analytics.
2. **Action Item & Decision Extraction**:
   - Forensic extraction of commitments: Who agreed to what, deadlines, blockers, and assigned deliverables.
   - Automated generation of executive meeting minutes (MoM) and SOP execution checklists.
3. **Enterprise CRM & Workflow Sync**:
   - n8n integration (`n8n-nodes-fireflies`) automatically routing call summaries into HubSpot, Salesforce, Notion, and Slack.
4. **Conversational Audio Synthesis**:
   - Integrates Podcastfy dual-voice synthesis to transform dense executive meeting notes into 3-minute audio briefings.

## 🛠️ Usage in Omni-Auto
- **Command**: `/omni-auto fireflies meeting: Transcribe, summarize, and extract action items from [audio/transcript]`
- Deployed during corporate operations, stakeholder interviews, and thesis committee feedback transcription.

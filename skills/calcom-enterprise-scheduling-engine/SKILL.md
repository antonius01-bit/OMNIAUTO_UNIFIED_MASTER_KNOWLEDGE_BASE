---
name: calcom-enterprise-scheduling-engine
description: Enterprise appointment scheduling infrastructure, multi-calendar synchronization, booking API webhooks, and self-hosted Cal.com deployments.
---

# Cal.com Enterprise Scheduling Engine (S65)

## Overview
Self-hosted and enterprise scheduling infrastructure engine powered by Cal.com (calcom/cal.com). Automates calendar booking, multi-calendar conflict checking, dynamic availability rules, round-robin team scheduling, and booking API integrations.

## Key Capabilities
1. Multi-Calendar Sync: Two-way synchronization across Google Calendar, Office 365, Apple Calendar, and CalDAV.
2. Dynamic Routing & Round-Robin: Routes prospects to the optimal team member based on criteria, time zones, and availability.
3. Webhook & Payment Workflows: Dispatches booking webhooks to CRM/Zapier/n8n and accepts deposits via Stripe.
4. White-Label Self-Hosting: Docker and Kubernetes deployment templates with custom branding (cal.diy).

## Activation
- Command: /omni-auto calcom: Configure event booking type [meeting_name] with availability rules and webhook notifications

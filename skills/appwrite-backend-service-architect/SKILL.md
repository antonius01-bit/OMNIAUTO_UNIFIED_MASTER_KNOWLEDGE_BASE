---
name: appwrite-backend-service-architect
description: Local-first and self-hosted Backend-as-a-Service (BaaS), authentication, real-time databases, storage, and Cloud Functions via Appwrite.
---

# 🛡️ Appwrite Backend-as-a-Service Architect (S151)

## 📌 Overview & Core Architecture
The `appwrite-backend-service-architect` Super-Skill provides complete self-hosted backend infrastructure, replacing Google Firebase:
1. **Authentication & User Management**: OAuth2 (GitHub, Google, Apple), magic URL, phone SMS, and session management with granular RBAC permissions.
2. **Real-time Database & Document Store**: Schematized document collections, indexes, cascading relations, and WebSocket event streams.
3. **Storage & Media Delivery**: File storage with chunked uploads, built-in image transformations, and encryption at rest.
4. **Serverless Cloud Functions**: Polyglot function runtimes (Node.js, Python, Deno, Dart, PHP, Go) triggered by events, CRON schedules, or HTTP.

---

## ⚡ Core Operational Modes & Commands
- `/appwrite-baas init`: Bootstraps an Appwrite project with database schemas, attributes, and permission gates.
- `/self-hosted-backend docker`: Generates production Docker Compose files with Traefik SSL and Redis caching.
- `/baas-architect rbac [role]`: Defines Document-Level Permissions (`read("any")`, `write("team:admins")`).
- `/appwrite-func deploy [name]`: Packages and deploys Python or TypeScript serverless functions with environment variables.

---

## 🔒 Permission & Security Paradigm
- **Granular Security**: Every document, bucket, and file requires explicit permission rules.
- **Data Sovereignty**: 100% self-hosted on your own cloud VPS or bare metal; zero vendor lock-in.

---
name: free-tier-developer-infrastructure
description: Curated comprehensive catalog of zero-cost developer infrastructure, free APIs, cloud hosting, DBaaS, BaaS, CDN, CI/CD, and open-source alternatives.
---

# 🌐 Free-Tier Developer Infrastructure & Zero-Cost Cloud Catalog (S144)

## 📌 Overview & Core Architecture
The `free-tier-developer-infrastructure` Super-Skill indexes and operationalizes the entire `free-for-dev` (Ripienaar / Jixserver / ItsFree.dev) repository ecosystem:
1. **300+ Verified Zero-Cost Cloud Services**: Compute, Serverless, Database-as-a-Service (Postgres, MySQL, Redis, Vector), Authentication, Storage, CDN, CI/CD, and Monitoring.
2. **Automated Tier Budget & Limit Governance**: Strict monitoring of monthly free-tier limits, compute hour quotas, bandwidth caps, and graceful failover configurations.
3. **Zero-Cost Enterprise Architecture**: Blueprints for building production-ready, globally distributed SaaS platforms entirely on permanent free tiers.
4. **FOSS Self-Hosted SaaS Replacements**: Drop-in open-source self-hosted alternatives to high-cost SaaS tools.

---

## ⚡ Core Operational Modes & Commands
- `/free-infra search [category]`: Queries curated free-tier providers for a specific category (DB, Hosting, Auth, Vector, Email).
- `/free-for-dev architecture [project]`: Generates a complete zero-cost architecture diagram and provider breakdown for a new application.
- `/zero-cost-cloud budget-check`: Audits active services against free-tier thresholds to prevent surprise charges.
- `/free-api-catalog list`: Displays verified free API endpoints with authentication methods, rate limits, and response schemas.

---

## 🚀 The Definitive Zero-Cost Production Stack
- **Web & Frontend Hosting**: Cloudflare Pages, Vercel (Hobby), Netlify, GitHub Pages (Unlimited bandwidth on Cloudflare).
- **Serverless & Edge Compute**: Cloudflare Workers (100k requests/day), Supabase Edge Functions, Deno Deploy.
- **Relational Databases (Postgres)**: Supabase (500MB free), Neon (0.5GB compute, autosuspend), CockroachDB (5GB free).
- **Document & Vector Storage**: Upstash (Redis 10k cmd/day, Vector 10k queries/day), MongoDB Atlas (512MB free), Pinecone (Starter free).
- **Object Storage**: Cloudflare R2 (10GB/mo free, 0 egress fees), Backblaze B2 (10GB free), Supabase Storage (1GB free).
- **Authentication**: Clerk (10k MAU free), Supabase Auth (50k MAU free), Kinde (7.5k MAU free).
- **CI/CD**: GitHub Actions (2,000 Linux min/month), Cloudflare Webhooks, GitLab CI (400 min/mo).
- **DNS & CDN**: Cloudflare Free Tier (Unlimited DNS, SSL, DDoS protection, global caching).

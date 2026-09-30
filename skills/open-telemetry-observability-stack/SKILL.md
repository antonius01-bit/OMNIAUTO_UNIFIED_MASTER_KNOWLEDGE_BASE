---
name: open-telemetry-observability-stack
description: Enterprise full-stack observability, application telemetry, error tracking, and session replay powered by Highlight.io, Prometheus, and OpenTelemetry.
---

# 🔭 OpenTelemetry & Highlight.io Full-Stack Observability (S149)

## 📌 Overview & Core Architecture
The `open-telemetry-observability-stack` Super-Skill provides complete full-stack monitoring, replacing high-cost APM SaaS (Datadog, New Relic, Sentry):
1. **Highlight.io Web Observability**: Open-source session replay, frontend error monitoring, and network performance tracking.
2. **OpenTelemetry (OTel) Standard**: Vendor-neutral distributed tracing, metrics, and log pipelines across microservices.
3. **Prometheus & Grafana Stack**: Time-series metrics collection, alerting rules, and real-time operational dashboarding.
4. **Agent Observability (LLM Tracing)**: Detailed tracing of agent tool calls, latency budgets, token expenditures, and exception trees.

---

## ⚡ Core Operational Modes & Commands
- `/observability init [framework]`: Instruments Node.js, Python, or Go backends with OpenTelemetry auto-instrumentation.
- `/highlight-telemetry setup`: Embeds Highlight.io error tracking and session replay into Next.js/React frontends.
- `/trace-metrics audit`: Inspects distributed traces for database bottleneck queries, slow HTTP endpoints, and memory spikes.
- `/apm-monitor alert`: Configures Prometheus alerting thresholds for CPU, error rate, and agent tool failures.

---

## 📊 Telemetry Golden Signals
- **Latency**: Sub-millisecond tracking for internal service-to-service calls; $\le 200\text{ms}$ for external API responses.
- **Traffic**: High-precision request rate monitoring (RPS).
- **Errors**: Automated root-cause stack trace grouping with correlated DOM session recording.
- **Saturation**: Memory ceiling and CPU usage telemetry.

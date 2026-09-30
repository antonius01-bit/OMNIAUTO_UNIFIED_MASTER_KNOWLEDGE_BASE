---
name: midday-enterprise-financial-automation
description: Modern enterprise business and financial intelligence engine, automated invoice processing, real-time runway/revenue telemetry, multi-bank syncing, and financial agent workflows.
---

# 💼 Midday Enterprise Financial Automation Suite (S141)

## 📌 Overview & Core Architecture
The `midday-enterprise-financial-automation` Super-Skill provides end-to-end corporate financial intelligence, inspired by Midday AI (the modern financial OS for startups):
1. **Automated Document & Invoice Processing**: Intelligent extraction of vendor data, line items, taxes, and payment terms from PDF invoices and receipts via specialized vision models.
2. **Real-Time Financial Telemetry**: Live computation of Monthly Recurring Revenue (MRR), burn rate, customer acquisition cost (CAC), runway duration, and cash flow projections.
3. **Multi-Bank & Multi-Provider Syncing**: Secure financial data ingestion via open banking APIs, Stripe, Wise, and CSV bank export reconciliation.
4. **Autonomous Financial Assistant**: Natural-language financial auditing, anomaly detection in corporate expenses, and automated tax preparation reports.

---

## ⚡ Core Operational Modes & Commands
- `/midday invoice-parse [file]`: Ingests and extracts structured line items, tax IDs, and totals from PDF/image invoices.
- `/financial-automation runway`: Calculates net burn, cash runway in months, and stress-tests various revenue decline scenarios.
- `/runway-telemetry report`: Generates an executive board-ready financial memo with waterfall charts, EBITDA forecasts, and unit economics.
- `/invoice-engine reconcile`: Matches bank transactions against issued invoices and pending payables to detect discrepancies.

---

## 📊 Financial Heuristics & Audit Standards
- **Quick Ratio**: $(	ext{Cash} + 	ext{Marketable Securities} + 	ext{Receivables}) / 	ext{Current Liabilities} \ge 1.5$.
- **Burn Multiple**: $	ext{Net Burn} / 	ext{Net New ARR} \le 1.2$ for high-efficiency startups.
- **Rule of 40**: $	ext{Revenue Growth Rate} + 	ext{Profit Margin} \ge 40\%$.

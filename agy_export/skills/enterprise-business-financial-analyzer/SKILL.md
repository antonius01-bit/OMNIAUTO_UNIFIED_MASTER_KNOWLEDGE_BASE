---
name: enterprise-business-financial-analyzer
description: >-
  Enterprise financial and business analysis engine fusing Pabrik AI (Breakdown Modal & Profit, Property AI, File Analyzer) with Dola Product Analytics for unit economics, ROI calculations, and property valuation.
---

# 📈 Enterprise Business & Financial Analyzer (Pabrik AI + Dola Analytics Fusion)

Use this skill when calculating unit economics, breaking down CapEx/OpEx, calculating profit margins, modeling real estate/property investment ROI, or conducting deep multi-format financial file analysis.

## Analysis Framework

```mermaid
flowchart TD
    subgraph Data ["1. Business & Financial Inputs"]
        RAW["Financial Files (Excel / CSV / PDF)"] --> FA["Pabrik AI Multi-File Analyzer"]
        INPUT["User Cost & Revenue Parameters"] --> FA
    end

    subgraph Modeling ["2. Quantitative Modeling"]
        FA --> U["Unit Economics & COGS (HPP) Breakdown"]
        FA --> P["Property Investment ROI & Cap Rate (AI Property)"]
        FA --> S["Sensitivity & Break-Even Point (BEP) Analysis"]
    end

    subgraph Insights ["3. Executive Deliverable"]
        U & P & S --> REP["Comprehensive Financial Model & Executive Summary Table"]
    end
```

## Core Capabilities
1. **Pabrik AI Modal & Profit Breakdown**:
   - Fixed vs Variable cost decomposition.
   - Cost of Goods Sold (COGS / HPP) per unit.
   - Gross Margin, Net Margin, and Break-Even Point (BEP in units & currency).
2. **AI Property & Real Estate Valuation**:
   - Capitalization Rate (Cap Rate), Net Operating Income (NOI), Cash-on-Cash Return.
   - Rental yield projections and 5-10 year appreciation modeling.
3. **Automated Financial Statement Parsing**: Extracts income statements, balance sheets, and cash flow reports from PDFs and Excel sheets into structured analytical matrices.

## How to Use
`Analyze financial model for [business/property] with CapEx/OpEx breakdown, COGS, profit margin, BEP, and 5-year ROI forecast.`

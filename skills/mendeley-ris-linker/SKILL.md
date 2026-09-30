---
name: mendeley-ris-linker
description: >-
  Generates synchronized RIS citation files for Mendeley, Zotero, and EndNote where each reference entry ID matches exact manuscript citation markers like [1#E], [2#E], enabling 100% automated citation pairing.
---

# 🔗 Mendeley / Zotero RIS Citation Synchronizer

Use this skill when generating, formatting, or cleaning reference lists, RIS files, BibTeX, or connecting in-text citations `[N#E]` to reference management software.

## Workflow

### 1. In-Text Numbering Convention
During manuscript drafting, every referenced fact or data point is assigned a unique tag:
- `...kemiskinan turun 2,3% [1#E].`
- `...lama sekolah berpengaruh signifikan terhadap produktivitas [2#E].`

### 2. RIS Format Specification
Export references into standard `.ris` files using matching `ID` numbers:
```text
TY  - JOUR
ID  - 1
AU  - Badan Pusat Statistik
TI  - Profil Kemiskinan di Indonesia 2024
JO  - Berita Resmi Statistik
PY  - 2024
VL  - 12
IS  - 3
SP  - 45
EP  - 58
DO  - 10.1016/j.brs.2024.01.002
ER  - 

TY  - JOUR
ID  - 2
AU  - Sutanto, Budi
AU  - Wijaya, Agus
TI  - Pengaruh Rata-Rata Lama Sekolah Terhadap Tingkat Kemiskinan
JO  - Jurnal Ekonomi dan Pembangunan
PY  - 2023
VL  - 31
IS  - 2
SP  - 110
EP  - 125
ER  - 
```

### 3. Automated Reference Management
When imported into Mendeley or Zotero, entries map 1-to-1 with manuscript tokens without manual relinking.

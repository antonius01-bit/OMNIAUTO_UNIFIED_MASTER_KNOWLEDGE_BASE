---
name: web-check-dashy-secops-suite
description: Comprehensive on-demand OSINT website reconnaissance (DNS, SSL, WHOIS, open ports, security headers, tech stack fingerprinting), SecOps risk auditing, and responsive operations dashboarding powered by Lissy93 (Web-Check & Dashy).
---

# 🔍 Web-Check & Dashy SecOps Suite (S123)

Automated All-in-One OSINT Website Reconnaissance and SecOps Dashboarding Suite powered by Alicia Sykes (**lissy93**: `web-check` - 23.0k★, `dashy` - 26.4k★, `personal-security-checklist` - 22.2k★).

---

## 🌐 1. 20+ Automated Website Reconnaissance Vectors

`web-check` executes non-destructive OSINT profiling against any target domain:

| Modul Analisis | Target Data & Temuan Keamanan |
| :--- | :--- |
| **IP & Geo-IP** | Server host location, ASN number, organization ISP, latitude/longitude. |
| **SSL / TLS Certificate** | Issuer authority, validity period, SAN domains, cryptographic cipher strength. |
| **DNS Records** | A, AAAA, MX, TXT (SPF/DKIM/DMARC audit), NS, CNAME configuration checks. |
| **Security Headers** | HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy scores. |
| **Open Ports (Nmap-lite)**| 80, 443, 8080, 21, 22, 3306, 5432 exposure checks. |
| **Tech Stack Fingerprint** | Web server (Nginx/Apache), CMS (WordPress/Drupal), frameworks (React/Next.js). |
| **WHOIS & Domain Age** | Registrar, registration date, expiration deadline, nameserver status. |
| **Threat Intelligence** | URLhaus, PhishTank, Google Safe Browsing, Shodan metadata. |

---

## 📊 2. Dashy Responsive Operations Dashboard

Enables rapid deployment of privacy-respecting, highly customizable status dashboards:
- Multi-page layouts for devops, microservices, and AI agent health.
- Real-time status indicators (ping, HTTP response codes, latency checks).
- Built-in authentication (Keycloak, Okta, HTTP Basic Auth).
- Zero external tracking, 100% self-hosted local-first architecture.

---

## 🚀 3. Trigger & Workflows
- **Trigger**: `/omni-auto web-check` atau `/secops-dashboard`
- **Sub-skills**:
  - `web_check_recon`: Pemindaian OSINT komprehensif atas domain publik sasaran.
  - `security_headers_auditor`: Evaluasi dan rekomendasi konfigurasi header HTTP aman.
  - `dashy_service_monitor`: Konfigurasi dashboard monitoring status endpoint agen.

---
name: foss-developer-api-testing-stack
description: Git-friendly offline API testing and execution engine powered by Bruno and VSCodium, replacing Postman and proprietary API tooling.
---

# 🚀 FOSS Developer API Testing Stack (Bruno & VSCodium) (S147)

## 📌 Overview & Core Architecture
The `foss-developer-api-testing-stack` Super-Skill replaces high-cost proprietary API testing SaaS (Postman Pro, Insomnia Cloud) with 100% open-source, local-first, Git-native alternatives:
1. **Bruno Open-Source API Client**: Plain-text Bru markup language stored directly inside your Git codebase, eliminating cloud sync leaks, login walls, and paywalls.
2. **Git-Native Collaboration**: Collections live alongside application source code; API changes, assertions, and environment variables are versioned via standard pull requests.
3. **Automated CLI Regression Runner (`@usebruno/cli`)**: Headless execution in CI/CD pipelines without SaaS subscription tokens.
4. **VSCodium / Offline Developer Workflows**: Zero-telemetry, offline-first development environments with local secret encryption.

---

## ⚡ Core Operational Modes & Commands
- `/bruno-api scaffold [name]`: Generates a declarative Bruno collection directory (`.bru` files) for an API endpoint.
- `/foss-api test [collection]`: Runs headless automated API contract tests with assertions and response timing gates.
- `/api-test-offline mock`: Sets up an offline HTTP mock server for air-gapped local development.
- `/git-api sync`: Exports Postman/OpenAPI specs into version-controlled Bru files.

---

## 📝 Declarative `.bru` Specification Format
```bru
meta {
  name: GetUserProfile
  type: http
  seq: 1
}

get {
  url: {{baseUrl}}/api/v1/users/:id
  body: none
  auth: bearer
}

auth:bearer {
  token: {{jwtToken}}
}

assert {
  res.status: eq 200
  res.body.id: isDefined
  res.responseTime: lte 250
}
```

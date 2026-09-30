---
name: secure-distributed-storage
description: >-
  Zero-knowledge encrypted cloud disk and resilient gRPC streaming protocol engine powered by MangoDisk and Sonora. Secures agent files, backups, and distributed data pipelines.
---

# 🔒 Secure Distributed Storage & Resilient Transport (MangoDisk + Sonora)

Use this skill when managing sensitive agent artifacts, configuring encrypted distributed file storage, auditing cloud disk access controls, or designing high-throughput gRPC-Web transport pipelines.

## Architecture

```mermaid
flowchart LR
    subgraph DataPlane ["1. Agent Artifacts & Backups"]
        ART["Skills, DBs, Transcripts, Research Artifacts"]
    end

    subgraph MangoDiskSecurity ["2. MangoDisk Zero-Knowledge Encryption (harry0703/MangoDisk)"]
        ART --> ENC["AES-256-GCM Client-Side Encryption"]
        ENC --> RBAC["Role-Based Access Control (RBAC) & Audit Logs"]
        RBAC --> DISK["Encrypted Distributed Disk Storage Pods"]
    end

    subgraph SonoraTransport ["3. Sonora gRPC-Web Streaming (sonoramac/Sonora)"]
        DISK --> STR["Bi-directional Resilient gRPC-Web Stream"]
        STR --> CLOUD["Synchronized Cloud Replicas (GDrive / OneDrive / S3)"]
    end
```

## Key Capabilities
1. **MangoDisk Encrypted Storage Engine**: End-to-end client-side encryption ensuring zero-knowledge privacy for AI training files and proprietary codebases.
2. **Access Control & Security Auditing**: Automated vulnerability scans against storage endpoints, permission leaks, and unauthenticated file exposures.
3. **Sonora Streaming Transport**: Ultra-low latency binary serialization over gRPC-Web, enabling fast cross-machine skill synchronization.

## How to Use
`Store and encrypt [file/directory] via MangoDisk security protocol with Sonora streaming replication.`

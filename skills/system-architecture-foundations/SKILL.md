---
name: system-architecture-foundations
description: >-
  Enterprise distributed systems architecture, high-scale backend design, low-level systems engineering (from Build Your Own X), and high-performance algorithms inspired by System Design Primer and TheAlgorithms.
---

# 🏗️ System Architecture & Distributed Foundations (System Design Primer + Build Your Own X Fusion)

Use this skill when designing scalable distributed systems, microservices architectures, low-latency caching layers, distributed databases, or implementing low-level protocols from scratch (databases, key-value stores, event brokers).

## Architectural Patterns & Trade-offs

```mermaid
flowchart TD
    subgraph ClientLayer ["1. Ingress & Edge"]
        C["Clients (Web / Mobile / IoT)"] --> CDN["CDN / Anycast Edge"]
        CDN --> LB["Layer 4/7 Load Balancers (HAProxy, Nginx)"]
        LB --> API["API Gateway (Rate Limiting, Auth, Routing)"]
    end

    subgraph ServiceLayer ["2. Microservices & Distributed Logic"]
        API --> S1["Stateless Services (App Nodes)"]
        S1 --> AS["Async Event Queue (Kafka / RabbitMQ)"]
        AS --> W["Background Worker Cluster"]
    end

    subgraph StorageLayer ["3. Storage & Distributed Caching"]
        S1 --> CA["Distributed Cache (Redis Cluster / Memcached)"]
        S1 --> DB["Sharded Database (Postgres / Spanner / DynamoDB)"]
        DB --> READ["Read Replicas (Consistent Hashing)"]
    end
```

## Core Architectural Pillars
1. **Scalability & Partitioning**: Consistent hashing, horizontal database sharding, partition keys, read/write splitting.
2. **Resilience & Fault Tolerance**: Circuit breakers, exponential backoff with jitter, leader election (Raft/Paxos), idempotent APIs.
3. **Data Consistency Models**: ACID vs BASE, event-driven eventual consistency, Saga pattern for distributed transactions.
4. **Low-Level Protocol Implementation**: Deep knowledge of implementing socket networking, binary wire protocols, write-ahead logs (WAL), and LSM-tree / B-tree storage engines.

## How to Use
`Design high-scale distributed system architecture for [system/service] handling [target QPS/scale] with high availability and partition tolerance.`

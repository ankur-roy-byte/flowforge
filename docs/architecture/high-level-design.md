# FlowForge High-Level Design

FlowForge is a stateless FastAPI API backed by PostgreSQL for metadata, Redis for broker and pub/sub duties, and Celery workers for durable task execution.

## Components

- API service: exposes REST and WebSocket endpoints, authenticates users, validates requests, and delegates business operations to services.
- PostgreSQL: stores users, versioned DAG definitions, schedules, runs, task runs, and append-only logs.
- Redis: acts as Celery broker/result backend and later as the pub/sub transport for live run events.
- Celery worker pool: executes task operators outside the API process.
- Celery Beat: periodically triggers scheduler polling.

## Runtime Flow

1. A user registers, logs in, and receives JWT tokens.
2. The user publishes a DAG definition.
3. FlowForge validates task references, operator types, and acyclic topology.
4. A manual or scheduled trigger creates a DagRun and TaskRuns.
5. Root TaskRuns are enqueued to Celery.
6. Workers update TaskRun state and publish events.
7. The executor service observes completion and enqueues newly ready tasks.
8. WebSocket clients receive state and log events without polling.

## Operational Principles

- API nodes are stateless and horizontally scalable.
- Execution is state-driven, not memory-driven.
- At-least-once execution semantics are handled with idempotency keys and database constraints.
- DAG versions are immutable; edits create a new version.


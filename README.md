# FlowForge

FlowForge is a distributed DAG orchestration engine built with FastAPI, PostgreSQL, Redis, and Celery. It is designed as a production-style learning project: every phase adds real backend patterns that matter in interviews and in industrial Python services.

## Documentation

- [Project context and recovery notes](docs/PROJECT_CONTEXT.md)
- [High-level design](docs/architecture/high-level-design.md)
- [Low-level design](docs/architecture/low-level-design.md)
- [Phase 0 notes](docs/phases/phase-0.md)

## Phase 0 Status

Implemented:

- Full repository structure.
- FastAPI app factory.
- `/health` endpoint.
- `/metrics` endpoint.
- Pydantic settings via `.env`.
- `structlog` configuration.
- Async SQLAlchemy session scaffolding.
- Celery app scaffolding.
- Docker Compose services: `api`, `worker`, `beat`, `db`, `redis`.
- Alembic async migration environment.
- First unit test for health.

## Quick Start

```bash
cd flowforge
cp .env.example .env
python -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

On Windows with the Python launcher, use `py -3.10 -m venv .venv` or newer.

Open:

- API docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`
- Metrics: `http://localhost:8000/metrics`

With Docker:

```bash
cd flowforge
make up
```

## Developer Commands

```bash
make test
make lint
make format
make migrate
make api
make worker
make beat
```

## Phase Plan

1. Phase 0: Scaffolding.
2. Phase 1: Auth and users.
3. Phase 2: DAG persistence and validation.
4. Phase 3: Manual run execution.
5. Phase 4: Real-time WebSocket updates.
6. Phase 5: Scheduling.
7. Phase 6: Retries, timeouts, cancellation.
8. Phase 7: Observability.
9. Phase 8: LLM extension.
10. Phase 9: Hardening.

## Interview Talking Points

1. Why async? Most orchestrator work is I/O: database calls, HTTP calls, Redis pub/sub, and WebSockets. FastAPI's async model lets a small API fleet handle many concurrent connections efficiently.
2. Why Celery for execution, not asyncio tasks? Celery gives worker isolation, retries, hard timeouts, horizontal scaling, and durability across API restarts.
3. How do you prevent duplicate runs? DagRun idempotency keys are enforced with a database unique constraint.
4. How do you guarantee correct execution order? Kahn's topological sort plus a state-driven executor only enqueue a task when every upstream task has succeeded.
5. How do you detect cycles? DFS with three-color marking catches cycles when the DAG is published.
6. How do WebSocket clients stay in sync without polling? Redis pub/sub channels per run feed a WebSocket manager that fans out state changes.
7. How is this testable? Pure algorithms are unit tested without infrastructure; integration tests use real PostgreSQL and Redis.

## Context Recovery

This project intentionally stores working context in [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md). If chat context is lost, continue from that file and the phase notes instead of guessing from memory.

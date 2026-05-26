# FlowForge Project Context

Last updated: 2026-05-26

This file is the durable handoff point for FlowForge. If chat context is lost, read this file first, then inspect the repository before continuing.

## Mission

Build FlowForge, a production-grade distributed DAG orchestration engine using FastAPI, SQLAlchemy async, PostgreSQL, Redis, Celery, WebSockets, and Pydantic v2.

The project is intentionally educational: the code should teach modern Python backend patterns that are useful in interviews and production systems.

## Non-Negotiable Constraints

- Keep all source for this project inside `flowforge/`.
- Use repository, service, route layering. Route handlers should not contain orchestration business logic.
- Use async I/O in FastAPI paths and services. Avoid blocking calls inside async functions.
- Use SQLAlchemy 2.0 typed declarative models with async sessions.
- Keep the API service stateless. Long-running work belongs in Celery workers.
- Validate DAG topology before persistence or execution.
- Add explicit tests as each phase lands.
- Update this context file and the phase notes after every major phase.

## Current Phase Status

Phase 0 is implemented:

- Full directory skeleton exists.
- FastAPI app factory exists in `app/main.py`.
- `/health` returns structured service metadata.
- `/metrics` exposes Prometheus metrics bytes.
- Config loads through `pydantic-settings`.
- Structured logging is configured with `structlog`.
- Docker Compose includes `api`, `worker`, `beat`, `db`, and `redis`.
- Alembic async environment is scaffolded.
- Worker and operator packages are scaffolded for later phases.
- Built-in operator modules are imported from `app.workers.operators`, so `OPERATOR_REGISTRY` is populated when the package is imported.
- WebSocket routes are wired into the app shell; concrete `/ws/runs/{run_id}` behavior lands in Phase 4.
- README links high-level and low-level docs.
- `docs/implementation-checklist.md` tracks the spec-to-repo audit and remaining phase work.
- CI workflow skeleton exists in `.github/workflows/ci.yml`.
- Core dependency pins were checked against PyPI on 2026-05-26.
- `redis` is pinned to `6.4.0` because Celery/Kombu's Redis extra currently requires `redis<6.5`.
- Local `.venv` dependency install succeeds.
- Verification passes locally: `ruff check .`, `black --check .`, `mypy app`, and `pytest`.
- Syntax verification passed with `.venv\Scripts\python -m compileall app tests`.
- Docker Compose was not validated locally because Docker is not installed on this machine.

## Next Phase

Phase 1: Auth and users.

Implement:

- SQLAlchemy `User` model.
- User schemas.
- Password hashing with `passlib[bcrypt]`.
- JWT access and refresh tokens with `python-jose`.
- `/api/v1/auth/register`, `/login`, `/refresh`.
- `get_current_user` dependency.
- Unit and integration tests.

## External Input Still Expected

The user mentioned they will provide one more file. When it arrives, read it and reconcile it with this context before making further implementation choices.

## Continuation Checklist

1. Read `README.md`, `docs/architecture/high-level-design.md`, and `docs/architecture/low-level-design.md`.
2. Run `rg --files` from `flowforge/` to verify current files.
3. Run `python -m compileall app tests` after edits.
4. Install dev dependencies in a virtual environment before running pytest locally.
5. Prefer small, phase-focused changes with tests.
6. Update this file with the new phase status.

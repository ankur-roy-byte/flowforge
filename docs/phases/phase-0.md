# Phase 0 - Scaffolding

## New Files

Phase 0 created the project skeleton, app factory, config, logging, Docker setup, test harness, and durable docs.

Key files:

- `app/main.py`
- `app/core/config.py`
- `app/core/logging.py`
- `app/core/exceptions.py`
- `app/db/session.py`
- `app/workers/celery_app.py`
- `docker-compose.yml`
- `pyproject.toml`
- `README.md`
- `docs/PROJECT_CONTEXT.md`

## Commands

```bash
cd flowforge
cp .env.example .env
make up
```

```bash
cd flowforge
python -m compileall app tests
pytest tests/unit/test_health.py
```

## Verification

- Passed: `py -3.10 -m compileall app tests`
- Not run locally: `pytest tests/unit/test_health.py`, because pytest is not installed for the available Python interpreters.
- Not run locally: `docker compose config --quiet`, because Docker is not installed.

## What We Just Learned

Phase 0 establishes the boundary lines of a production backend: app factory, typed settings, structured logs, database session lifecycle, worker process configuration, and Dockerized dependencies. Even before business logic exists, the project is shaped so API code, data access, services, and workers can grow independently.

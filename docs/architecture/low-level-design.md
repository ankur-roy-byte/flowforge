# FlowForge Low-Level Design

This document tracks module-level responsibilities. It will become more concrete as each phase lands.

## API Layer

- `app/main.py`: FastAPI app factory, health endpoint, metrics endpoint, exception registration.
- `app/api/deps.py`: shared dependencies, including async database session and later current-user resolution.
- `app/api/v1/router.py`: aggregates v1 endpoint routers.
- `app/api/v1/endpoints/*`: thin HTTP adapters that validate input and call services.

## Core Layer

- `app/core/config.py`: typed settings using `pydantic-settings`.
- `app/core/logging.py`: `structlog` setup, later correlation ID binding.
- `app/core/exceptions.py`: domain exception types and JSON error handlers.
- `app/core/security.py`: planned for Phase 1 JWT and password utilities.

## Data Layer

- `app/db/base.py`: SQLAlchemy declarative base.
- `app/db/session.py`: async engine and `async_sessionmaker`.
- `app/models/*`: SQLAlchemy models by aggregate.
- `app/repositories/*`: query and persistence methods. Services depend on repositories, not raw route-level SQL.

## Service Layer

- `dag_parser.py`: parse YAML/Python DAGs, validate topology, verify operators.
- `topology.py`: cycle detection and Kahn execution layering.
- `executor_service.py`: state-driven scheduling of TaskRuns as upstreams complete.
- `scheduler_service.py`: cron and interval next-run calculation.
- `event_bus.py`: Redis publish/subscribe abstraction.
- `ws_manager.py`: WebSocket fan-out registry.
- `llm_service.py`: only module allowed to import an LLM SDK.

## Worker Layer

- `workers/celery_app.py`: Celery configuration.
- `workers/tasks.py`: Celery task entry points.
- `workers/operators/base.py`: operator registry and execution protocol.
- `workers/operators/*_op.py`: concrete operators.

## Testing Layers

- Unit tests cover pure algorithms and state transitions.
- Integration tests cover database, Redis, API routes, Celery behavior, and WebSockets.


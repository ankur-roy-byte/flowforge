# FlowForge Implementation Checklist

Last audited: 2026-05-26

This checklist maps the project prompt to the current repository. It is intentionally durable so work can resume even if chat context is lost.

## Phase 0 - Scaffolding

Status: complete.

- [x] Repository structure exists under `flowforge/`.
- [x] FastAPI app factory exists in `app/main.py`.
- [x] `/health` endpoint exists.
- [x] `/metrics` endpoint exists.
- [x] API v1 router is wired under `/api/v1`.
- [x] WebSocket router package is wired into the app shell.
- [x] `pydantic-settings` config loads `.env`.
- [x] Async SQLAlchemy engine and `async_sessionmaker` are scaffolded.
- [x] Alembic async environment exists.
- [x] Celery app, worker entry points, and beat schedule scaffold exist.
- [x] Built-in operator registry pattern exists and imports built-in operators.
- [x] Docker Compose defines `api`, `worker`, `beat`, `db`, and `redis`.
- [x] Compose services load `.env`; `.env.example` is the template.
- [x] `Makefile` includes `up`, `test`, `migrate`, and `lint`.
- [x] `pyproject.toml` configures ruff, black, mypy, pytest, and coverage.
- [x] README links high-level and low-level docs.
- [x] Persistent context file exists at `docs/PROJECT_CONTEXT.md`.
- [x] CI skeleton exists.
- [x] Local checks pass: ruff, black, mypy, pytest.

## Phase 1 - Auth And Users

Status: pending.

- [ ] Implement SQLAlchemy `User` model with UUID primary key and timestamps.
- [ ] Add first Alembic migration.
- [ ] Implement user repository methods.
- [ ] Implement Pydantic user request and response schemas.
- [ ] Implement password hashing in `app/core/security.py`.
- [ ] Implement JWT access and refresh token helpers.
- [ ] Add `/api/v1/auth/register`.
- [ ] Add `/api/v1/auth/login`.
- [ ] Add `/api/v1/auth/refresh`.
- [ ] Add `get_current_user` dependency.
- [ ] Add auth unit tests.
- [ ] Add auth integration tests.

## Testing And CI

Status: partially complete.

- [x] GitHub Actions workflow runs compile, lint, format, type-check, and tests.
- [x] PostgreSQL and Redis service containers are available in CI for upcoming integration tests.
- [ ] Enforce coverage threshold in CI once service and worker implementations are non-placeholder.

## Phase 2 - DAG Persistence

Status: pending.

- [ ] Implement `DAG`, `Task`, and `Schedule` ORM models.
- [ ] Add JSONB and text-array PostgreSQL columns.
- [ ] Add unique constraints and indexes.
- [ ] Implement DAG and task Pydantic schemas using Pydantic v2 validators.
- [ ] Implement YAML DAG parser.
- [ ] Implement missing-upstream validation.
- [ ] Implement unknown-operator validation.
- [ ] Implement DFS three-color cycle detection.
- [ ] Implement Kahn topological layering.
- [ ] Implement DAG repository and service methods.
- [ ] Add `/api/v1/dags` create/list/latest/version/graph/update/delete endpoints.
- [ ] Add unit tests for parser and topology.
- [ ] Add DAG API integration tests.

## Phase 3 - Manual Run Execution

Status: pending.

- [ ] Implement `DagRun`, `TaskRun`, and `LogEntry` ORM models.
- [ ] Implement task lifecycle finite state machine.
- [ ] Implement run repository and executor service.
- [ ] Implement `BashOperator` execution.
- [ ] Implement `HTTPOperator` execution.
- [ ] Implement Celery `run_task_run`.
- [ ] Implement manual run trigger endpoint.
- [ ] Implement idempotency-key behavior.
- [ ] Implement ready-task enqueue after task completion.
- [ ] Add end-to-end integration test for a three-task linear DAG.

## Phase 4 - Real-Time Updates

Status: pending.

- [ ] Implement Redis event bus publish/subscribe abstraction.
- [ ] Implement WebSocket connection manager with one subscriber per active run channel.
- [ ] Add `/ws/runs/{run_id}` endpoint.
- [ ] Publish task state changes and log events.
- [ ] Add WebSocket tests.
- [ ] Add manual `wscat` README instructions.

## Phase 5 - Scheduling

Status: pending.

- [ ] Implement schedule repository and service.
- [ ] Implement cron and interval next-run calculation.
- [ ] Implement Celery Beat scheduler poll task every 30 seconds.
- [ ] Implement schedule create/update/delete endpoints.
- [ ] Add `freezegun` tests.

## Phase 6 - Retries, Timeouts, Cancellation

Status: pending.

- [ ] Implement retry policy on `TaskRun`.
- [ ] Implement retry transitions through the FSM.
- [ ] Configure Celery soft and hard time limits.
- [ ] Implement cancellation endpoint behavior.
- [ ] Revoke pending Celery tasks on cancellation.
- [ ] Add tests for retry exhaustion and cancellation.

## Phase 7 - Observability

Status: pending.

- [ ] Add correlation ID middleware.
- [ ] Propagate trace IDs through Celery task headers.
- [ ] Add Prometheus counters for task runs by status.
- [ ] Add structured access logs.
- [ ] Add tests for trace ID propagation where practical.

## Phase 8 - LLM Extension

Status: pending.

- [ ] Define abstract `LLMClient`.
- [ ] Keep provider SDK imports inside `app/services/llm_service.py`.
- [ ] Implement `/api/v1/ai/generate-dag`.
- [ ] Build prompt from `OPERATOR_REGISTRY` config schemas.
- [ ] Validate generated YAML through the DAG parser.
- [ ] Retry invalid LLM outputs up to two rounds.
- [ ] Implement optional SSE streaming.
- [ ] Implement `/api/v1/ai/explain-failure`.
- [ ] Add tests with mocked LLM client.

## Phase 9 - Hardening

Status: pending.

- [ ] Add CORS middleware from settings.
- [ ] Add security headers middleware.
- [ ] Add rate limiting with `slowapi`.
- [ ] Implement refresh-token rotation.
- [ ] Add OpenAPI request/response examples.
- [ ] Ensure Docker images run as non-root users.
- [ ] Add production deployment notes.

## Stretch Goals

Status: blocked until Phase 9 is complete.

- [ ] Web UI for DAG graph and live run status.
- [ ] Sensor operators.
- [ ] XCom-style task output sharing.
- [ ] Per-DAG SLA breach alerts.
- [ ] Multi-tenancy with workspaces.
- [ ] Replay from task.

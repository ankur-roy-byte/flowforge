COMPOSE ?= docker compose
PYTHON ?= python

.PHONY: up down test lint format migrate revision worker beat api logs clean

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down --remove-orphans

test:
	pytest

lint:
	ruff check .
	black --check .
	mypy app

format:
	ruff check . --fix
	black .

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate -m "$(message)"

api:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

worker:
	celery -A app.workers.celery_app:celery_app worker --loglevel=INFO

beat:
	celery -A app.workers.celery_app:celery_app beat --loglevel=INFO

logs:
	$(COMPOSE) logs -f

clean:
	$(PYTHON) -m compileall app tests


from app.workers.celery_app import celery_app


@celery_app.task(name="flowforge.healthcheck")  # type: ignore[misc]
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@celery_app.task(name="flowforge.run_task_run")  # type: ignore[misc]
def run_task_run(task_run_id: str) -> dict[str, str]:
    raise NotImplementedError(f"TaskRun execution is implemented in Phase 3: {task_run_id}")

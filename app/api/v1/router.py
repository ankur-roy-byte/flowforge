from fastapi import APIRouter

from app.api.v1.endpoints import ai, auth, dags, runs, schedules, tasks

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(dags.router, prefix="/dags", tags=["dags"])
api_router.include_router(runs.router, tags=["runs"])
api_router.include_router(tasks.router, tags=["task-runs"])
api_router.include_router(schedules.router, prefix="/schedules", tags=["schedules"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])

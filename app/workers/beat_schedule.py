from app.workers.celery_app import celery_app

celery_app.conf.beat_schedule = {
    "flowforge-healthcheck-every-minute": {
        "task": "flowforge.healthcheck",
        "schedule": 60.0,
    }
}


from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from starlette.responses import Response

from app.api.v1.router import api_router
from app.core.config import Settings, get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging, get_logger
from app.schemas.health import HealthResponse
from app.websockets.routes import router as websocket_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings: Settings = app.state.settings
    configure_logging(settings.log_level)
    logger = get_logger(__name__)
    logger.info("flowforge_starting", app_env=settings.app_env)
    yield
    logger.info("flowforge_stopping", app_env=settings.app_env)


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings.log_level)

    app = FastAPI(
        title=resolved_settings.app_name,
        version=resolved_settings.app_version,
        description="Distributed DAG orchestration engine built with FastAPI.",
        lifespan=lifespan,
        openapi_url=f"{resolved_settings.api_v1_prefix}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.state.settings = resolved_settings

    register_exception_handlers(app)
    app.include_router(api_router, prefix=resolved_settings.api_v1_prefix)
    app.include_router(websocket_router)

    @app.get(
        "/health",
        response_model=HealthResponse,
        response_model_exclude_none=True,
        tags=["system"],
        summary="Check API process health",
    )
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            service=resolved_settings.app_name,
            version=resolved_settings.app_version,
            environment=resolved_settings.app_env,
        )

    @app.get(
        "/metrics",
        include_in_schema=False,
    )
    async def metrics() -> Response:
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

    return app


app = create_app()

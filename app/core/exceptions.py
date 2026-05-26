from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class FlowForgeError(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
    code = "flowforge_error"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundError(FlowForgeError):
    status_code = status.HTTP_404_NOT_FOUND
    code = "not_found"


class ConflictError(FlowForgeError):
    status_code = status.HTTP_409_CONFLICT
    code = "conflict"


class ValidationError(FlowForgeError):
    status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
    code = "validation_error"


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(FlowForgeError)
    async def flowforge_error_handler(
        request: Request,
        exc: FlowForgeError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                    "path": str(request.url.path),
                }
            },
        )

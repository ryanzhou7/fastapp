from fastapi import FastAPI

from rz_fastapp.web.api.health_check import router as health_router
from rz_fastapp.web.api.lifespan import lifespan_setup
from rz_fastapp.web.api.table import router as table_router


def get_app() -> FastAPI:
    """Get FastAPI application.

    This is the main constructor of an application.
    :return: application.
    """
    app = FastAPI(
        lifespan=lifespan_setup,
        title="fastapp",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
    )
    app.include_router(health_router)
    app.include_router(table_router)
    return app

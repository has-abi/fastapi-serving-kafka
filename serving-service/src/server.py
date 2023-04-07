from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src import settings
from src.api.serving_api import serving_router
from src.containers import Container


def server() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME, docs_url=f"{settings.API_PREFIX}/docs")
    app.include_router(serving_router, prefix=settings.API_PREFIX)
    container = Container()
    app.container = container
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

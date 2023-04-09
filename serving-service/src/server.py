from fastapi import FastAPI
from src.api.serving_api import serving_router
from src.config import Settings, get_settings
from src.containers import Container
from src.producer.kafka_producer import create_topic
from starlette.middleware.cors import CORSMiddleware


def server(settings: Settings = get_settings()) -> FastAPI:
    app = FastAPI(title=settings.app_name, docs_url=f"{settings.api_prefix}/docs")

    @app.on_event("startup")
    async def create_kafaka_topic():
        await create_topic()

    app.include_router(serving_router, prefix=settings.api_prefix)
    container = Container()
    app.container = container
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

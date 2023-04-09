import threading

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, FastAPI

from src.config import get_settings
from src.consumer.kafka_consumer import KafkaConsumer
from src.containers import Container


def server(settings=get_settings()) -> FastAPI:
    app = FastAPI(title=settings.app_name, docs_url=f"{settings.api_prefix}/docs")

    @app.on_event("startup")
    @inject
    async def start_consumer(
        kafka_consumer: KafkaConsumer = Depends(Provide[Container.kafka_consumer]),
    ):
        kafka_thread = threading.Thread(target=kafka_consumer.start_kafka_consumer)
        kafka_thread.start()

    container = Container()
    app.container = container

    return app

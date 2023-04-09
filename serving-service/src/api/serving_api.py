from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, BackgroundTasks, Depends
from src.containers import Container
from src.producer.kafka_producer import produce_event
from src.schemas import EntitiesResponse, TextQuery
from src.services.serving_service import ServingService

serving_router = APIRouter()


@serving_router.post("/entities", response_model=EntitiesResponse)
@inject
async def extract_entities(
    text_query: TextQuery,
    background_tasks: BackgroundTasks,
    serving_service: ServingService = Depends(Provide[Container.serving_service]),
):
    prediction = serving_service.extract_entities(text_query.text)
    background_tasks.add_task(produce_event, prediction)
    return prediction

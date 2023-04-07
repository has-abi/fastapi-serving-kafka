from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.containers import Container
from src.schemas import EntitiesResponse, TextQuery
from src.services.serving_service import ServingService

serving_router = APIRouter()


@serving_router.post("/entities", response_model=EntitiesResponse)
@inject
def extract_entities(
    text_query: TextQuery,
    serving_service: ServingService = Depends(Provide[Container.serving_service]),
):
    return serving_service.extract_entities(text_query.text)

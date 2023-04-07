from dependency_injector import containers, providers

from src.services.serving_service import ServingService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.api.serving_api"])
    serving_service = providers.Factory(ServingService)

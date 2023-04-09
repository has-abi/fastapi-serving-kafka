from dependency_injector import containers, providers
from pymongo import MongoClient

from src.config import get_settings
from src.consumer.kafka_consumer import KafkaConsumer
from src.repository.prediction_repository import PredictionRepository

settings = get_settings()


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.server"])
    mongo_client = providers.Singleton(MongoClient, settings.mongodb_uri)
    prediction_repository = providers.Singleton(
        PredictionRepository, client=mongo_client
    )
    kafka_consumer = providers.Singleton(
        KafkaConsumer,
        bootstrap_servers=settings.kafka_bootstrap_servers,
        topic_name=settings.kafka_topic_name,
        prediction_repository=prediction_repository,
    )

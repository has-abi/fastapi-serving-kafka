from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "serving-service"
    api_prefix: str = "/api/serving"
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_name: str = "ner.predictions"
    kafka_topic_partitions: int = 1
    kafka_topic_replication_factor: int = 1


@lru_cache()
def get_settings():
    return Settings()

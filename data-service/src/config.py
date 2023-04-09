from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "data-service"
    api_prefix: str = "/api/data"
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_name: str = "ner.predictions"
    mongodb_uri: str


@lru_cache()
def get_settings():
    return Settings()

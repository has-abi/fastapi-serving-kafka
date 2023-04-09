# pylint: disable=no-name-in-module
from datetime import datetime

from pydantic import BaseModel


class Entity(BaseModel):
    label: str
    text: str


class Prediction(BaseModel):
    text: str
    created_at: datetime
    entities: list[Entity]

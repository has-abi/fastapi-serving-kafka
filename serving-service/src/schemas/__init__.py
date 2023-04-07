# pylint: disable=no-name-in-module
from pydantic import BaseModel


class TextQuery(BaseModel):
    text: str


class Entity(BaseModel):
    label: str
    text: str


class EntitiesResponse(BaseModel):
    text: str
    entities: list[Entity]

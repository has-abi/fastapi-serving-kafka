from typing import Tuple

from spacy.tokens import Span

from src.schemas import EntitiesResponse, Entity


def spacy_entities_to_entities_response(
    spacy_entities: Tuple[Span], text: str
) -> EntitiesResponse:
    entities = [Entity(label=ent.label_, text=ent.text) for ent in spacy_entities]
    return EntitiesResponse(text=text, entities=entities)

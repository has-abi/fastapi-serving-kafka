import spacy
from spacy.language import Language

from src import logger
from src.mapers.spacy_mappers import spacy_entities_to_entities_response
from src.schemas import EntitiesResponse

SPACY_PIPELINE = "en_core_web_sm"


class ServingService:
    spacy_model: Language = None

    @classmethod
    def load_spacy_model(cls) -> Language:
        if cls.spacy_model is None:
            logger.info("Loading NLP pipline=%s", SPACY_PIPELINE)
            cls.spacy_model = spacy.load(SPACY_PIPELINE)
        return cls.spacy_model

    def extract_entities(self, text: str) -> EntitiesResponse:
        nlp = self.load_spacy_model()
        # pylint: disable=not-callable
        doc = nlp(text)
        return spacy_entities_to_entities_response(doc.ents, text)

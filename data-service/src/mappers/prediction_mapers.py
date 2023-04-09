from datetime import datetime

from src.schemas import Entity, Prediction


def json_msg_to_prediction(json_msg):
    entities = [
        Entity(text=ent["text"], label=ent["label"]) for ent in json_msg["entities"]
    ]
    return Prediction(
        text=json_msg["text"], entities=entities, created_at=datetime.today()
    )

from pymongo import MongoClient

from src.schemas import Prediction


class PredictionRepository:
    def __init__(self, client: MongoClient) -> None:
        self.client = client
        self.db = self.client["predictionsdb"]
        self.predictions = self.db["predictions"]

    def save_prediction(self, prediction: Prediction):
        self.predictions.insert_one(prediction.dict())

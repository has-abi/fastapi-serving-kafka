import asyncio
import json

from confluent_kafka import Consumer

from src import logger
from src.mappers.prediction_mapers import json_msg_to_prediction
from src.repository.prediction_repository import PredictionRepository


class KafkaConsumer:
    def __init__(
        self,
        bootstrap_servers: str,
        topic_name: str,
        prediction_repository: PredictionRepository,
    ) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.topic_name = topic_name
        self.prediction_repository = prediction_repository
        self.config = {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": "dataservice",
            "auto.offset.reset": "earliest",
        }
        self.consumer = Consumer(self.config)
        logger.info(
            "Subscribing to %s kafka topic using config=%s",
            self.topic_name,
            str(self.config),
        )
        self.consumer.subscribe([self.topic_name])

    def consume_and_save_topic_predictions(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logger.error("Consumer error: %s", msg.error())
                continue
            json_msg = json.loads(msg.value().decode("utf-8"))
            logger.debug("Received message: %s", {str(json_msg)})
            prediction = json_msg_to_prediction(json_msg)
            self.prediction_repository.save_prediction(prediction)

    def start_kafka_consumer(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.consume_and_save_topic_predictions())

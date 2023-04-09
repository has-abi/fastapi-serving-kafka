from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic
from src import logger
from src.config import get_settings
from src.schemas import EntitiesResponse

settings = get_settings()

print(settings.kafka_bootstrap_servers)


async def create_topic():
    admin_client = AdminClient({"bootstrap.servers": settings.kafka_bootstrap_servers})
    new_topic = NewTopic(
        topic=settings.kafka_topic_name,
        num_partitions=settings.kafka_topic_partitions,
        replication_factor=settings.kafka_topic_replication_factor,
    )
    future_created = admin_client.create_topics([new_topic])
    for topic, future in future_created.items():
        try:
            future.result()
            logger.info("Topic %s created", topic)
        # pylint: disable=broad-exception-caught
        except Exception as ex:
            logger.error("Failed to create topic %s error= %s", topic, str(ex))


def delivery_report(err, msg):
    if err is not None:
        logger.error("Message delivery failed: %s", str(err))
    else:
        logger.debug("Message delivered to %s [%s]", msg.topic(), str(msg.partition()))


async def produce_event(data: EntitiesResponse):
    json_data = data.json()
    producer = Producer({"bootstrap.servers": settings.kafka_bootstrap_servers})
    producer.poll(0)
    producer.produce(
        settings.kafka_topic_name, json_data.encode("utf-8"), callback=delivery_report
    )
    producer.flush()

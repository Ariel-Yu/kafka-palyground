from kafka_playground.infrastructure.producers.avro_producer import AvroProducer
from kafka_playground.infrastructure.producers.producer import Producer
from kafka_playground.settings import kafka_broker, schema_registry_broker


def create_avro_producer(schema: str):
    config = {
        "bootstrap.servers": kafka_broker,
        "schema.registry.url": schema_registry_broker,
        "default.topic.config": {"acks": 1},
    }

    return AvroProducer(config, schema)


def create_producer():
    config = {
        "bootstrap.servers": kafka_broker,
        "default.topic.config": {"acks": 1},
    }

    return Producer(config)

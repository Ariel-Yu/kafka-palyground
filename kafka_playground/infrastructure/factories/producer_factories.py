from typing import Optional

from kafka_playground.infrastructure.producers.avro_producer import AvroProducer
from kafka_playground.infrastructure.producers.producer import Producer
from kafka_playground.settings import kafka_broker, schema_registry_broker


def create_producer():
    config = {
        "bootstrap.servers": kafka_broker,
        "default.topic.config": {"acks": 1},
    }

    return Producer(config)


def create_avro_producer(value_schema: str, key_schema: Optional[str] = None):
    config = {
        "bootstrap.servers": kafka_broker,
        "schema.registry.url": schema_registry_broker,
        "default.topic.config": {"acks": 1},
    }

    return AvroProducer(config=config, value_schema=value_schema, key_schema=key_schema)

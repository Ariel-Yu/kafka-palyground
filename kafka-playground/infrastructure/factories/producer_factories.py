from project_kafka.infrastructure.producers.avro_producer import AvroProducer
from project_kafka.infrastructure.producers.producer import Producer


def create_avro_producer(schema: str):
    # TODO: extract config to settings?
    config = {
        "bootstrap.servers": "kafka:29092",
        "schema.registry.url": "schema-registry:8081",
        "default.topic.config": {"acks": 1},
    }

    return AvroProducer(config, schema)


def create_producer():
    # TODO: extract config to settings?
    config = {
        "bootstrap.servers": "kafka:29092",
        "default.topic.config": {"acks": 1},
    }

    return Producer(config)

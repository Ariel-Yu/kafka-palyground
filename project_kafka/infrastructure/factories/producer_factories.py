from project_kafka.infrastructure.producers.avro_producer import AvroProducer


class AvroProducerFactory:
    def create_avro_producer(self, schema: str):
        # TODO: extract config to settings?
        config = {
            "bootstrap.servers": "confluent-kafka:9092",
            "schema.registry.url": "schema-registry:8081",
            "default.topic.config": {"acks": 1},
        }

        return AvroProducer(config, schema)

import json

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer as ConfluentAvroProducer

_POLL_TIMEOUT_SECONDS = 0
_FLUSH_TIMEOUT_SECONDS = 60


class AvroProducer:
    def __init__(self, config: dict, schema: str):
        schema = avro.load(schema)
        self._producer = ConfluentAvroProducer(config, default_value_schema=schema)

    def produce(self, topic: str, value: str):
        self._producer.produce(topic=topic, value=json.loads(value))
        self._producer.poll(_POLL_TIMEOUT_SECONDS)

    def flush(self):
        self._producer.flush(_FLUSH_TIMEOUT_SECONDS)

import json
from typing import Optional

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer as ConfluentAvroProducer

_POLL_TIMEOUT_SECONDS = 0
_FLUSH_TIMEOUT_SECONDS = 60


class AvroProducer:
    def __init__(self, config: dict, value_schema: str, key_schema: Optional[str] = None):
        schema = avro.load(value_schema)
        self._producer = ConfluentAvroProducer(config, default_value_schema=schema, default_key_schema=key_schema)

    def produce(self, topic: str, value: str, key: Optional[str] = None):
        self._producer.produce(topic=topic, value=json.loads(value), key=key)
        self._producer.poll(_POLL_TIMEOUT_SECONDS)

    def flush(self):
        self._producer.flush(_FLUSH_TIMEOUT_SECONDS)

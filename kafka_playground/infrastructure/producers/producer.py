from typing import Optional

from confluent_kafka.cimpl import Producer as ConfluentProducer

from kafka_playground.domain.interfaces.producer_interface import ProducerInterface

_POLL_TIMEOUT_SECONDS = 0
_FLUSH_TIMEOUT_SECONDS = 60


class Producer(ProducerInterface):
    def __init__(self, config: dict):
        self._producer = ConfluentProducer(config)

    def produce(self, topic: str, value: str, key: Optional[str] = None):
        self._producer.produce(topic=topic, value=value, key=key)
        self._producer.poll(_POLL_TIMEOUT_SECONDS)

    def flush(self):
        self._producer.flush(_FLUSH_TIMEOUT_SECONDS)

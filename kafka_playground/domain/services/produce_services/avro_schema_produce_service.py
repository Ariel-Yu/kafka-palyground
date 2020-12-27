import json
import random
from datetime import datetime

from kafka_playground.domain.interfaces.producer_interface import ProducerInterface


class AvroSchemaProduceService:
    def __init__(self, producer: ProducerInterface):
        self.producer = producer

    def produce(self, topic: str, with_key: bool = False):
        messages = []
        for i in range(2):
            now = str(datetime.now())
            messages.append(self._get_message(now))

        for msg in messages:
            value = json.dumps(msg)
            for j in range(5):
                print(f"-> Produce message: {msg}")
                if with_key:
                    self.producer.produce(topic=topic, value=value, key=msg["OrderId"])
                else:
                    self.producer.produce(topic=topic, value=value)

        self.producer.flush()

    @staticmethod
    def _get_message(now: str):
        order_id = random.randrange(0, 1000000)
        return {
            "OrderId": order_id,
            "OrderDate": now,
        }

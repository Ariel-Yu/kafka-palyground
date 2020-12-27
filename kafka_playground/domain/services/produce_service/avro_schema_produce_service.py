import json
import random
from datetime import datetime

from kafka_playground.domain.interfaces.producer_interface import ProducerInterface


class AvroSchemaProduceService:
    def __init__(self, producer: ProducerInterface):
        self.producer = producer

    def produce(self, topic: str):
        for i in range(10):
            now = str(datetime.now())
            msg = self._get_message(now)

            print(f"-> Produce message: {msg}")
            self.producer.produce(topic, value=json.dumps(msg))

        self.producer.flush()

    @staticmethod
    def _get_message(now: str):
        order_id = random.randrange(0, 1000000)
        return {
            "OrderId": order_id,
            "OrderDate": now,
        }

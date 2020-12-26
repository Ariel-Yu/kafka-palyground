from datetime import datetime


class KeyPartitionProduceService:
    def __init__(self, producer):
        self.producer = producer

    def produce(self, topic: str):
        for i in range(10):
            now = datetime.now()
            msg = str(now)
            timestamp = datetime.timestamp(now)
            key = str(timestamp)[-1]

            print(f"-> Produce message: {msg}, key: {key}")
            self.producer.produce(topic, value=msg, key=key)

        self.producer.flush()

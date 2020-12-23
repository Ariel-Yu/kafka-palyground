from datetime import datetime


class MultiConsumerGroupsProduceService:
    def __init__(self, producer):
        self.producer = producer

    def produce(self, topic: str):
        for i in range(10):
            msg = str(datetime.now())
            print(f"-> Produce message: {msg}")
            self.producer.produce(topic, value=msg)

        self.producer.flush()

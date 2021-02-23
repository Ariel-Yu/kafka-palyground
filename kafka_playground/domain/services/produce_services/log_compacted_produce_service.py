from kafka_playground.domain.interfaces.producer_interface import ProducerInterface


class LogCompactedProduceService:
    def __init__(self, producer: ProducerInterface):
        self.producer = producer

    def produce(self, topic: str, key: str, value: str):
        print(f"-> Produce message with key: {key} and value: {value}")
        self.producer.produce(topic, value=value, key=key)

        self.producer.flush()

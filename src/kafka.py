from datetime import datetime

import confluent_kafka


class Config():
    def __init__(self):
        bootstrap_servers = 'confluent-kafka:9092'
        self.topic = 'confluent-kafka-topic'
        self.producer_conf = {
            'bootstrap.servers': bootstrap_servers,
            # 'broker.version.fallback': '0.9.0.0',
            # 'api.version.request': False
        }
        self.consumer_conf_1 = {
            'bootstrap.servers': bootstrap_servers,
            'broker.version.fallback': '0.9.0.0',
            'api.version.request': False,
            'group.id': 'consumer_group_1',
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }
        }
        self.consumer_conf_2 = {
            'bootstrap.servers': bootstrap_servers,
            'broker.version.fallback': '0.9.0.0',
            'api.version.request': False,
            'group.id': 'consumer_group_2',
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }
        }


def produce(config: Config):
    producer = confluent_kafka.Producer(**config.producer_conf)
    msg = datetime.now()

    producer.produce(config.topic, value=msg)


def consume_consumer_group_1(config: Config):
    consumer = confluent_kafka.Consumer(**config.consumer_conf_1)
    consumer.subscribe([config.topic])

    print(consumer.poll(1))


def consume_consumer_group_2(config: Config):
    consumer = confluent_kafka.Consumer(**config.consumer_conf_2)
    consumer.subscribe([config.topic])

    print(consumer.poll(1))

from confluent_kafka import Consumer

from kafka_playground.settings import kafka_broker


def create_consumer(consumer_group_name: str):
    config = {
        'bootstrap.servers': kafka_broker,
        'group.id': consumer_group_name,
        'max.poll.interval.ms': 6000,
        'session.timeout.ms': 6000,
        'default.topic.config': {
            'auto.offset.reset': 'earliest'
        }
    }

    return Consumer(config)

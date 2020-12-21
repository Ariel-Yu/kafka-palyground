from confluent_kafka import Consumer


def create_consumer(consumer_group_name: str):
    config = {
        'bootstrap.servers': "kafka:29092",
        'group.id': consumer_group_name,
        'max.poll.interval.ms': 6000,
        'session.timeout.ms': 6000,
        'default.topic.config': {
            'auto.offset.reset': 'earliest'
        }
    }

    return Consumer(config)

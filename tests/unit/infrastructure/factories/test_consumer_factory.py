from confluent_kafka.cimpl import Consumer

from kafka_playground.infrastructure.factories.consumer_factories import create_consumer


def test_create_consumer():
    assert isinstance(create_consumer("consumer_group_name"), Consumer)

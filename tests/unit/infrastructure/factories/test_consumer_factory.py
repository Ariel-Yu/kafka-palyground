from confluent_kafka.cimpl import Consumer

from project_kafka.infrastructure.factories.consumer_factory import create_consumer


def test_create_consumer():
    assert isinstance(create_consumer("consumer_group_name"), Consumer)

from confluent_kafka.avro import AvroConsumer
from confluent_kafka.cimpl import Consumer

from kafka_playground.infrastructure.factories.consumer_factories import create_consumer, create_avro_consumer


def test_create_consumer():
    assert isinstance(create_consumer("consumer_group_name"), Consumer)


def test_create_avro_consumer(mocker):
    mocker.patch("kafka_playground.infrastructure.factories.consumer_factories.AvroConsumer.__init__", return_value=None)
    assert isinstance(create_avro_consumer("consumer_group_name"), AvroConsumer)

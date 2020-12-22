from project_kafka.infrastructure.factories.producer_factories import create_avro_producer, create_producer
from project_kafka.infrastructure.producers.avro_producer import AvroProducer
from project_kafka.infrastructure.producers.producer import Producer


def test_create_avro_producer(mocker):
    mocker.patch("kafka-playground.infrastructure.factories.producer_factories.AvroProducer.__init__", return_value=None)
    assert isinstance(create_avro_producer("schema"), AvroProducer)


def test_create_producer(mocker):
    mocker.patch("kafka-playground.infrastructure.factories.producer_factories.Producer.__init__", return_value=None)
    assert isinstance(create_producer(), Producer)
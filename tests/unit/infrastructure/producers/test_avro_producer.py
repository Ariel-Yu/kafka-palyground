from project_kafka.infrastructure.producers.avro_producer import AvroProducer


class TestAvroProducer:
    def test_produce(self, mocker):
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.avro.load")

        producer = mocker.Mock()
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.ConfluentAvroProducer", return_value=producer)

        avro_producer = AvroProducer({"config": "config"}, "schema")
        avro_producer.produce("topic", '{"value": "value"}')

        assert producer.produce.called
        assert producer.poll.called

    def test_flush(self, mocker):
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.avro.load")

        producer = mocker.Mock()
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.ConfluentAvroProducer", return_value=producer)

        avro_producer = AvroProducer({"config": "config"}, "schema")
        avro_producer.flush()

        assert producer.flush.called

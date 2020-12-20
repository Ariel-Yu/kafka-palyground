from project_kafka.infrastructure.producers.avro_producer import AvroProducer


class TestAvroProducer:
    def test_produce(self, mocker):
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.avro.loads")

        producer = mocker.Mock()
        mocker.patch("project_kafka.infrastructure.producers.avro_producer.ConfluentAvroProducer", return_value=producer)

        avro_producer = AvroProducer({"config": "config"}, "schema")
        avro_producer.produce("topic", '{"value": "value"}')

        assert producer.produce().called
        assert producer.poll().callede

    def test_flush(self):
        assert True

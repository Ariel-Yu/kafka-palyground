from project_kafka.infrastructure.producers.producer import Producer


class TestProducer:
    def test_produce(self, mocker):
        mocked_producer = mocker.Mock()
        mocker.patch("project_kafka.infrastructure.producers.producer.ConfluentProducer", return_value=mocked_producer)

        producer = Producer({"config": "config"})
        producer.produce("topic", '{"value": "value"}')

        assert mocked_producer.produce.called
        assert mocked_producer.poll.called

    def test_flush(self, mocker):
        mocked_producer = mocker.Mock()
        mocker.patch("project_kafka.infrastructure.producers.producer.ConfluentProducer", return_value=mocked_producer)

        producer = Producer({"config": "config"})
        producer.flush()

        assert mocked_producer.flush.called

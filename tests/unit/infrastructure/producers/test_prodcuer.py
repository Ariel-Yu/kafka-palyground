from kafka_playground.infrastructure.producers.producer import Producer


class TestProducer:
    def test_produce_without_key(self, mocker):
        mocked_producer = mocker.Mock()
        mocker.patch("kafka_playground.infrastructure.producers.producer.ConfluentProducer", return_value=mocked_producer)

        producer = Producer({"config": "config"})
        producer.produce("topic", '{"value": "value"}')

        assert mocked_producer.produce.called
        assert mocked_producer.produce.call_args == mocker.call(topic='topic', value='{"value": "value"}', key=None)
        assert mocked_producer.poll.called

    def test_produce_with_key(self, mocker):
        mocked_producer = mocker.Mock()
        mocker.patch("kafka_playground.infrastructure.producers.producer.ConfluentProducer", return_value=mocked_producer)

        producer = Producer({"config": "config"})
        producer.produce("topic", '{"value": "value"}', "key")

        assert mocked_producer.produce.called
        assert mocked_producer.produce.call_args == mocker.call(topic='topic', value='{"value": "value"}', key="key")
        assert mocked_producer.poll.called

    def test_flush(self, mocker):
        mocked_producer = mocker.Mock()
        mocker.patch("kafka_playground.infrastructure.producers.producer.ConfluentProducer", return_value=mocked_producer)

        producer = Producer({"config": "config"})
        producer.flush()

        assert mocked_producer.flush.called

from pytest import raises

from kafka_playground.domain.services.consume_service import ConsumeService


class TestConsumeService:
    def test_consume(self, mocker):
        consumer = mocker.Mock()
        # TODO: is this kind of a hack to test while True: loop?
        consumer.poll.side_effect = Exception()
        service = ConsumeService(consumer)

        with raises(Exception):
            service.consume("topic")

        assert consumer.subscribe.called

from pytest import raises

from project_kafka.domain.services.multi_consumer_groups_consume_service import MultiConsumerGroupsConsumeService


class TestMultiConsumerGroupsConsumeService:
    def test_consume(self, mocker):
        consumer = mocker.Mock()
        # TODO: is this kind of a hack to test while True: loop?
        consumer.poll.side_effect = Exception()
        service = MultiConsumerGroupsConsumeService(consumer)

        with raises(Exception):
            service.consume("topic")

        assert consumer.subscribe.called

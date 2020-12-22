from kafka_playground.domain.services.multi_consumer_groups_produce_service import MultiConsumerGroupsProduceService


class TestMultiConsumerGroupsProduceService:
    def test_produce(self, mocker):
        producer = mocker.Mock()
        service = MultiConsumerGroupsProduceService(producer)

        service.produce("topic")
        assert producer.produce.call_args.args[0] == "topic"

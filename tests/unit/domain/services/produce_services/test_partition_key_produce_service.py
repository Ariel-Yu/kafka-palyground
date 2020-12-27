from kafka_playground.domain.services.produce_services.partition_key_produce_service import PartitionKeyProduceService


class TestPartitionKeyProduceService:
    def test_produce(self, mocker):
        producer = mocker.Mock()
        service = PartitionKeyProduceService(producer)

        service.produce("topic")
        assert producer.produce.call_args.args[0] == "topic"
        assert producer.produce.call_count == 10
        assert producer.flush.call_count == 1

from kafka_playground.domain.services.produce_service.key_partition_produce_service import KeyPartitionProduceService


class TestKeyPartitionProduceService:
    def test_produce(self, mocker):
        producer = mocker.Mock()
        service = KeyPartitionProduceService(producer)

        service.produce("topic")
        assert producer.produce.call_args.args[0] == "topic"
        assert producer.produce.call_count == 10
        assert producer.flush.call_count == 1

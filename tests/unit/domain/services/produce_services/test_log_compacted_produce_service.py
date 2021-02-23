from kafka_playground.domain.services.produce_services.log_compacted_produce_service import LogCompactedProduceService


class TestLogCompactedProduceService:
    def test_produce(self, mocker):
        producer = mocker.Mock()
        service = LogCompactedProduceService(producer)

        service.produce("topic", "key", "value")
        assert producer.produce.call_args.args[0] == "topic"
        assert producer.produce.call_args.kwargs["key"] == "key"
        assert producer.produce.call_args.kwargs["value"] == "value"
        assert producer.flush.called

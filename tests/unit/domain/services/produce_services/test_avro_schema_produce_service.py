from kafka_playground.domain.services.produce_services.avro_schema_produce_service import AvroSchemaProduceService


class TestAvroSchemaProduceService:
    def test_produce_with_key(self, mocker):
        mocker.patch(
            "kafka_playground.domain.services.produce_services.avro_schema_produce_service.random.randrange",
            side_effect=[1, 2]
        )
        producer = mocker.Mock()
        service = AvroSchemaProduceService(producer)

        service.produce("topic", True)

        assert producer.produce.call_args.kwargs["topic"] == "topic"
        assert producer.produce.call_args.kwargs.get("key")
        assert producer.produce.call_count == 10
        assert producer.flush.call_count == 1

    def test_produce_without_key(self, mocker):
        producer = mocker.Mock()
        service = AvroSchemaProduceService(producer)

        service.produce("topic")

        assert producer.produce.call_args.kwargs["topic"] == "topic"
        assert not producer.produce.call_args.kwargs.get("key")
        assert producer.produce.call_count == 10
        assert producer.flush.call_count == 1

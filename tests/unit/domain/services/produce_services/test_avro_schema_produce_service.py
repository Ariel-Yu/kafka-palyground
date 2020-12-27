from kafka_playground.domain.services.produce_services.avro_schema_produce_service import AvroSchemaProduceService


class TestAvroSchemaProduceService:
    def test_produce(self, mocker):
        producer = mocker.Mock()
        service = AvroSchemaProduceService(producer)

        service.produce("topic")

        assert producer.produce.call_args.args[0] == "topic"
        assert producer.produce.call_count == 10
        assert producer.flush.call_count == 1

import click

from kafka_playground.domain.services.consume_service import ConsumeService
from kafka_playground.domain.services.produce_services.avro_schema_produce_service import AvroSchemaProduceService
from kafka_playground.domain.services.produce_services.partition_key_produce_service import PartitionKeyProduceService
from kafka_playground.domain.services.produce_services.multi_consumer_groups_produce_service import MultiConsumerGroupsProduceService
from kafka_playground.infrastructure.factories.consumer_factories import create_consumer, create_avro_consumer
from kafka_playground.infrastructure.factories.producer_factories import create_producer, create_avro_producer


@click.group()
def cli():
    """
    All funcs decorated with `@cli.command()` will be a part of the `cli` group.
    """
    pass


@cli.command()
@click.argument('topic')
def multi_consumer_groups__produce_messages(topic: str):
    producer = create_producer()
    service = MultiConsumerGroupsProduceService(producer)

    click.echo("##### Start to produce messages")
    service.produce(topic)


@cli.command()
@click.argument('topic')
@click.argument('consumer_group_name')
def multi_consumer_groups__consume_messages(topic: str, consumer_group_name: str):
    consumer = create_consumer(consumer_group_name)
    service = ConsumeService(consumer)

    click.echo(f"##### Start to consume message from {consumer_group_name}")
    service.consume(topic)


@cli.command()
@click.argument('topic')
def partition_key__produce_messages(topic: str):
    producer = create_producer()
    service = PartitionKeyProduceService(producer)

    click.echo("##### Start to produce messages")
    service.produce(topic)


@cli.command()
@click.argument('topic')
@click.argument('consumer_group_name')
def partition_key__consume_messages(topic: str, consumer_group_name: str):
    consumer = create_consumer(consumer_group_name)
    service = ConsumeService(consumer)

    click.echo(f"##### Start to consume message from {consumer_group_name}")
    service.consume(topic)


@cli.command()
@click.argument('topic')
def avro_schema__produce_messages(topic: str):
    value_schema = "/app/kafka_playground/infrastructure/schemas/value_schemas/order_value_schema.avsc"
    producer = create_avro_producer(value_schema=value_schema)
    service = AvroSchemaProduceService(producer)

    click.echo("##### Start to produce messages")
    service.produce(topic)


@cli.command()
@click.argument('topic')
def avro_schema_with_key__produce_messages(topic: str):
    value_schema = "/app/kafka_playground/infrastructure/schemas/value_schemas/order_value_schema.avsc"
    key_schema = "/app/kafka_playground/infrastructure/schemas/key_schemas/order_key_schema.avsc"
    producer = create_avro_producer(value_schema=value_schema, key_schema=key_schema)
    service = AvroSchemaProduceService(producer)

    click.echo("##### Start to produce messages")
    service.produce(topic, with_key=True)


@cli.command()
@click.argument('topic')
@click.argument('consumer_group_name')
def avro_schema__consume_messages(topic: str, consumer_group_name: str):
    consumer = create_avro_consumer(consumer_group_name)
    service = ConsumeService(consumer)

    click.echo(f"##### Start to consume message from {consumer_group_name}")
    service.consume(topic)


if __name__ == "__main__":
    cli()

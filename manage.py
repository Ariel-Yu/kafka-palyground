import click

from kafka_playground.domain.services.consume_service import ConsumeService
from kafka_playground.domain.services.produce_service.key_partition_produce_service import KeyPartitionProduceService
from kafka_playground.domain.services.produce_service.multi_consumer_groups_produce_service import MultiConsumerGroupsProduceService
from kafka_playground.infrastructure.factories.consumer_factory import create_consumer
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

    click.echo("##### Start to produce message")
    service.produce(topic)


@cli.command()
@click.argument('topic')
def partition_key__produce_messages(topic: str):
    producer = create_producer()
    service = KeyPartitionProduceService(producer)

    click.echo("##### Start to produce message")
    service.produce(topic)


@cli.command()
@click.argument('topic')
def avro_schema__produce_messages(topic: str):
    value_schema = "kafka_playground/infrastructure/schemas/value_schemas/order_value_schema.avsc"
    producer = create_avro_producer(value_schema)
    service = KeyPartitionProduceService(producer)

    click.echo("##### Start to produce message")
    service.produce(topic)


@cli.command()
@click.argument('topic')
@click.argument('consumer_group_name')
def consume_messages(topic: str, consumer_group_name: str):
    consumer = create_consumer(consumer_group_name)
    service = ConsumeService(consumer)

    click.echo(f"##### Start to consume message from {consumer_group_name}")
    service.consume(topic)


if __name__ == "__main__":
    cli()

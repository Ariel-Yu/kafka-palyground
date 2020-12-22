import click

from kafka_playground.domain.services.multi_consumer_groups_consume_service import MultiConsumerGroupsConsumeService
from kafka_playground.domain.services.multi_consumer_groups_produce_service import MultiConsumerGroupsProduceService
from kafka_playground.infrastructure.factories.consumer_factory import create_consumer
from kafka_playground.infrastructure.factories.producer_factories import create_producer


@click.group()
def cli():
    """
    All funcs decorated with `@cli.command()` will be a part of the `cli` group.
    """
    pass


@cli.command()
@click.argument('topic')
def multi_consumer_groups_produce(topic: str):
    producer = create_producer()
    service = MultiConsumerGroupsProduceService(producer)

    click.echo("##### Start to produce message")
    service.produce(topic)


@cli.command()
@click.argument('topic')
@click.argument('consumer_group_name')
def multi_consumer_groups_consume(topic: str, consumer_group_name: str):
    consumer = create_consumer(consumer_group_name)
    service = MultiConsumerGroupsConsumeService(consumer)

    click.echo(f"##### Start to consume message from {consumer_group_name}")
    service.consume(topic)


if __name__ == "__main__":
    cli()

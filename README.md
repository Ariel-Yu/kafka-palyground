# project-kafka

## Consumer Group

1. Spin up 2 containers running kafka and zookeeper:
```
docker-compose [--verbose] up --build
```

2. Produce messages: 
```
docker-compose run --rm test-kafka produce
```
- The message is a simple string of current datetime

3. Consume messages by providing the consumer group name: 
```
docker-comopse run --rm test-kafak consume <consumer_group_name>
```
- <consumer_group_name> can be given arbitrary 
- ex: docker-compose run --rm test-kafka consume consumer_group_1
- Each consumer group will consume **all** the messages from the defined topic `confluent-kafka-topic`
- If multiple instances are spinned up from the same consumer group, only **one** of the instances will consume messages from the defined topic

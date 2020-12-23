# kafka-playground
Playground for beginners new to Kafka

## Practice 1: Consumer group

1. Spin up kafka, zookeeper and schema registry:
```
docker-compose [--verbose] up [--build]
```

2. Produce messages: 
```
docker-compose run --rm services multi-consumer-groups-produce <topic_name>
```
- Please replace <topic_name> with any arbitrary string. ex: topic1
- ex: _docker-compose run --rm services multi-consumer-groups-produce topic1_ 
- The message is a simple string of current datetime

3. Consume messages by providing the consumer group name: 
```
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
```
- Please replace <topic_name> with the string given to the producer. ex: topic1
- Please replace <consumer_group_name> with any arbitrary string. ex: consumer_group_1
- ex: _docker-compose run --rm services multi-consumer-groups-consume topic1 consumer_group_1_

#### Learning
1. Each consumer group will consume **all** the messages from the topic. Consumers running under different consumer groups will not impact one another
1. If multiple consumers are running under the same consumer group and are consuming from the same topic, only **one** of the consumers will consume a message **at a time** from the topic
(Number of partition of the topic is _1_ in this practice)

## Practice 2: Partition without Key
We'll increase the number of partition in this practice without setting a key. Kafka will default to use **round robin** strategy to conduct messages partitioning

1. Access Kafka container:
```
docker ps [--format "table {{.ID}}\t{{.Names}}\t{{.Status}}"]
docker exec -it <container_id> /bin/bash
```

2. List out all the topics:
```
/usr/bin/kafka-topics --list --zookeeper zookeeper:2181
```
- _zookeeper:2181_ works because we have set up kafka with `"KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181"` in docker_compose.yml

3. Modify the number of partition of a topic
```
/usr/bin/kafka-topics --alter --zookeeper zookeeper:2181 --topic <topic> --partitions <number_of_partition>
```
- ex: _/usr/bin/kafka-topics --alter --zookeeper zookeeper:2181 --topic topic1 --partitions 3_
- ex result: _WARNING: If partitions are increased for a topic that has a key, the partition logic or ordering of the messages will be affected
Adding partitions succeeded!_

4. Produce messages and consume messages from 3 consumers under the same consumer group
```
docker-compose run --rm services multi-consumer-groups-produce <topic_name>
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
```
- <topic_name> and <consumer_group_name> should be all identical to test the parallelism provided by partition

#### Learning
1. Messages will be produced to different partitions by round robin strategy
1. Each partition will be consumed by only *one* consumer
1. Each consumer can consume more than one partition if the number of consumer is smaller than the number of partition
1. The consumers under the same consumer group will consume messages from different partitions at the same time

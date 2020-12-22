# kafka-playground
Playground for beginners new to Kafka. I personally wanted to test out lots of theories read and leart online and would like to practice by my own building and see the effects by my own eyes.

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
1. If multiple consumers are running under the same consumer group and are consuming from the same topic, only **one** of the consumers will consume a message at a time from the topic
(Topic for this practice is with default 1 partition)

## Practice 2: Partition and Key
Presume that kafka, zookeeper and schema registry are already spin up

1. Access Kafka container:
```
docker exec -t <container_id> /bin/bash
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
- Example output: _WARNING: If partitions are increased for a topic that has a key, the partition logic or ordering of the messages will be affected
Adding partitions succeeded!_

4. Produce messages and consume messages from 2 consumers under the same consumer group
```
docker-compose run --rm services multi-consumer-groups-produce <topic_name>
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
```

#### Learning
1. The 2 consumers under the same consumer group name will consume different messages at the same time from the topic
1. Each message will be consumed by only one consumer but both consumers can consume messages at the same time
 
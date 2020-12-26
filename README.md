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
docker-compose run --rm services consume <topic_name> <consumer_group_name>
```
- Please replace <topic_name> with the string given to the producer. ex: topic1
- Please replace <consumer_group_name> with any arbitrary string. ex: consumer_group_1
- ex: _docker-compose run --rm services multi-consumer-groups-consume topic1 consumer_group_1_

#### Learning
1. Each consumer group will consume **all** the messages from the topic. Consumers running under different consumer groups will not impact one another
1. If multiple consumers are running under the same consumer group and are consuming from the same topic, only **one** of the consumers will consume a message **at a time** from the topic
(Number of partition of the topic is _1_ in this practice)

## Practice 2: Partition without Key
We'll increase the number of partition in this practice without setting a key. Kafka will default to use **round robin** strategy to conduct messages partition

1. Access Kafka container:
```
docker ps [--format "table {{.ID}}\t{{.Names}}\t{{.Status}}"]
docker exec -it <container_id> /bin/bash
```

2. List out all the topics:
```
/usr/bin/kafka-topics --describe --zookeeper zookeeper:2181 [--topic <topic_name>]
/usr/bin/kafka-topics --list --zookeeper zookeeper:2181
```
- _zookeeper:2181_ works because we have set up kafka with `"KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181"` in docker_compose.yml

3. Increase number of partition of a topic
 
    i. Modify the number of partition of a created topic
    ```
    /usr/bin/kafka-topics --alter --zookeeper zookeeper:2181 --topic <topic_name> --partitions <number_of_partition>
    ```
    - ex: _/usr/bin/kafka-topics --alter --zookeeper zookeeper:2181 --topic topic1 --partitions 3_
    - ex result: _WARNING: If partitions are increased for a topic that has a key, the partition logic or ordering of the messages will be affected
    Adding partitions succeeded!_

    ii. Create a new topic with desired number of partition
    ```
    /usr/bin/kafka-topics --create --zookeeper zookeeper:2181 --topic <topic_name> --replication-factor 1 --partitions <number_of_partition>
    ```
    - ex: _/usr/bin/kafka-topics --create --zookeeper zookeeper:2181 --topic topic1 --replication-factor 1 --partitions 3_
    - ex result: _Created topic "topic1"._

4. Produce messages and consume messages from <number_of_partition> consumers under the same consumer group
```
docker-compose run --rm services multi-consumer-groups-produce <topic_name>
docker-compose run --rm services consume <topic_name> <consumer_group_name>
```
- <topic_name> and <consumer_group_name> should be all identical to test the parallelism provided by partition

#### Learning
1. Messages will be produced to different partitions by round robin strategy
1. Each partition will be consumed by only **one** consumer
1. Each consumer can consume more than one partition if the number of consumer is smaller than the number of partition. Some consumers may not consume any messages if the number of consumer is greater than the number of partition
1. The consumers under the same consumer group will consume messages from different partitions at the same time

## Practice 3: Partition with Key
We will increase the number of partition of a topic as well as assign a key with each message in this practice. Kafka will use the provided key to assign each message to a partition 

1. Requirements of the setup for this practice are exactly the same as Practice 2
2. Produce messages to the desired topic
```
docker-compose run --rm services key-partition-produce <topic_name>
```
- Please replace <topic_name> with the desired topic name. ex: topic1
- ex: _docker-compose run --rm services key-partition-produce topic1_ 
- The message is a simple string of current datetime
- The key is the last number of the current timestamp `str(datetime.timestamp(datetime.now()))[-1]`

3. Consume messages from the desired topic
```
docker-compose run --rm services consume <topic_name> <consumer_group_name>
```

### Learning
1. Messages with the same key will be always produced to the **same** partition
1. Messages with the same key will be always consumed by the **same** consumer

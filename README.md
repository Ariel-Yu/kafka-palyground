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
1. Each consumer group will consume **all** the messages from the topic that the consumer is consuming from. Consumers running under different consumer groups will not impact one another
1. If multiple consumers are running under the same consumer group and are consuming from the same topic, only **one** of the consumers will consume messages from the topic that the consumers are consuming from
(Topic for this practice is setup with only 1 partition)

# project-kafka

## Concept 1: Consumer group

1. Spin up kafka, zookeeper and schema registry:
```
docker-compose [--verbose] up [--build]
```

1. Produce messages: 
```
docker-compose run --rm services multi-consumer-groups-produce <topic_name>
```
- Please replace <topic_name> with any arbitrary string. ex: topic1
- _ex: docker-compose run --rm services multi-consumer-groups-produce topic1_ 
- The message is a simple string of current datetime

1. Consume messages by providing the consumer group name: 
```
docker-compose run --rm services multi-consumer-groups-consume <topic_name> <consumer_group_name>
```
- Please replace <topic_name> with the string given to the producer. ex: topic1
- Please replace <consumer_group_name> with any arbitrary string. ex: consumer_group_1
- _ex: docker-compose run --rm services multi-consumer-groups-consume topic1 consumer_group_1_
- Each consumer group will consume **all** the messages from the given topic
- If multiple instances are spin up from the same consumer group, only **one** of the instances will consume messages from the defined topic

from time import sleep


class MultiConsumerGroupsConsumeService:
    def __init__(self, consumer):
        self.consumer = consumer

    def consume(self, topic: str):
        self.consumer.subscribe([topic])
        while True:
            msg = self.consumer.poll(1)
            if not msg:
                print("x No message to consume")
                sleep(2)
                continue

            msg_object = {
                "value": msg.value(),
                "partition": msg.partition(),
                "topic": msg.topic(),
                "key": msg.key(),
                "offset": msg.offset()
            }
            print(f"v Consuming message: {str(msg_object)}")

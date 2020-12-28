from abc import ABC, abstractmethod
from typing import Optional


class ProducerInterface(ABC):
    @abstractmethod
    def produce(self, topic: str, value: str, key: Optional[str] = None):
        pass

    @abstractmethod
    def flush(self):
        pass

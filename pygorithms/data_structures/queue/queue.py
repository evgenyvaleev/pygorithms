from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

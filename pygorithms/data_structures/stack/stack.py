from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self, value):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

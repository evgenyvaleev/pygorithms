from .queue import Queue
from pygorithms.data_structures.linked_list import LinkedList


class LinkedListQueue(Queue):
    def __init__(self):
        self._items = LinkedList()

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if len(self) == 0:
            return None

        item = self._items.first
        self._items.delete(self._items.first)

        return item.value

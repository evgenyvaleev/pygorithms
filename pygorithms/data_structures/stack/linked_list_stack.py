from .stack import Stack
from pygorithms.data_structures.linked_list import LinkedList


class LinkedListStack(Stack):
    def __init__(self):
        self._items = LinkedList()

    def __len__(self):
        return len(self._items)

    def push(self, value):
        """O(1)."""
        self._items.prepend(value)

    def pop(self):
        """O(1)."""
        value = self._items.first.value
        self._items.delete(self._items.first)

        return value

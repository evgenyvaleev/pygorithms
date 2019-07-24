from .stack import Stack


class ListStack(Stack):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

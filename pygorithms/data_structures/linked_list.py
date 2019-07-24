class ListNode:
    """Node of a linked list. Contains a value and a link to the next node."""
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __repr__(self):
        return f'<{self.value}>'

    def __str__(self):
        return str(self.value)


class LinkedList:
    """A collection that provides fast inserts at first and last positions.

    Consists of nodes. Each node contains a link to the next one.
    Stores links to the first and the last nodes, so they can be accessed very fast - O(1), but
    random access is very slow, because we have to iterate through all the nodes until we find the required one - O(n).
    """
    def __init__(self):
        self._count = 0
        self.first = None
        self.last = None

    def __repr__(self):
        '[{}]'.format(', '.join(map(str, self)))

    def __len__(self):
        return self._count

    def __iter__(self):
        if self._count == 0:
            raise StopIteration

        node = self.first
        while node is not None:
            yield node
            node = node.next_item

    def __getitem__(self, key):
        return self.find_at(key)

    def prepend(self, value):
        """ Inserts an element at the beginning of the list.

        Since we store link to the first element, it takes O(1).
        """
        if self.first is not None:
            new = ListNode(value, self.first)
            self.first = new
        else:
            new = ListNode(value)
            self.first = new
            self.last = new

        self._count += 1

    def append(self, value):
        """ Inserts an element at the end of the list.

        Since we store link to the last element, it takes O(1).
        """
        new = ListNode(value)

        if self.last is not None:
            self.last.next_item = new
            self.last = new
        else:
            self.first = new
            self.last = new

        self._count += 1

    # O(n)
    # We have to iterate through the list to find the element preceding the new one
    def insert(self, target, value):
        """Inserts a new element before another.

        Because in a singly linked list elements store a link only to the next element,
        we have to iterate through the list to find the preceding element - O(n).
        """
        new = ListNode(value, target)

        if target == self.first:
            self.first = new
        else:
            for node in self:
                if node.next_item == target:
                    node.next_item = new
                    break

        self._count += 1

    def find(self, value):
        """Finds the first element with the specified value.

        O(n).
        """
        for node in self:
            if node.value == value:
                return node

        return None

    def find_last(self, value):
        """Finds the last element with the specified value.

        O(n).
        """
        res = None

        for node in self:
            if node.value == value:
                res = node

        return res

    def find_at(self, index):
        """Returns the element at the specified index.

        O(n).
        """
        if not isinstance(index, int):
            raise KeyError

        if index > len(self) - 1:
            raise KeyError

        for i, node in enumerate(self):
            if i == index:
                return node

    def delete(self, target):
        """Deletes an element from the list.

        Complexity is only linear when we are to delete the first element.
        In all the other cases it is O(n).
        """
        if self._count == 0:
            raise ValueError("Collection doesn't contain the specified element")

        if target == self.first:
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next_item
        elif target == self.last:
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                for node in self:
                    if node.next_item == self.last:
                        node.next_item = None
                        self.last = node
                        break
        else:
            found = False
            for node in self:
                if node.next_item == target:
                    node.next_item = target.next_item
                    found = True
                    break

            if not found:
                raise ValueError("Collection doesn't contain the specified element")

        self._count -= 1

    def clear(self):
        """Clears the list.

        O(1).
        """
        self.first = None
        self.last = None
        self._count = 0

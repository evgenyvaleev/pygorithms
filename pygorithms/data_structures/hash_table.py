from pygorithms.data_structures.linked_list import LinkedList


class HashTable:
    _empty = object()
    _initial_size = 10
    _max_load_factor = 0.7
    _resize_multiplier = 2

    def __init__(self, resizing=True):
        self._count = 0
        self._size = self._initial_size
        self._keys = [self._empty] * self._initial_size
        self._values = [self._empty] * self._initial_size
        self._is_resizing = resizing

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self._count

    def _hash(self, data):
        """Calculates hash of the data and returns index of the bucket to store it in."""
        return hash(data) % self._size

    def _load_factor(self):
        """Calculates current load factor."""
        return self._count / self._size

    def _resize(self):
        """Resizes underlying data structures."""
        keys = self._flatten(self._keys)
        values = self._flatten(self._values)
        count = self._count

        self._size *= self._resize_multiplier
        self._count = 0
        self._keys = [self._empty] * self._size
        self._values = [self._empty] * self._size

        for i in range(count):
            self.put(keys[i], values[i])

    def _flatten(self, items):
        flattened = []
        for item in items:
            if isinstance(item, LinkedList):
                flattened.append(self._flatten(item))
            else:
                flattened.append(item)

        return flattened

    def put(self, key, value):
        """Puts an item into the hash table.

        Time depends on whether there is a collision or not. Average time is O(1), but if there is a collision,
        the items with the same hash moves into a linked list - O(n). This is the worst case scenario.
        """
        key_hash = self._hash(key)

        if self._keys[key_hash] is self._empty:  # Bucket is empty, we can freely add the new item
            self._keys[key_hash] = key
            self._values[key_hash] = value
            self._count += 1
        elif self._keys[key_hash] == key:  # It's the same key, rewriting value
            self._values[key_hash] = value
        else:  # Collision
            if isinstance(self._keys[key_hash], LinkedList):  # Items in the bucket are already in a linked list
                for i, node in enumerate(self._keys[key_hash]):  # Rewriting if key already exists
                    if node.value == key:
                        self._values[key_hash][i].value = value
                        return

                self._keys[key_hash].append(key)
                self._values[key_hash].append(value)
            else:
                key_list = LinkedList()
                key_list.append(self._keys[key_hash])
                key_list.append(key)

                value_list = LinkedList()
                value_list.append(self._values[key_hash])
                value_list.append(value)

                self._keys[key_hash] = key_list
                self._values[key_hash] = value_list

            self._count += 1

        # Resizing if necessary
        if self._is_resizing and self._load_factor() > self._max_load_factor:
            self._resize()

    def get(self, key):
        """Retrieves the item with the specified key.

        It is O(1) if the item is stored in a bucket, and O(n) if it's in a linked list.
        """
        key_hash = self._hash(key)

        if self._keys[key_hash] is self._empty:  # Item with the given key doesn't exist
            raise KeyError
        # Items with this hash are contained in a linked list. We need to iterate through it to get the required
        # one. This is O(n).
        elif isinstance(self._keys[key_hash], LinkedList):
            for i, node in enumerate(self._keys[key_hash]):
                if node.value == key:
                    return self._values[key_hash][i].value

            raise KeyError
        else:
            return self._values[key_hash]

    # O(1) - average, O(n) - worst
    def delete(self, key):
        """Deletes the item with the specified key.

        It is O(1) if the item is stored in a bucket, and O(n) if it's in a linked list.
        """
        key_hash = self._hash(key)

        if self._keys[key_hash] is self._empty:
            raise KeyError
        elif isinstance(self._keys[key_hash], LinkedList):
            for i, node in enumerate(self._keys[key_hash]):
                if node.value == key:
                    self._keys[key_hash].delete(node)
                    node = self._values[key_hash][i]
                    self._values[key_hash].delete(node)

                    # If there is only one item left in the linked list, we can move it straight into the bucket
                    if len(self._keys[key_hash]) == 1:
                        self._keys[key_hash], self._values[key_hash] = (self._keys[key_hash].first.value,
                                                                        self._values[key_hash].first.value)

                    self._count -= 1
                    return

            raise KeyError
        else:
            self._keys[key_hash] = self._empty
            self._values[key_hash] = self._empty
            self._count -= 1

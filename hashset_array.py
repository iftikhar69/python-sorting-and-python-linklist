"""HashSet built on top of HashTableArray."""
from hashtable_array import HashTableArray


class HashSetArray:
    def __init__(self):
        self._ht = HashTableArray()

    def add(self, value):
        self._ht.put(value, True)

    def remove(self, value):
        return self._ht.remove(value)

    def contains(self, value):
        return self._ht.contains(value)

    def size(self):
        return self._ht.size()

    def __repr__(self):
        return f"HashSetArray({self._ht})"

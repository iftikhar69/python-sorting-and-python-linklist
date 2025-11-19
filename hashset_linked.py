"""HashSet built on top of HashTableLinked."""
from hashtable_linked import HashTableLinked


class HashSetLinked:
    def __init__(self):
        self._ht = HashTableLinked()

    def add(self, value):
        self._ht.put(value, True)

    def remove(self, value):
        return self._ht.remove(value)

    def contains(self, value):
        return self._ht.contains(value)

    def size(self):
        return self._ht.size()

    def __repr__(self):
        return f"HashSetLinked({self._ht})"

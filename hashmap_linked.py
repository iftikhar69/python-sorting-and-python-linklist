"""HashMap (key->value) using HashTableLinked directly."""
from hashtable_linked import HashTableLinked


class HashMapLinked:
    def __init__(self):
        self._ht = HashTableLinked()

    def put(self, key, value):
        self._ht.put(key, value)

    def get(self, key, default=None):
        return self._ht.get(key, default)

    def remove(self, key):
        return self._ht.remove(key)

    def contains(self, key):
        return self._ht.contains(key)

    def size(self):
        return self._ht.size()

    def __repr__(self):
        return f"HashMapLinked({self._ht})"

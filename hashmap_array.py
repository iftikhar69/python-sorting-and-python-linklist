"""HashMap (key->value) using HashTableArray directly.

This file exposes a small Map-like wrapper API (put/get/remove).
"""
from hashtable_array import HashTableArray


class HashMapArray:
    def __init__(self):
        self._ht = HashTableArray()

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
        return f"HashMapArray({self._ht})"

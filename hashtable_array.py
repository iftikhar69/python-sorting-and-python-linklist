"""Simple hash table using array-of-buckets (separate chaining with Python lists)."""

class HashTableArray:
    def __init__(self, capacity=16):
        self._cap = max(4, int(capacity))
        self._buckets = [[] for _ in range(self._cap)]
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % self._cap

    def put(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key, default=None):
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return default

    def remove(self, key):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key, None) is not None

    def size(self):
        return self._size

    def __repr__(self):
        pairs = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k!r}:{v!r}")
        return "HashTableArray({" + ", ".join(pairs) + "})"

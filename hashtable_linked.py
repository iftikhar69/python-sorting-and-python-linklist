"""Hash table using linked-list buckets (simple Node chains)."""

class NodeH:
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.next = nxt


class HashTableLinked:
    def __init__(self, capacity=16):
        self._cap = max(4, int(capacity))
        self._buckets = [None] * self._cap
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % self._cap

    def put(self, key, value):
        idx = self._bucket_index(key)
        head = self._buckets[idx]
        cur = head
        while cur:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next
        node = NodeH(key, value, head)
        self._buckets[idx] = node
        self._size += 1

    def get(self, key, default=None):
        idx = self._bucket_index(key)
        cur = self._buckets[idx]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return default

    def remove(self, key):
        idx = self._bucket_index(key)
        cur = self._buckets[idx]
        prev = None
        while cur:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    self._buckets[idx] = cur.next
                self._size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        return self.get(key, None) is not None

    def size(self):
        return self._size

    def __repr__(self):
        pairs = []
        for head in self._buckets:
            cur = head
            while cur:
                pairs.append(f"{cur.key!r}:{cur.value!r}")
                cur = cur.next
        return "HashTableLinked({" + ", ".join(pairs) + "})"

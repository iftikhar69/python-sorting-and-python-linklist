"""Array-backed queue using circular buffer semantics."""

class QueueArray:
    def __init__(self, capacity=16):
        self._cap = max(2, int(capacity))
        self._data = [None] * self._cap
        self._head = 0
        self._tail = 0
        self._size = 0

    def _grow(self):
        new_cap = self._cap * 2
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._cap]
        self._data = new_data
        self._cap = new_cap
        self._head = 0
        self._tail = self._size

    def enqueue(self, value):
        if self._size == self._cap:
            self._grow()
        self._data[self._tail] = value
        self._tail = (self._tail + 1) % self._cap
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        val = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        return val

    def peek(self):
        return None if self.is_empty() else self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __repr__(self):
        out = [str(self._data[(self._head + i) % self._cap]) for i in range(self._size)]
        return "QueueArray([" + ", ".join(out) + "])"

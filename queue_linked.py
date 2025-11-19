"""Linked-list-backed queue (singly linked, head/tail pointers)."""

class NodeQ:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, value):
        node = NodeQ(value)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return val

    def peek(self):
        return None if self.is_empty() else self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def __repr__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(repr(cur.value))
            cur = cur.next
        return "QueueLinked(front-> [" + ", ".join(vals) + "])"

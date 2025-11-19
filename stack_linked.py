"""Linked-list-backed stack implementation."""

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class StackLinked:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        node = Node(value, self.head)
        self.head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self.head.value
        self.head = self.head.next
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
        return "StackLinked(top-> [" + ", ".join(vals) + "])"

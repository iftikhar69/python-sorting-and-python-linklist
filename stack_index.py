"""Main index/menu to demo data structure implementations.

Menu structure follows the user's numbering and demonstrates both array
and linked-list implementations where requested.
"""
from stack_array import StackArray
from stack_linked import StackLinked
from queue_array import QueueArray
from queue_linked import QueueLinked
from hashtable_array import HashTableArray
from hashtable_linked import HashTableLinked
from hashset_array import HashSetArray
from hashset_linked import HashSetLinked
from hashmap_array import HashMapArray
from hashmap_linked import HashMapLinked


def demo_stack():
    print("--- Stack: Array implementation ---")
    sa = StackArray()
    sa.push(1)
    sa.push(2)
    sa.push(3)
    print(sa, "peek=", sa.peek())
    print("pop->", sa.pop())
    print(sa)

    print("--- Stack: Linked implementation ---")
    sl = StackLinked()
    sl.push('a')
    sl.push('b')
    sl.push('c')
    print(sl, "peek=", sl.peek())
    print("pop->", sl.pop())
    print(sl)


def demo_queue():
    print("--- Queue: Array implementation ---")
    qa = QueueArray(4)
    qa.enqueue(10)
    qa.enqueue(20)
    qa.enqueue(30)
    print(qa, "peek=", qa.peek())
    print("dequeue->", qa.dequeue())
    print(qa)

    print("--- Queue: Linked implementation ---")
    ql = QueueLinked()
    ql.enqueue('x')
    ql.enqueue('y')
    ql.enqueue('z')
    print(ql, "peek=", ql.peek())
    print("dequeue->", ql.dequeue())
    print(ql)


def demo_hashtable():
    print("--- Hash Table: Array (separate chaining) ---")
    ha = HashTableArray()
    ha.put('k1', 100)
    ha.put('k2', 200)
    print(ha, "get(k1)=", ha.get('k1'))
    ha.remove('k1')
    print(ha)

    print("--- Hash Table: Linked-bucket ---")
    hl = HashTableLinked()
    hl.put('a', 1)
    hl.put('b', 2)
    print(hl, "get(a)=", hl.get('a'))
    hl.remove('a')
    print(hl)


def demo_hashset():
    print("--- Hash Set: Array ---")
    sa = HashSetArray()
    sa.add(1)
    sa.add(2)
    sa.add(2)
    print(sa, "contains(2)=", sa.contains(2))
    sa.remove(1)
    print(sa)

    print("--- Hash Set: Linked ---")
    sl = HashSetLinked()
    sl.add('v')
    sl.add('w')
    print(sl, "contains('v')=", sl.contains('v'))


def demo_hashmap():
    print("--- Hash Map: Array ---")
    ma = HashMapArray()
    ma.put('one', 1)
    ma.put('two', 2)
    print(ma, "get(two)=", ma.get('two'))
    ma.remove('one')
    print(ma)

    print("--- Hash Map: Linked ---")
    ml = HashMapLinked()
    ml.put(10, 'ten')
    ml.put(20, 'twenty')
    print(ml, "get(10)=", ml.get(10))


def main_menu():
    print("\n=== Data Structures Demo Index ===")
    print("1. Stack (1 array, 2 linked list)")
    print("2. Queue (1 array, 2 linked list)")
    print("3. Hash Table (1 array, 2 linked list)")
    print("4. Hash Set (1 array, 2 linked list)")
    print("5. Hash Map (1 array, 2 linked list)")
    print("0. Exit")
    while True:
        choice = input("Choose an option: ").strip()
        if choice == '1':
            demo_stack()
        elif choice == '2':
            demo_queue()
        elif choice == '3':
            demo_hashtable()
        elif choice == '4':
            demo_hashset()
        elif choice == '5':
            demo_hashmap()
        elif choice == '0':
            print("Bye")
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main_menu()
# --------------------------------------------------------
# DATA STRUCTURES SECTION  (CODE FIRST)
# --------------------------------------------------------

# ----------------- STACK USING ARRAY --------------------
class StackArray:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            return "Stack Empty"
        return self.data.pop()

    def display(self):
        return self.data


# ---------------- STACK USING LINKED LIST ----------------
class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = StackNode(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return "Stack Empty"
        val = self.top.value
        self.top = self.top.next
        return val

    def display(self):
        elements = []
        cur = self.top
        while cur:
            elements.append(cur.value)
            cur = cur.next
        return elements


# ----------------- QUEUE USING ARRAY ---------------------
class QueueArray:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            return "Queue Empty"
        return self.data.pop(0)

    def display(self):
        return self.data


# -------------- QUEUE USING LINKED LIST ------------------
class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = QueueNode(value)
        if not self.front:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            return "Queue Empty"
        val = self.front.value
        self.front = self.front.next
        return val

    def display(self):
        elements = []
        cur = self.front
        while cur:
            elements.append(cur.value)
            cur = cur.next
        return elements


# ------------------- HASH TABLE (ARRAY) -------------------
class HashTableArray:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % self.size
        if key not in self.table[index]:
            self.table[index].append(key)

    def display(self):
        return self.table


# ---------------- HASH TABLE (LINKED LIST) ----------------
class HashNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTableLinkedList:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = key % self.size
        node = HashNode(key)

        if self.table[index] is None:
            self.table[index] = node
        else:
            cur = self.table[index]
            while cur.next:
                if cur.value == key:
                    return
                cur = cur.next
            cur.next = node

    def display(self):
        result = []
        for head in self.table:
            bucket = []
            cur = head
            while cur:
                bucket.append(cur.value)
                cur = cur.next
            result.append(bucket)
        return result


# --------------------------------------------------------
# MENU SECTION (AT THE END)
# --------------------------------------------------------

def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Stack")
    print("   1. Array")
    print("   2. Linked List")
    print("2. Queue")
    print("   1. Array")
    print("   2. Linked List")
    print("3. Hash Table")
    print("   1. Array")
    print("   2. Linked List")
    print("4. Hash Set")
    print("   1. Array")
    print("   2. Linked List")
    print("5. Hash Map")
    print("   1. Array")
    print("   2. Linked List")
    print("6. Exit")


def get_choice(txt):
    try:
        return int(input(txt))
    except ValueError:
        print("Enter a valid number.")
        return get_choice(txt)


def run_menu():

    while True:
        main_menu()

        choice1 = get_choice("Enter main choice: ")

        if choice1 == 6:
            print("Exiting...")
            break

        choice2 = get_choice("Enter sub-choice (1/2): ")

        # ---------------- STACK ----------------
        if choice1 == 1:
            if choice2 == 1:
                ds = StackArray()
            else:
                ds = StackLinkedList()

            while True:
                op = input("Push (p), Pop (o), Display (d), Exit (e): ").lower()
                if op == 'p':
                    ds.push(int(input("Enter value: ")))
                elif op == 'o':
                    print("Popped:", ds.pop())
                elif op == 'd':
                    print("Stack:", ds.display())
                else:
                    break

        # ---------------- QUEUE ----------------
        elif choice1 == 2:
            ds = QueueArray() if choice2 == 1 else QueueLinkedList()

            while True:
                op = input("Enqueue (e), Dequeue (d), Display (s), Exit (x): ").lower()
                if op == 'e':
                    ds.enqueue(int(input("Enter value: ")))
                elif op == 'd':
                    print("Dequeued:", ds.dequeue())
                elif op == 's':
                    print("Queue:", ds.display())
                else:
                    break

        # ------------- HASH TABLE / SET / MAP --------------
        elif choice1 in [3, 4, 5]:
            ds = HashTableArray() if choice2 == 1 else HashTableLinkedList()

            while True:
                op = input("Insert (i), Display (d), Exit (e): ").lower()
                if op == 'i':
                    ds.insert(int(input("Enter key: ")))
                elif op == 'd':
                    print("Table:", ds.display())
                else:
                    break


# Run Program
run_menu()

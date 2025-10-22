# Refence form "https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/"  //   Greeks for Greeks

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # used only in doubly-linked variants


# ===== Singly Linked List =====
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):  # add at end (existing behavior)
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def add_begin(self, value):  # add at beginning (new)
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete_begin(self):  # delete at beginning (new)
        if not self.head:
            return False
        self.head = self.head.next
        return True

    def search(self, value):
        cur = self.head
        pos = 1
        while cur:
            if cur.data == value:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def delete(self, value):
        cur = self.head
        prev = None
        while cur:
            if cur.data == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def length(self):
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        if not self.head:
            print("Singly Linked List: Empty (Length: 0)")
            return
        cur = self.head
        out = []
        while cur:
            out.append(str(cur.data))
            cur = cur.next
        print(f"Singly Linked List: Length = {self.length()} | Head -> " + " -> ".join(out) + " -> None")


# ===== Doubly Linked List =====
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def add_begin(self, value):  # add at beginning (new)
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def delete_begin(self):  # delete at beginning (new)
        if not self.head:
            return False
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        return True

    def search(self, value):
        cur = self.head
        pos = 1
        while cur:
            if cur.data == value:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def delete(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def length(self):
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        if not self.head:
            print("Doubly Linked List: Empty (Length: 0)")
            return
        cur = self.head
        out = []
        while cur:
            out.append(str(cur.data))
            cur = cur.next
        print(f"Doubly Linked List: Length = {self.length()} | Head <-> " + " <-> ".join(out) + " -> None")


# ===== Singly Circular Linked List =====
class SinglyCircularList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        node.next = self.head

    def add_begin(self, value):  # add at beginning (new)
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            return
        # find last
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = node
        node.next = self.head
        self.head = node

    def delete_begin(self):  # delete at beginning (new)
        if not self.head:
            return False
        if self.head.next == self.head:
            self.head = None
            return True
        # find last to update its next
        last = self.head
        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        last.next = self.head
        return True

    def search(self, value):
        if not self.head:
            return -1
        cur = self.head
        pos = 1
        while True:
            if cur.data == value:
                return pos
            cur = cur.next
            pos += 1
            if cur == self.head:
                break
        return -1

    def delete(self, value):
        if not self.head:
            return False
        cur = self.head
        prev = None
        while True:
            if cur.data == value:
                if prev:  # deleting non-head
                    prev.next = cur.next
                else:  # deleting head
                    # find last to update its next
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    if last == self.head:  # single node
                        self.head = None
                        return True
                    last.next = cur.next
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
            if cur == self.head:
                break
        return False

    def length(self):
        if not self.head:
            return 0
        cnt = 1
        cur = self.head
        while cur.next != self.head:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        if not self.head:
            print("Singly Circular List: Empty (Length: 0)")
            return
        cur = self.head
        out = []
        while True:
            out.append(str(cur.data))
            cur = cur.next
            if cur == self.head:
                break
        print(f"Singly Circular List: Length = {self.length()} | Head -> " + " -> ".join(out) + " -> (back to head)")


# ===== Doubly Circular Linked List =====
class DoublyCircularList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            node.prev = node
            return
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node

    def add_begin(self, value):  # add at beginning (new)
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            node.prev = node
            return
        last = self.head.prev
        last.next = node
        node.prev = last
        node.next = self.head
        self.head.prev = node
        self.head = node

    def delete_begin(self):  # delete at beginning (new)
        if not self.head:
            return False
        if self.head.next == self.head:  # single node
            self.head = None
            return True
        last = self.head.prev
        new_head = self.head.next
        last.next = new_head
        new_head.prev = last
        self.head = new_head
        return True

    def search(self, value):
        if not self.head:
            return -1
        cur = self.head
        pos = 1
        while True:
            if cur.data == value:
                return pos
            cur = cur.next
            pos += 1
            if cur == self.head:
                break
        return -1

    def delete(self, value):
        if not self.head:
            return False
        cur = self.head
        while True:
            if cur.data == value:
                if cur.next == cur:  # single node
                    self.head = None
                    return True
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                if cur == self.head:
                    self.head = cur.next
                return True
            cur = cur.next
            if cur == self.head:
                break
        return False

    def length(self):
        if not self.head:
            return 0
        cnt = 1
        cur = self.head
        while cur.next != self.head:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        if not self.head:
            print("Doubly Circular List: Empty (Length: 0)")
            return
        cur = self.head
        out = []
        while True:
            out.append(str(cur.data))
            cur = cur.next
            if cur == self.head:
                break
        print(f"Doubly Circular List: Length = {self.length()} | Head <-> " + " <-> ".join(out) + " -> (back to head)")


# ===== Submenu helper =====
def run_submenu(list_obj, list_name):
    while True:
        print(f"\n-- {list_name} MENU (Length: {list_obj.length()}) --")
        print("1. Addition")
        print("2. Search")
        print("3. Deletion")
        print("4. Show list")
        print("5. Back to main menu")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            print("Addition: 1) Add at end  2) Add at beginning")
            sub = input("Choose (1 or 2): ").strip()
            val = input("Enter value to add: ").strip()
            try:
                v = int(val)
            except ValueError:
                v = val
            if sub == '2':
                if hasattr(list_obj, 'add_begin'):
                    list_obj.add_begin(v)
                else:
                    list_obj.add(v)  # fallback
            else:
                list_obj.add(v)
            print("Added.")
            list_obj.display()
        elif choice == '2':
            val = input("Enter value to search: ").strip()
            try:
                v = int(val)
            except ValueError:
                v = val
            pos = list_obj.search(v)
            if pos == -1:
                print("Not found.")
            else:
                print(f"Found at position {pos}.")
        elif choice == '3':
            print("Deletion: 1) Delete by value  2) Delete at beginning")
            sub = input("Choose (1 or 2): ").strip()
            if sub == '2':
                if hasattr(list_obj, 'delete_begin'):
                    ok = list_obj.delete_begin()
                    print("Deleted first node." if ok else "List empty.")
                else:
                    print("Delete at beginning not supported for this list.")
            else:
                val = input("Enter value to delete: ").strip()
                try:
                    v = int(val)
                except ValueError:
                    v = val
                ok = list_obj.delete(v)
                print("Deleted." if ok else "Value not found.")
            list_obj.display()
        elif choice == '4':
            list_obj.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


# ===== MENU =====
def main():
    # persist lists across submenu visits
    singly = SinglyLinkedList()
    doubly = DoublyLinkedList()
    singly_circ = SinglyCircularList()
    doubly_circ = DoublyCircularList()

    while True:
        print("\n===== LINKED LIST MENU =====")
        print("1. Singly Linked List")
        print("2. Doubly Linked List")
        print("3. Singly Circular Linked List")
        print("4. Doubly Circular Linked List")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            run_submenu(singly, "Singly Linked List")
        elif choice == '2':
            run_submenu(doubly, "Doubly Linked List")
        elif choice == '3':
            run_submenu(singly_circ, "Singly Circular Linked List")
        elif choice == '4':
            run_submenu(doubly_circ, "Doubly Circular Linked List")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# ===== Run Program =====
if __name__ == "__main__":
    main()
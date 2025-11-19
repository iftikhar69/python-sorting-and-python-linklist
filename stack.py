class stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        if not self.is_empty():
             return self.stack.pop()
        else:
            return "Error: pop form empty stack"
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self[-1]
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("stack :",self.stack)

s = stack()
s.peek()
s.display()
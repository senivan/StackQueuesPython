class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev

class Stack:
    def __init__(self):
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.tail is None

    def push(self, item):
        if self.tail is None:
            self.tail = Node(item)
        else:
            self.tail = Node(item, self.tail)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.size -= 1
            item = self.tail.data
            self.tail = self.tail.prev
            return item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tail.data

    def len(self):
        return self.size
    

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def len(self):
        return self.stack1.len() + self.stack2.len()

    
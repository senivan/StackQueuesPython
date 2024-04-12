class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None or self.tail is None or self.size == 0
    
    def add(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    
    def get(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return temp.data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def len(self):
        return self.size
    

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def empty(self):
        return self.queue1.is_empty() and self.queue2.is_empty()
    
    def push(self, val):
        self.queue1.add(val)
        
    def pop(self):
        while self.queue1.len() > 1:
            self.queue2.add(self.queue1.get())
        temp = self.queue1.get()
        if not self.queue1.is_empty():
            self.queue2.add(self.queue1.get())
        while not self.queue2.is_empty():
            self.queue1.add(self.queue2.get())
        return temp
        
    def top(self):
        while self.queue1.len() > 1:
            self.queue2.add(self.queue1.get())
        temp = self.queue1.peek()
        if not self.queue1.is_empty():
            self.queue2.add(self.queue1.get())
        while not self.queue2.is_empty():
            self.queue1.add(self.queue2.get())
        return temp
        
    def size(self):
        return self.queue1.size + self.queue2.size
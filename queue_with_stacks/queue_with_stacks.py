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

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()        

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
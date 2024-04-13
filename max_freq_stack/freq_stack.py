from collections import deque

class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pop(self):
        if not self.head:
            return None
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return node

class FreqStack:
    def __init__(self):
        self.dll = DLL()
        self.freq = deque()

    def push(self, val):
        if not self.freq or self.freq[-1].val != val:
            self.freq.append(Node(val, 1))
        else:
            self.freq[-1].freq += 1
        self.dll.append(self.freq[-1])

    def pop(self):
        node = self.dll.pop()
        if node:
            if node.freq > 1:
                node.freq -= 1
                self.freq.append(node)
            else:
                self.freq.pop()
            return node.val
        return None
if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5); # The stack is [5]
    freqStack.push(7); # The stack is [5,7]
    freqStack.push(5); # The stack is [5,7,5]
    freqStack.push(7); # The stack is [5,7,5,7]
    freqStack.push(4); # The stack is [5,7,5,7,4]
    freqStack.push(5); # The stack is [5,7,5,7,4,5]
    print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    print(freqStack.pop())  # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
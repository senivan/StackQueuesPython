from collections import deque
class FreqStack:
    def __init__(self):
        self.frq_stacks = {}
        self.freq_map = {}
        self.max_freq = 0
    
    def push(self, val):
        freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = freq
        if freq > self.max_freq:
            self.max_freq = freq
        if freq not in self.frq_stacks:
            self.frq_stacks[freq] = deque()
        self.frq_stacks[freq].append(val)
    
    def pop(self):
        val = self.frq_stacks[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.frq_stacks[self.max_freq]:
            self.max_freq -= 1
        return val

if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5) # The stack is [5]
    freqStack.push(7) # The stack is [5,7]
    freqStack.push(5) # The stack is [5,7,5]
    freqStack.push(7) # The stack is [5,7,5,7]
    freqStack.push(4) # The stack is [5,7,5,7,4]
    freqStack.push(5) # The stack is [5,7,5,7,4,5]
    print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    print(freqStack.pop())  # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
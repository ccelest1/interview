class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def add(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        print(val)
        self.minStack.append(val)

    def remove(self):
        self.stack.pop()
        self.minStack.pop()

    def getTop(self):
        self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


MS = MinStack()
MS.add(1)
MS.add(2)

MS.add(-1)

print(MS.stack)
print(MS.minStack)

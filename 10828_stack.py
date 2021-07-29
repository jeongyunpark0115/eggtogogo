class stack:
    def __init__(self):
        self.myStack = []
    
    def push(self, n):
        self.myStack.append(n)
    
    def pop(self):
        if self.empty() == 1:
            return -1

        self.myStack.pop(-1)

    def size(self):
        return len(self.myStack)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def top(self):
        if self.empty == 1:
            return -1
        return self.myStack[-1]
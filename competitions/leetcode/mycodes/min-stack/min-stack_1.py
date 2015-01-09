class MinStack:
    def __init__(self):
        self.stack = []
        self.masks = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        
        self.stack.append(x)
        self.masks |= (1 << x)
        return 1

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.masks &= ~(1 << x)

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        r = self.masks & -self.masks
        return len(r)-1

    def show(self):
        print a.stack
        print a.masks


a = MinStack()
a.push(-3)
a.show()
print a.getMin()


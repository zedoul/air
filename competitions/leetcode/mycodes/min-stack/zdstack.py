class ZDStack:
    def __init__(self):
        self.stack = []
        self.minval = None; # should be None, not zero. because input value can be a negative value

    def push(self, x):
        if self.stack == [] :
            self.stack.append(x)
            self.minval = x
        else :
            if self.minval > x :
                self.stack.append(self.minval) # Trick!
                self.stack.append(x)
                self.minval = x
            else :
                self.stack.append(x)
        return 1

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack.pop()
            if self.minval == val :
                if len(self.stack) != 0:
                    self.minval = self.stack.pop() # Trick!
                else :
                    self.minval = None
            if 1 == len(self.stack):
                self.minval = self.stack[0]
            return val
        else :
            return None

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minval

    def show(self):
        print "========="
        print a.stack
        print a.minval
        print "========="


a = ZDStack()
a.push(2)
a.push(0)
a.push(1)
assert(a.minval == 0) # normal test

a = ZDStack()
a.push(-2)
a.push(0)
a.push(-1)
assert(a.minval == -2) # negative value test

a = ZDStack()
a.push(3)
a.pop()
assert(a.minval == None) # error handling test

a = ZDStack()
a.push(3)
a.push(2)
a.push(1)
assert(a.minval == 1) # minval test
a.pop()
assert(a.minval == 2)
a.pop()
assert(a.minval == 3)
a.pop()
assert(a.minval == None)

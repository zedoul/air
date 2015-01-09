class MinStack:
    def __init__(self):
        self.stack = []
        self.pos_masks = 0
        self.neg_masks = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if x >= 0 :
            self.pos_masks |= (1 << x)
        else :
            self.neg_masks |= (1 << abs(x))
        return 1

    # @return nothing
    def pop(self):
        val = self.stack.pop()
        if val >= 0:
            self.pos_masks &= ~(1 << val)
        else :
            self.neg_masks &= ~(1 << abs(val))

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        r = ""
        if self.neg_masks == 0 :
            r = self.pos_masks & -self.pos_masks
            return len(bin(r))-3
        else : 
            r = self.neg_masks.bit_length()
            return -1*(len(bin(r))-2)

    def show(self):
        print "========="
        print a.stack
        print a.pos_masks
        print a.neg_masks
        print "========="


a = MinStack()
a.push(2147483646)
a.push(2147483646)
a.push(2147483647)
#top
#pop
#getMin
#pop
#getMin
#pop
#push(2147483647)
#top
#getMin,push(-2147483648),top,getMin,pop,getMin

#a.push(-2)
#a.push(0)
#a.push(-1)
#a.show()
#print a.getMin()
#a.top()
#a.pop()
#a.show()
#print a.getMin()
#

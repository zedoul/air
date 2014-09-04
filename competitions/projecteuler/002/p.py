def fib(i,j,s):
    if j % 2 == 0:
        s += j
    if i+j > 4000000 :
        return s
    return fib(j,i+j,s)
print fib(1,2,0)

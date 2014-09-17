import time

cache = {}
cache[1] = 1
cache[2] = 1

def _Fibonacci(i):
    assert(i>=1)
    if not cache.has_key(i):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[i]

def Fibonacci(i):
    assert(i>=3)
    return _Fibonacci(i)

def Number25():
    i = 3;
    while True:
        if len(str(Fibonacci(i))) >= 1000:
            break
        i = i+1
    return i

start = time.time()
ret = Number25()
elapsed = (time.time() - start)
print "found %d in %s seconds" % (ret,elapsed)


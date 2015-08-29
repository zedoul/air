cache = {}

def _LenCollatzSeq(n, target, size):
    if cache.has_key(n):
        cache[target] = size + cache[n]
        return cache[target]

    if n % 2 == 0:
        return _LenCollatzSeq(n/2, target, size+1)
    else :
        if n == 1:
            cache[target] = size+1
            return cache[target]
        else :
            return _LenCollatzSeq(3*n+1, target, size+1)

def LenCollatzSeq(n):
    return _LenCollatzSeq(n,n,0)

def LongestLenCollatzSeq(upperbound=1000000):
    longest = -1
    for i in xrange(1,upperbound+1):
        det = LenCollatzSeq(i)
        if det > longest:
            print "val "+str(i)+" generates "+str(det)+" (cache len="+str(len(cache))+")"
            longest = det
    return longest

print LongestLenCollatzSeq(1000000)

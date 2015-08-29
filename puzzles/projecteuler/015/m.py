import math
import time

cache = {}
cache[(0,0)] = 1

def _LatticePath(down, right, nroutes):
    if cache.has_key((down,right)):
        return cache[(down,right)]
    if(down == 0 or right == 0):
        cache[(down,right)] = nroutes + 1
        return cache[(down,right)]
    else:
        ret = LatticePath(down-1,right) + LatticePath(down,right-1)
        cache[(down,right)] = ret
        return cache[(down,right)]

def LatticePath(down, right):
    return _LatticePath(down, right, 0)

start = time.time()
for i in xrange(20):
    for j in xrange(20):
        print str(i) + ","+str(j) + " = " + str(LatticePath(i,j))+" (cache len="+str(len(cache))+")"
ret = LatticePath(20,20)
elapsed = (time.time() - start)

print "found %d in %s seconds" % (ret,elapsed)

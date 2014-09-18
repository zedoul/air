# http://mathworld.wolfram.com/MultiplicativeOrder.html
# http://eli.thegreenplace.net/2009/02/25/project-euler-problem-26/
# http://zacharydenton.com/project-euler-solutions/26/
def _ReciprocalCycle(denom):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    s = 0
    for t in range(1, denom):
        if 10**s == 10**(s+t) % denom:
            return t
    return 0

def ReciprocalCycles():
    return max(_ReciprocalCycle(i) for i in range(2,1001))

import time
start = time.time()
ret = ReciprocalCycles()
elapsed = (time.time() - start)
print "found %d in %s seconds" % (ret,elapsed)

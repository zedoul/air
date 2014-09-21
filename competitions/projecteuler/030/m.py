def is_equal_to_sum_of_powers(n,p):
    r = 0
    for t in str(n):
        r += int(t)**p
    return r == n

def problem30():
    ret = 0
    for n in range(2,200000):
        if is_equal_to_sum_of_powers(n,5):
            ret += n
    return ret 

import time
start = time.time()
ret = problem30()
elapsed = (time.time() - start)
print "found %d in %s seconds" % (ret,elapsed)

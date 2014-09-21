def problem30(a_max, b_max):
    ret = 0
    terms = []
    for a in range(2,a_max+1):
        for b in range(2,b_max+1):
            terms.append(a**b);
    return len(list(set(terms)))

import time
start = time.time()
ret = problem30(100,100)
elapsed = (time.time() - start)
print "found %d in %s seconds" % (ret,elapsed)

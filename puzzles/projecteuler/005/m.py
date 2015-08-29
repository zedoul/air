import sys
divisors = [11,13,14,16,17,18,19,20]
for i in xrange(20,sys.maxint,20):
    if all(i % n == 0 for n in divisors):
        print i
        break

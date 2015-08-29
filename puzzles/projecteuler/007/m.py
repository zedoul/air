import time
import math
primes = [2]

def is_prime(n):
    if n % 2 == 0:
        return False
    logt = math.sqrt(n)
    for p in primes:
        if p > logt:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True

def find_nthprime(n):
    count = 1
    number = 1
    while count < n:
        number += 2
        if is_prime(number):
            count += 1
    return number

start = time.time()
ret = find_nthprime(10001)
elapsed = (time.time() - start)

print "found %d in %s seconds" % (ret,elapsed)

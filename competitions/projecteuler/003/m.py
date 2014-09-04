import math
target = 600851475143
primes = []
pivot = 3
while pivot < math.sqrt(target):
    isPrime = True
    for p in primes:
        if pivot % p == 0:
            isPrime = False
    if isPrime:
        if target % pivot == 0:
            primes.append(pivot)
    pivot += 2

print primes[-1]

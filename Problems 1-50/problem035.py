# Project Euler Problem 35

import time
from math import sqrt

startTime = time.clock()

MAX = 1000000

def primes(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]

    sieve = [True] * (n + 1)
    for x in range(3, int(sqrt(n)) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def isPrime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2

    return True

def rotate(theList):
    return theList[-1:] + theList[:-1]

primeList = map(lambda x: str(x), primes(MAX))

circularPrimeCount = 0
for prime in primeList:
    isCircularPrime = True
    rotated = prime
    while True:
        rotated = rotate(rotated)
        if rotated == prime:
            break
        
        if not isPrime(int(rotated)):
            isCircularPrime = False

    if isCircularPrime:
        circularPrimeCount += 1
        
print("The number of circular primes below {0} is {1}.".format(MAX, circularPrimeCount))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

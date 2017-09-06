# Project Euler Problem 27

import time
from math import sqrt

startTime = time.clock()

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

MAX = 1000
MIN = -MAX

maxSequence = 0
primeProduct = 0

# b itself must be prime to account for where n = 0
listOfB = primes(MAX)
# a must be odd since b must be prime to account for n = 1, and it must be even if b = 2
listOfA = [a for a in range(MIN + 1, MAX) if a % 2 != 0]

for a in listOfA:
    for b in listOfB:
        n = 0
        while isPrime(abs(n ** 2 + a * n + b)):
            n += 1

        if n > maxSequence:
            maxSequence = n
            primeProduct = a * b

print("The product of the coefficients that produce the maximum number of primes for consecutive values of n is {0}.".format(primeProduct))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

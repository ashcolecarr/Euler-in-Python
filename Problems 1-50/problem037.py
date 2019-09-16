# Project Euler Problem 37

import time
from math import sqrt

startTime = time.clock()

# There are only 11 of these.
TRUNCATABLE_PRIMES = 11
# Ignore the single-digit primes.
START = 11

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

primeCount = 0
primeSum = 0
candidate = START
while primeCount < TRUNCATABLE_PRIMES:
    isTruncatablePrime = True
    if isPrime(candidate):
        leftTruncator = 10 ** (len(str(candidate)) - 1)
        leftTruncated = candidate
        rightTruncated = candidate
        while leftTruncator > 1:
            leftTruncated = leftTruncated % leftTruncator
            rightTruncated //= 10
            leftTruncator //= 10

            if not isPrime(leftTruncated) or not isPrime(rightTruncated):
                isTruncatablePrime = False
                break

        if isTruncatablePrime:
            primeCount += 1
            primeSum += candidate

    candidate += 2

print("The sum of the 11 primes truncatable left to right and right to left is {0}.".format(primeSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

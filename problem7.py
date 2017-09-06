# Project Euler Problem 7

import time

startTime = time.clock()

POSITION = 10001

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

# All primes have the form 6(n) +/- 1 except 2 and 3
primeCount = 2
candidateCount = 1
finalPrime = 0
while primeCount < POSITION:
    if isPrime(6 * candidateCount - 1):
        primeCount += 1
        if primeCount == POSITION:
            finalPrime = 6 * candidateCount - 1
    
    if isPrime(6 * candidateCount + 1):
        primeCount += 1
        if primeCount == POSITION:
            finalPrime = 6 * candidateCount + 1

    candidateCount += 1

print("Prime number {0} is {1}.".format(POSITION, finalPrime))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

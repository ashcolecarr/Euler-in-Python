# Project Euler Problem 10 

import time
from math import sqrt

startTime = time.clock()

MAX = 2000000

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

sumOfPrimes = sum(primes(MAX))

print("The sum of the primes below {0} is {1}.".format(MAX, sumOfPrimes))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

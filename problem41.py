# Project Euler Problem 41

import time
from math import sqrt

startTime = time.clock()

# Pandigital numbers are divisible by 3 except for 1234 pandigital and 1234567 pandigital.
MAX = 7654321
# The problem already gives this number so it cannot be lower than this.
MIN = 2143

def isPandigital(n):
    number = str(n)
    size = len(number)
    if '0' in number:
        return False

    for i in range(1, size + 1):
        if str(i) not in number:
            return False

    return True

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

pandigitalPrimes = [x for x in primes(MAX) if isPandigital(x)]

largest = max(pandigitalPrimes)

print("The largest n-digit pandigital prime is {0}.".format(largest))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

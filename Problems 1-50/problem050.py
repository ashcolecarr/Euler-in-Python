# Project Euler Problem 50

import time
from math import sqrt
from itertools import accumulate
from operator import add

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

primeNumbers = primes(MAX)
cumulativePrimeSums = list(accumulate(primeNumbers, add))
primeSequenceSum = 0
primeSequence = 0

for i, num1 in enumerate(cumulativePrimeSums):
    for j, num2 in enumerate(cumulativePrimeSums[i - primeSequence::-1]):
        if num1 - num2 > MAX:
            break

        if num1 - num2 in primeNumbers:
            primeSequence = i - j
            primeSequenceSum = num1 - num2

print("The prime below {0} that can be written as the sum of the most consecutive primes is {1}.".format(MAX, primeSequenceSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

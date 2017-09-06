# Project Euler Problem 23 

import time
from functools import reduce
from math import sqrt

startTime = time.clock()

UPPER_LIMIT = 20161 # Every number above this can be written as the sum of two abundant numbers.
LOWER_LIMIT = 12 # The smallest abundant number.

def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

# First, get all the abundant numbers up to UPPER_LIMIT.
abundants = [x for x in range(LOWER_LIMIT, UPPER_LIMIT + 1) if sum(list(factors(x))) - x > x]

# Mark all numbers which can be expressed as the sum of two abundant numbers.
markers = [False for x in range(UPPER_LIMIT + 1)]
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        # Mark the value as the sum of two abundants.
        if abundants[i] + abundants[j] <= UPPER_LIMIT:
            markers[abundants[i] + abundants[j]] = True
        else:
            break

nonAbundantsSum = 0
for i in range(len(markers)):
    if markers[i] == False:
        nonAbundantsSum += i

print("The sum of the positive integers whose sum cannot be written as two abundant numbers is {0}.".format(nonAbundantsSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

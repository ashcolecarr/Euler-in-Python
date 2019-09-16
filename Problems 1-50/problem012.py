# Project Euler Problem 12

import time
from functools import reduce
from math import sqrt

startTime = time.clock()

DIVISORS = 500
triangleNumbers = [1]

def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

while len(factors(sum(triangleNumbers))) <= DIVISORS:
    triangleNumbers.append(triangleNumbers[-1] + 1)

print("The first triangular number to have over {0} divisors is {1}.".format(DIVISORS, sum(triangleNumbers)))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

# Project Euler Problem 5 

import time
from functools import reduce
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

MAX = 20
primeNums = primes(MAX)

# Exclude the primes here since they will be already included in the product.
numbers = [x for x in range(2, MAX + 1) if x not in primeNums]

# Get all the primes below the max number and multiply them together.
product = reduce((lambda x, y: x * y), primeNums)
smallest = product

found = False
while not found:
    for number in numbers:
        if smallest % number != 0:
            smallest += product 
            break
        elif number == MAX:
            found = True

print("The smallest number evenly divisible by 1 to {0} is {1}.".format(MAX, smallest))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

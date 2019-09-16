# Project Euler Problem 21 

import time
from functools import reduce
from math import sqrt

startTime = time.clock()

LIMIT = 10000

def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

amicableSum = 0

for i in range(2, LIMIT):
    num1 = sum(factors(i)) - i

    num2 = sum(factors(num1)) - num1

    if num2 == i and num1 != i:
        amicableSum += i

print("The sum of all the amicable numbers under {0} is {1}.".format(LIMIT, amicableSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

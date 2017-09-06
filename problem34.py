# Project Euler Problem 34

import time
from math import factorial

startTime = time.clock()

# Set upper bound to 9! + 8! + 7! + 6! + 5! + 4! + 3! + 2! + 1! since each individual digit is a factorial.
UPPER_BOUND = 409113
# 1! and 2! are not under consideration.
START = 3

digitFactorials = [fac for fac in range(START, UPPER_BOUND) if sum(map(lambda x: factorial(int(x)), str(fac))) == fac]

digitFactorialSum = sum(digitFactorials)

print("The sum of all numbers equal to the factorial of their digits is {0}.".format(digitFactorialSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

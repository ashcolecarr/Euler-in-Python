# Project Euler Problem 45

import time
from math import sqrt

startTime = time.clock()

# The problem already lists a number, so start here.
START = 40755

def getTriangular():
    # Start here since the problem already gave a number (n = 285) which satisfies the condition.
    n = 286
    while True:
        t = (n * (n + 1)) // 2
        yield t
        n += 1

def isPentagonal(x):
    n = (sqrt(24 * x + 1) + 1) / 6
    return int(n) == n

def isHexagonal(x):
    n = (sqrt(8 * x + 1) + 1) / 4
    return int(n) == n

triangulars = getTriangular()
intersection = 0
for i in triangulars:
    if isPentagonal(i) and isHexagonal(i):
        intersection = i
        break

print("The next triangular number after {0} which also pentagonal and hexagonal is {1}.".format(START, intersection))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

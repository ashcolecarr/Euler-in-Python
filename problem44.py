# Project Euler Problem 44

import time
from math import sqrt

startTime = time.clock()

def getPentagonal():
    n = 1
    while True:
        p = (n * (3 * n - 1)) // 2
        yield p
        n += 1

def isPentagonal(x):
    n = (sqrt(24 * x + 1) + 1) / 6
    return int(n) == n

pentagonals = getPentagonal()
storedPentagonals = []
isFound = False
foundPentagonal = 0
for i in pentagonals:
    if isFound:
        break

    storedPentagonals.append(i)
    for j in storedPentagonals:
        if isPentagonal(i + j) and isPentagonal(i - j):
            isFound = True
            foundPentagonal = abs(i - j)
            break

print("The absolute value of the difference of the pair of pentagonal numbers with both a pentagonal sum and difference, for which that difference is minimized is {0}.".format(foundPentagonal))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

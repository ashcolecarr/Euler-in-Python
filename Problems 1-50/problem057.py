# Project Euler Problem 57

import time
from fractions import Fraction
from sys import setrecursionlimit

startTime = time.clock()

RECURSION_LIMIT = 1500
EXPANSIONS = 1000

def expandFraction(n):
    if n == 1:
        return Fraction(1, 2)
    else:
        return Fraction(1, 2 + expandFraction(n - 1))

setrecursionlimit(RECURSION_LIMIT)
numeratorWithMoreDigitsCount = 0
for i in range(1, EXPANSIONS + 1):
    fractionValue = 1 + expandFraction(i)

    if len(str(fractionValue.numerator)) > len(str(fractionValue.denominator)):
        numeratorWithMoreDigitsCount += 1

print("In the first {0} expansion, there are {1} fractions having a numerator with more digits than the denominator.".format(EXPANSIONS, numeratorWithMoreDigitsCount))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

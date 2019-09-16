# Project Euler Problem 33

import time
from math import isclose
from math import gcd
from functools import reduce

startTime = time.clock()

MIN = 10
MAX = 99

def hasCommonDigit(num, denom):
    return num // MIN == denom % MIN or num % MIN == denom // MIN

# Screen out trivial fractions and any fraction without a common digit as they are not under consideration.
fractions = [(a, b) for a in range(MIN, MAX + 1) for b in range(MIN, MAX + 1) if a < b and (a % MIN != 0 and b % MIN != 0) and hasCommonDigit(a, b)]

curiousFractions = []
for fraction in fractions:
    if isclose(fraction[0] / fraction[1], (fraction[0] // MIN) / (fraction[1] % MIN)):
        curiousFractions.append(fraction)
    elif isclose(fraction[0] / fraction[1], (fraction[0] % MIN) / (fraction[1] // MIN)):
        curiousFractions.append(fraction)

fractionProduct = reduce((lambda x, y: (x[0] * y[0], x[1] * y[1])), curiousFractions)
denominator = fractionProduct[1] // gcd(fractionProduct[0], fractionProduct[1])

print("The denominator of the product of the four curious fractions, given in lowest terms, is {0}.".format(denominator))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

# Project Euler Problem 60

import time
import euler
from math import floor, log10

startTime = time.clock()

# Setting this rather arbitrarily; not sure the best number to use.
PRIME_LIMIT = 10000

primeList = euler.primes(PRIME_LIMIT)
minimumSum = PRIME_LIMIT ** 2
primePairsSet = set()

def getPair(p1, p2):
    p1Val = floor(log10(p1)) + 1
    p2Val = floor(log10(p2)) + 1
    return (p1 * (10 ** p2Val) + p2, p2 * (10 ** p1Val) + p1)

def isConcatPrimePair(p1, p2):
    pair = getPair(p1, p2)
    if pair[0] in primePairsSet:
        if pair[1] in primePairsSet:
            return True
    else:
        if euler.isPrime(pair[0]) and euler.isPrime(pair[1]):
            primePairsSet.update(pair)
            return True
        else:
            return False

# Use brute force to check all possible primes -- not at all elegant or original, but what are you gonna do?
for i, a in enumerate(primeList):
    if a * 10 > minimumSum:
        break

    for j, b in enumerate(primeList[i + 1:]):
        if a + b * 8 > minimumSum:
            break

        if isConcatPrimePair(a, b):
            for k, c in enumerate(primeList[j + 1:]):
                if sum([a, b, c * 6]) > minimumSum:
                    break
                
                if isConcatPrimePair(a, c) and isConcatPrimePair(b, c):
                    for l, d in enumerate(primeList[k + 1:]):
                        if sum([a, b, c, d * 4]) > minimumSum:
                            break
                        
                        if isConcatPrimePair(a, d) and isConcatPrimePair(b, d) and isConcatPrimePair(c, d):
                            for e in primeList[l + 1:]:
                                if sum([a, b, c, d, e]) > minimumSum:
                                    break

                                if isConcatPrimePair(a, e) and isConcatPrimePair(b, e) and isConcatPrimePair(c, e) and isConcatPrimePair(d, e):
                                    tempSum = sum([a, b, c, d, e])
                                    if tempSum < minimumSum:
                                        minimumSum = tempSum

print("The lowest sum for a set of five primes where any two are concatenatable into another prime is {0}.".format(minimumSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

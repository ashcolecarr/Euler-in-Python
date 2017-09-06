# Project Euler Problem 39 

import time
from collections import Counter

startTime = time.clock()

MAX = 1000

def getB(p, a):
    return (p ** 2 - 2 * p * a) // (2 * p - 2 * a)

triangleSolutions = [(p, a, getB(p, a), p - a - getB(p, a)) for p in range(2, MAX + 1, 2) for a in range(1, p // 3 + 1)  if a ** 2 + getB(p, a) ** 2 == (p - a - getB(p, a)) ** 2]

perimeters = [x[0] for x in triangleSolutions]

maximized = Counter(perimeters).most_common()[0][0]

print("The right-triangle perimeter below {0} with the most solutions is {1}.".format(MAX, maximized))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

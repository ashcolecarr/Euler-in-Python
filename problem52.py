# Project Euler Problem 52

import time
from itertools import permutations

startTime = time.clock()

START = 10
MAX_MULTIPLIER = 6

def getNumbers():
    n = START
    while True:
        yield n
        n += 1

smallest = 0
for i in getNumbers():
    # Any number with a leftmost digit greater than 1 will need another digit place for its products, so no need to check it.
    if int(str(i)[0]) > 1:
        continue
    
    digits = list(map(lambda x: int(''.join(x)), permutations(str(i))))

    products = [i * x for x in range(2, MAX_MULTIPLIER + 1)]

    if all(x in digits for x in products):
        smallest = i
        break

print("The smallest integer x where 2x, 3x, 4x, 5x, and 6x contain the same digits is {0}.".format(smallest))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

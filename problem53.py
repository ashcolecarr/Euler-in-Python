# Project Euler Problem 53

import time
from math import factorial

startTime = time.clock()

THRESHOLD = 1000000
MIN = 23 # The problem states that no n less than this is more than a million.
MAX = 100 

numberOfValues = len(list(filter(lambda x: x > THRESHOLD, [(factorial(n)) // (factorial(r) * (factorial(n - r))) for n in range(MIN, MAX + 1) for r in range(1, n + 1)]))) 

print("The number of values of nCr greater than {0} is {1}.".format(THRESHOLD, numberOfValues))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

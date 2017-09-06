# Project Euler Problem 38

import time
from functools import reduce

startTime = time.clock()

# The problem already gives the pandigital number 9 x 1, 2, 3, 4, 5, so the final answer must also start with a 9 and be at least as large (9 x 1,2,3,4,5).
LOWER_BOUND = 9123
UPPER_BOUND = 9876

multiples = [int(str(x) + str(x * 2)) for x in range(LOWER_BOUND, UPPER_BOUND + 1)]

pandigitals = [x for x in multiples if len(set(str(x))) == 9]
largest = max(pandigitals)

print("The largest 1 to 9 pandigital number which is a concatenated product of a number times (1, 2, ..., n) is {0}.".format(largest))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

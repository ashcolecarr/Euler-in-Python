# Project Euler Problem 56

import time

startTime = time.clock()

MAX = 100

maximumDigitalSum = max([sum(map(lambda x: int(x), str(a ** b))) for a in range(MAX) for b in range(MAX)])

print("The maximum digital sum for the numbers a ^ b below {0} is {1}.".format(MAX, maximumDigitalSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

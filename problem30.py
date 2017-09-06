# Project Euler Problem 30

import time

startTime = time.clock()

# Set the upper limit to 6 * (9 ^ 5) since 7 * (9 ^ 5) is not a 7-digit number.
UPPER_LIMIT = 354294

fifthPowersSum = sum([num for num in range(2, UPPER_LIMIT + 1) if sum(map(lambda x: int(x) ** 5, str(num))) == num])

print("The sum of the numbers that can written as the fifth powers of their digits is {0}.".format(fifthPowersSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

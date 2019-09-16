# Project Euler Problem 63

import time
from itertools import count

startTime = time.clock()

# Go up to 9 since 10 ^ 1 = 10, which is two digits.
MAX = 9

def countPowerfulDigits():
    digitCount = 0
    for power in count(1):
        for base in range(1, MAX + 1):
            digitLength = len(str(base ** power))

            if base == MAX and digitLength < power:
                return digitCount
            elif digitLength == power:
                digitCount += 1

totalDigits = countPowerfulDigits()

print("The number of n-digit integers which are also an n-digit power is {0}.".format(totalDigits))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

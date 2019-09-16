# Project Euler Problem 16 

import time

startTime = time.clock()

POWER = 1000

digitSum = sum(map(lambda x: int(x), str(2 ** POWER)))

print("The sum of the digits of the number 2 ^ {0} is {1}.".format(POWER, digitSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

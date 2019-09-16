# Project Euler Problem 20 

import time
from math import factorial

startTime = time.clock()

NUMBER = 100

digitSum = sum(map(lambda x: int(x), str(factorial(NUMBER))))

print("The sum of the digits of {0}! is {1}.".format(NUMBER, digitSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

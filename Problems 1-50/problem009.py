# Project Euler Problem 9 

import time

startTime = time.clock()

SUM = 1000

product = [a * b * (SUM - (a + b)) for a in range(401) for b in range(401) if a ** 2 < b ** 2 and (SUM - (a + b)) ** 2 == a ** 2 + b ** 2]

print("The product of the Pythagorean triplet where a + b + c = {0} is {1}.".format(SUM, product[0]))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

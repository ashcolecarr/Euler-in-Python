# Project Euler Problem 28 

import time

startTime = time.clock()

SPIRAL_SIZE = 1001

addend = 2
number = 1
finalSum = 1

while number < SPIRAL_SIZE ** 2:
    for i in range(1, 5):
        number += addend
        finalSum += number

    addend += 2

print("The sum of the diagonal numbers in a {0} by {0} spiral is {1}.".format(SPIRAL_SIZE, finalSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

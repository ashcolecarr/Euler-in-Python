# Project Euler Problem 58

import time
import euler

startTime = time.clock()

TARGET_PERCENTAGE = .1

def incrementSpiralDiagonals():
    num = 1
    cycle = 0
    increment = 2

    while True:
        yield num, increment
        cycle += 1
        num += increment

        if cycle == 4:
            cycle = 0
            increment += 2

primeCount = 0
sideLength = 0
for i, values in enumerate(incrementSpiralDiagonals()):
    num = values[0]
    inc = values[1]

    if euler.isPrime(num):
        primeCount += 1

    if primeCount > 0 and primeCount / (i + 1) < TARGET_PERCENTAGE:
        sideLength = inc - 1
        break

print("The side length of a square spiral with a prime ratio on the diagonals where first less than {0}% is {1}.".format(TARGET_PERCENTAGE * 100, sideLength))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

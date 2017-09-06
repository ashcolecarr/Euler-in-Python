# Project Euler Problem 26

import time

startTime = time.clock()

MAX = 1000
TEN = 10

remainderWasFound = False
listOfRemainders = [[0],[1]]
remainders = []

for divisor in range(2, MAX):
    dividend = 1
    remainders = []
        
    # Repeat until divisor divides evenly into dividend.
    while dividend != 0:

        while dividend < divisor:
            dividend *= TEN

        dividend = dividend % divisor

        # Check remainder against those already stored.
        if dividend in remainders:
            remainderWasFound = True

        if remainderWasFound:
            remainderWasFound = False
            break

        remainders.append(dividend)

    listOfRemainders.append(remainders)

remainderSizes = list(map(lambda x: len(x), listOfRemainders))

print("The denominator below {0} for which 1 / denominator gives the longest recurring cycle is {1}.".format(MAX, remainderSizes.index(max(remainderSizes))))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

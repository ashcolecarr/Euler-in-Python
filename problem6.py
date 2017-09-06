# Project Euler Problem 6 

import time

startTime = time.clock()

MAX = 100
numbers = range(1, MAX + 1)

sumOfSquares = sum(map(lambda x: x ** 2, numbers))
squareOfSum = (sum(numbers)) ** 2

print("The difference between the sum of the squares and the square of the sum of the first {0} numbers is {1}.".format(MAX, squareOfSum - sumOfSquares))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

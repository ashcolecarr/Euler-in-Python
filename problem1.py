# Project Euler Problem 1

import time

startTime = time.clock()

THREE = 3
FIVE = 5
MAX = 1000

numbers = range(MAX) 
sum = 0 

for number in numbers:
    if number % THREE == 0 or number % FIVE == 0:
        sum += number

print("The sum of all the multiples below {0} is {1}.".format(MAX, sum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

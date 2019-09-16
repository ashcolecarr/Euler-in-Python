# Project Euler Problem 36

import time

startTime = time.clock()

MAX = 1000000

numbers = [num for num in range(1, MAX)]

palindromicSum = 0
for number in numbers:
    binary = "{0:b}".format(number)
    if str(number) == str(number)[::-1] and binary == binary[::-1]:
        palindromicSum += number

print("The sum of the numbers less than {0} which are palindromic in base 10 and base 2 is {1}.".format(MAX, palindromicSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

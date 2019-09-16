# Project Euler Problem 4 

import time

startTime = time.clock()

MAX = 999
MIN = 100

numbers = set([x * y for x in range(MIN, MAX) for y in range(MIN, MAX)])
numStrings = list(map(lambda x: str(x), numbers))
palindromes = filter(lambda x: x == x[::-1], numStrings)
converts = map(lambda x: int(x), palindromes)

print("The largest palindrome from the product of two 3-digit numbers is {0}.".format(max(converts)))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

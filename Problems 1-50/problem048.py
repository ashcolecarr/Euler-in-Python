# Project Euler Problem 48

import time

startTime = time.clock()

MAX = 1000
NUMBER_OF_DIGITS = 10

total = sum([x ** x for x in range(1, MAX + 1)])

lastTenDigits = (str(total)[-1:-(NUMBER_OF_DIGITS + 1):-1])[::-1]

print("The last ten digits of the series ending in {0} ^ {0} is {1}.".format(MAX, lastTenDigits))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

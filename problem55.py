# Project Euler Problem 55

import time

startTime = time.clock()

LIMIT = 10000
MAX_ITERATIONS = 50

def isLychrelNumber(num):
    number = num
    for n in range(MAX_ITERATIONS):
        number += int(str(number)[::-1])
        if str(number) == str(number)[::-1]:
            return False

    return True

lychrels = [x for x in range(LIMIT) if isLychrelNumber(x)]

print("There are {0} Lychrel numbers below {1}.".format(len(lychrels), LIMIT))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

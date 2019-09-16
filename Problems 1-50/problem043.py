# Project Euler Problem 43

import time
from itertools import permutations

startTime = time.clock()

PANDIGITAL = 9876543210 

def isDivisible(number):
    d = str(number)

    if int(d[1:4]) % 2 == 0 and int(d[2:5]) % 3 == 0 and int(d[3:6]) % 5 == 0 and int(d[4:7]) % 7 == 0 and int(d[5:8]) % 11 == 0 and int(d[6:9]) % 13 == 0 and int(d[7:10]) % 17 == 0:
        return True

    return False

allPandigitals = [int(''.join(x)) for x in list(permutations(str(PANDIGITAL))) if x[0] != '0']

divisibles = [x for x in allPandigitals if isDivisible(x)]

total = sum(divisibles)

print("The sum of all 0 to 9 pandigital digits with the substring divisibility property is {0}.".format(total))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

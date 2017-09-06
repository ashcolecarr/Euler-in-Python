# Project Euler Problem 32

import time
from itertools import permutations
from functools import reduce

startTime = time.clock()

digits = "123456789"
pandigitalList = list(permutations(digits))

def getNumber(start, end, numList):
    return int(reduce((lambda x, y: str(x) + str(y)), numList[start:end]))

# To get pandigital product, the multiplicand and multiplier must be a certain number of digits, or else the product will have too many or too few digits.
pandigitalProducts = []
product = 0
for pd in pandigitalList:
    product = getNumber(0, 1, pd) * getNumber(1, 5, pd)
    if product == getNumber(5, 9, pd):
        pandigitalProducts.append(product)

    product = getNumber(0, 2, pd) * getNumber(2, 5, pd) 
    if product == getNumber(5, 9, pd):
        pandigitalProducts.append(product)

finalSum = sum(set(pandigitalProducts))

print("The sum of the pandigital products is {0}.".format(finalSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

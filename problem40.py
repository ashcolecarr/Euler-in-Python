# Project Euler Problem 40

import time

startTime = time.clock()

MAX = 1000000

digits = ["."]
digitCount = 0
digit = 1

while digitCount <= MAX:
    digitString = str(digit)
    digits.append(digitString)
    digitCount += len(digitString)
    digit += 1

digitSequence = ''.join(digits)

product = int(digitSequence[1]) * int(digitSequence[10]) * int(digitSequence[100]) * int(digitSequence[1000]) * int(digitSequence[10000]) * int(digitSequence[100000]) * int(digitSequence[MAX]) 

print("The product of the digits is {0}.".format(product))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

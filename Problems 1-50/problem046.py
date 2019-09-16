# Project Euler Problem 46

import time
from math import sqrt

startTime = time.clock()

def isPrime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2

    return True

def getOddComposites():
    n = 9
    while True:
        while(isPrime(n)):
            n += 2
        yield n
        n += 2

def getSquareTerms(num):
    n = 1
    while 2 * (n ** 2) < num:
        yield 2 * (n ** 2)
        n += 1

oddComposites = getOddComposites()
smallest = 0
isFound = False
for i in oddComposites:
    squareTerms = getSquareTerms(i)
    isFound = True
    for j in squareTerms:
        if isPrime(i - j):
            isFound = False
            break

    if isFound:
        smallest = i
        break

print("The smallest odd composite that cannot be written as the sum of a prime and twice a square is {0}.".format(smallest))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

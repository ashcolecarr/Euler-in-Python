# Project Euler Problem 47

import time

startTime = time.clock()

NUMBER_OF_FACTORS = 4

def primeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def getNumbers():
    # Start at 210, since it is 2 x 3 x 5 x 7
    n = 210
    while True:
        yield n
        n += 1

firstNumber = 0
for i in getNumbers():
    if len(set(primeFactors(i))) == NUMBER_OF_FACTORS:
        if len(set(primeFactors(i + 1))) == NUMBER_OF_FACTORS:
            if len(set(primeFactors(i + 2))) == NUMBER_OF_FACTORS:
                if len(set(primeFactors(i + 3))) == NUMBER_OF_FACTORS:
                    firstNumber = i
                    break

print("The first number in the first four consecutive numbers to have four distinct primes each is {0}.".format(firstNumber))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

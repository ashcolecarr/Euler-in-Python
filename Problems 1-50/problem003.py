# Project Euler Problem 3 
import time
from math import sqrt
from functools import reduce

startTime = time.clock()

NUMBER = 600851475143

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

largestFactor = max(primeFactors(NUMBER))

print("The largest prime factor of {0} is {1}.".format(NUMBER, largestFactor)) 
print("Program execution took {0} seconds.".format(time.clock() - startTime))

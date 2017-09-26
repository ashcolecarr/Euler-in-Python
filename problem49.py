# Project Euler Problem 49

import time
from math import sqrt
from itertools import permutations

startTime = time.clock()

DIGIT_COUNT = 4
MAX_DIGIT = 9999
GIVEN_DIGIT = 1487

def primes(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]

    sieve = [True] * (n + 1)
    for x in range(3, int(sqrt(n)) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2] + [i for i in range(3, n, 2) if sieve[i]]

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

# Get all the primes with the specified number of digits.
excludedDigits = [''.join(x) for x in list(permutations(str(GIVEN_DIGIT)))]
primeNumbers = list(filter(lambda y: y not in excludedDigits, [str(x) for x in primes(MAX_DIGIT) if len(str(x)) == DIGIT_COUNT]))

concatenatedNumber = ""
isFound = False
for i in primeNumbers:
    primePermutations = [''.join(x) for x in list(permutations(i)) if isPrime(int(''.join(x)))]
    for j in primePermutations:
        # Skip if it's the same number
        if i == j:
            continue

        if j in primeNumbers:
            if str(int(j) + (int(j) - int(i))) in primePermutations:
                concatenatedNumber = i + j + str(int(j) + (int(j) - int(i)))
                isFound = True
                break

    if isFound:
        break

print("The 12-digit number formed by concatenating the terms in the 4-digit prime-permutation sequence is {0}.".format(concatenatedNumber))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

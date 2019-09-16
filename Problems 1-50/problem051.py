# Project Euler Problem 51

import time
import euler
from itertools import permutations

startTime = time.clock()

# Notes and Assumptions:
# The first replaced digit must be no greater than 2, to get eight primes.
# The number of digits replaced will be three.
# Assume that the number will be five or six digits.
# The ones digits will never change.
# The prime can only end in 1, 3, 7, or 9.

START = 57001 # 56003 was already given by the problem. 

def smallestPrimeOfEightMemberFamily(numString):
    DIGITS = "***"

    # Generate digit pattern and all permutations.
    pattern = ''.join([''.join(['x' for x in range(len(numString[0:-1:]) - len(DIGITS))]), DIGITS])
    patterns = list(map(lambda x: ''.join(x), set(permutations(pattern))))

    # Check the digit patterns to determine if a number is an eight-member family.
    for pat in patterns:
        patMarker = [i for i, x in enumerate(pat) if x == '*']
        candidatePattern = ''.join(['*' if i in patMarker else x for i, x in enumerate(numString)])
        tally = 0
        smallestInFamily = 0
        for i in range(10):
            # If no prime has been found by now (0, 1, 2), then it won't be an eight-member family.
            if i == 3 and tally == 0:
                break

            number = candidatePattern.replace('*', str(i))
            if number[0] == '0':
                continue

            if euler.isPrime(int(number)):
                tally += 1
                if tally == 1:
                    smallest = int(candidatePattern.replace('*', str(i)))

                if tally == 8:
                    return smallest

    return 0

candidate = START
primeMember = 0
while True:
    if candidate % 5 == 0:
        candidate += 2
        continue

    primeMember = smallestPrimeOfEightMemberFamily(str(candidate))
    if primeMember > 0:
        break

    candidate += 2

print("The smallest prime, which by replacing some or all digits, gives an eight-member prime family is {0}.".format(primeMember))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

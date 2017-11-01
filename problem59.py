# Project Euler Problem 59

import time
from itertools import takewhile

startTime = time.clock()

FILENAME = "cipher.txt"
ENCRYPTION_KEY = "god"

encryptedValues = []
plainTextAsciiSum = 0
with open(FILENAME, 'r') as cipherFile:
    cipherLines = cipherFile.readlines()
    for line in cipherLines:
        encryptedValues = line.split(',')

# Shear off the extraneous newline character from the final value.
encryptedValues[-1] = (encryptedValues[-1])[:-1]

for i, value in enumerate(encryptedValues):
    plainTextAsciiSum += ord(ENCRYPTION_KEY[i % len(ENCRYPTION_KEY)]) ^ int(value)

print("The sum of the plaintext ascii values is {0}.".format(plainTextAsciiSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

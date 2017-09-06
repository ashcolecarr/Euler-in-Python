# Project Euler Problem 42

import time
from string import ascii_uppercase

startTime = time.clock()

FILENAME = "words.txt"
ALPHABET = ['\0'] + list(map(lambda x: str(x), ascii_uppercase))

def getWordScore(word):
    wordScore = 0
    for letter in word:
        wordScore += ALPHABET.index(letter)

    return wordScore

def isTriangleNumber(number):
    n = 1
    triangleNumber = int((n / 2) * (n + 1))
    while triangleNumber <= number:
        if number == triangleNumber:
            return True
        
        n += 1
        triangleNumber = int((n / 2) * (n + 1))

    return False

with open(FILENAME, 'r') as wordFile:
    data = wordFile.readlines()

    for line in data:
        words = line.split(',')

words = [word[1:-1] for word in words] # Strip off parentheses.

wordCount = 0
for word in words:
    wordCount += 1 if isTriangleNumber(getWordScore(word)) else 0

print("The number of words in {0} that are triangle numbers is {1}.".format(FILENAME, wordCount))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

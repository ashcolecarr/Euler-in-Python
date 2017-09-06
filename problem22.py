# Project Euler Problem 22 

import time

startTime = time.clock()

FILENAME = "names.txt"

def getNameScore(name):
    alphabet = ['\0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    nameScore = 0
    for letter in name:
        nameScore += alphabet.index(letter)

    return nameScore

with open(FILENAME, 'r') as nameFile:
    data = nameFile.readlines()

    for line in data:
        names = line.split(',')

names.sort()
names = [name[1:-1] for name in names] # Strip off parentheses.

namesScore = 0
for i, name in enumerate(names):
    namesScore += (i + 1) * getNameScore(name)

print("The total score of all the alphabetized names in {0} is {1}.".format(FILENAME, namesScore))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

# Project Euler Problem 62

import time
from itertools import count

startTime = time.clock()

PERMUTATION_NUMBER = 5

smallestCube = 0
cubeGenerator = (x ** 3 for x in count())
cubes = []
# Permutations with the same digits will always result in the same sorted list.
for cubeGen in cubeGenerator:
    cube = sorted(list(str(cubeGen)))
    cubes.append(cube)

    if cubes.count(cube) == PERMUTATION_NUMBER:
        smallestCube = cubes.index(cube) ** 3
        break

print("The smallest cube for which exactly {0} of its permutations are cubes is {1}.".format(PERMUTATION_NUMBER, smallestCube))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

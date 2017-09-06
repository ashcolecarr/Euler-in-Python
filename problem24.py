# Project Euler Problem 24

import time
from itertools import permutations

startTime = time.clock()

PERMUTATION_TO_GET = 1000000

digits = "0123456789"

allPermutations = list(permutations(digits))

print("Permutation number {0} from the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 is {1}.".format(PERMUTATION_TO_GET, "".join(allPermutations[PERMUTATION_TO_GET - 1])))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

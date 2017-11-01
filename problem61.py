# Project Euler Problem 61

import time
from itertools import count, takewhile, permutations

startTime = time.clock()

LOWER_BOUND = 999
UPPER_BOUND = 10000

# Build lists of figurate numbers
figurates = []
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, ((z * (z + 1)) // 2 for z in count())))))
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, (z ** 2 for z in count())))))
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, ((z * (3 * z - 1)) // 2 for z in count())))))
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, (z * (2 * z - 1) for z in count())))))
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, ((z * (5 * z - 3)) // 2 for z in count())))))
figurates.append(list(filter(lambda x: x > LOWER_BOUND, takewhile(lambda y: y < UPPER_BOUND, (z * (3 * z - 2) for z in count())))))

allFigurates = permutations(figurates)

orderedSetSum = 0
for fig in allFigurates:
    for a in fig[0]:
        for b in fig[1]:
            if str(a)[2:4] == str(b)[0:2]:
                for c in fig[2]:
                    if str(b)[2:4] == str(c)[0:2]:
                        for d in fig[3]:
                            if str(c)[2:4] == str(d)[0:2]:
                                for e in fig[4]:
                                    if str(d)[2:4] == str(e)[0:2]:
                                        for f in fig[5]:
                                            if str(e)[2:4] == str(f)[0:2] and str(f)[2:4] == str(a)[0:2]:
                                                orderedSetSum = sum((a, b, c, d, e, f))
                                                break
    
print("The sum of the ordered set of six cyclic 4-digit figurate numbers is {0}.".format(orderedSetSum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

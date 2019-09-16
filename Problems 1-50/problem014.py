# Project Euler Problem 14

import time

startTime = time.clock()

UPPER_LIMIT = 1000000
final = 0
interim = 0
finalCount = 0
count = 0

i = UPPER_LIMIT - 1 
while True:
    # Skip even numbers as their sequences are likely to be shorter.
    i -= 2
    interim = i
    count = 0

    # Set a lower bound, since Collatz sequences of lower values will have already been covered by higher values. 
    if interim * 3 < UPPER_LIMIT:
        break

    while interim > 1:
        if interim % 2 == 0:
            interim //= 2
        else:
            interim = 3 * interim + 1

        count += 1
    count += 1

    if count > finalCount:
        finalCount = count
        final = i

print("The starting number under {0} producing the longest Collatz chain is {1}.".format(UPPER_LIMIT, final))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

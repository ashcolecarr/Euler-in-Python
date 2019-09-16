# Project Euler Problem 2

import time

startTime = time.clock()

TWO = 2
MAX = 4000000

fibonacci = [1, 1]
sum = 0

# Build Fibonacci sequence.
while True:
    term = fibonacci[-1] + fibonacci[-2] 
    if term < MAX:
        fibonacci.append(term)
        if term % TWO == 0:
            sum += term
    else:
        break

print("The sum of the even-valued Fibonacci terms below {0} is {1}.".format(MAX, sum))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

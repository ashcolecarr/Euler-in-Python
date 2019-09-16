# Project Euler Problem 25

import time

startTime = time.clock()

COUNT = 1000
fibonacci = [1, 1]

while True:
    term = fibonacci[-1] + fibonacci[-2] 
    if len(str(term)) < COUNT:
        fibonacci.append(term)
    else:
        break

print("The index of the first term in the Fibonacci sequence to contain {0} digits is {1}.".format(COUNT, len(fibonacci) + 1))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

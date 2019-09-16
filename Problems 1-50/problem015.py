# Project Euler Problem 15

import time
from math import factorial

startTime = time.clock()

GRID_LENGTH = 20

# There are n steps in the grid, with n / 2 down and n / 2 right.
# So the combination is n! / (n / 2)! / (n / 2)! since it goes only one way.
routes = (factorial(GRID_LENGTH + GRID_LENGTH) // factorial(GRID_LENGTH)) // factorial(GRID_LENGTH)

print("A grid of size {0} x {0} has {1} routes.".format(GRID_LENGTH, routes))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

# Project Euler Problem 31

import time

startTime = time.clock()

totalMoney = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# The coin change algorithm
def countChange(money, change):
    if money < 0 or change <= 0:
        return 0
    elif money == 0:
        return 1
    else:
        return countChange(money, change - 1) + countChange(money - coins[change - 1], change)

print("Change for two pounds can be made in {0} different ways.".format(countChange(200, len(coins))))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

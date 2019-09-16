# Project Euler Problem 17 

import time

startTime = time.clock()

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] 
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"
AND = "and"

MAX = 1000

numberString = []
finalString = ""

for i in range(1, MAX + 1):
    if i < 10:
        numberString.append(ONES[i])
    elif i >= 10 and i < 20:
        numberString.append(TEENS[i % 10])
    elif i >= 20 and i < 100:
        if i % 10 == 0:
            numberString.append(TENS[i // 10])
        else:
            numberString.append(TENS[i // 10])
            numberString.append(ONES[i % 10])
    elif i >= 100 and i < 1000:
        if i % 100 == 0:
            numberString.append(ONES[i // 100])
            numberString.append(HUNDRED)
        else:
            numberString.append(ONES[i // 100])
            numberString.append(HUNDRED)
            numberString.append(AND)
            if (i % 100) < 10:
                numberString.append(ONES[i % 100])
            elif (i % 100) >= 10 and (i % 100) < 20:
                numberString.append(TEENS[(i % 100) % 10])
            elif (i % 100) >= 20 and (i % 100) < 100:
                if ((i % 100) % 10) == 0:
                    numberString.append(TENS[(i % 100) // 10])
                else:
                    numberString.append(TENS[(i % 100) // 10])
                    numberString.append(ONES[(i % 100) % 10])
    elif i == 1000:
        numberString.append(ONES[i // 1000])
        numberString.append(THOUSAND)

print("The letters of the numbers from 1 to {0}, written as words, is {1}.".format(MAX, len(finalString.join(numberString))))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

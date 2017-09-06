# Project Euler Problem 19

import time

startTime = time.clock()

CENTURY_START = 1901
CENTURY_END = 2000
DAYS_IN_WEEK = 7

def addLeapDay(year):
    return 1 if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0 else 0

totalSundays = 0

# The first Sunday of 1901 was 6 January
day = 6
year = CENTURY_START
while year <= CENTURY_END:
    JANUARY = 1
    FEBRUARY = 32
    MARCH = 60 + addLeapDay(year)
    APRIL = 91 + addLeapDay(year)
    MAY = 121 + addLeapDay(year)
    JUNE = 152 + addLeapDay(year)
    JULY = 182 + addLeapDay(year)
    AUGUST = 213 + addLeapDay(year)
    SEPTEMBER = 244 + addLeapDay(year)
    OCTOBER = 274 + addLeapDay(year)
    NOVEMBER = 305 + addLeapDay(year)
    DECEMBER = 335 + addLeapDay(year)
    YEAR = 365 + addLeapDay(year)
    
    while day < YEAR:
        if day == JANUARY or day == FEBRUARY or day == MARCH or day == APRIL or day == MAY or day == JUNE or day == JULY or day == AUGUST or day == SEPTEMBER or day == OCTOBER or day == NOVEMBER or day == DECEMBER:
            totalSundays += 1

        day += DAYS_IN_WEEK

    #Reset day counter for next year.
    day -= YEAR
    year += 1

print("From 1 Jan {0} to 31 Dec {1}, {2} Sundays fell on the first of the month.".format(CENTURY_START, CENTURY_END, totalSundays))

print("Program execution took {0} seconds.".format(time.clock() - startTime))

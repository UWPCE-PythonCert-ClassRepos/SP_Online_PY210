#!/usr/bin/env python
import math


def printGrid():
    plus = '+'
    minus = '-'

    dashes = '- ' * 4
    plusLine = '+ ' + dashes
    wholePlusLine = plusLine + plusLine + '+'

    spaces = '    ' * 4
    barLine = '| ' + spaces
    wholeBarLine = barLine + barLine + '|'

    print(wholePlusLine)

    i = 1
    while i < 5:
        print(wholeBarLine)
        i += 1

    print(wholePlusLine)

    ii = 1
    while ii < 5:
        print(wholeBarLine)
        ii += 1

    print(wholePlusLine)


def print_grid2(n):

    numberOfDashes = math.floor(n/2)
#    print(numberOfDashes)
    dashes = '- ' * numberOfDashes
    plusLine = '+ ' + dashes
    wholePlusLine = plusLine + plusLine + '+'

    spaces = '    ' * numberOfDashes
    barLine = '| ' + spaces
    wholeBarLine = barLine + barLine + '|'

    print(wholePlusLine)

    i = 1
    while i < numberOfDashes+1:
        print(wholeBarLine)
        i += 1

    print(wholePlusLine)

    ii = 1
    while ii < numberOfDashes+1:
        print(wholeBarLine)
        ii += 1

    print(wholePlusLine)


def print_grid3(columns_rows, width):

    numberOfDashes = columns_rows

    dashes = '- ' * width
    plusLine = '+ ' + dashes
    wholePlusLine = (plusLine * columns_rows) + '+'

    spaces = '    ' * width
    barLine = '| ' + spaces
    wholeBarLine = (barLine * columns_rows) + '|'

    print(wholePlusLine)
    p = 1
    while p < columns_rows+1:
        i = 1
        while i < width+1:
            print(wholeBarLine)
            i += 1

        print(wholePlusLine)
        p += 1


printGrid()

print_grid2(3)
print_grid2(9)
print_grid2(15)

print_grid3(3, 4)
print_grid3(5, 3)


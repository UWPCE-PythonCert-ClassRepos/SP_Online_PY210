#!/usr/bin/env python3

"""
Lesson 2: Grid Printer Exercise
Course: UW PY210
Author: Jason Jenkins
"""


def print_grid(totalsize=8):
    """
    print a grid with length 8 and 2 columns

    :param size=8: value of the total size
    """

    print_grid2(2, totalsize // 2)


def print_grid2(rows, size):
    """
    print a grid based on the total rows and size

    :param rows: total rows
    :param size: size of rows
    """

    for x in range(rows):
        printGridLine(rows, size)
        for y in range(size):
            printGridSide(rows, size)
    printGridLine(rows, size)


def printGridLine(rows, size):
    """
    print a line on the grid
    """

    for x in range(rows):
        print("+", end=' ')
        for y in range(size):
            print("-", end=' ')
    print("+")


def printGridSide(rows, size):
    """
    print a side on the grid
    """

    for x in range(rows):
        print("|", end=' ')
        for y in range(size):
            print(end="  ")
    print("|")


if __name__ == "__main__":
    # tests print_grid
    print_grid()
    print_grid(3)
    print_grid(15)

    # tests print_grid2
    print_grid2(3, 4)
    print_grid2(5, 3)

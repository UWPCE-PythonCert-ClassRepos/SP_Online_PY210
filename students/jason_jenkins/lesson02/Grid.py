# Lesson 1: Grid Printer Exercise
# Course: UW PY210
# Author: Jason Jenkins


def print_grid(size = 8):
    print_grid2(2, size // 2)


def print_grid2(rows, size):
    for x in range(rows):
        printGridLine(rows, size)
        for y in range(size):
            printGridSide(rows, size)
    printGridLine(rows, size)


def printGridLine(rows, size):
    for x in range(rows):
        print("+", end=' ')
        for y in range(size):
            print("-", end=' ')
    print("+")


def printGridSide(rows, size):
    for x in range(rows):
        print("|", end=' ')
        for y in range(size):
            print(end="  ")
    print("|")

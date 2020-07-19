# Lesson 1: Grid Printer Exercise
# Couse: UW PY210
# Auther: Jason Jenkins

# Was hoping to overload function to enable all parts
# Turns out overloading is not as simple in python

def print_grid_Part1():
    print_grid2(2, 4)


def print_grid(size):
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

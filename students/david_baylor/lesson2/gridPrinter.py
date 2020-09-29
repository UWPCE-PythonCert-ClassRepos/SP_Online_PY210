"""
gridPrinter.py 
by David Baylor
This program prints a grid
using python 3

+ - - + - - +  A
|     |     |  B
|     |     |
+ - - + - - +
|     |     |
|     |     |
+ - - + - - +
""" 


def lineA(col, size):
    """makes the first line"""
    for i in range(col):
        print("+ " + "- "*size, end="")
    print("+")

def lineB(col, size):
    """makes the second line"""
    for i in range(col):
        print("|" + " "*((size*2)+1), end="")
    print("|")

def printGrid(col, row, size):
    """ prints a grid based on the parameters given"""
    for i in range(row):
        lineA(col, size)
        for n in range(size):
            lineB(col, size)
    lineA(col, size)

try:
    printGrid(int(input("how many coulmns?")), int(input("how many rows?")), int(input("size of cell?")))
except ValueError:
    print("error: all inputs must be integers")

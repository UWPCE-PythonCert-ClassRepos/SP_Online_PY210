#Lesson 2
#Grid Printer Exercise
#Run program print_grid (c,s) where c is the number of rows/columns
# and s i the size of each cell.

def print_horiz(c,s):
    """print grid dividers +---+ 
    c -- number of rows/columns, where rows == columns
    s -- size of each cell, s is the number of -s and |s for each grid
    """
    for i in range (c):
        print("+", end = " ")
        for j in range (s):
            print("-", end = " ")
    print("+")

def print_vertical(c,s):
    """print vertical bars and spaces"""
    for i in range (s):
        for j in range (c):
            print("|", end = " ")
            for k in range(s):
                print(" ", end = " ")
        print("|")

def print_grid(c,s):
    """print grid using variable how many cells (c) and 
    how big is each cell (s)
    """
    print_horiz(c,s)
    print_vertical(c,s)
    for i in range(c-1):
        print_horiz(c,s)
        print_vertical(c,s)
    print_horiz(c,s)
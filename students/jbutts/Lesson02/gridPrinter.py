#!/usr/bin/env python

'''
py210: Mod2: FizzBuzz

'''

def basic_grid(size):
    '''
    write a 2 x 2 grid, with the length of cell walls as an input
    :param size: width and height sizes of square cells
    :return: write a string that summarizes what we just did
    '''
    x = size  # dimensions
    cells_horizontal = "+" + (" - " * x) + "+" + (" - " * x) + "+"
    cells_vertical = "|" + ("   " * x) + "|" + ("   " * x) + "|"

    for i in range(0, 2):
        print(cells_horizontal)
        for j in range(0, x):
            print(cells_vertical)
    print(cells_horizontal) # print the bottom horizontal lines
    return "Printed a 2x2 grid with cell wall that are " + str(x) + " by " + str(x) + " units"

def adv_grid(x, y):
    '''
    Write a square (equal rows and columns) grid. Take size of cells as input.

    :param x: x is the number of rows and columns
    :param y: y is the number of "units" on each side of the cell's "square"
    :return: write a string that summarizes what we just did
    '''


    h_unit = "+" + (" - " * y)  # horizontal line in the cell
    v_unit = "|" + ("   " * y)  # line that makes up the vertical lines of the cell
    cells_horizontal = h_unit * x + "+"
    cells_vertical = v_unit * x + "|"

    for i in range(0, x):  # horizontal lines
        print(cells_horizontal)
        for j in range(0, y):  # write out vertical walls of each cell
            print(cells_vertical)
    print(cells_horizontal) # print the bottom horizontal line
    return "Printed a " + str(x) + " by " + str(x) + " grid, with cells " + str(y) + " units square"


#  Write a basic grid

print(basic_grid(3))
print("\n\n")

# Write an advanced grid
print(adv_grid(11, 2))

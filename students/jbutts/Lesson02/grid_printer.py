#!/usr/bin/env python

'''
py210: Mod2: GridPrinter

'''

def basic_grid(size):
    '''
    write a 2 x 2 grid, with the length of cell walls as an input
    :param size: width and height sizes of square cells
    :return: write a string that summarizes what we just did
    '''
    cells_horizontal = "+" + (" - " * size) + "+" + (" - " * size) + "+"
    cells_vertical = "|" + ("   " * size) + "|" + ("   " * size) + "|"

    for horizontal in range(0, 2):
        print(cells_horizontal)
        for vertical in range(0, size):
            print(cells_vertical)
    print(cells_horizontal) # print the bottom horizontal lines
    return "\nPrinted a 2x2 grid with cell wall that are " + str(size) +\
           " by " + str(size) + " units"

def adv_grid(x_size, y_size):
    '''
    Write a square (equal rows and columns) grid. Take size of cells as input.

    :param x_size: x is the number of rows and columns
    :param y_size: y is the number of "units" on each side of the cell's "square"
    :return: write a string that summarizes what we just did
    '''


    h_unit = "+" + (" - " * y_size)  # horizontal line in the cell
    v_unit = "|" + ("   " * y_size)  # line that makes up the vertical lines of the cell
    cells_horizontal = h_unit * x_size + "+"
    cells_vertical = v_unit * x_size + "|"

    for horizontal in range(0, x_size):  # horizontal lines
        print(cells_horizontal)
        for veritical in range(0, y_size):  # write out vertical walls of each cell
            print(cells_vertical)
    print(cells_horizontal) # print the bottom horizontal line
    return "\nPrinted a " + str(x_size) + " by " + str(x_size) + " grid, with cells " + str(y_size) + " units square"


#  Write a basic grid

print(basic_grid(3))
print("\n\n")

# Write an advanced grid
print(adv_grid(11, 2))

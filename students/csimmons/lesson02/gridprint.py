#!/usr/bin/env python3
# Craig Simmons
# Python 210
# gridprint.py - Lesson02 Grid Printer exercises
# Created 11/13/2020 - csimmons
# Modified 11/14/2020 - csimmmons

# Part 1 - Prints basic 2 x 2 grid using simple string manipulation
def basic_grid():
    horizontal_line = 2 * ('+ ' + 4 *'- ') + '+\n'
    vertical_line = 4 * (2 * ('| ' + 4 *'  ') + '|\n')
    print(horizontal_line + vertical_line + horizontal_line + vertical_line + horizontal_line)

# Part 2 - Prints a 2 x 2 grid similar to  basic_grid(), but size determined by value of n
def print_grid(n):
    horizontal_line = 2 * ('+ ' + n * ('- ')) + '+\n'
    vertical_line = n * (2 * ('| ' + n * ('  ')) + '|\n')
    print('\nPrinting a ' + str(2) + 'x' + str(2) + ' grid with a cell size of ' + str(n) + ' character units\n')
    print(2 * (horizontal_line + vertical_line) + horizontal_line)

# Part 3 - Prints grid with variable numbers of rows and columns and variable size
# The cells argument determines number of rows/colums. 3 will create a 3x3 grid
# cellsize argument determines size of each cell 
def print_grid2(cells,cellsize):
    horizontal_line = cells * ('+ ' + cellsize * ('- ')) + '+\n'
    vertical_line = cellsize * (cells * ('| ' + cellsize * ('  ')) + '|\n')
    print('\nPrinting a ' + str(cells) + 'x' + str(cells) + ' grid with a cell size of ' + str(cellsize) + ' character units\n')
    print(cells * (horizontal_line + vertical_line) + horizontal_line)


# Simple tests for grid functions
basic_grid()
#print_grid(8)
#print_grid(4)
#print_grid(15)
#print_grid2(2,8)
#print_grid2(3,4)
#print_grid2(7,3)
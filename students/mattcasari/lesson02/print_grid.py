#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 2, Excercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/grid_printer.html

Part 1: Write a function that draws a grid
Part 2: Make it more general
Part 3: Make it even more general

"""


def print_grid_part1():
    """ Create a simple grid

        Prints a 2x2 grid to screen with the 4 dashes and spaces between the corner '+'s

        Args:
            None
        Returns:
            None
    """

    text1 = "+ " + "- "*4 + "+ " + "- "*4 + "+"
    text2 = "| " + "  "*4 + "| " + "  "*4 + "|"

    for j in range(2):
        print(text1)
        for i in range(4):
            print(text2)
    print(text1)


def print_grid_part2(x):
    """ Create a user defined grid

    Print a 2x2 grid with x number of dashes/spaces between columns and rows.

    Args:
        x (int): number of "units" (dashes/spaces) between rows/columns
    Returns:
        None
    """
    total_width = x+2
    for i in range(total_width):
        temp = ""
        for j in range(total_width):
            if i % (total_width//2) == 0:
                if j % (total_width//2) == 0:
                    temp += "+ "
                else:
                    temp += "- "
            else:
                if j % (total_width//2) == 0:
                    temp += "| "
                else:
                    temp += "  "

        # Remove extra space at end of line
        temp = temp[:-1]
        print(temp)

def print_grid_part3(x, y):
    """ Create a complex user defined grid

    Print a user defined grid of size x by x cells, with y "units"
    (dashes/spaces) between each row/column

    Args:
        x (int): number of cells
        y (int): number of "units" (dashes/spaces) between rows/columns
         
    Returns:
        None
    """
    total_width = x*(y+1)+1
    for i in range(total_width):
        temp = ""
        for j in range(total_width):
            if i % (total_width//x) == 0:
                if j % (total_width//x) == 0:
                    temp += "+ "
                else:
                    temp += "- "
            else:
                if j % (total_width//x) == 0:
                    temp += "| "
                else:
                    temp += "  "
        # Remove extra space at end of line
        temp = temp[:-1]
        print(temp)


if __name__ == "__main__":
    # Run Part 1
    print("\n\nPart 1:")
    print_grid_part1()

    # Run Part 2
    print("\n\nPart 2:")
    print_grid_part2(3)

    # Run Part 3
    print("\n\nPart 3:")
    print_grid_part3(3,5)
#!/usr/bin/env python3

"""gridprinter exercise for lesson02"""

# example grid
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# part one; this is a function that prints the example grid


def grid_printer():
    """
    this function prints a 2x2 grid
    :return:
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    """
    plus = "+ "
    minus = "- "
    pipe = "| "
    space = " "
    linebegin = plus + minus * 4
    pipespace = pipe + space * 8

    gridline = linebegin + linebegin + plus + '\n'
    gridspace = 4 * (pipespace * 2 + pipe + '\n')

    full4x = gridline + gridspace + gridline + gridspace + gridline
    # experimenting here
    print(len(linebegin))
    # experimenting here
    print(full4x)


grid_printer()

# part 2 - start here
# base print_grid(3)
#
# + - + - +
# |   |   |
# + - + - +
# |   |   |
# + - + - +


def print_grid(n=3):
    """
    this function prints a 2x2 grid with its size specified by 'n'
    :param n: size of square in 2x2 square grid
    :return: grid of 2x2 squares, each square 'n' units in size
    """
    plus = "+ "
    minus = "- "
    pipe = "| "
    space = " "
    height = int(n / 2)
    width = 2 * (plus + (height * minus)) + plus + "\n"
    stack = 2 * (pipe + (height * (space * 2))) + pipe + "\n"
    print(2 * (width + (stack * height)) + width)


print_grid(3)

# part trés  - a function with 2 params! tight.


def print_grid2(h, w):
    """
    this function prints a square grid based on the following parameters -
    :param h: numbers of squares tall/wide the grid will be
    :param w: the size of each square
    :return: square grid of specified size (hxh) with each square being wxw in size
    """
    plus = "+ "
    minus = "- "
    pipe = "| "
    space = " "
    horiz = h * (plus + (w * minus)) + plus + "\n"
    vert = w * (h * (pipe + (w * (2 * space))) + pipe + "\n")
    stack = h * (horiz + vert) + horiz
    print(stack)


print_grid2(5, 2)

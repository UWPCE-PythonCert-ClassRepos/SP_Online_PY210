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

# part 2 start here -
# base print_grid(3)
#
# + - + - +
# |   |   |
# + - + - +
# |   |   |
# + - + - +


def print_grid(n=3):
    plus = "+ "
    minus = "- "
    pipe = "| "
    space = " "
    height = int(n / 2)
    width = 2 * (plus + (height * minus)) + plus + "\n"
    stack = 2 * (pipe + (height * (space * 2))) + pipe + "\n"
    print(2 * (width + (stack * height)) + width)


print_grid(9)

# part 3 - a function with 2 params! tight.


def print_grid2(h, w):
    plus = "+ "
    minus = "- "
    pipe = "| "
    space = " "
    horiz = h * (plus + (w * minus)) + plus + "\n"
    vert = w * (h * (pipe + (w * (2 * space))) + pipe + "\n")
    stack = h * (horiz + vert) + horiz
    print(stack)


print_grid2(5, 2)

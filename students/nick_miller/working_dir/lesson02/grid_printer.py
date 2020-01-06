#!/usr/bin/env python3

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

    print(full4x)


grid_printer()

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

    width = str(input("Select a grid width [1 to 3]: "))
    if width.strip() == '1':
        # code for 1x
        print("thank you")
    elif width.strip() == '2':
        # code for 2x
        print("thank you")
    elif width.strip() == '3':
        # code for 3x
        print("thank you")
    elif width.strip != '1' or '2' or '3':
        str(input("Select a grid width [1 to 3]: "))
    print(width)


grid_printer()

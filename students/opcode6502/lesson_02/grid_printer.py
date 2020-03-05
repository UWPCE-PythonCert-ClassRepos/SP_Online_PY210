# opcode6502: SP_Online_PY210

# REQ-01: Write a function that draws a grid like the following:
'''
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
'''


# Declare some variables we will use for the raw printing version
plus = '+'
minus = '-'
slash = '|'
space = ' '
space_minus = ' -'
space_plus = ' +'


# This is a simple and literal implementation.
# Experimenting with the print() statement and multiplication.
def print_grid_concatenation():
    print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(slash + (space * 9) + slash + (space * 9) + slash)
    print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)


# REQ-02: Write a function print_grid(n) that takes one integer argument and
# prints a grid just like before, BUT the size of the grid is given by the argument.


# REQ-03: Write a function that draws a similar grid with a specified number of rows and columns,
# and with each cell a given size.


# TESTS
print_grid_concatenation()

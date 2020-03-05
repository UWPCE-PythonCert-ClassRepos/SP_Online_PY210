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


# Declare some variables we will use for printing the grid.
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


# This is a variation on the print_grid_concatenation() function.
# I am experimenting with refactoring and simplifying this function.
# I removed some redundant code and I used a loop to print the grid.
def print_grid_concatenation_loop():

    # Use a loop to print the grid.
    for i in range(2):
        print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)
        for i in range(4):
            print(slash + (space * 9) + slash + (space * 9) + slash)

    # Print a final footer row to complete the grid.
    print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)


# REQ-02: Write a function print_grid(n) that takes one integer argument and
# prints a grid just like before, BUT the size of the grid is given by the argument.


# REQ-03: Write a function that draws a similar grid with a specified number of rows and columns,
# and with each cell a given size.


# TESTS
print("REQ-01: TEST 01: Testing the print_grid_concatenation() function:")
print_grid_concatenation()
print("REQ-01: TEST 02: Testing the print_grid_concatenation_loop() function:")
print_grid_concatenation_loop()

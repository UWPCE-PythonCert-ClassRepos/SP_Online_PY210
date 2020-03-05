# opcode6502: SP_Online_PY210

# REQ-01: Write a function that draws a grid like the following:
# [example provided]

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


# Removing redundant code and using a loop.
def print_grid_concatenation_loop():

    # Using a loop to print the grid.
    for i in range(2):
        print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)
        for i in range(3):
            print(slash + (space * 9) + slash + (space * 9) + slash)

    # Print a final footer row to complete the grid.
    print(plus + (space_minus * 4) + space_plus + (space_minus * 4) + space_plus)


#
def print_grid(x):
    print_header_row_v1(x)
    for i in range(x // 2):
        print_body_row_v1(x)
    print_header_row_v1(x)
    for i in range(x // 2):
        print_body_row_v1(x)
    print_header_row_v1(x)


#
def print_header_row_v1(n):
    print("+ ", end='')
    for size_of_grid in range(n // 2):
        print("- ", end='')
    print("+ ", end='')
    for size_of_grid in range(n // 2):
        print("- ", end='')
    print("+")


#
def print_body_row_v1(n):
    print("|", end='')
    for x in range(n):
        print(" ", end='')
    print("| ", end='')
    for x in range(n - 1):
        print(" ", end='')
    print("|", )


#
def print_grid2(x, y):
    #
    for i in range(x):
        print_header_row_v2(x, y)
        for z in range(y):
            print_body_row_v2(x, y)

    print_header_row_v2(x, y)


#
def print_header_row_v2(x, b):
    # Print the upper leftmost '+' symbol
    print("+ ", end='')

    # Main loop
    for i in range(x):
        for i in range(b):
            print("- ", end='')
        print("+ ", end='')
    print()


#
def print_body_row_v2(x, y):
    # LOOP
    # print("|", end='')
    for x in range(x):
        print("|", end='')
        for x in range((y * 2) + 1):
            print(" ", end='')
    print("|")


# PART ONE: Write a function that draws a grid like the following [example provided]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print()
print("PART ONE: EX 01: Testing print_grid_concatenation():")
print()
print_grid_concatenation()
print()
print("PART ONE: EX 01: Testing print_grid_concatenation_loop():")
print()
print_grid_concatenation_loop()
print()


# PART TWO: Write a function print_grid(n) that takes one integer argument and
# prints a grid just like before, BUT the size of the grid is given by the argument.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("PART TWO: EX 01: Testing print_grid(3):")
print()
print_grid(3)
print()
print("PART TWO: EX 02: Testing print_grid(9):")
print()
print_grid(9)
print()
print("PART TWO: EX 03: Testing print_grid(15):")
print()
print_grid(15)
print()


# PART THREE: Write a function that draws a similar grid with a specified number of rows and columns,
# and with each cell a given size.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("PART THREE: EX 01: Testing print_grid2(5, 3):")
print()
print_grid2(5, 3)
print()
print("PART THREE: EX 02: Testing print_grid2(3, 4):")
print()
print_grid2(3, 4)
print()

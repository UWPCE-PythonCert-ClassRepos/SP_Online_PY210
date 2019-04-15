# Lesson 02 : Grid Printer Exercise
# Write a function that draws a grid like the following:
#
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


# Part 1: Print the simple grid
def print_grid_simple():
    plus = '+ - - - - + - - - - +'
    pipe = '|         |         |'
    for i in range(2):
        print(plus)
        for i in range(4):
            print(pipe)
    print(plus)
# print_grid_simple()


# Part 2: Print the simple grid with a squre input size (n)
def print_grid(n):
    grid_size = n//2    # Divide the size by two sections
    if n & 1:   # Used to set the correct spacing for odd/even n
        pipe_space = n
    else:
        pipe_space = n + 1
    # print(n,' | ',grid_size,' | ',pipe_space)

    plus = '+' + ' -'*grid_size + ' +' + ' -'*grid_size + ' +'
    pipe = '|' + ' '*pipe_space + '|' + ' '*pipe_space + '|'

    for i in range(2):
        print(plus)
        for i in range(grid_size):
            print(pipe)
    print(plus)
# print_grid(10)


# Part 3: Write a function that draws a similar grid with a specified
#         number of rows and columns, and with each cell a given size.
# Example: print_grid2(3,4)
# (three rows, three columns, and each grid cell four “units” in size)

def print_grid(n,s):
    grid_size = s
    pipe_space = s*2 + 1
    # print(s,' | ',grid_size,' | ',pipe_space)

    plus = '+' + (' -'*grid_size + ' +')*n
    pipe = '|' + (' '*pipe_space + '|')*n

    for i in range(n):
        print(plus)
        for i in range(grid_size):
            print(pipe)
    print(plus)

# print_grid(3,4)
# print_grid(5,3)

#! bin/user/env python3
''' Creating a script that uses functions to create a grid using only "+", "-" and "|."
'''

# Variables
plus = '+ '
minus = '- '
post = '| '
space = ' '

# Simple function that prints a fixed size grid
def grid():
    print(plus + minus * 4 + plus + minus * 4 + plus)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(plus + minus * 4 + plus + minus * 4 + plus)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(post + space * 8 + post + space * 8 + post)
    print(plus + minus * 4 + plus + minus * 4 + plus)

# Print a grid at an arbitrary size "n"
def print_grid(n):
    x = n // 2  # Number of columns in the grid
    y = n - 1  # Cell units in size for each row
    print(plus + minus * x + plus + minus * x + plus)  # Printing the column pattern
    for i in range(x):
        print(post + space * y + post + space * y + post)  # Print the row pattern
    print(plus + minus * x + plus + minus * x + plus)
    for i in range(x):
        print(post + space * y + post + space * y + post)
    print(plus + minus * x + plus + minus * x + plus)

# Parameters X for the number of columns and Y for cell unit size
def print_col(x, y):
    print((plus + minus * y) * x + '+')

# Parameters X for the number of posts and Y for cell unit size
def print_row(x, y):
    print((post + space * (y * 2)) * x + '|')


# Print a grid by setting the rows and columns
def col_row(x, y):  # x = number of rows/columns, y = cell units size
    print_col(x, y)
    for i in range(y):
        print_row(x, y)

# Parameters X for the number of rows/columns and Y for the cell unit size
def advanced_grid(x, y):
    for i in range(x):
        col_row(x,y)
    print_col(x,y)


grid()

print_grid(3)

print_grid(9)

print_grid(15)

advanced_grid(3,4)

advanced_grid(5,3)

advanced_grid(6,2)
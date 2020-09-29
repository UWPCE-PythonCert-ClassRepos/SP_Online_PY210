
# Russell Felts
# Assignment 2 - Grid Printer Exercise - Part 1
# Build a grid using string manipulation and the print function

print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('|', ' ' * 7, '|', ' ' * 7, '|')
print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')


# Assignment 2 - Grid Printer Exercise - Part 2
# Write a function print_grid(n) that takes one integer argument and prints a
# grid just like before, BUT the size of the grid is given by the argument.
# params  i is an integer used to set the size of the grid created


def print_grid(i):
    """"Divide the size by 2, define the pattern, loop pattern to create the grid"""
    # Using the abs function and flooring the division of i ensures an even
    # absolute number for a square grid
    size = abs(i // 2)
    # spaces = 0
    # Determine the correct number of spaces based on i being odd or even
    if i % 2 == 0:
        spaces = i + 1
    else:
        spaces = i
    pattern1 = '+' + ' ' + '- ' * size
    pattern2 = '|' + ' ' * spaces
    print(pattern1 * 2 + '+')
    for loop in range(size * 2):
        if loop == size:
            print(pattern1 * 2 + '+')
        print(pattern2 * 2 + '|')
    print(pattern1 * 2 + '+')


# Assignment 2 - Grid Printer Exercise - Part 3
# Write a function print_grids(n,n) that takes two integer arguments and draws
# a similar grid with a specified number of rows and columns, and with each
# cell a given size.
# params  x is an integer the determines the number of rows and columns
# params  i is an integer used to set the size of the grid created


def print_grids(x, i):
    # Using the abs function and flooring the division of i ensures an even
    # absolute number for a square grid
    size = abs(i // 2)
    # spaces = 0
    # Determine the correct number of spaces based on i being odd or even
    if i % 2 == 0:
        spaces = i + 1
    else:
        spaces = i
    # Configure the gid patterns
    pattern1 = '+' + ' ' + '- ' * size
    pattern2 = '|' + ' ' * spaces
    # Use a loop to generate the rows and multiply the number of desired
    # columns by the gird size to generate the pattern to print the columns
    for loop1 in range(x):
        print(pattern1 * (x * 2) + '+')
        # Create the grids
        for loop in range(size * 2):
            if loop == size:
                print(pattern1 * (x * 2) + '+')
            print(pattern2 * (x * 2) + '|')
    print(pattern1 * (x * 2) + '+')


print_grid(5)
print_grid(6)
print_grid(9)
print_grid(14)
print_grids(3, 3)
print_grids(3, 6)
print_grids(6, 4)

"""
Draw a grid like the following:
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
multiply = 4
# Construct rows containing pluses and minuses
plus_minuses = ('+ ' + ('- ' * multiply)) * 2 + '+' + '\n'
# Construct rows containing '|' characters
dividers = ('| ' + ('  ' * multiply)) * 2 + '|' + '\n'
# Create the entire grid based on the above rows
grid = (plus_minuses + (dividers * multiply)) * 2 + plus_minuses
# Print grid
print(grid, end='')

def print_grid(n):
    """
    Takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument
    """
    multiply = int((n - 1)/2)
    # Construct rows containing pluses and minuses
    plus_minuses = ('+ ' + ('- ' * multiply)) * 2 + '+' + '\n'
    # Construct rows containing '|' characters
    dividers = ('| ' + ('  ' * multiply)) * 2 + '|' + '\n'
    # Create the entire grid based on the above rows
    grid = (plus_minuses + (dividers * multiply)) * 2 + plus_minuses
    # Print grid
    print(grid, end='')

def print_grid2(size, unit):
    """
    Draw a similar grid with a specified number of rows and columns, and with each cell a given size.
    """
    # Construct rows containing pluses and minuses
    plus_minuses = ('+ ' + ('- ' * unit)) * size + '+' + '\n'
    # Construct rows containing '|' characters
    dividers = ('| ' + ('  ' * unit)) * size + '|' + '\n'
    # Create the entire grid based on the above rows
    grid = (plus_minuses + (dividers * unit)) * size + plus_minuses
    # Print grid
    print(grid, end='')

# Only print the grids for testing purposes
if __name__ == "__main__":

    print_grid(9)
    print()
    print_grid(3)
    print()
    print_grid(15)
    print()

    print_grid2(3,4)
    print()
    print_grid2(5,3)
    print()
    
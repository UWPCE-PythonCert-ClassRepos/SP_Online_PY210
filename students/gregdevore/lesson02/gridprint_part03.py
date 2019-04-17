# For part 3, create a function that accepts two input variables
# The first input is the number of cells, the second is the size of each cell
# For example, input parameters of 3 and 4 would result in the following grid
# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# 3x3 grid, each is size 4

def print_grid2(num_rc,size):
    # 'num_rc' is an integer representing the number of rows and columns
    # 'size is' an integer representing the size of each cells

    # Round in the case of floating input
    num_rc, size = round(num_rc), round(size)

    # Define the four symbols used to print the grid
    plus = '+'
    dash = '-'
    pipe = '|'
    space = ' '

    # Form the two types of lines based on the input
    # For boundary lines, number of '+' is num_rc + 1
    # In between each '+' is 'size' number of '-'
    boundary_line = ''
    for _ in range(num_rc):
        boundary_line += '+'
        boundary_line += '-'*size
    boundary_line += '+'
    # For the interior line, number of '|' is num_rc + 1
    # In between each '|' is 'size' number of ' '
    interior_line = ''
    for _ in range(num_rc):
        interior_line += '|'
        interior_line += ' '*size
    interior_line += '|'

    # Form grid
    # Print each boundary line followed by 'size' number of interior num_lines
    for _ in range(num_rc):
        print(boundary_line)
        for _ in range(size):
            print(interior_line)
    print(boundary_line)

if __name__ == "__main__":
    # Run some test on different size grids
    tests = [(0,0),(1,1),(2,2),(3,4),(5,3)]
    for grid in tests:
        num_rc, size = grid
        print('\nPrinting a grid with %i rows and columns and size %i\n' % (num_rc, size))
        print_grid2(num_rc, size)

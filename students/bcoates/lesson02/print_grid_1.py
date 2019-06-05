# Define variables for characters for easier readability
DASH = '-'
PIPE = '|'
PLUS = '+'
SPACE = ' '

def print_grid():
    """ Print a 4 character, 2 x 2 grid using dashes, pipes, and plus signs """
    cell_size = 4
    grid_size = 2

    for row in range(grid_size + 1):    # Add one to account for closing line
        # Print a row separator
        for column in range(grid_size):
            print(PLUS, end=' ')
            for i in range(cell_size):
                print(DASH, end=' ')
        print(PLUS)

        # Print blank rows for given cell and grid size
        if row < grid_size:    # Only print to the grid size to account for closing line
            for line in range(cell_size):
                for column in range(grid_size):
                    print(PIPE, end=' ')
                    for i in range(cell_size):
                        print(SPACE, end=' ')
                print(PIPE)

print_grid()
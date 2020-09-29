def print_grid(size, cell_size):
    """ 
    prints a grid of size X, with cell size of Y. 

    Postional arguments:
    size -- size of grid to print
    cell_size -- cell size within each grid.

    """
    # address floating point values as invalid arguments.
    size = round(size) 
    cell_size = round(cell_size) 

    for i in range(size):
        print_top_grid(size, cell_size) 
        print_mid_grid(size, cell_size) 
    print_top_grid(size, cell_size)

def print_top_grid(size, cell_size):
    # prints the top of the grid. 

    print('+', end='')
    for row in range(size):
        print('-' * cell_size, end='')
        print('+', end='')
    print()

def print_mid_grid(size, cell_size):
    #prints the middle section of the grid 

    for i in range(size):
        print('|', end='')
        for row in range(size):
            print(' ' * cell_size, end='')
            print('|', end='')
        print()

if __name__ == "__main__":
    print_grid(5.5, 5)
#!/Lesson 2 grid printer

def print_grid(grid_dimensions=2,cell_size=4):
    """
    Print a square grid.

    Keyword Arguments
    grid_dimensions -- number of rows/columns (default=2)
    cell_size -- size of the cell (default=4)

    Both of the arguments must be interger values. If a non-integer value
    is input it will be truncated after the decimal point.
    For instance:
        1.5 -> 1
        2.359 -> 2
        5.0 -> 5
    """

    grid_dimensions = int(grid_dimensions)
    cell_size = int(cell_size)

    Building_line1 = ('+ ' + '- '*cell_size)*grid_dimensions + '+'
    Building_line2 = ('| ' + '  '*cell_size)*grid_dimensions + '|'

    for x in range(grid_dimensions):
        print(Building_line1)
        for y in range(cell_size):
            print(Building_line2)

    print(Building_line1)

    return 1

if (__name__ == '__main__'):

    print('==========================')
    print('Grid Printer Exercise 1')
    print('Showing ouput for: print_grid()')
    print_grid()

    print('==========================')
    print('Grid Printer Exercise 2')
    print('Showing ouput for: print_grid(cell_size=8)')
    print_grid(cell_size=8)

    print('==========================')
    print('Grid Printer Exercise 3')
    print('Showing ouput for: print_grid(5,3)')
    print_grid(5,3)
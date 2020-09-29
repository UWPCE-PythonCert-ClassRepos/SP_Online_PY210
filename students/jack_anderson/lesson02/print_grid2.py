#
#######################################################################################################################
'''
Part 1: Printing basic grid. Write a function that draws a grid like the following:
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


PART 2: Write a function print_grid(n) that takes one integer argument and prints a grid just like before,
BUT the size of the grid is given by the argument

ex: function_print_grid(3) should print a smaller grid

    + - + - +
    |   |   |
    + - + - +
    |   |   |
    + - + - +


PART 3 Write a function that draws a similar grid with a specified number of rows and columns,
and with each cell a given size.

For example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +

'''
#######################################################################################################################
#     Part 1:  print_basic_grid()
#######################################################################################################################

def print_basic_grid_post():
    print("|         ", end="")
    print("|         ", end="")
    print("|")

def print_basic_grid_beams():
    print('+ - - - - ', end='')
    print('+ - - - - ', end='')
    print('+')

def create_basic_grid_post():
    print_basic_grid_post()
    print_basic_grid_post()
    print_basic_grid_post()
    print_basic_grid_post()


def print_basic_grid():
    print_basic_grid_beams()
    create_basic_grid_post()
    print_basic_grid_beams()
    create_basic_grid_post()
    print_basic_grid_beams()

#######################################################################################################################
#     Part 2:  function_print_grid(n)
#######################################################################################################################

def function_print_posts(n):
    x = int(n)
    y = ' ' * x
    print("|" + y + "|" + y + "|")

def function_print_beams(n):
    x = n / 2
    y = int(x)
    z = "- " * y
    print('+', z, end='')
    print('+', z, end='')
    print('+')

def function_create_post(n):
    y = 0
    z = n / 2
    x = int(z)
    while y < x:
        function_print_posts(n)
        y = y + 1

def function_print_grid(n):
    function_print_beams(n)
    function_create_post(n)
    function_print_beams(n)
    function_create_post(n)
    function_print_beams(n)



#######################################################################################################################
#     Part 3:   print_grid2(a, n)
#######################################################################################################################

def print_grid_beam(num_of_columns, size):
    '''
    Action to Print out a grid beam line with column markers based on provided variables
    :param num_of_columns: number of columns for the grid
    :param size: the cell size to be created
    :return: Print out a beam with the given parameters
    '''
    current_column = 0
    total_columns = int(num_of_columns)
    cell_size = int(size)
    spacing = "- " * cell_size
    while current_column < total_columns:
        print('+', spacing, end='')
        current_column = current_column + 1
    print('+')



def print_grid_post(num_of_columns, size):
    '''
    Action to Print out grid posts and columns based on provided variables
    :param num_of_columns: number of columns to create
    :param size: the cell size to be created
    :return: Print out a row of column post with the given parameters
    '''
    current_column = 0
    total_columns = int(num_of_columns)
    cell_size = int(size) * 2
    spacing = " " * cell_size
    while current_column < total_columns:
        print("|", spacing, end='')
        current_column = current_column + 1
    print("|")


def print_grid_rows(num_of_columns, num_of_rows):
    '''
    Action to Call print_grid_post function each time a row is created
    :param num_of_columns: number of columns to create
    :param num_of_rows: the number of rows to create
    :return: Call print_grid_post action
    '''
    total_rows = int(num_of_rows)
    current_row = 0
    while current_row < total_rows:
        print_grid_post(num_of_columns, num_of_rows)
        current_row = current_row + 1



def print_grid2(grid_size, cell_size):
    '''
    Function to create a grid with a specified number of rows and specific cell sizes
    :param grid_size: number of rows and columns
    :param cell_size: the cell size
    :return: Prints out grid with the given parameters
    '''
    rows = grid_size
    start = 1
    print()
    print("Grid contains " +str(grid_size)+ " rows and " +str(grid_size)+ " columns and a grid size of " + str(cell_size))
    while start <= rows:
        print_grid_beam(grid_size, cell_size)
        print_grid_rows(grid_size, cell_size)
        start = start + 1
    print_grid_beam(grid_size, cell_size)
    print()


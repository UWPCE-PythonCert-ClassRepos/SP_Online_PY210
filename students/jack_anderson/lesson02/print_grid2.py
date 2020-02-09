
# Write a function that draws a grid like the following:
'''
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

'''

# def print_posts(n):
#     x = int(n)
#     y = ' ' * x
#     print("|" + y + "|" + y + "|")
#
# def print_beams(n):
#     x = n / 2
#     y = int(x)
#     z = "- " * y
#     print('+', z, end='')
#     print('+', z, end='')
#     print('+')
#
# def create_post(n):
#     y = 0
#     z = n / 2
#     x = int(z)
#     while y < x:
#         print_posts(n)
#         y = y + 1
#
# def create_beam(n):
#     print(print_beams(n))
#
# def print_grid(n):
#     print_beams(n)
#     create_post(n)
#     print_beams(n)
#     create_post(n)
#     print_beams(n)


def print_grid_beam(a, n):
    # Print out a grid beam line with column markers based on provided variables
    current_column = 0
    total_columns = int(a)
    grid_size = int(n)
    spacing = "- " * grid_size
    while current_column < total_columns:
        print('+', spacing, end='')
        current_column = current_column + 1
    print('+')



def print_grid_post(a, n):
    # Print out grid posts and columns based on provided variables
    current_column = 0
    total_columns = int(a)
    size = int(n) * 2
    spacing = " " * size
    while current_column < total_columns:
        print("|", spacing, end='')
        current_column = current_column + 1
    print("|")


def print_grid_rows(a, n):
    # Call print_grid_post function each time a row is created
    total_rows = int(n)
    current_row = 0
    while current_row < total_rows:
        print_grid_post(a, n)
        current_row = current_row + 1


def print_grid2(a, n):
    '''
    Function to create a grid with a specified number of rows and specific cell sizes
    :param a: number of rows and columns
    :param n: the cell size
    :return: Prints out grid with the given parameters
    '''
    rows = a
    start = 1
    print()
    print("Grid contains " +str(a)+ " rows and " +str(a)+ " columns and a grid size of " + str(n))
    while start <= rows:
        print_grid_beam(a, n)
        print_grid_rows(a, n)
        start = start + 1
    print_grid_beam(a, n)
    print()




print_grid2(6,14)
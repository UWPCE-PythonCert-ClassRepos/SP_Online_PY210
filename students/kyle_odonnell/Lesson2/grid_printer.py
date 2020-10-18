# ------------------------------------------------------------------------ #
# Title: Grid Printer Exercise
# Description: Introduction to Python: Lesson 2 Exercise 2.2
# ChangeLog:
# KODonnell,10.14.2020,Created script
# KODonnell,10.17.2020,Added Comments
# ------------------------------------------------------------------------- #


def print_grid():
    """ Print 2x2 square grid
    :return: nothing
    """
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+4*minus)*2+plus  # define row for top and bottom of square perimeters with 2 squares
    down = (column+12*" ")*2+column  # define row for sides of square perimeters with 2 squares
    print(across)  # print top row
    for i in range(4):  # print 'down' columns for square size 4
        print(down)
    print(across)   # print 'across' row
    for i in range(4):  # print 'down' columns for square size 4
        print(down)
    print(across)  # print bottom row


def print_grid1(n):
    """ Print square grid based on size "n"
    :param n: (int) size of grid
    :return: nothing
    """

    if n < 2:  # assign square size x to 1 if n less than 2
        x =1
    else:  # assign square size x to closest integer under n if n larger than 2
        x = n//2
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+x*minus)*2+plus  # define row for top and bottom of square perimeters
    down = (column+x*3*" ")*2+column  # define row for sides of square perimeters
    print(across)
    for i in range(x):
        print(down)
    print(across)
    for i in range(x):
        print(down)
    print(across)



def print_grid2(m,n):
    """ Print grid based on size "n"
    :param m: (int) m squares in grid row/column
    :param n: (int) size of each grid
    :return: nothing
    """

    if n < 2:  # assign square size x to 1 if n less than 2
        x = 1
    else:  # assign square size x to closest integer under n if n larger than 2
        x = n//1
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+x*minus)*m+plus  # define row for top and bottom of square perimeters
    down = (column+x*3*" ")*m+column  # define row for sides of square perimeters
    for z in range(m):
        print(across)  # print 'across' row for each square in grid height m
        for i in range(n):  #
            print(down)  # print n 'down' rows for each square in grid height m
    print(across)  # print bottom border of grid


#  Test grid functions
print("print_grid() - 2x2 grid:")
print_grid()
print("print_grid1(4) - grid with relative square size 4:")
print_grid1(4)
print("print_grid1(10) - grid with relative square size 10:")
print_grid1(10)
print("print_grid2(10,5) - 10x10 grid with squares size 5:")
print_grid2(10,5)
print("print_grid2(3,10) - 3x3 grid with squares size 10:")
print_grid2(3,10)
# ------------------------------------------------------------------------ #
# Title: Grid Printer Exercise
# Description: Introduction to Python: Lesson 2 Exercise
# ChangeLog:
# KODonnell,10.14.2020,Created script
# ------------------------------------------------------------------------- #


def print_grid():
    """" Print 2x2 square grid
    :return: nothing
    """
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+4*minus)*2+plus
    down = (column+12*" ")*2+column
    print(across)
    for i in range(4):
        print(down)
    print(across)
    for i in range(4):
        print(down)
    print(across)


def print_grid1(n):
    """ Print square grid based on size "n"
    :param n: (int) size of grid
    :return: nothing
    """
    if n < 2:
        x =1
    else: x = n//2
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+x*minus)*2+plus
    down = (column+x*3*" ")*2+column
    print(across)
    for i in range(x):
        print(down)
    print(across)
    for i in range(x):
        print(down)
    print(across)



def print_grid2(m,n):
    """ Print grid based on size "n"
    :param n: (int) size of grid
    :return: nothing
    """

    if n < 2:
        x = 1
    else: x = n//1
    plus = "+"
    minus = " - "
    column = "|"
    across = (plus+x*minus)*m+plus
    down = (column+x*3*" ")*m+column
    for z in range(m):
        print(across)
        for i in range(n):
            print(down)
    print(across)

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
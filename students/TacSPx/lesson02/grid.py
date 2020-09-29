# ---------------------------------------------------------------------------- #
# Title: Grid.py
# Description: Creating grids in Python
#
# Part 1 print simple quick grid
# Part 2 print custom function grid by size
# Part 3 print custom function grid by columns and rows
# ---------------------------------------------------------------------------- #

# Part 1 print a simple grid using a function -------------------------------- #

def quick_grid():
    """
    Print a quick grid
    :return: A string of characters to form a grid
    """
    print('''

+ -(*4) + -(*4) +
|         (*3)
|         (*3)
|         (*3)
|         (*3)
+ -(*4) + -(*4) +
|         (*3)
|         (*3)
|         (*3)
|         (*3)
+ -(*4) + -(*4) +

''')

# Part 2 Custom function grid -------------------------------------------- #

def print_grid(n):
    """
    The grid will expand in size based on the user input(n)
    :param n: Grid size based on user input
    :return: A string of characters to form a grid
    """
    if n < 3:
        print("Must choose number larger than '3'!")
    else:
        print("+ " + '-'*n + " + " + '-'*n + " +")
        for i in range(n//3):
            print("|" + " "*n + "  |" + " "*n + "  |")
        print("+ " + '-' * n + " + " + '-' * n + " +")
        for i in range(n//3):
            print("|" + " "*n + "  |" + " "*n + "  |")
        print("+ " + '-' * n + " + " + '-' * n + " +")
    return

# Part 3 Custom function grid by columns and rows------------------------- #


def print_grid2(x,y):
    """
    A custom grid by columns and rows based on user input
    :param x: Horizontal row grid quantity
    :param y: Vertical column grid quantity
    :return: Custom grid with exact rows and columns user specifies
    """

    # Data ---------------------------------------------------------------------- #
    plus = "+ "
    minus = "--- "
    bar = ("|     ")

    grid_x = (plus + minus)
    grid_y = (bar)

    # Processing  --------------------------------------------------------------- #
    def grid_plus():
        print()
        print(grid_x * x, end="+")
        print()
    def grid_bar():
        print(grid_y * x, end="|")
        print()
        print(grid_y * x, end="|")
        print()
        print(grid_y * x, end="|")

    # Presentation ------------------------------------------------------------ #
    grid_plus()
    for _ in range(y):
        grid_bar()
        grid_plus()

#############################
#############################
#Sample runs:
quick_grid()
print_grid(10)
print_grid2(10,4)




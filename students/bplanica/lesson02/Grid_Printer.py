# ------------------------------ #
# Grid Printer Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/3/2019, Created and tested script
# ------------------------------ #

# ----- DATA ----- #
# ---------------- #

sub_x = 0  # Determine the size of each cell (number of "-")
interim = ""  # Interim string value for later concatenation
plus = ""  # Cell top/bottom lines
bar = ""  # Cell border lines


# ----- PROCESSING ----- #
# ---------------------- #

def grid():
    """function that draws a grid"""

    print("""+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +""")


def print_grid(x):
    """a function that takes one integer argument 
            and the size of the grid is given by the argument."""

    sub_x = int((x - 1)/2)  # Determine the size of each cell (number of "-")
    if sub_x <= 1:
        interim = " - "  # If the size is <= to one, there will only be one "-"
    else:
        interim = " -" + ((" -") * (sub_x - 2)) + " - "  # Otherwise, there will be 2 or more depending
    plus = "+" + interim + "+" + interim + "+"  # Cell top/bottom lines
    bar = "|" + ( " " * ((sub_x * 2) + 1)) + "|" + ( " " * ((sub_x * 2) + 1)) + "|"  # Cell border lines
    
    # Each output will only have 4 cells, as defined below
    print(plus)
    i = 1
    while i <= sub_x:
        print(bar)  # Print as many bar lines as there are "-" in the top/bottom line
        i += 1
    print(plus)
    i = 1
    while i <= sub_x:
        print(bar)  # Print as many bar lines as there are "-" in the top/bottom line
        i += 1
    print(plus)


def print_grid2(x, y):
    """a function that draws a grid with a specified number of rows and columns (x) 
            and with each cell a given size (y)"""

    if y <= 1:
        interim = " - "  # If the size is <= to one, there will only be one "-"
    else:
        interim = " -" + ((" -") * (y - 2)) + " - "  # Otherwise, there will be 2 or more depending
    plus = (("+" + interim) * x) + "+"  # Cell top/bottom lines, number of columns determined by x
    bar = (("|" + ( " " * ((y * 2) + 1))) * x) + "|"  # Cell border lines, number of columns determined by x
    
    print(plus)  # print a top/bottom line
    i = 1
    while i <= x:  # Do until the counter = the number of rows desired
        j = 1
        while j <= y:
            print(bar)  # Print as many bar lines as there are "-" in the top/bottom line
            j += 1
        print(plus)  # Print correcponding top/bottom line and repeat
        i += 1


# ----- PRESENTATION ----- #
# ------------------------ #

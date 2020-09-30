# Title: Grid Printer
# Dev: Roslyn Melookaran
# Date: 9/2/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/2/20, created script)
# --------------------------------------------------------------

# ---------------------PART 1---------------------#
n=10
grid_size=2
if (n-1)%2 != 0:n=n-1 # Handling Rounding
sqr_width=int((n - 1) / grid_size)
print(n)

for i in range(grid_size):
    # Horizontal
    for i in range(grid_size):
        print("+", end=" ")
        print("- " * sqr_width, end="")
    print("+")
    # Vertical
    for i in range(sqr_width):
        for i in range(2):
            print("|", end=" ")
            print("  " * sqr_width, end="")
        print("| ")
# Horizontal Lower
for i in range(2):
    print("+", end=" ")
    print("- " * sqr_width, end="")
print("+")

# ---------------------PART 2---------------------#
# This section uses a function to create the grid. We pass only the grid size argument into it

def print_grid(x):
    """ prints grid
                :param: x (integer): grid size
                :return: nothing
                """
    if (x - 1) % 2 != 0: x = x - 1  # Handling Rounding
    sq = int((x - 1) / 2)
    for i in range(2):
        # Horizontal
        for i in range(2):
            print("+", end=" ")
            print("- " * sq, end="")
        print("+")
        # Vertical
        for i in range(sq):
            for i in range(2):
                print("|", end=" ")
                print("  " * sq, end="")
            print("| ")
    # Horizontal Lower
    for i in range(2):
        print("+", end=" ")
        print("- " * sq, end="")
    print("+")
    return

# ---------------------PART 3---------------------#
# This section uses a function to create the grid. We pass two arguments, grid size and square width

def print_grid_2(x,y):
    """ prints grid
                :param: x (integer): grid size
                :param: y (integer): square width
                :return: nothing
                """
    for i in range(x):
        # Horizontal
        for i in range(x):
            print("+", end=" ")
            print("- " * y, end="")
        print("+")
        # Vertical
        for i in range(y):
            for i in range(x):
                print("|", end=" ")
                print("  " * y, end="")
            print("| ")
    # Horizontal Lower
    for i in range(x):
        print("+", end=" ")
        print("- " * y, end="")
    print("+")
    return

# ---------------------Main---------------------#
#print_grid(15)
print_grid_2(5,3)



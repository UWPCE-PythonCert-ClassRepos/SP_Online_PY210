def print_horiz(m,b):
    """print horizontal header and footer"""
    for i in range (m):
        print("+", end = " ")
        for j in range (b):
            print("-", end = " ")
    print("+")

def print_vertical(m,b):
    """print vertical bars and spaces"""
    for i in range (b):
        for j in range (m):
            print("|", end = " ")
            for k in range(b):
                print(" ", end = " ")
        print("|")

def print_grid(m,b):
    """print grid using variable how many cells and how big is each cell.
    m -- how many cells/number of rows and columns
    b -- how big is each cell/size of each cell
    """
    print_horiz(m,b)
    print_vertical(m,b)
    for i in range(m-1):
        print_horiz(m,b)
        print_vertical(m,b)
    print_horiz(m,b)

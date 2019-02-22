#UWPCE PY210
#Lesson02, Grid Printer

def print_grid(size, n):
    """Prints a cell grid."""
    print_rowBreak(size, n)
    print_cellRow(size, n)
    for i in range(size-1):
        print_rowBreak(size, n)
        print_cellRow(size, n)
    print_rowBreak(size, n)

def print_rowBreak(size, n):
    """Prints the header/footer of a row in a cell"""
    for i in range(size): #Number of columns.
        print("+", end = " ")
        for j in range(n): #Width of column.
            print("-", end = " ")
    print("+")

def print_cellRow(size, n):
    """Prints the cells in a row."""
    for i in range(n): #Height of cell.
        for num in range(size): #Number of columns.
            print("|", end = " ")
            for j in range(n): #Width of cell.
                print(" ", end = " ")
        print("|")
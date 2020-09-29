# To use, type "python GridPrinter2.py" at the command line then answer the question regarding grid size
# Author: Brian Minsk

def print_grid(size_interior):
    """This is what's called for the rest of the stack.

    Keyword arguments:
    size_interior -- for a 2x2 square grid size_interior is 2 * the cell length (or width) + 1
    """
    length = int(size_interior)//2
    really_print_grid(length_cell=length, width_cell=length)


def really_print_grid(num_rows=2, num_cols=2, length_cell=4, width_cell=4):
    """Print a grid like the following.

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

    Keyword arguments:
    num_rows -- number of rows in the grid (default 2)
    num_cols -- number of columns in the grid (default 2)
    length_cell -- number of characters down for a single cell (default 4)
    width_cell -- number of characters across for a single cell (default 4)
    """
    for i in range(0,num_rows):
        print_row(num_cols, length_cell, width_cell)
    # Print the bottom of the grid     
    print_cross_line(num_cols, width_cell)

def print_row(num_cols, length_cell, width_cell):
    """Print a row without the bottom, as the following.
    
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |

    Keyword arguments:
    num_cols -- number of columns in the grid
    length_cell -- number of characters down for a single cell
    width_cell -- number of characters across for a single cell
    """
    print_cross_line(num_cols, width_cell)
    for i in range(0, length_cell):
        print_down_line(num_cols, width_cell)

def print_cross_line(num_cols, width_cell):
    """Print a top/bottom of a grid row, as the following.
    
    + - - - - + - - - - +
   
    Keyword arguments:
    num_cols -- number of columns in the grid
    width_cell -- number of characters across for a single cell
    """
    for i in range(0, num_cols):
        # A cross_bar looks like this (width 4): +----
        cross_bar = "+" + (width_cell * "-")
        print(cross_bar, end="")
        
    # After the last cross_bar print a "+" to end the cross_line
    print("+")

def print_down_line(num_cols, width_cell):
    """Print one line of the cell sides of a grid row, as the following.
    
    |         |         |
   
    Keyword arguments:
    num_cols -- number of columns in the grid
    width_cell -- number of characters across for a single cell
    """
    for i in range(0, num_cols):
        cell_side = "|" + (width_cell * " ")
        print(cell_side, end="")
    # After the last cell_side print a "|" to end the row line
    print("|")

if __name__ == "__main__":
    size = input("Enter a grid size > 1: ")
    int(size)
    print_grid(size)



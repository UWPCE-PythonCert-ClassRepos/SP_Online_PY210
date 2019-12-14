#### Grid Printer Exercises ####

# Part 1 
def print_top():
    print("+ - - - - + - - - - +")

def print_second():
    print("|         |         |")

def part_1_grid():
    print_top()
    print_second()
    print_second()
    print_second()
    print_second()
    print_top()
    print_second()
    print_second()
    print_second()
    print_second()
    print_top()

# Run    
part_1_grid()


# Part 2 - Make a more general grid function with one input.

def print_grid(n):

    # Find units of grid
    u = (n-1)//2

    # Set up grid size
    top = u * '-' 
    space = u * ' ' 

    # Print grid
    # Top line
    print('+', top, '+', top, '+')

    for i in range(u):
        print('|', space, '|', space, '|')

    # Repeat for second half of grid
    print('+', top, '+', top, '+')

    for i in range(u):
        print('|', space, '|', space, '|')

    print('+', top, '+', top, '+')

# Run
print_grid()


# Part 3 - Make function to print grid with columns and rows args

def print_grid_2(grid, units):

# units - size of grid squares
# grid - number of rows (and columns) of our grid
    
    tab = '- '
    space = ' '
    
    # Make two types of rows for grid based on inputs
    top_row = grid * ('+ ' + tab * units) + '+'
    col_row = grid * ('| ' + space * units * 2) + '|'

    # Print over rows/columns
    for i in range(grid):
        
        print(top_row)

        for i in range(units):
            print(col_row)
    
    # Print last row
    print(top_row)

# Run
print_grid_2(3,4)

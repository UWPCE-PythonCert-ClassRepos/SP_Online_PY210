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

print_grid()


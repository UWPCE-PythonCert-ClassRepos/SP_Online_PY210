
 # Simple grid with defined size per assignment instructions
def step_one_grid():
    """step_one_grid prints a grid of a defined size per assignment instructions"""
    x = 4
    dash = x * '-'
    space = x * ' '

    # Print out grid
    print('+', dash, '+', dash, '+')

    for i in range(4):
        print('|', space, '|', space, '|')
    
    print('+', dash, '+', dash, '+')

    for i in range(4):
        print('|', space, '|', space, '|')
    
    print('+', dash, '+', dash, '+')

# Level 2 grid with size based on one input argument: n
def print_grid(n):
    """ print_grid prints a grid based on one input argument: n"""
    
    # Number of dashes or spaces as function of size n
    x = (n-1)//2

    dash = x * '-'
    space = x * ' '

    # Print out grid
    print('+', dash, '+', dash, '+')

    for i in range((n-1)//2):
        print('|', space, '|', space, '|')
    
    print('+', dash, '+', dash, '+')

    for i in range((n-1)//2):
        print('|', space, '|', space, '|')
    
    print('+', dash, '+', dash, '+')

# Level 3 grid with size based on two input arguments: col and units
def print_grid2(col, units):
    """ print_grid2 prints a grid based on input parameters col and units"""
    dash = units * '-'
    space = units * ' '

    # Iteratively print over columns and rows
    for i in range(col):
        
        for i in range(col):
            print('+', dash, sep = '', end = '')
        print('+')
        
        for i in range(units):
            for i in range(col):
                print('|', space, sep = '', end = '')
            print('|')

    # Last line
    for i in range(col):
            print('+', dash, sep = '', end = '')
    print('+')

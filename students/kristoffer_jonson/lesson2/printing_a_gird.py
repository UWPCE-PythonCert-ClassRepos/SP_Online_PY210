def print_grid_part_1():
    '''
    Print a 2x2 grid of pre-defined size
    '''
    edge_row = '+ - - - - + - - - - +'
    middle_row = '|         |         |'
    for j in range(2):
        print(edge_row)
        for i in range(4):
            print(middle_row)
    print(edge_row)

def print_grid(n):
    '''
    Print a 2x2 grid
    :param n: This parameter scales size of the grid
    '''
    k = n //2
    edge_row = '+ ' + '- ' * k + '+ ' + '- ' * k + '+'
    middle_row = '| ' + '  ' * k + '| '+ '  ' * k + '|'
    for j in range(2):
        print(edge_row)
        for i in range(k):
            print(middle_row)
    print(edge_row)

def print_grid2(m,n):
    '''
    Print a grid
    :param m: Defines how many boxes wide the grid is
    :param n: Defines the size of each box within the grid
    '''
    edge_row =  '+ '
    middle_row = '| '
    for i in range(m):
        edge_row += '- ' * n + '+ '
        middle_row += '  ' * n + '| '
    for j in range(m):
        print(edge_row)
        for i in range(n):
            print(middle_row)
    print(edge_row)
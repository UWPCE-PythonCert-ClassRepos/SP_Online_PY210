def print_row_for_grid(x, y = 1):
    i = 0
    y = (x-1)/2
    z = int(round(y))
    print_row_edge(z, 2)
    while i < z:
        print_row_middle(z, 2)
        i += 1

def print_row_for_grid2(x, y = 1):
    i = 0
    print_row_edge(y, x)
    while i < y:
        print_row_middle(y, x)
        i += 1

def print_row_edge(x, y):
    for i in range(y):
        print('+', end='')
        print(' -'*x, end=' ')
    print('+')

def print_row_middle(x, y):
    for i in range(y):
        print('|', end='')
        print('  '*x, end=' ')
    print('|')

def print_grid(x):
    print_row_for_grid(x, 2)
    print_row_for_grid(x, 2)
    print_row_edge(int(round((x-1)/2)), 2)

def print_grid2(x, y):
    i = 0
    while i < x:
        print_row_for_grid2(x, y)
        i += 1
    print_row_edge(y, x)
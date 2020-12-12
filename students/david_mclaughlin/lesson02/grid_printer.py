"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""
#!/usr/bin/env python

# PART 1
def print_grid1():
    
    print('+', '-'*4, '+', '-'*4, '+')
    for i in range(4):
        print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
    for i in range(4):
        print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
    

# PART 2
def print_grid2(size):
    
    n = size//2
    print('+', '-'*n, '+', '-'*n, '+')
    for i in range(n):
        print('|', ' '*n, '|', ' '*n, '|')
    print('+', '-'*n, '+', '-'*n, '+')
    for i in range(n):
        print('|', ' '*n, '|', ' '*n, '|')
    print('+', '-'*n, '+', '-'*n, '+')


# PART 3
def print_grid3(box_size, cell_size):
    
    for i in range(box_size):
        print('+', end=' ')
        for i in range(box_size): 
            print('-'*cell_size, '+', end=' ')
        print()
    
        for i in range(cell_size):
            print('|', end=' ')
            for i in range(box_size):
                print(' '*cell_size, '|', end=' ')
            print()
        
    print('+', end=' ')
    for i in range(box_size): 
        print('-'*cell_size, '+', end=' ')

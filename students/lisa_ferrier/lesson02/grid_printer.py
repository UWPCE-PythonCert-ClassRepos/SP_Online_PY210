# grid_printer.py
# Lisa Ferrier, Python 201, Lesson 02

def print_gridV1():
    '''prints a grid size 4x4'''
    num_cols=(('+' + (' -'*4)+' ')*2+'+')
    num_rows=((('|' + ('  '*4)+' ')*2+'|'+'\n')*4)
    print(num_cols)
    print(num_rows, end='')
    print(num_cols)
    print(num_rows, end='')
    print(num_cols)

print_gridV1()

def print_gridV2(n):
    '''
    Prints a grid with number of rows/cols specified by user (n).
    Input value must be >=0.
    Input value is rounded down to the nearest integer if decimals are entered.
    '''
    n=int(round(n))
    if n >=0:
        num_cols=(('+' + (' -'*n)+' ')*2+'+')
        num_rows=((('|' + ('  '*n)+' ')*2+'|'+'\n')*n)
        print(num_cols)
        print(num_rows, end='')
        print(num_cols)
        print(num_rows, end='')
        print(num_cols)
    else:
        print("n must be >=0")

print_gridV2(3)


def print_gridv3(x,y):
    '''
    Takes two inputs (x,y) and creates a grid sized (x) with a specified number of rows & columns.(y)
    Input value must be >=0.
    Input value is rounded down to the nearest integer if decimals are entered.
    '''
    x=int(round(x,1))
    y=int(round(y,1))
    if x>=0 and y>=0:
        cols=(('+' + (' -'*y)+' ')*x+'+'+'\n')
        rows=((('|' + ('  '*y)+' ')*x+'|'+'\n')*y)
        grid_unit = (cols+rows)*x
        last_row=(cols)
        print(grid_unit+last_row,end='')
    else:
        print("x and y must be >=0")

print_gridv3(5,3)
'''Grid Printer
    Print grids based on user inputs.
'''
 

def full_line(m=2,n=9):
    '''Print a full line grid with m grids and n columns'''
    line = '+ ' + (n//2)*'- '
    print(m* line + '+')

def side_line(m=2,n=9):
    '''Print a side line grid with m grids and n columns'''
    line = '|' + n*' '
    print(m* line + '|')

def print_grid(n=9):
    '''Print a 2x2 grid that has a size of n columns
    Note: n includes the number of spaces and dashes
    '''
    for i in range(0,3):
        full_line(n=n)
        for j in range(0,n//2):
            if i < 2:
                side_line(n=n)
            else:
                pass
                
def print_grid2(m,n):
    '''Print a m by m grid with n columns and rows
    Note: Unlike in print_grid n is the number of dashes
    '''
    for i in range(0,m+1):
        full_line(m,2*n)
        for j in range(0,n):
            if i < m:
                side_line(m,2*n +1)
            else:
                pass
                
#actually print the grids                
print('Basic Grid (Part 1)')
print_grid()

print('\nThree different grids (Part 2)')
print_grid(9)
print_grid(3)
print_grid(15)

print('\nGrids of different sizes (Part 3)')
print_grid2(3,4)
print_grid2(5,3)
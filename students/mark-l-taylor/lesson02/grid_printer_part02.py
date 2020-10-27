#Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
 

def full_line(n):
    '''Print a full line grid of size n'''
    print('+ ' + (n//2)*'- ' + '+ ' + (n//2)*'- ' + '+')

def side_line(n):
    '''Print a side line grid of size n'''
    print('|' + n*' ' + '|' + n*' ' + '|')

def print_grid(n):
    '''Print a 2x2 grid that has a size of n'''
    for i in range(0,3):
        full_line(n)
        for j in range(0,n//2):
            if i < 2:
                side_line(n)
            else:
                pass
                
#Actually print the grids
print_grid(9)
print_grid(3)
print_grid(15)
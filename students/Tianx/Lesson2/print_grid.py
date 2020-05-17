#------------------------------------------#
# Title: print_grid.py
# Desc: Write a function that draws a grid.
# Tian Xie, 2020-04-04, Created File
#------------------------------------------#

# Part 1

horizontal = '+ - - - - + - - - - +'
gridpost = '|         |         |'
plus = '+'
minus = '- '
post = '|'
space = '  '

def grid1():
    print(horizontal)
    print(gridpost)
    print(gridpost)
    print(gridpost)
    print(gridpost)
    print(horizontal)
    print(gridpost)
    print(gridpost)
    print(gridpost)
    print(gridpost)
    print(horizontal)

# Part 2
def print_grid(n):
    """Function to create grid.
            Args:
            n : grid number, size of the grid is given by the argument.
            """
    m = (n//2) # determine the # of '-' in the grid.
    print(plus, minus * m + plus, minus * m + plus) #top horizonal line

    for i in range(m):
        print(post, space * m + post, space * m + post) #loop thru the half of the argument given as the number of spaces.
    print(plus, minus * m + plus, minus * m + plus) #middle horizontal line

    for i in range(m):
        print(post, space * m + post, space * m + post) #loop thru the half of the argument given as the number of spaces.
    print(plus, minus * m + plus, minus * m + plus)  #bottom horizontal line


# Part 3
def print_grid2(grid, cell_size):
    grid = round(grid)
    cell_size = round(cell_size)
    horizontal_line = ('+ ' + minus * cell_size)*grid + plus #creating horizontal line
    vertical_line = ('| ' + space * cell_size)*grid + post #creating vertical line

    for h in range(grid):
        print(horizontal_line)
        for v in range(cell_size):
            print(vertical_line)
    print(horizontal_line)

# Test
if (__name__ == '__main__'):
    print('Part 1')
    grid1()
    print('Part 2')
    print_grid(3)
    print_grid(15)
    print('Part 3')
    print_grid2(5,3)
    print_grid2(5.4,3.1)

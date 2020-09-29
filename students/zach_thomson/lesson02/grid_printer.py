#part 1
DASH = ' -'
PLUS = '+'
SPACE = ' '
VERT = '|'

LINE = (PLUS + (4*DASH) + SPACE + PLUS + (4*DASH) + SPACE + PLUS)
BAR = (VERT + (9*SPACE) + VERT + (9*SPACE) + VERT)

def grid_basic():
    """Prints a basic grid pattern"""
    print(LINE + ((('\n' + BAR) * 4) + '\n' + LINE)*2)
#grid_basic()

#part 2
def print_grid(n):
    """Takes an odd number and prints a grid sized relative to that number"""
    if n % 2 == 0:
        print('Please use an odd number for n')
    else:
        a = int((n-1)/2)
        b = int(n)
        line = (PLUS + (a*DASH) + SPACE + PLUS + (a*DASH) + SPACE + PLUS)
        bar = (VERT + (b*SPACE) + VERT + (b*SPACE) + VERT)
        grid = (line + ('\n' + bar) * a + '\n') * 2 + line
        print(grid)

#test print_grid function
#print_grid(3)
#print_grid(9)
#print_grid(15)
#print_grid(6)

#part 3
def print_grid2(n, size):
    """Prints a grid of int(n) columns/rows and int(size) dashes"""
    n = int(n)
    size = int(size)
    line_grid2 = ((PLUS + (size * DASH) + SPACE)*n) + PLUS
    bar_grid2 = (VERT + (size * 2 + 1) * SPACE)*n + VERT
    grid2 = (line_grid2 + ('\n' + bar_grid2) * size +'\n') * n + line_grid2
    print(grid2)

#test print_grid2
#print_grid2(3, 4)
#print_grid2(5, 6)
#print_grid2(1,1)
#print_grid2(2.5, 3.5)

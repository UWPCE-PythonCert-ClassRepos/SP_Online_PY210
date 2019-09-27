
#A function that draws a GRID
def grid():
    x=4
    space = x * ' '
    dash = x * '-'
    print('+', dash, '+', dash, '+')
    for i in range(x):
         print('|', space, '|', space, '|')

    print('+', dash, '+', dash, '+')

    for i in range(x):
         print('|', space, '|', space, '|')
    print('+', dash, '+', dash, '+')

grid()

# A function print_grid(n) that takes one integer argument and prints a GRID. The size of the grid is determined by the argument.

def print_grid(x):
    
    space = x * ' '
    dash = x * '-'
    print('+', dash, '+', dash, '+')
    for i in range(x):
         print('|', space, '|', space, '|')

    print('+', dash, '+', dash, '+')

    for i in range(x):
         print('|', space, '|', space, '|')
    print('+', dash, '+', dash, '+')

print_grid(6)

# A function that draws a GRID with a specified number of rows and columns, and with each cell a given size.

def grid_3(row, col):
     plus = "+"
     minus ="-"
     pipe="|"
     space=" "
     horizontal_line = (plus +minus*(col))*row + plus
     vertical_line = (pipe+space*(col))*row + pipe
     print(horizontal_line)
     print(vertical_line)
     for i in range(0, row):
          for j in range(0, col):
               print(vertical_line)
          print(horizontal_line)


grid_3(3,4)
      
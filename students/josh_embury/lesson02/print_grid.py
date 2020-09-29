#--------------------------------------------------------------#
# Title: Lesson 2, Print Grid
# Description: Functions used to print grids (3 parts)
# ChangeLog (Who,When,What):
# JEmbury, 9/18/2020, created new script
#--------------------------------------------------------------#
# ------- PART 1 ----------------------------------------------#
def grid():
    """
    Desc - This function prints a hard-coded grid, no input parameters, no return
    :return: No return; output is grid printed to console
    """
    print('+ '+ 2*(4*'- ' + '+ '))
    for i in range(0,4):
        print(('|'+2*(9*' '+ '|')))
    print('+ ' + 2 * (4 * '- ' + '+ '))
    for i in range(0,4):
        print(('|'+2*(9*' '+ '|')))
    print('+ ' + 2 * (4 * '- ' + '+ '))
# ------- PART 2 ----------------------------------------------#
def print_grid(m):
    """
    Desc - This function prints a grid, scaled to input value
    :param: m, int, scaling factor for size of grid to be output
    :param:
    :return: No return; output is a grid printed to console
    """
    print_grid_horz(m)
    print_grid_vert(m)
    print_grid_horz(m)
    print_grid_vert(m)
    print_grid_horz(m)
def print_grid_horz(num):
    print('+ ' + 2 * (num * '- ' + '+ '))

def print_grid_vert(num):
    for i in range(0,num):
        print(('|'+2*((2*num+1)*' '+ '|')))
# ------- PART 3 ----------------------------------------------#
def print_grid2(n,m):
    """
    Desc - This function prints a square grid, with specified number of n columns/rows, scaled to input value m
    :param: n, int, number of rows/columns in grid
    :param: m, int, scaling factor for size of grid to be output
    :return: No return; output is a grid printed to console
    """
    print_grid_horz2(n,m) # call horizontal line helper function
    for i in range(0,n): # for loop to iterate for number of rows in grid
        print_grid_vert2(n,m) # call vertical line helper function
        print_grid_horz2(n,m) # call horizontal line helper function
def print_grid_horz2(n,num):
    """
    Desc - Grid helper function; prints single row with specified number of n columns/rows, scaled to input value m
    :param: n, int, number of rows/columns in grid
    :param: m, int, scaling factor for size of grid to be output
    :return: No return; output is a horizontal gridline printed to console
    """
    print('+ ' + n * (num * '- ' + '+ '))
def print_grid_vert2(n,num):
    """
     Desc - Grid helper function; prints vertical lines with n columns with specified number of n columns/rows,
      scaled to input value m
     :param: n, int, number of rows/columns in grid
     :param: m, int, scaling factor for size of grid to be output
     :return: No return; output is vertical gridlines printed to console
     """
    for i in range(0,num):
        print(('|'+n*((2*num+1)*' '+ '|')))
# ------- MAIN/TEST ----------------------------------------------#
if __name__ == '__main__':
    grid() # Test part 1 grid function
    print_grid(9) # Test part 2 grid function
    print_grid2(5,6) # Test part 3 grid function
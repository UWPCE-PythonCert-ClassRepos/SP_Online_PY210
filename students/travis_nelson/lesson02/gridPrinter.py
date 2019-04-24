
def grid():
    """"This function prints a 2x2 grid"""
    print('+', end=' ')
    print('- '*4, end= '')
    print('+', end=' ')
    print('- '*4, end= '')
    print('+')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|')
    print('+', end=' ')
    print('- '*4, end= '')
    print('+', end=' ')
    print('- '*4, end= '')
    print('+')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = ' ')
    print(' '*8, end= '')
    print('|')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = ' ')
    print(' '*8, end= '')
    print('|')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|', end = '')
    print(' '*8, end= ' ')
    print('|')
    print('|', end = ' ')
    print(' '*8, end= '')
    print('|', end = ' ')
    print(' '*8, end= '')
    print('|')
    print('+', end=' ')
    print('- '*4, end= '')
    print('+', end=' ')
    print('- '*4, end= '')
    print('+')
    return "Done"

def print_grid(lengthOfCell=2):
    """This function accepts a parameter to specify length/width (n x n) of the individual cells"""
    def grid_columns(lengthOfCell):
        """This function prints the horizontal borders of the grid. The length of these borders is specified by the input parameter"""
        print('+', end=' ')
        print('- '*lengthOfCell, end= '')
        print('+', end=' ')
        print('- '*lengthOfCell, end= '')
        print('+')
    def grid_row(lengthOfCell):
        """This function prints a row of vertical grid borders"""
        print('|', end = ' ')
        print(' '*(lengthOfCell*2), end= '')
        print('|', end = ' ')
        print(' '*(lengthOfCell*2), end= '')
        print('|')   
    grid_columns(lengthOfCell)
    for i in range(lengthOfCell):
        grid_row(lengthOfCell)
    grid_columns(lengthOfCell)
    for i in range(lengthOfCell):
        grid_row(lengthOfCell)
    grid_columns(lengthOfCell)
    return "Done"

def print_grid2(rowsAndColumnsLength=2, lengthOfCell=2):
    """This function accepts 2 parameters to print a customizable grid"""
    def createGridRowsBorder(rowsAndColumnsLength, lengthOfCell):
        """This prints a row border of user input row/column length and cell size"""
        print('+ ', end='')
        for i in range(rowsAndColumnsLength):
            print('- '*lengthOfCell, end= '+ ')
    def createGridColumnsBorder(rowsAndColumnsLength, lengthOfCell):
        """This prints a column line of user input row/column length and cell size"""
        print('|', end='')
        for i in range(rowsAndColumnsLength):
            print(' '*(lengthOfCell*2), end= ' |')
    def createCustomGrid(rowsAndColumnsLength, lengthOfCell):
        """This uses the previously written functions to print a customizable grid"""
        for i in range(rowsAndColumnsLength):
            createGridRowsBorder(rowsAndColumnsLength, lengthOfCell)
            print('')
            for i in range(lengthOfCell):
                createGridColumnsBorder(rowsAndColumnsLength, lengthOfCell)
                print('')
        createGridRowsBorder(rowsAndColumnsLength, lengthOfCell)   
    createCustomGrid(rowsAndColumnsLength, lengthOfCell)
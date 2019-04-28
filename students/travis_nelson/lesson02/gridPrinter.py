
def grid():
    """"Prints a 2x2 grid and returns a completion message."""
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
    """Prints a 2x2 grid of int parameter cell-length/width"""
    def grid_columns(lengthOfCell):
        """Prints the horizontal borders of the grid. The length of these borders is specified by the input parameter"""
        print('+', end=' ')
        print('- '*lengthOfCell, end= '')
        print('+', end=' ')
        print('- '*lengthOfCell, end= '')
        print('+')
    def grid_row(lengthOfCell):
        """Prints a row of vertical grid borders"""
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
    """Prints a grid of variable dimensions, as specified by the two int parameters"""
    def createGridRowsBorder(rowsAndColumnsLength, lengthOfCell):
        """Prints a row border of user input row/column length and cell size"""
        print('+ ', end='')
        for i in range(rowsAndColumnsLength):
            print('- '*lengthOfCell, end= '+ ')
    def createGridColumnsBorder(rowsAndColumnsLength, lengthOfCell):
        """Prints a column line of user input row/column length and cell size"""
        print('|', end='')
        for i in range(rowsAndColumnsLength):
            print(' '*(lengthOfCell*2), end= ' |')
    def createCustomGrid(rowsAndColumnsLength, lengthOfCell):
        """Prints the grid using the previously declared functions"""
        for i in range(rowsAndColumnsLength):
            createGridRowsBorder(rowsAndColumnsLength, lengthOfCell)
            print('')
            for i in range(lengthOfCell):
                createGridColumnsBorder(rowsAndColumnsLength, lengthOfCell)
                print('')
        createGridRowsBorder(rowsAndColumnsLength, lengthOfCell)   
    createCustomGrid(rowsAndColumnsLength, lengthOfCell)
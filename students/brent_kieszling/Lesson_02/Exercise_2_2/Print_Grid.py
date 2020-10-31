#-------------------------------------------#
#Tittle: Print_Grid, PYTHON210
#Desc: Print Grid Pattern
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Oct-25>, created file
#-------------------------------------------#


#PROCESS------------------------------------
def print_grid0():
    print("""\
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +""")



def print_grid(n):
    """Print a grid of 4 squares with side length equal to n
    
    Args:
        n (integer): input used to change table size
    """
    top = "+" + (" -" * n)
    side = "|" + ("  " * n)
    rows = 2
    while rows != 0:
        sideLength = n
        print(top, top, sep =" ", end = " +")
        print()
        while sideLength != 0:
            print( side, side, sep = " ", end =" |")
            print()
            sideLength -= 1
        rows -= 1
    print(top, top, sep =" ", end = " +")



def print_grid2(squareSize, gridSize):
    """Display a grid of squares (gridSize by gridSize).
    
    Args:
        squareSize (integer): Length of one side of the square.
        gridSize (integer): Number of rows and columns in the grid.
        
    """
    #Define patters for the top/bottom of the square and the sides.
    squareP1 = "+" + (" -" * squareSize)
    squareP2 = "|" + ("  " * squareSize)
    
    rows = gridSize
    #Builds each row of the grid one pattern at a time.
    while rows != 0:
        columnsTop = gridSize
        rowP2 = squareSize
        columnsBot = gridSize
        
        while columnsTop != 0:
            print(squareP1, end = " ")
            columnsTop -= 1
        print("+")
        
        while rowP2 != 0:
            columnsP2 = gridSize
            while columnsP2 !=0:
                print( squareP2, end =" ")
                columnsP2 -= 1
            print("|")
            rowP2 -= 1

        rows -= 1

    #Finishes last line of the grid
    while columnsBot != 0:
        print(squareP1, end = " ")
        columnsBot -= 1
    print("+")




#PRESENTATION INPUT/OUTPUT------------------
print_grid0()

print_grid(2)
print()

print_grid2(4, 6)

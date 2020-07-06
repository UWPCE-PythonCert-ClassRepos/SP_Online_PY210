def print_grid(gridSize=3):
    """
    Print a grid given one parameter

    :param gridSize: (int) grid size
    """

    if (gridSize >= 3):
        numUnits = int((gridSize-1)/2)
    else:
        print("Error: minimum grid size is 3")
        return
    
    print("+" + numUnits*" -" + " +" + numUnits*" -" + " +")
    
    for i in range(numUnits):
        print("|" + numUnits*"  " + " |" + numUnits*"  " + " |")

    print("+" + numUnits*" -" + " +" + numUnits*" -" + " +")

    for i in range(numUnits):
        print("|" + numUnits*"  " + " |" + numUnits*"  " + " |")

    print("+" + numUnits*" -" + " +" + numUnits*" -" + " +")

def print_grid2(numRowCol,numUnits):
    """
    Print a grid given two parameters

    :param numRowCol: (int) number of row and column of grid cells
    :param numUnits:  (int) number of units of each grid cell
    """

    if (numRowCol < 1 or numUnits < 1):
        print("Error: minimum number of row/column or unit is 1")
        return
    
    for row in range(numRowCol):
        for col in range(numRowCol):
            print("+ ", end="")
            print(numUnits*"- ", end="")
        print("+")

        for unit in range(numUnits):
            for col in range(numRowCol):
                print("| ", end="")
                print(numUnits*"  ", end="")
            print("|")

    for col in range(numRowCol):
        print("+ ", end="")
        print(numUnits*"- ", end="")
    print("+")


if (__name__ == "__main__"):
    print_grid(3)
    print_grid(4)
    print_grid(9)


    print_grid2(1,1)
    print_grid2(3,4)
    print_grid2(2,5)

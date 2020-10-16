# PY210 Lesson 02 Grid Printer - Chase Dullinger

def print_grid(n):
    horizontalLine = "+" + ((n-1)//2)*"-" + "+" + ((n-1)//2)*"-" + "+"
    verticalLine = "|" + ((n-1)//2)*" " + "|" + ((n-1)//2)*" " + "|"

    # range(n+2) accounts for the outer lines
    for i in range(n+2):
        # need to multiply by 2 before the mod operator to account
        # for the middle line.
        if (2*i) % (n+1) == 0:
            print(horizontalLine)
        else:
            print(verticalLine)

def print_grid2(nRowsCols,nUnits):
    horizontalLine = "+"
    verticalLine = "|"
    for i in range(nRowsCols):
        for j in range(nUnits):
            horizontalLine += "-"
            verticalLine += " "
        horizontalLine += "+"
        verticalLine += "|"

    for i in range(nRowsCols):
        for j in range(nUnits+1):
            if j==0:
                print(horizontalLine)
            else:
                print(verticalLine)
    print(horizontalLine) #print last horizontal line


if __name__=="__main__":
    print_grid(9)
    print("\n")
    print_grid(3)
    print("\n")
    print_grid(15)
    print("\n")
    print_grid2(3,4)
    print("\n")
    print_grid2(5,3)

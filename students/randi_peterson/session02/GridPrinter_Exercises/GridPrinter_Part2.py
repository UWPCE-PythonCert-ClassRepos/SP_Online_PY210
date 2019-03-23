#This Prints the grid for Part 2 of Lesson 2
#This code makes the Part 1 code into a function and considers user input

def GridPrinterPart2(n):
    """
    Print a grid of the size specified by the user
    """
    if n % 2 ==0:
        print("Error: Please re-run and enter an odd number or your grid may not be correct")
    else:
        number = n - 1
        dashes = "- " * int(number/2)
        spaces = " " *(len(dashes) + 1)
        horizontal_row = "+ " + dashes + "+ " + dashes + "+"
        bar_row = "|" + spaces + "|" + spaces + "|"
        print(horizontal_row)
        for x in range(0,int(number/2)):
            print(bar_row)
        print(horizontal_row)
        for x in range(0,int(number/2)):
            print(bar_row)
        print(horizontal_row)


#This Prints the grid for Part 3 of Lesson 2
#This code expands on part 2 to allow choosing of grid format and size

def GridPrinterPart3(dims,units):
    #Print grid of the size specified by the user
    dashes = "- " * units
    #Set spacing for upright bars
    spaces = " " *(len(dashes) + 1)

    #Creates +-+ rows, deletes extra space at the end of row
    horizontal_row = "+ " + dims*(dashes + "+ ")
    horizontal_row = horizontal_row[0:-1]
    bar_row = "|" + (spaces + "|")*dims

    #Prints the first row of + and -, then loops to create full grid
    print(horizontal_row)
    for row in range(0,dims):
        for x in range(0,units):
            print(bar_row)
        print(horizontal_row)
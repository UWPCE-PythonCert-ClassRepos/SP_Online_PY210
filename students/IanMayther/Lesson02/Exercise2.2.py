#Exercise2.2.py
import math

#CREATING STATIC GRID
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")

#CREATING GRID WITH ARBITRARY WIDTHS
def print_grid1(n):
    #arbitrary values
    x = math.ceil(n/2)
    y = 2
    #header to generate columns
    for t in range(y):
        line = ""
        #first row
        for g in range(y):
            for z in range(x): 
                if z == 0:
                    line = line + "+"
                else:
                    line = line + " -"
            line = line + " "
        print(line + "+")

        #Vertical Rows.
        for r in range(x-1):
            line = ""
            for w in range(y):
                for z in range(x+1): 
                    if z == 0:
                        line = line + "|"
                    elif z == x:
                        line = line + " "
                    else:
                        line = line + "  "
            line = line + "|"
            print(line)

    #Footer
    line = ""
    for z in range(y*x):
        if z == 0:
            line = line + "+"
        elif z >= x and x%z == 0:
            line = line + " +"
        else:
            line = line + " -"
    line = line + " +"
    print(line)

#CREATING A MULTIPLE INPUT FUNCTION
def print_grid2(n, m):
    #arbitrary values
    x = math.ceil(n/2)
    y = m
    #header to generate columns
    for t in range(y):
        line = ""
        #first row
        for g in range(y):
            for z in range(x): 
                if z == 0:
                    line = line + "+"
                else:
                    line = line + " -"
            line = line + " "
        print(line + "+")

        #Vertical Rows.
        for r in range(x-1):
            line = ""
            for w in range(y):
                for z in range(x+1): 
                    if z == 0:
                        line = line + "|"
                    elif z == x:
                        line = line + " "
                    else:
                        line = line + "  "
            line = line + "|"
            print(line)

    #Footer
    line = ""
    for z in range(y*x):
        if z == 0:
            line = line + "+"
        elif z >= x and z%x == 0:
            line = line + " +"
        else:
            line = line + " -"
    line = line + " +"
    print(line)


print_grid1(7)
print_grid2(10, 5)
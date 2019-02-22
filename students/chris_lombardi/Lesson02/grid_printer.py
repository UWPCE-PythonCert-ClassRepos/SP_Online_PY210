#UWPCE PY210
#Lesson02, Grid Printer

PLUS = "+"
MINUS ="-"
VERT_BAR = "|"

def print_grid(n):

    #Print Header/Footer Row
    print(PLUS, end=" ")
    for i in range(n//2):
        print(MINUS, end=" ")
    print(PLUS, end = " ")
    for i in range(n//2):
        print(MINUS, end = " ")
    print(PLUS)

    #Print Cell Rows
    for i in range(n//2):
        print("|", end = " ")
        for j in range(n//2):
            print(" ", end = " ")
        print("|", end = " ")
        for j in range(n//2):
            print(" ", end = " ")
        print("|")

    #Print Header/Footer Row
    print(PLUS, end=" ")
    for i in range(n//2):
        print(MINUS, end=" ")
    print(PLUS, end = " ")
    for i in range(n//2):
        print(MINUS, end = " ")
    print(PLUS)

    #Print Cell Rows
    for i in range(n//2):
        print("|", end = " ")
        for j in range(n//2):
            print(" ", end = " ")
        print("|", end = " ")
        for j in range(n//2):
            print(" ", end = " ")
        print("|")

    #Print Header/Footer Row
    print(PLUS, end=" ")
    for i in range(n//2):
        print(MINUS, end=" ")
    print(PLUS, end = " ")
    for i in range(n//2):
        print(MINUS, end = " ")
    print(PLUS)
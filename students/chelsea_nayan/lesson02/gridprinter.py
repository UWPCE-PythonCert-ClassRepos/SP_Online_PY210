#chelsea_nayan, PYTHON 210, UWPCE
#Lesson 02: Grid Printer Exercise


# PART I: This function prints out a static 2x2 grid
def gridprinter1():
    width = 1
    height = 4
    horizontal = '+ - - - - + - - - - +'
    vertical = '|         |         |'

    print(horizontal)
    i = 1
    while i < height-1:
        j = 0
        while j < height:
            print(vertical)
            j += 1
        print(horizontal)
        i += 1

gridprinter1()

#PART II: This function prints out a 2x2 grid at an arbitrary size. Size would indicate the number of dashes in the horizontal and the vertical per unit cell
def gridprinter2(size):
    square = 2
    horizontal = '+ ' + ('- ' * size)
    vertical = '| ' + (' '*(2*size))
    print(horizontal*square + '+')
    i = 1
    while i <= square:#2
        j = 0
        while j < size:#3
            print(vertical*square + '|')
            j += 1
        print(horizontal*square + '+')
        i += 1

gridprinter2(7)

#PART III: This function takes in two parameters that (1) determine the specified number of rows and columns and (2) the size of a cell unit

def gridprinter3(square, size):
    horizontal = '+ ' + ('- ' * size)
    vertical = '| ' + (' '*(2*size))
    print(horizontal*square + '+')
    i = 1
    while i <= square:#2
        j = 0
        while j < size:#3
            print(vertical*square + '|')
            j += 1
        print(horizontal*square + '+')
        i += 1

gridprinter3(8,2)

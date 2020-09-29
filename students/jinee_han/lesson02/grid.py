###-----------------------------
# Printing a Grid
# 06/24/2019 Jinee Han
# Python Programming Lesson 2
###--------------------------------

# 1. Printing a grid (2*2)

# Creating '+ - - - - + - - - - +'
def horizontal_line(a, b):
    for i in range(a):
        print ('+', end =" ")
        for j in range(b):
                print ('-', end =" ")
    print ('+')

# Creating '|       |       |'
def vertical_line(a,b):
    for i in range(a):
        print ('|', end =" ")
        for j in range(b):
            print (' ', end =" ")
    print ('|')

# Creating the grid with horizontal/vertical_line


def print_grid(a,b):
    for i in range (a):
        horizontal_line(a,b)
        for i in range (b):
            vertical_line(a,b)
    return horizontal_line(a,b)


print_grid(2,4)

# 2. Print adjustable size grid

print_grid(6,6)

# 3. Print with two parameters

print_grid(5,3)





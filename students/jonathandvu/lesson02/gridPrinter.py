#!/usr/bin/env python
# PY210 Lesson 2 Grid Printer Excercise
# Jonathan Vu 08/21/19
# 

# --------------------------------------------------------
# PART 1 - Print Basic Grid
# Assign Variables
plusRow = '+ - - - - + - - - - +' # Row with Plus Signs
vertRow = '|         |         |' # Row without Plus Signs

def grid_print(): # Iterate and print corresponding pattern
    for i in range(11):
        if i == 0 or i == 5 or i == 10:
            print(plusRow)
        else:
            print(vertRow)

# -------------------------------------------------------
# PART 2 - Print Grid with Variable Entered
def grid_print2(size):
    n = int(size/2) # Finds the median Plus row
    plusRow2 = '+' + (' -'*n) + ' +' + (' -'*n) + ' +' # Creates Plus Row
    vertRow2 = '|' + ('  '*n) + ' |' + ('  '*n) + ' |' # Creates Vert Row
    
    print(plusRow2) # Prints first row
    for vert in range(size): # Iterates to find median plus row
        if vert == n:
            print(plusRow2)
        else:
            print(vertRow2)
    print(plusRow2) # prints last row

# -------------------------------------------------------
# PART 3 - Print Grid with Two Variables Entered
def grid_print3(gridUnits, gridSpaces):
    plusRow3 = ('+' + (' -'*gridSpaces) + ' ')*gridUnits + '+'
    vertRow3 = ('|' + ('  '*gridSpaces) + ' ')*gridUnits + '|'
    
    for pluses in range(gridUnits):
        print(plusRow3)
        for dashes in range(gridSpaces):
            print(vertRow3)
    print(plusRow3) # Prints the last row

# Example Scripts
print("Example 1:")
grid_print()
print("Example 2:")
grid_print2(15)
print("Example 3:")
grid_print3(5,2)

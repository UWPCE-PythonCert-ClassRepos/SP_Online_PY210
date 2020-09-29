"""
rc = Rows or Columns

s = Space

"""

def grid_horizontal(rc,s):
    for i in range(rc):
        print('+', end= ' ')
        for j in range(s):
            print('-', end = ' ')
    print('+')
    
def grid_vertical(rc,s): #looking at the second parameter to correspond to the number of space
    for i in range(s):
        for j in range(rc): # Looking for column breaks
            print('|', end =' ')
            for j in range(s): # for each break get the number of space from the second parameter
                print(' ', end=' ')
        print('|') # print last "|"

def print_grid(rc,s):
    grid_horizontal (rc,s) #Print first horizontal grid line
    for i in range(rc): 
        grid_vertical(rc,s) #print the number of columns and also correspond to the number of space in the second parameter
        for j in range (1): #for each loop print a horizontal grid line
            grid_horizontal (rc,s)
#print_grid(2,2)
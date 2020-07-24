#! python

#----------------------------------------------
# Lesson 2 - Grid Printer Exercise
#----------------------------------------------

# Part 1 - Print a fixed 2 by 2 grid

x = '+' + (' -' * 4 + ' +') * 2
y = '|' + ('  ' * 4 + ' |') * 2

for i in range(2):
    print (x)
    for j in range(4):
        print (y)

print (x)                    # print last border line at the bottom



# Part 2 - Create a print_grid function with one parameter

def print_grid(n):

   # This function prints a 2 by 2 grid with specified size.
   # The input parameter n is an integer that defines the size of the grid.
   # The maximum size is 60. If input is greater than 80, it will default to 60.

   if n > 60:
     n = 30

   # Determine the size of a single cell
   q = n // 2

   x = '+' + (' -' * q + ' +') * 2
   y = '|' + ('  ' * q + ' |') * 2

   for i in range(2):
       print (x)
       for j in range(q):
           print (y)

   print (x)                    # print last border line at the bottom



def print_grid2(RowCol, CellSize):

   # This function prints a grid with specified number of rows and columns,
   # and with each cell a given size.
   # The maximum cell size is 15. If input is greater than 15, it will default
   # to 15.

   if CellSize > 15:
     CellSize = 15

   x = '+' + (' -' * CellSize + ' +') * RowCol
   y = '|' + ('  ' * CellSize + ' |') * RowCol

   for i in range(RowCol):
       print (x)
       for j in range(CellSize):
           print (y)

   print (x)                    # print last border line at the bottom


if __name__ == "__main__": 
    
    #test the print_grid function
    print_grid(3)
    print_grid(5)
    print_grid(9)  
  
    #test the print_grid2 function
    print_grid2(3,4)
    print_grid2(5,3)
    print_grid2(5,7)

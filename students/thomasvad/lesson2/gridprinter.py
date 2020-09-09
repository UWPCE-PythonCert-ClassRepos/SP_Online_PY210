def line1(col,size=1):
    for i in range(col):
        print('+'+'-'*size,end='')
    print('+')
    
def line2(col,size=1):
    for i in range(col):
        print('|'+' '*size,end='')
    print('|')
	
# print 2x2 grid size 4X4 cells	
def grid():
    for i in range(2):
        line1(2,4)
        for i in range(4):
            line2(2,4)
    line1(2,4) 	

#prints 2x2 grid any size cells
def print_grid(size):
    for i in range(2):
        line1(2,size)
        for i in range(size):
            line2(2,size)
    line1(2,size) 
	
#Prints grid with a specified number of rows,columns, and cell size.
def print_grid2(col,row,size):
    for i in range(row):
        line1(col,size)
        for i in range(size):
            line2(col,size)
    line1(col,size) 


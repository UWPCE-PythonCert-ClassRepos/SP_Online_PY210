""" Grid Printer Exercise for Lesson 2"""
#by Reem Alqaysi
"""function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
def print_grid_1():
	#rows loop
	row = ("+" + ("-"*4))*2
	for i in range(0,2):
		print (row + "+")
		#"|" loop
		for v in range(0,4):
			print (("|"+" "*4)*2+"|")
	print (row + "+") 

#function that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.
def print_grid_2(x):
	n=int(x/2)
	row = '+'+('-'*n)
	for i in range(2):
		print(row*2 +"+")
		for v in range(n):
			print (("|"+" "*n)*2+"|")
	print (row *2 + "+")


#function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.
#def print_grid_3(x,y):
def print_grid_3(x,y):
    row = '+'+('-'*y)
#loop to draw given rows x
    for i in range(0,x): 
        print((row * x) +'+')
# loop to draw columns x per row      
        for v in range(0,y): 
            print((('|'+(' '*y))*(x))+'|')
# print the last line   
    print((row * x) +'+')



if __name__ == "__main__":
    print_grid_1()
    print_grid_2(5)
    print_grid_3(5,5)

## Lesson 2 Assignment Grid Printer
## By: B. Matthews
## 9/8/2020

#import math
plus = '+ '
minus = '- '
pipe = '|'

count = 4
#grid = math.sqrt(count)
grid = 2

print (plus + minus*count + plus, end='') 
print (minus*count + plus)

while grid:

	i=count
	while i>0 :
		cell = pipe + ' '*count*2 + ' '
		print (cell*3)
		#print()
		i-=1

	print (plus + minus*count + plus, end='')
	print (minus*count + plus)
	
	grid-=1

#def print_grid(n):




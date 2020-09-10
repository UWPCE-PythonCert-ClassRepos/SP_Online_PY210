## Lesson 2 Assignment Grid Printer, Part 2
## By: B. Matthews
## 9/8/2020

#import math

def print_grid(n):

	if n<=0:
		print("sorry, it's so small you can't see it.")
		return None

	plus = '+ '
	minus = '- '
	pipe = '|'

	count = n
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

	print ('Done!!')

print_grid(12)



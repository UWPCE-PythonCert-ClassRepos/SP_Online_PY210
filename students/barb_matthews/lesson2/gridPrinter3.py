## Lesson 2 Assignment Grid Printer, Part 3
## By: B. Matthews
## 9/9/2020

def print_grid(rowsandcol,units):

	if rowsandcol<=0 or units<=0:
		print("sorry, it's so small you can't see it.")
		return None

	plus = '+ '
	minus = '- '
	pipe = '| '

	for i in range(rowsandcol):
		print ((plus + minus * units) * rowsandcol + plus)
		for i in range(units):
			print ((pipe + ' ' * units * 2) * rowsandcol + pipe)

	print ((plus + minus * units) * rowsandcol + plus)
	print ('Done!!')

print_grid(6,3)



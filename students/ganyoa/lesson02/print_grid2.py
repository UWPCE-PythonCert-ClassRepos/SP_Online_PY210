def printgrid2(a,b):
	'''
	Prints a grid; size of each square and number of rows/columns based on variable input. 

	:param a: sets number of rows and columns
	:param b: sets the number of lines/dashes per quadrant
	'''
	for i in range(a):	
		for i in range(a):
			print('+ ',end='')
			print('- '*b,end='')
		print('+')	
		
		for i in range(b):
			for i in range(a):
				print('| ',end='')
				print('  '*b,end='')
			print('|')
	
	for i in range(a):
		print('+ ',end='')
		print('- '*b,end='')
	print('+')
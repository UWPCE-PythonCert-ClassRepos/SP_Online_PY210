def print_grid(a):
	'''
	Print a 2x2 grid; input value (a) sets the size with the number of dashes/lines per quadrant.
	'''
	print('+','- '*a+'+','- '*a+'+')
	
	for i in range(a):
		print('|','  '*a+'|','  '*a+'|')
	print('+','- '*a+'+','- '*a+'+')
	
	for i in range(a):
		print('|','  '*a+'|','  '*a+'|')
	print('+','- '*a+'+','- '*a+'+')
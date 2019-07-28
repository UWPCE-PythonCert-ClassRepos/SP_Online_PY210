n = 15 # enter the grid size


def print_grid(n):
	b = n/2-.5
	b = int(b)
	#print(b)

	
	for i in range(n):

		if i == 0 or i ==b or i == n-1:
			print('+','- '*b +'+','- '*b +'+')
			
		else:
			print('|','  '*b +'|','  '*b +'|')

		if i == 0:
			print('|','  '*b +'|','  '*b +'|')

		if n%2 != 0 and i == n-2:
			print('|','  '*b +'|','  '*b +'|')
					
	print()
			
			
print_grid(n)		
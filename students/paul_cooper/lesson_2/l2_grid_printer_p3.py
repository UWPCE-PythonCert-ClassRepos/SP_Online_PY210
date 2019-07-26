n = 4 #enter the nuber of nxn squares
q = 5 #enter the nuber of dash lines in the squares

def print_grid(n,q):
	print('+',('- '*q +'+ ')*n)

	for i in range(n):
		for j in range(q):
			print('|',('  '*q +'| ')*n)
		print('+',('- '*q +'+ ')*n)



	
print_grid(n,q)
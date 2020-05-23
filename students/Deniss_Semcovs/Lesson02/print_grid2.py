 def print_grid(m,n):
	addl1 = (" -"*(n)+" +")
	addl2 = ("  "*(n)+" |")
	for i in range(m):
		print("+"+(addl1*m))
		for i in range(n):
			print("|"+(addl2*m))
	print("+"+(addl1*m))
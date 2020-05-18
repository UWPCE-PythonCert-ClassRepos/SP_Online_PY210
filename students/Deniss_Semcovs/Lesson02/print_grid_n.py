 def print_grid(n):
	line1 = ("+"+" -"*(n)+" +"+" -"*(n)+" +")
    line2 = ("|"+"  "*(n)+" |"+"  "*(n)+" |")
    print(line1)
	for i in range(n):
		print(line2)
    print(line1)
	for i in range(n):
		print(line2)
    print(line1)
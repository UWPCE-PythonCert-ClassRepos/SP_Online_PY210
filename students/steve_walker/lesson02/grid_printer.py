def print_grid(x,y):
	
	# create the horizontal (cross) lines
	segment = " -"
	str = segment*x
	section = "+"
	
	for i in range(x):
		section =  section + str[i]
	
	cross = section*(y-1) + "+"

	# create the vertical lines
	vertrow = ("|"+" "*x)*(y-1) + "|"
	vertline = ""
	
	for i in range(round(x/2)):
		vertline = vertline + vertrow + "\n"
	
	vertline = vertline[:-1]
	
	# print the grid
	for i in range(y-1):
		print(cross)
		print(vertline)
	print(cross)

print_grid(9,5)

# To the teacher: let me know if you'd like error messages for invalid
# inputs (like negative numbers) or whether I can trust you to behave!

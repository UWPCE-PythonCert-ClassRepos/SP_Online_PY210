def print_grid(num,size):
	plus = "+ "
	minus = "- "
	endline = "| "
	space = "  "
	top = (plus + minus * (size))*num + plus
	line = (endline+ ((size)*space))*num + endline
	i=0
	j=0
	m=0
	print(top)
	while m < num:
		while i < (size):
			print(line)
			i += 1
		print(top)
		i=0
		m += 1
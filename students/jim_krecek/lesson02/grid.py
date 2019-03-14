def print_grid():
	#prints 2x2 grid
	#part 1
	plus = "+ "
	minus = "- "
	endline = "| "
	space = "  "
	top = (plus + minus * (4))*2 + plus
	line = (endline+ ((4)*space))*2 + endline
	i=0
	print(top)
	while i < 4:
		print(line)
		i += 1
	print(top)
	i=0
	while i < 4:
		print(line)
		i += 1
	print(top)


def print_grid2(n):
	#part 2
	plus = "+ "
	minus = "- "
	endline = "| "
	space = "  "
	top = (plus + minus * (n//2))*2 + plus
	line = (endline+ ((n//2)*space))*2 + endline
	i=0
	print(top)
	while i < n//2:
		print(line)
		i += 1
	print(top)
	i=0
	while i < n//2:
		print(line)
		i += 1
	print(top)


def print_grid3(num,size):
	#part 3
	plus = "+ "
	minus = "- "
	endline = "| "
	space = "  "
	top = (plus + minus * (size))*num + plus
	line = (endline+ ((size)*space))*num + endline
	i=0
	m=0
	print(top)
	while m < num:
		while i < (size):
			print(line)
			i += 1
		print(top)
		i=0
		m += 1
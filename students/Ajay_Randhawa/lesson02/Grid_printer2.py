def print_grid2(s, n):
	plus = "+"
	minus = "- "
	space = " "
	bar = "|"
	startPattern1 = plus + space
	endPattern1 = plus
	startPattern2 = bar + space
	endPattern2 = bar
	for i in range(0,s,1):
		print(s*(startPattern1 + n*(minus)) + endPattern1)
		for j in range(0,s,1):
			print((s)* (startPattern2 + 2*n*space) + endPattern2)
	print(s*(startPattern1 + n*(minus)) + endPattern1)
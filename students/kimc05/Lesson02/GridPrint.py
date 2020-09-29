def print_grid(n):
	size = n // 2
	plusline = "+ " + (("- " * size) + "+ ") *2
	sideline = "| " + (("  " * size) + "| ") *2
	for x in range(2):
		print(plusline)
		for x in range(size):
			print(sideline)
	print(plusline)

print_grid(9)
print_grid(3)
print_grid(15)

def print_grid2(x,y):
	plusline = "+ " + (("- " * y) + "+ ") *x
	sideline = "| " + (("  " * y) + "| ") *x
	for x in range(x):
		print(plusline)
		for x in range(y):
			print(sideline)
	print(plusline)

print_grid2(3,4)
print_grid2(5,3)
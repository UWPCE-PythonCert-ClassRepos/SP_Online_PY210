#/usr/bin/env python3


def buttress(a, b):
	buttress = '+ '
	for i in range(a):
		buttress += '- '
	return ((buttress * b) + '+')

def row(a, b):
	row = '| '
	for i in range(a):
		row += '  '
	return ((row * b) + '|')

def make_box(a, b):
	bttrs = buttress(a, b)
	rw = row(a, b)
	for i in range(a):
		print(bttrs)
		for i in range(b):
			print(rw)
	print(bttrs)


def main():
	make_box(4, 5)

if __name__ == "__main__":
	main()
def formatString(a,b,c,d):
	A = str(a).zfill(3)
	A = "file_" + A
	print(A)
	B = float("{:.2f}".format(b))
	print(B)
	C = "{:.2e}".format(c)
	print(C)
	D = "{:.2e}".format(d)
	print(D)
def task2(a,b,c,d):
	A = f'{a:03d}'
	print(A)
	B = f'{b:.2f}'
	print(B)
	C = f'{c:.2e}'
	print(C)
	d = f'{d:.2e}'
	print(d)
def formatter(in_tuple):
	a = len(in_tuple)
	format_string = f'the {a} numbers are:'
	while a>0:
		if a>1:
			format_string = format_string + " {},"
		else:
			format_string = format_string + " {}"
		a = a-1
	print(format_string)
	return format_string.format(*in_tuple)
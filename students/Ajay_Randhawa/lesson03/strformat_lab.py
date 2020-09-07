def formatString(a,b,c,d):
	#Function for Task1
	#pad the integer with zero for a total of 3 numbers
	#convert the integer into a string to form the output
	A = str(a).zfill(3)
	A = "file_" + A
	print(A)
	#format the float to use only 2 decimal places.
	B = float("{:.2f}".format(b))
	print(B)
	#format the integer to use 2 decimal places with scientific notation
	C = "{:.2e}".format(c)
	print(C)
	#format the integer to use 2 decimal places with scientific notation
	D = "{:.2e}".format(d)
	print(D)

def task2(a,b,c,d):
	#Task2
	#use f-string to pad integer with 0s
	A = f'{a:03d}'
	print(A)
	#use f-string to format float to 2 decimal places
	B = f'{b:.2f}'
	print(B)
	#use f-string to change int to scientific notation with 2 decimal places
	C = f'{c:.2e}'
	print(C)
	#use f-string to change int to scientific notation with 2 decimal places
	d = f'{d:.2e}'
	print(d)

def formatter(in_tuple):
	#Task3
	#store the length of the tuple
	a = len(in_tuple)
	#add the lenth of the tuple to the string
	format_string = f'the {a} numbers are:'
	#add place holders for the tuple values
	while a>0:
		if a>1:
			format_string = format_string + " {},"
		else:
			format_string = format_string + " {}"
		a = a-1
	#return string with tuple values
	return format_string.format(*in_tuple)
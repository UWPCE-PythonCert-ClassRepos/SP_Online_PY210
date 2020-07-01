#/usr/bin/env python3

def scientific_notation(num):
	return "{:e}".format(num)

def task_one(tup):	

	file_name = "file_" + str(tup[0]).zfill(3)

	rounded_num = round(tup[1], 2)

	first_exponent = scientific_notation(tup[2])

	second_exponent = scientific_notation(tup[3])

	return "{0:1} {1:3} {2:1} {3} {4} {5} {6}".format(file_name, ":", rounded_num, ",", first_exponent, ",",second_exponent)

def task_two(tup):
	# file_name = format_file_num(tup[0])

	file_name = "file_" + str(tup[0]).zfill(3)

	rounded_num = round(tup[1], 2)

	first_exponent = scientific_notation(tup[2])

	second_exponent = scientific_notation(tup[3])

	return F"{file_name}:   {rounded_num}, {first_exponent}, {second_exponent}"

def task_three(tuple_):
	len_tup = len(tuple_)
	tup = [x for x in tuple_]
	string = "The {} numbers are: ".format(len_tup)
	for i in tup:
	 	string += "{:d} "
	return string.format(*tuple_)

def task_four(tuple_):
	tuple_to_list= [ tuple_[tuple_.index(member)] if len(str(tuple_[tuple_.index(member)])) > 1 else str(tuple_[tuple_.index(member)]).zfill(2) for member in tuple_ ]

	string = ""
	for element in tuple_to_list:
		string += "{} "
	
	return string.format(*tuple_to_list)

def task_five(list_):
	return f"The weight of an {p[0].upper()} is {p[1] * 1.2} and the weight of a {p[2]} is {p[3]}"

def task_six():
	ar = ['First', '$99.01', 'Second', '$88.09']

	arr = ['First', '$993333.01', 'Second', '$80000008.09']

	#print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))
	print(ar[0].ljust(20) + ar[1].ljust(10) + ar[2].ljust(20) + ar[3].ljust(8))


	# If the string of numbers between the $ and . is more than 2, find out by how much and return that figure
	def adjust(p):
		dollar_index = p.find('$') + 1
		dot_index = p.find('.')
		range_ = dot_index - dollar_index
		if range_ > 2:
			return range_ - 2
		else:
			return 0

	price_one_width = adjust(arr[1])
	price_two_width = adjust(arr[3])


	# Adjust the ljust by how much extra characters there are in the prices
	t = arr[0].ljust(20 - price_one_width) + arr[1].ljust(10 + price_one_width) + arr[2].ljust(20 - price_two_width) + arr[3].ljust(8 + price_two_width)

	print(t)



def main():
	# print(task_one((2, 123.4567, 10000, 12345.67)))
	#print(task_two((2, 123.4567, 10000, 12345.67)))
	#print(task_three((1,2,3)))
	# print(task_four((1,2,3,4,5)))
	# print(task_five(['oranges', 1.3, 'lemons', 1.1]))
	task_six()


	
if __name__ == "__main__":
	main()
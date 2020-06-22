#/usr/bin/env python3

# with the first and last items exchanged

def exchange_first_last(seq):	
	def switch(input_):
		output = input_
		reverse = input_[::-1]
		output[0:1] = reverse[0:1]
		output[-1] = reverse[-1]
		return output
		
	if type(seq) == tuple:
		return tuple(switch(list(seq)))
	elif type(seq) == str:
		return ''.join(switch(list(seq)))
	else:
		print('Please input a string or tuple')

def every_other_removed(seq):
	if type(seq) == tuple:
		output = list(seq)
		return tuple(output[::2])
	elif type(seq) == str:
		return seq[::2]
	else:
		print('Please input a string or tuple')

# with the first 4 and the last 4 items removed, and the nevery other item in the remaning sequence
def first_and_last_four_removed(seq):
	if type(seq) == str:
		return seq[4:-4]
	elif type(seq) == tuple:
		output = list(seq)
		return tuple(output[4:-4])
	else:
		print('Please input a string or tuple')

#with the elements reversed (just with slicing)
def elements_reversed(input):
	if type(input == str):
		# return reverse(input)
		return input[::-1]

	elif type(seq) == tuple:
		output = list(seq)
		return tuple(output[::-1])

# Pass
assert exchange_first_last("hello") == "oellh"
assert exchange_first_last((1,2,3)) == (3,2,1)

# Pass
assert every_other_removed("hello") == "hlo"
assert every_other_removed((1,2,3,4,5)) == (1,3,5)

# Pass 
assert first_and_last_four_removed("helloworld") == "ow"
assert first_and_last_four_removed((1,2,3,4,5,6,4,3,2,1)) == (5,6) 

# Pass
assert elements_reversed("hello") == "olleh"
assert elements_reversed((1,2,3)) == (3,2,1)


print("All tests pass")


# with every other item removed

# def main():
#     print(exchange_first_last("hello world")

# if __name__ == "__main__":
#     main()



# switch first and last
# first = _input[0]
# last = _input[-1]
# _list = [char for char in _input]
# _list[-1] = first
# _list[0] = last

# exclude first and last four
# output = [_input[i] for i in range(4, length - 4)]
# print(''.join(output))

# elements reversed
# return seq[::-1]

#midrange
	# for i in range(length):
	# 	index = int(len(_input)/3)
		# return [_input[j] for j in range(index)]
		# return [_input[-j] for j in range(index)]
		# return [_input[j] for j in range(index, length-index)]

def firstLast(seq):
	""" switches the first and last values of a sequence"""
	seq1 = seq[-1:] + seq[1:-1] + seq[:1]
	return seq1

def everyOther(seq):
	""" using the step function to return
	every other item in sequence"""
	seq1 = seq[::2]
	return seq1

def function3(seq):
	"""removes first 4 and last 4 items, and
	then evey other item in the sequence"""
	seq1 = seq[4:-4:2]
	return seq1

def function4(seq):
	""" reverses elements in a sequence"""
	seq1 = seq[::-1]
	return seq1

def function5(seq):
	"""last third, then first third, then
	the middle thrid in the new order"""
	x = len(seq)//3
	seq1 = seq[(-1*(len(seq)//3)):]
	seq2 = seq1[:((len(seq1)//3))]
	seq3 = seq2[((len(seq2)//3)):(-1*(len(seq2)//3))]
	return seq3

a_string = "this is a string"
a_tuple = (2,54,13,12,5,32)
a_short_list = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
a_long_string = "blahblahblahblahblahblahblahblahblah***hblahblahblah"

assert firstLast(a_string) == "ghis is a strint"
assert firstLast(a_tuple) == (32,54,13,12,5,2)
assert everyOther(a_string) == "ti sasrn"
assert everyOther(a_tuple) == (2, 13, 5)
assert function3(a_string) == " sas"
assert function3(a_short_list) == (4,6,8,10,12,14)
assert function4(a_string) == "gnirts a si siht"
assert function4(a_tuple) == (32,5,12,13,54,2)
assert function5(a_long_string) == "***"
def exchange_first_last(seq):
	return seq[-1:] + seq[1:-1] + seq[:1]

def every_other(seq):
	return seq[0::2]

def f4_l4(seq):
	return seq[4:-4:2]

def rev(seq):
	return seq[::-1]

def rearrange(seq):
	third = len(seq)//3
	return seq[third*2:] + seq[:third*2]

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
assert every_other(a_string) == 'ti sasrn'
assert every_other(a_tuple) == (2, 13, 5)
assert every_other(a_list) == [1, 3, 5, 7, 9]
assert f4_l4(a_string) == ' sas'
assert f4_l4(a_tuple) == ()
assert f4_l4(a_list) == [5]
assert rev(a_string) == 'gnirts a si siht'
assert rev(a_tuple) == (32, 5, 12, 13, 54, 2)
assert rev(a_list) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert rearrange(a_string) == 'stringthis is a '
assert rearrange(a_tuple) == (5, 32, 2, 54, 13, 12)
assert rearrange(a_list) == [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
print("You've passed")
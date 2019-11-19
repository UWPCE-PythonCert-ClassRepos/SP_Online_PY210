
def exchange_first_last(seq):
	return(seq[-1:] + seq[1:-1] + seq[:1])

exchange_first_last("abcdefghi")

def remove_every_other(seq):
	return(seq[::2])

remove_every_other("abcdef")

def first4_last4_every_other(seq):
	return(seq[4:-4:2])

first4_last4_every_other("abcdefghijklmno")

def reverse_seq(seq):
	return(seq[::-1])

reverse_seq("abcdef")

def third_bump(seq):
	return(seq[int(len(seq)/3*2):]+seq[:int(len(seq)/3)]
	+seq[int(len(seq)/3):int(len(seq)/3*2)])
	
	

a_string = "abcdefghi"
a_tuple = (2, 54, 13, 12, 5, 32)
a_long_string = "abcdefghijklmnop"
a_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)


if __name__ == "__main__":
	assert exchange_first_last(a_string) == "ibcdefgha"
	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
	
	assert remove_every_other(a_string) == "acegi"
	assert remove_every_other(a_tuple) == (2, 13, 5)
	
	assert first4_last4_every_other(a_string) == "e"
	assert first4_last4_every_other(a_tuple) == ()
	assert first4_last4_every_other(a_long_string) == "egik"
	assert first4_last4_every_other(a_long_tuple) == (5, 7, 9, 11)
	
	assert reverse_seq(a_string) == "ihgfedcba"
	assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)
	
	assert third_bump(a_string) == "ghiabcdef"
	assert third_bump(a_tuple) == (5, 32, 2, 54, 13, 12)
	
	print("tests passed. clear skies ahead.")

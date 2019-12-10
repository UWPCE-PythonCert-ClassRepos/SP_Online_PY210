
def exchange_first_last(seq):
	return(seq[-1:] + seq[1:-1] + seq[:1])

def remove_every_other_item(seq):
	return(seq[::2])

def first4_last4_every_other_item(seq):
	return(seq[4:-4:2])

def reversed(seq):
	return(seq[::-1])

def third_new_order(seq):
	return(seq[int(len(seq)/3*2):] + seq[:int(len(seq)/3)]
	+ seq[int(len(seq)/3):int(len(seq)/3*2)])

#tests
print(exchange_first_last("1234567"))
print(remove_every_other_item("1234567"))
print(first4_last4_every_other_item("123456789"))
print(reversed("1234567"))
print(third_new_order("123456789"))

#assert tests
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

if __name__ == "__main__":
	assert exchange_first_last(a_string) == "ghis is a strint"
	assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

	assert remove_every_other_item(a_string) == "ti sasrn"
	assert first4_last4_every_other_item(a_string) == " sas"
	assert reversed(a_string) == "gnirts a si siht"
	assert third_new_order(a_string) == "stringthis is a "

	print("Assert tests passed!")

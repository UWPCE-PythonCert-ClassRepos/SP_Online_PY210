a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

def exchange_first_and_last(seq):
    return seq[-1:] + seq[1:len(seq) - 1] + seq[:1]

assert exchange_first_and_last(a_string) == "ghis is a strint"
assert exchange_first_and_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def remove_every_other(seq):
    return seq[::2]
assert remove_every_other(b_tuple) == (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)

def first_4_last_4(seq):
    return seq[4:len(seq) - 4:4]

print(first_4_last_4(a_tuple))

def elements_reversed(seq):
    return seq[::-1]
assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

def first_3rd_last_3rd_middle(seq):
    return seq[3:len(seq)-3:3]
print(first_3rd_last_3rd_middle(a_tuple))

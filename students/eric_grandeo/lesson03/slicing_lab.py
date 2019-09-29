#first and last item exchanged
def exchange_first_last(seq):
    first = seq[:1]
    last = seq[-1:]
    return last + seq[1:-1] + first


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
print("exchange_first_last tests passed" )

#every other item removed

def every_other_item(seq):
    return seq[::2]

assert every_other_item(a_string) == "ti sasrn"
assert every_other_item(a_tuple) == (2, 13, 5)
print("every_other_item tests passed")

#with the first 4 and the last 4 items removed,
#and then every other item in the remaining sequence.

a_tuple_2 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
a_string_2 = "This is a really long string for a test"


def first4_last4_every_other(seq):
    return seq[4:-4:2]

assert first4_last4_every_other(a_tuple_2) == (5, 7, 9, 11)
assert first4_last4_every_other(a_string_2) == ' saral ogsrn o  '
print("first4_last4 tests passed")


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



def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] +seq[0:1]

def remove_every_other(seq):
    return seq[::2]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
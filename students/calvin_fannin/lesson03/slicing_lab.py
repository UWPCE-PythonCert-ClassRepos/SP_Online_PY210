def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] +seq[0:1]

def remove_every_other(seq):
    return seq[::2]

def remove_items(seq):
    return remove_every_other(seq[4:-4])

def reverse_sequence(seq):
    return seq[-1::-1]

def reverse_thirds(seq):
    third = len(seq) // 3
    return seq[third * 2:] + seq[third:third * 2] + seq[:third]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
b_string = "ABCDEFGHIJKL"
b_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
short_string = "Mike"
short_tuple = (9, 8, 7)
palindrom_string = "rotator"
c_string = "The quick brown fox jump over the lazy dog"
c_tuple = (7, 'dog', 5.0, 3, 2, 1, 4, 5, 7)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert remove_every_other(b_string) == "ACEGIK"
assert remove_every_other(b_tuple) == (0, 2, 4, 6, 8)
assert remove_every_other(c_tuple) == (7, 5.0, 2, 4, 7)
assert remove_items(b_tuple) == (4,)
assert reverse_sequence(c_string) == "god yzal eht revo pmuj xof nworb kciuq ehT"
assert reverse_sequence(palindrom_string) == "rotator"
assert reverse_thirds(c_tuple) == (4, 5, 7, 3, 2, 1, 7, 'dog', 5.0)


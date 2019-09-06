def swap_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
    return seq[::2]


def drop_every_4(seq):
    return seq[4:-4]


def reserve_elements(seq):
    return seq[::-1]


def new_world_order(seq):
    third = int(len(seq) / 3)
    return seq[third:-third] + seq[-third:] + seq[:third]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
long_string = "this is a longer string"
long_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

assert swap_first_last(a_string) == "ghis is a strint"
assert swap_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
print("swap_first_last passed!")

assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)
print("every_other passed!")

assert drop_every_4(long_string) == " is a longer st"
assert drop_every_4(long_tuple) == (4, 5, 6)
print("drop_every_4 passed!")

assert reserve_elements(a_string) == "gnirts a si siht"
assert reserve_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
print("reserve_elements passed!")

assert new_world_order(a_string) == "is a stringthis "
assert new_world_order(a_tuple) == (13, 12, 5, 32, 2, 54)
print("new_world_order passed!")

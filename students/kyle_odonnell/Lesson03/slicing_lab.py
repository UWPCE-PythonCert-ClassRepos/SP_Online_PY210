# the first and last items exchanged
def exchange_first_last(seq):
    return seq[-1::] + seq[1:-1] + seq[0:1]


# every other item removed
def remove_every_other(seq):
    return seq[0::2]


# the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove_four_and_every_other(seq):
    if len(seq) > 8:
        mid = seq[4:-4]
        ans = mid[0::2]
    else:
        ans = "Not enough items in sequence"
    return ans


# the elements reversed (just with slicing)
def reverse_seq(seq):
    return seq[::-1]


# the last third, then first third, then the middle third in the new order.
def reorder_thirds(seq):
    third = len(seq)//3
    return seq[-third::] + seq[:third] + seq[third:-third]


# Test Functions
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [2, 54, 13, 12, 5, 32]
b_tuple = (4, 7, 34, 53, 9, 85, 34, 50, 24, 13, 25, 68, 94)
b_list = [4, 7, 34, 53, 9, 85, 34, 50, 24, 13, 25, 68, 94]


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [32, 54, 13, 12, 5, 2]
assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)
assert remove_every_other(a_list) == [2, 13, 5]
assert remove_four_and_every_other(a_string) == ' sas'
assert remove_four_and_every_other(a_tuple) == "Not enough items in sequence"
assert remove_four_and_every_other(b_tuple) == (9, 34, 24)
assert remove_four_and_every_other(b_list) == [9, 34, 24]
assert reverse_seq(a_string) == "gnirts a si siht"
assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)
assert reverse_seq(a_list) == [32, 5, 12, 13, 54, 2]
assert reorder_thirds(a_string) == "tringthis is a s"
assert reorder_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
assert reorder_thirds(a_list) == [5, 32, 2, 54, 13, 12]
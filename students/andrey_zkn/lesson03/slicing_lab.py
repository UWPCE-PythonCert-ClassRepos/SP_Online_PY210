
# Sequence with the first and last items exchanged.
def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
    new_sequence = last_item + seq[1:-1] + first_item
    return new_sequence


# Sequence with every other item removed.
def every_other_item(seq):
    new_sequence = seq[::2]
    return new_sequence


# Sequence with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove_first_last_four_everyother(seq):
    return seq[4:-4:2]
	

# Sequence with the elements reversed (just with slicing).
def reverse(seq):
    return seq[::-1]
	

# Sequence with the last third, then first third, then the middle third in the new order.
def thirds_new_order(seq):
    thirds =  len(seq) // 3
    return (seq[2*thirds:]+seq[:thirds]+seq[thirds:2*thirds])


# Test
a_string = "this is the longest string I have ever seen"
a_tuple = (2, 54, 13, 12, 5, 32, 10, 54, 78, 83, 24, 61)

assert exchange_first_last(a_string) == "nhis is the longest string I have ever seet"
assert exchange_first_last(a_tuple) == (61, 54, 13, 12, 5, 32, 10, 54, 78, 83, 24, 2)
assert every_other_item(a_string) == "ti stelnetsrn  aeee en"
assert every_other_item(a_tuple) == (2, 13, 5, 10, 78, 24)
assert remove_first_last_four_everyother(a_string) == " stelnetsrn  aeee"
assert remove_first_last_four_everyother(a_tuple) == (5, 10)
assert reverse(a_string) == "nees reve evah I gnirts tsegnol eht si siht"
assert reverse(a_tuple) == (61, 24, 83, 78, 54, 10, 32, 5, 12, 13, 54, 2)
assert thirds_new_order(a_string) == " have ever seenthis is the longest string I"
assert thirds_new_order(a_tuple) == (78, 83, 24, 61, 2, 54, 13, 12, 5, 32, 10, 54)


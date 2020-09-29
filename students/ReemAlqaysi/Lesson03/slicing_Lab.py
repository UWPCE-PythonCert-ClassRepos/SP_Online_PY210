
#sequence with the first and last items exchanged.
def exchange_first_last(seq):
    first = seq[-1:]
    mid = seq[1:-1]
    last = seq[:1]
    a_new_sequence = first + mid + last
    return a_new_sequence

#sequence with every other item removed.
def remove_every_oher_item(seq):
    a_new_sequence = seq[::2]
    return a_new_sequence


#sequence with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove_first_last4(seq):
	a_new_sequence = seq[4:-4]
	return a_new_sequence

#sequence with the elements reversed (just with slicing).
def elements_reversed(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

#sequence with the last third, then first third, then the middle third in the new order.
def difrent_sequence(seq):
    midthird = len(seq)//3
    first = seq[:midthird]
    mid = seq[midthird:-midthird]
    last = seq[-midthird:]
    a_new_sequence = last + first + mid
    return a_new_sequence



# block of code that use series of assert statements that demonstrate the all functions work properly.
if __name__ == "__main__":

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_oher_item(a_string) == "ti sasrn"
    assert remove_every_oher_item(a_tuple) ==  (2, 13, 5)
    assert remove_first_last4(a_string) == " is a st"
    assert remove_first_last4(a_tuple) == ()
    assert elements_reversed(a_string) == "gnirts a si siht"
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert difrent_sequence(a_string) =="tringthis is a s"
    assert difrent_sequence(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("tests passed")
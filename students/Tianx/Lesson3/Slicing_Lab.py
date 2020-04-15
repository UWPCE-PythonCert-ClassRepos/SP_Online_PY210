# ------------------------------------------#
# Title: Slicing_Lab.py
# Desc: Get the basics of sequence slicing down.
# Tian Xie, 2020-04-05, Created File
# ------------------------------------------#
# with the first and last items exchanged.
def exchange_first_last(seq):
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence


# with every other item removed.
def remove_every_other(seq):
    a_new_sequence = seq[::2]
    return a_new_sequence


# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def remove_first_last_4(seq):
    a_new_sequence = seq[4:-4]
    return a_new_sequence


# with the elements reversed (just with slicing).
def reverse_elements(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence


# with the last third, then first third, then the middle third in the new order.
def new_order(seq):
    mid_third = len(seq) // 3
    last = seq[-mid_third:]
    first = seq[:mid_third]
    middle = seq[mid_third:-mid_third]
    a_new_sequence = last + first + middle
    return a_new_sequence


# Run some tests
if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5,)
    assert remove_first_last_4(a_string) == " is a st"
    assert remove_first_last_4(a_tuple) == ()
    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert new_order(a_string) == "tringthis is a s"
    assert new_order(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("test passed")

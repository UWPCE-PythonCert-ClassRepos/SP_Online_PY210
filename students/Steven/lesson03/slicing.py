#! bin/user/env python3
'''
Write some functions that take a sequence as an argument, and return a copy of that sequence:

* with the first and last items exchanged.
* with every other item removed.
* with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
* with the elements reversed (just with slicing).
* with the last third, then first third, then the middle third in the new order.

NOTE: These should work with ANY sequence – but you can use strings to test, if you like.
'''

my_string = "this is a string"
my_tuple = (2, 54, 13, 12, 5, 32)

# exchange first and last positions in a sequence
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# return every other item in a sequence
def every_other(seq):
    return seq[::2]

# remove the first 4 and last 4 of a sequence but return every other remaining in the sequence
def remove_four_everyOther(seq):
    return seq[4:-4:2]

# reverse the sequence
def reversed(seq):
    return seq[::-1]

# given a sequence, return the last third, then first third and middle third in the new order
def new_order(seq):
    step = len(seq) // 3  # determine length of sequence in thirds
    last = seq[-step:]  # last third of a sequence
    first = seq[:step]  # first third of a sequence
    middle = seq[step:-step]  # middle third of a sequence
    return last + first + middle


if __name__ == "__main__":
    # test exchange function
    assert exchange_first_last(my_string) == "ghis is a strint"
    assert exchange_first_last(my_tuple) == (32, 54, 13, 12, 5, 2)

    # test every other function
    assert every_other(my_string) == "ti sasrn"
    assert every_other(my_tuple) == (2, 13, 5)

    # test remove and return every other funtion
    assert remove_four_everyOther(my_string) == " sas"
    assert remove_four_everyOther(my_tuple) == ()

    # test reversing function
    assert reversed(my_string) == "gnirts a si siht"
    assert reversed(my_tuple) == (32, 5, 12, 13, 54, 2)

    # test new order sequence function
    assert new_order(my_string) == "tringthis is a s"
    assert new_order(my_tuple) == (5, 32, 2, 54, 13, 12)

    print("tests passed")

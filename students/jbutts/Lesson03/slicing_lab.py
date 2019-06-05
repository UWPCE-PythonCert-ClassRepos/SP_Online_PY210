#!/usr/bin/env python

'''
py210
Module 3: slicing_lab

Exercises to learn slicing, asserts at the end to test.

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.

'''


<<<<<<< HEAD
A_STRING = "one two three four five six seven eight nine ten eleven twelve"
A_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


def exchange_first_last(test):
    '''
    Replace first and last items
    '''
=======
a_string = "one two three four five six seven eight nine ten eleven twelve"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


def exchange_first_last(test):
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    result = test[-1:] + test[1:-1] + test[:1]
    return result


def remove_every_other(test):
<<<<<<< HEAD
    '''
    Slice to print every other value
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    result = test[::2]
    return result


def first_and_last_four(test):
<<<<<<< HEAD
    '''
    Slice to return the first 4 and the last 4 items removed, and then every other item
    in the remaining sequence.
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    result = test[:4] + test[-4:]
    return result


def reverse(test):
<<<<<<< HEAD
    '''
    Slice to return the elements reversed (just with slicing).
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    result = test[::-1]
    return result


def thirds_jumble(test):
<<<<<<< HEAD
    '''
    Slice with the last third, then first third, then the middle third in the new order.
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    chunk_size = int(len(test)/3)
    #  Modulo naturally gets handled in the middle third
    result = test[-chunk_size:] + test[chunk_size:-chunk_size] + test[:chunk_size]
    return result


<<<<<<< HEAD
assert exchange_first_last(A_STRING) == "ene two three four five six seven eight nine ten eleven " \
                                        "twelvo"
assert exchange_first_last(A_TUPLE) == (12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1)
assert remove_every_other(A_STRING) == "oetotrefu iesxsvnegtnn e lvntev"
assert remove_every_other(A_TUPLE) == (1, 3, 5, 7, 9, 11)
assert first_and_last_four(A_STRING) == "one elve"
assert first_and_last_four(A_TUPLE) == (1, 2, 3, 4, 9, 10, 11, 12)
assert reverse(A_STRING) == "evlewt nevele net enin thgie neves xis evif ruof eerht owt eno"
assert reverse(A_TUPLE) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
assert thirds_jumble(A_STRING) == "ne ten eleven twelveive six seven eight nione two three four f"
assert thirds_jumble(A_TUPLE) == (9, 10, 11, 12, 5, 6, 7, 8, 1, 2, 3, 4)
=======
assert exchange_first_last(a_string) == "ene two three four five six seven eight nine ten eleven twelvo"
assert exchange_first_last(a_tuple) == (12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1)
assert remove_every_other(a_string) == "oetotrefu iesxsvnegtnn e lvntev"
assert remove_every_other(a_tuple) == (1, 3, 5, 7, 9, 11)
assert first_and_last_four(a_string) == "one elve"
assert first_and_last_four(a_tuple) == (1, 2, 3, 4, 9, 10, 11, 12)
assert reverse(a_string) == "evlewt nevele net enin thgie neves xis evif ruof eerht owt eno"
assert reverse(a_tuple) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
assert thirds_jumble(a_string) == "ne ten eleven twelveive six seven eight nione two three four f"
assert thirds_jumble(a_tuple) == (9, 10, 11, 12, 5, 6, 7, 8, 1, 2, 3, 4)


>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7


#!/usr/bin/python3
'''
Author: Alex Sotelo
Exercise 3.1
Python 3 required
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html
Task:Write some functions that take a sequence as an argument, and return a copy of that sequence:

    with the first and last items exchanged.
    with every other item removed.
    with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    with the elements reversed (just with slicing).
    with the last third, then first third, then the middle third in the new order.
'''


def exchange_first_last(seq):
    a_new_sequence = (seq[-1:] + seq[1:-1] + seq[:1])
    return a_new_sequence

def remove_every_other(seq):
    a_new_sequence = (seq[::2])
    return a_new_sequence

def remove_firstlast4_everyother(seq):
    a_new_sequence = seq[4:-4]
    return a_new_sequence

def reverse_elements(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

def new_order(seq):
    a_new_sequence = (seq[-3:] + seq[:3] + seq[3:-3])
    return a_new_sequence


if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_firstlast4_everyother(a_string) == " is a st"
    assert remove_firstlast4_everyother(a_tuple) == ()

    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert new_order(a_string) == "ingthis is a str"
    assert new_order(a_tuple) == (12, 5, 32, 2, 54, 13)
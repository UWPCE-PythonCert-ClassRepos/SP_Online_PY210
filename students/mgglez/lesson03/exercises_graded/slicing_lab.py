#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 3
# Description: Exercise 3.1 - Slicing Lab (Graded Exercise)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-10-2021, Created Slicing Lab Functions
# ---------------------------------------------------------------------------- #

def exchange_first_last(seq):
    """
    Function that take a sequence as an argument, and return a copy of that sequence
    with the first and last items exchanged.
    :param seq: (sequence) Original sequence
    :return: (sequence) Modified sequence
    """
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_item_removed(seq):
    """
    Function that take a sequence as an argument, and return a copy of that sequence
    with every other item removed.
    :param seq: (sequence) Original sequence
    :return: (sequence) Modified sequence
    """
    return seq[::2]

def first4_last4_removed_every_other_remaining_item(seq):
    """
    Function that take a sequence as an argument, and return a copy of that sequence
    with the first 4 and the last 4 items removed, and then every other item in the
    remaining sequence.
    :param seq: (sequence) Original sequence
    :return: (sequence) Modified sequence
    """
    return seq[4:-4:2]

def elements_reversed(seq):
    """
    Function that take a sequence as an argument, and return a copy of that sequence
    with the elements reversed (just with slicing).
    :param seq: (sequence) Original sequence
    :return: (sequence) Modified sequence
    """
    return seq[::-1]

def last_third_fist_third_middle_third(seq):
    last_third = seq[-(len(seq)//3):]
    first_third = seq[:(len(seq)//3)]
    middle_third = seq[(len(seq)//3):-(len(seq)//3)]
    return last_third + first_third + middle_third


if __name__ == '__main__':

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = list(range(20))

    print("\nRunning some tests ...")
    # run some tests

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert every_other_item_removed(a_string) == "ti sasrn"
    assert every_other_item_removed(a_tuple) == (2, 13, 5)

    assert first4_last4_removed_every_other_remaining_item(a_list) == [4, 6, 8, 10, 12, 14]
    assert first4_last4_removed_every_other_remaining_item(a_string) == ' sas'

    assert elements_reversed(a_string) == 'gnirts a si siht'
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert last_third_fist_third_middle_third(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert last_third_fist_third_middle_third(a_string) == 'tringthis is a s'

    print("\nTests Passed")
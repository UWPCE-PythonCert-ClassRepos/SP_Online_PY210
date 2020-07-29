#!/usr/bin/env python3

"""
Lesson 3: Slicing Lab
Course: UW PY210
Author: Jason Jenkins
"""


def exchange_first_last(seq):
    """
    Return the first and last item of seq

    :param seq: value to be changed
    """

    if(len(seq) > 0):
        return seq[len(seq) - 1:] + seq[1:len(seq) - 1] + seq[:1]


def remove_everyother_item(seq):
    """
    Return everyother item in seq

    :param seq: value to be changed
    """

    return seq[0::2]


def mid_everyother_item(seq):
    """
    Return the the first 4 and the last 4 items
    and then every other item in the remaining sequence.

    :param seq: value to be changed
    """

    return seq[:4] + seq[-4:] + remove_everyother_item(seq[4:-4])


def reverse_item(seq):
    """
    Return the elements in reverse seq

    :param seq: value to be changed
    """

    return(seq[::-1])


def last_first_mid_item(seq):
    """
    Return the last third
    then the first third
    then the middle third in the new order.

    :param seq: value to be changed
    """
    a_third = len(seq) // 3

    return seq[-a_third:] + seq[:a_third] + seq[a_third:-a_third]


if __name__ == "__main__":
    # testing
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_everyother_item(a_string) == "ti sasrn"
    assert remove_everyother_item(a_tuple) == (2, 13, 5)

    assert mid_everyother_item(a_string) == "thisring sas"
    assert mid_everyother_item(a_tuple) == (2, 54, 13, 12, 13, 12, 5, 32)

    assert reverse_item(a_string) == "gnirts a si siht"
    assert reverse_item(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert last_first_mid_item(a_string) == "tringthis is a s"
    assert last_first_mid_item(a_tuple) == (5, 32, 2, 54, 13, 12)

    print()
    print("All Tests Passed")

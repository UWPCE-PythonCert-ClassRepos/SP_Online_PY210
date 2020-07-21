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

    pass


def remove_everyother_item(seq):
    """
    Return everyother item in seq

    :param seq: value to be changed
    """

    pass


def mid_everyother_item(seq):
    """
    Return the the first 4 and the last 4 items
    and then every other item in the remaining sequence.

    :param seq: value to be changed
    """

    pass


def reverse_item(seq):
    """
    Return the elements in reverse seq

    :param seq: value to be changed
    """

    pass


def last_first_mid_item(seq):
    """
    Return copy of sew with the last third
    then first third
    then the middle third in the new order.

    :param seq: value to be changed
    """

    pass


if __name__ == "__main__":
    # testing
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

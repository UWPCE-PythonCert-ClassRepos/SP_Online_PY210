#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html

Tasks:
Write some functions that take a sequence as an argument, and return a copy of that sequence:
    - with the first and last items exchanged.
    - with every other item removed.
    - with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    - with the elements reversed (just with slicing).
    - with the last third, then first third, then the middle third in the new order.
"""

def exchange_first_last(seq):
    """ Exchanges the first and last items in a sequence and return the new sequence """
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    """ Removes every other item in a sequence """
    return seq[::2]

def first_last_4_removed_and_every_other(seq):
    """ Removes the first and last four items in a sequence and returns every other of remainder """
    return remove_every_other(seq[4:-4])

def elements_reversed(seq):
    """ Returns the sequence of elements """
    return seq[::-1]

def last_first_middle_third_ordered(seq):
    """ Reorders the sequence to last third, first third, middle third """
    idx = len(seq)//3
    return seq[-idx:] + seq[:-idx]

if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    # Test Exchange First Last Function 
    assert( exchange_first_last(a_string) == "ghis is a strint")
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    # Test Remove Middle Function
    assert( remove_every_other(a_string) == "ti sasrn")
    assert( remove_every_other(a_tuple) == (2, 13, 5))

    # Test Remove First Four and Last Four and every other
    assert( first_last_4_removed_and_every_other(a_string) == " sas")
    assert( first_last_4_removed_and_every_other(a_tuple) == () )

    # Test Elements Reversed
    assert( elements_reversed(a_string) == "gnirts a si siht")
    assert( elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2))

    # Test Last Third, First Third, Middle
    assert(last_first_middle_third_ordered(a_string) == "tringthis is a s")
    assert (last_first_middle_third_ordered(a_tuple) == (5, 32,2, 54, 13, 12 ))
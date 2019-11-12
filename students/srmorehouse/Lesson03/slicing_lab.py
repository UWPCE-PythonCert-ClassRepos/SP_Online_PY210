#!/usr/bin/env python3

"""
Steve Morehouse
Lesson 03

"""

"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first and last items exchanged.
"""
def exchange_first_last ( seq ):
    return seq[-1:] + seq[1:len(seq)-1] + seq[:1]

"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with every other item removed.
"""
def remove_every_other ( seq ):
    return seq[::2]

"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
"""
def remove_first_last_four ( seq ):
    return seq [4:-4:2]

"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the elements reversed (just with slicing).
"""
def reverse_sequence ( seq ):
    return seq [::-1]

"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the last third, then first third, then the middle third in the new order.
"""
def thirds ( seq ):
    size = int ( len (seq) / 3 )
    return seq[-size:] + seq[:-size]

if __name__ == "__main__":

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    long_string = 'antidisestablishmentarianism'

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(long_string) == 'mntidisestablishmentarianisa'

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(long_string) == 'atdssalsmnains'

    assert remove_first_last_four(a_string) == " sas"
    assert remove_first_last_four(a_tuple) == ()
    assert remove_first_last_four(long_string) == 'dssalsmnai'

    assert reverse_sequence(a_string) == "gnirts a si siht"
    assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse_sequence(long_string) == 'msinairatnemhsilbatsesiditna'

    assert thirds(a_string) == "tringthis is a s"
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert thirds(long_string) == 'tarianismantidisestablishmen'

    print ("tests pass")

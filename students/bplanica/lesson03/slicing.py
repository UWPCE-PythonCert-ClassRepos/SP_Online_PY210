#!/usr/bin/env python3

# ------------------------------ #
# Slicing Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/6/2019, Created and tested script
# ------------------------------ #

def first_to_last(seq):
    """replaces the first and last indexes in a sequence"""
    i = len(seq)
    new_seq = seq[i-1:] + seq[1:i-1] + seq[:1]
    return new_seq

def every_other(seq):
    """returns every other index item in a sequence"""
    new_seq = seq[::2]
    return new_seq

def every_other_middle(seq):
    """returns every other index item in a sequence after first and last 4 items are removed"""
    i = len(seq)
    new_seq = seq[4:i-4:2]
    return new_seq

def reversed(seq):
    """returns a sequence with the elements reversed"""
    new_seq = seq[::-1]
    return new_seq

def last_first_middle(seq):
    """returns the last third, then first third, then the middle third of a sequence"""
    i = len(seq)
    last = seq[(int((2*i)/3)):]
    first = seq[:(int((2*i)/3))]
    return last + first


a_string = 'here is a string'
a_tuple = (1, 2, 3, 4, 5)

assert first_to_last(a_string) == 'gere is a strinh'
assert first_to_last(a_tuple) == (5, 2, 3, 4, 1)
assert every_other(a_string) == 'hr sasrn'
assert every_other(a_tuple) == (1, 3, 5)
assert every_other_middle(a_string) ==  ' sas'
assert every_other_middle(a_tuple) == ()
assert reversed(a_string) == 'gnirts a si ereh'
assert reversed(a_tuple) == (5, 4, 3, 2, 1)
assert last_first_middle(a_string) == 'stringhere is a '
assert last_first_middle(a_tuple) == (4, 5, 1, 2, 3)

print("Passed!")
#!/usr/bin/env python3

"""A series of functions that return sequences altered in various ways."""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.

def first_last_exchange(seq):
    """Return a copy of the given sequence with the first and last items exchanged."""
    new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    
    return new_sequence

def remove_every_other(seq):
    """Return a copy of the given sequence with every other item removed."""
    new_seq = seq[::2]
    
    return new_seq

def remove4_every_other(seq):
    """Return a copy of the given sequence with the first 4 and last 4 items removed and every other remaining item."""
    new_seq = seq[4:-4:2]
    
    return new_seq

def reverse(seq):
    """Return a copy of the given sequence in reverse order."""
    new_seq = seq[::-1]
    
    return new_seq

def new_third_order(seq):
    """Return a copy of the given sequence in the order: last third, first third, middle third."""
    length_thirds = len(seq) // 3
    
    first_third = length_thirds
    second_third = first_third + length_thirds
    last_third  = first_third + second_third
    remainder = len(seq) % 3
    
    # ensure any remainders are distributed across each third instead of being
    # tacked on to the end of the sequence (last_third in this case)
    if len(seq) % 3 == 1:
        first_third += 1
    elif len(seq) % 3 == 2:
        first_third += 1
        second_third += 2
    
    print(first_third, second_third, last_third)
    
    new_seq = seq[last_third:] + seq[:first_third] + seq[first_third:second_third]
    
    return new_seq
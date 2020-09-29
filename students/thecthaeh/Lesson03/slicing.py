#!/usr/bin/env python3

"""A series of functions that return sequences altered in various ways."""

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
    
    first_third_end = length_thirds
    second_third_end = first_third_end + length_thirds
    remainder = len(seq) % 3
    
    # ensure any remainders are distributed across each third instead of being
    # tacked on to the end of the sequence (last_third in this case)
    if remainder == 1:
        first_third_end += 1
    elif remainder == 2:
        first_third_end += 1
        second_third_end += 2
    
    new_seq = seq[second_third_end:] + seq[:first_third_end] + seq[first_third_end:second_third_end]
    
    return new_seq

if __name__ == "__main__":
    #run some tests
    
    a_string = "this is a string"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a_tuple = (34, 6, 32, 4, 12, 9)
    
    # test that first_last_exchange works for strings, lists, and tuples
    assert first_last_exchange(a_string) == 'ghis is a strint'
    assert first_last_exchange(a_list) == [9, 2, 3, 4, 5, 6, 7, 8, 1]
    assert first_last_exchange(a_tuple) == (9, 6, 32, 4, 12, 34)
    
    # test that remove_every_other works for strings, lists, and tuples
    assert remove_every_other(a_string) == 'ti sasrn'
    assert remove_every_other(a_list) == [1, 3, 5, 7, 9]
    assert remove_every_other(a_tuple) == (34, 32, 12)
    
    # test that remove4_every_other works for strings, lists, and tuples
    assert remove4_every_other(a_string) == ' sas'
    assert remove4_every_other(a_list) == [5]
    assert remove4_every_other(a_tuple) == ()
    
    # test that reverse works for strings, lists, and tuples
    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_list) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse(a_tuple) == (9, 12, 4, 32, 6, 34)
    
    # test that new_third_order works for strings, lists, and tuples
    assert new_third_order(a_string) == 'stringthis is a '
    assert new_third_order(a_list) == [7, 8, 9, 1, 2, 3, 4, 5, 6]
    assert new_third_order(a_tuple) == (12, 9, 34, 6, 32, 4)
    
    print("tests passed")
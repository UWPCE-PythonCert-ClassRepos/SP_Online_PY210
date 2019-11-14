#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 11/9/2019
# slicing_lab.py

# returns the string with the first and last items exchanged.
def exchange_first_last(seq):
    return seq[-1 : ] + seq[1 : -1] + seq[ : 1]

# returns the string with every other item removed.
def remove_every_other(seq):
    return seq[ : : 2]

# returns the string with the first 4 and the last 4 items removed, 
# and then every other item in the remaining sequence.
def remove_first_last_4(seq):
    return seq[4 : -4 : 2]

# returns the string with the elements reversed.
def reverse_elements(seq):
    return seq[len(seq) : : -1]

# returns the string with the last third, then first third, 
# then the middle third in the new order.
def thirds_new_order(seq):
    third = len(seq) // 3
    if (len(seq) % 3) > 0:
        third += 1
    return seq[2 * third : ] + seq[third : 2 * third] + seq[ : third]

if __name__ == "__main__":
    
    # run some tests

    '''    
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)    

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_long_tuple) == (10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(a_long_tuple) == (0, 2, 4, 6, 8, 10)

    assert remove_first_last_4(a_string) == " sas"
    assert remove_first_last_4(a_tuple) == ()
    assert remove_first_last_4(a_long_tuple) == (4, 6)

    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse_elements(a_long_tuple) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

    assert thirds_new_order(a_string) == "rings a stthis i"
    assert thirds_new_order(a_tuple) == (5, 32, 13, 12, 2, 54)
    assert thirds_new_order(a_long_tuple) == (8, 9, 10, 4, 5, 6, 7, 0, 1, 2, 3)

    print("tests passed")'''
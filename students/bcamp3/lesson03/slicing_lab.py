#!/usr/bin/env python3

"""
Slicing Lab

"""

def exchange_first_last(seq):
    if len(seq)<=1:
        return seq
    else:
        return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]
    
def remove_first4_last4_every_other(seq):
    return seq[4:-4:2]

def reverse_seq(seq):
    return seq[::-1]

def thirds_jumble(seq):
    if len(seq)<=1:
        return seq
    elif len(seq)==2:
        return seq[-1:] + seq[:1]
    else:
        third = len(seq)//3
        return seq[-third:] + seq[:third] + seq[third:-third]

if __name__ == "__main__":
    #test sequences
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
        
    # run some tests for exchange_fist_last(seq)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    
    # run some tests for remove_every_other(seq)
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    
    # run some tests for remove_first4_last4_every_other(seq)
    assert remove_first4_last4_every_other(a_string) == " sas"
    assert remove_first4_last4_every_other(a_tuple) == ()
    
    # run some tests for reverse_seq(seq)
    assert reverse_seq(a_string) == "gnirts a si siht"
    assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)
    
    # run some tests for thirds_jumble(seq)
    assert thirds_jumble(a_string) == "tringthis is a s"
    assert thirds_jumble(a_tuple) == (5, 32, 2, 54, 13, 12)
    
    print("all tests passed")
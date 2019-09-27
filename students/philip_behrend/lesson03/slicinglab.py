# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:55:12 2019

Author: Philip Behrend
"""

def first_last(seq):
    if (type(seq) == tuple) or (type(seq) == str):
        return (seq[-1:] + seq[1:-1] + seq[:1])
    else:
        seq[0], seq[-1] = seq[-1], seq[0]
        return (seq)

def remove_eo(seq):
    return(seq[::2])

def rm_four_first_last(seq):
    if len(seq) >= 8:
        return (seq[4:-4])
    else:
        return([])

def reverse(seq):
    return(seq[::-1])
    
def reshuffle(seq):
    thresh1 = round(len(seq)/3)
    thresh2 = round(2*len(seq)/3)
    if (type(seq) == tuple) or (type(seq) == str):
        return (seq[thresh2:] + seq[0:thresh1]+seq[thresh1:thresh2])
    else:
        seq[0:thresh1],seq[thresh1:thresh2],seq[thresh2:] = seq[thresh2:], seq[0:thresh1],seq[thresh1:thresh2]
        return(seq)

# Lists are annoyingly mutable
seq = [1,2,3,4,5,6,7,8,9]
assert first_last(seq) == [9,2,3,4,5,6,7,8,1]
seq = [1,2,3,4,5,6,7,8,9]
assert remove_eo(seq) == [1,3,5,7,9]
seq = [1,2,3,4,5,6,7,8,9]
assert rm_four_first_last(seq) == [5]
seq = [1,2,3,4,5,6,7,8,9]
assert reverse(seq) == [9,8,7,6,5,4,3,2,1]
seq = [1,2,3,4,5,6,7,8,9]
assert reshuffle(seq) == [7,8,9,1,2,3,4,5,6]

tup = (1,2,3,4,5,6,7,8,9)
assert first_last(tup) == (9,2,3,4,5,6,7,8,1)
assert remove_eo(tup) == (1,3,5,7,9)
assert rm_four_first_last(tup) == (5,)
assert reverse(tup) == (9,8,7,6,5,4,3,2,1)
assert reshuffle(tup) == (7,8,9,1,2,3,4,5,6)




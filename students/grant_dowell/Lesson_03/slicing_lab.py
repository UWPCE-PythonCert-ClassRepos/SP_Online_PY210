# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 15:30:55 2019

@author: Grant Dowell
Excercise 3.1 - Slicing Lab
"""

def exchange_first_last(seq):
#    first = seq[0]
#    last = seq[-1]
#    new_seq = [last]+seq[1:-1]+[first]
    new_seq = seq[-1] + seq[1:-1] + seq[0]
    return new_seq

def remove_every_other(seq):
    return seq[::2]

def every_other_middle(seq):
    return seq[4:-3:2]

def reverse(seq):
    return seq[::-1]

def last_first_mid_third(seq):
    third_count = round(len(seq)/3)
    return seq[2*third_count:]+seq[0:third_count]+seq[third_count:2*third_count]

if __name__ == '__main__':
    test_string = "this is a string"
    test_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
#    print(test_seq)
#    print(exchange_first_last(test_seq))
#    print(remove_every_other(test_seq))
#    print(every_other_middle(test_seq))
#    print(reverse(test_seq))
#    print(last_first_mid_third(test_seq))

    assert exchange_first_last(test_tuple) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
                                               2, 1, 0)
    
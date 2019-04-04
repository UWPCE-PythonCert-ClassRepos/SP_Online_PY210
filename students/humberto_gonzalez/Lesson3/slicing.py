#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:39:51 2019

@author: humberto gonzalez
"""

### Slicing Lab ###

def exchange_first_last(seq):
    '''Exchnages the first and last element in a sequence'''
    e = len(seq)-1
    first = seq[:1]
    last = seq[e:]
    ans = last + seq[1:e] + first
    return ans


def every_other(seq):
    '''returns the sequence with every other item removed'''
    return seq[::2]


def fours_every_other(seq):
    '''removes the first and last four elements and then every 
       other after that'''
    new_seq = seq[4:-4]
    return new_seq[::2]

def reverse(seq):
    '''reverses order of sequence'''
    return seq[::-1]


def rearrange_thirds(seq):
    '''rearranges the first, middle, and last third of a sequence'''
    
    n = len(seq)
    t = int(n/3)
    
    first = seq[0:t]
    middle = seq[t:(2*t)]
    end = seq[(2*t):n]
    
    return end+first+middle
    

### TESTING ###
if __name__ == "__main__":
    # run some tests on the above functions
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)
    assert fours_every_other(b_tuple) == (5, 7)
    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert rearrange_thirds(a_string) == 'stringthis is a '
    assert rearrange_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("tests passed")
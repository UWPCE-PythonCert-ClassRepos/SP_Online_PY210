#!/usr/bin/env python

test_string = "This is a string."
test_tuple = (1,2,3,5,8,13)

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

assert exchange_first_last(test_string) == ".his is a stringT"
assert exchange_first_last(test_tuple) == (13,2,3,5,8,1)

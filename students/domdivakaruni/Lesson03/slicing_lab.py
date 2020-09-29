#!/usr/bin/env python3

# Dom Divakaruni
# Lesson03- slicing


def exchange_first_last(input):
    #take in a string, touple or list and return one with the first and last items exchanged. 
    return input[-1:] + input[1:-1] + input[:1]


def every_other_item(input):
    #with every other item removed.
    return input[::2]

def drop_eight_lose_half(input):
    #with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    return input[4:-4:2]

def reverse_slice(input):
    #with the elements reversed (just with slicing).
    return input[::-1]


def new_order(input):
    third = len(input)//3
    #with the last third, then first third, then the middle third in the new order.
    return input[-third:]+input[:third]+input[third:-third]

if __name__ == "__main__":
    #testing the code above
    s = "this is a string"
    t = (2, 54, 13, 12, 5, 32)
    #assert statements
    assert exchange_first_last(s) == 'ghis is a strint'
    assert exchange_first_last(t) == (32, 54, 13, 12, 5, 2)
    assert every_other_item(s) == 'ti sasrn'
    assert every_other_item(t) == (2, 13, 5)
    assert drop_eight_lose_half(s) == ' sas'
    assert drop_eight_lose_half(t) == ()
    assert reverse_slice(s) == 'gnirts a si siht'
    assert reverse_slice(t) == (32, 5, 12, 13, 54, 2)
    assert new_order(s) == 'tringthis is a s'
    assert new_order(t) == (5, 32, 2, 54, 13, 12)
    print("all tests passed")
#Exercise3.1.py
import math

#Exercise 3.1 Objective:
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

    #1 - with the first and last items exchanged.
    #2 - with every other item removed.
    #3 - with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    #4 - with the elements reversed (just with slicing).
    #5 - with the last third, then first third, then the middle third in the new order.
"""

#1 - with the first and last items exchanged function
def swap_first_last(seq):
    first = seq[:1]
    middle = seq[1:-1]
    last = seq[-1:]
    return last + middle + first

#2 - with every other item removed.
def remove_every_other(seq):
    return seq[::2]

#3 - with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def FirstFour_LastFour_EveryOther(seq):
    return seq[4:-4:2]

#4 - with the elements reversed (just with slicing).
def reverse_it(seq):
    return seq[::-1]

#5 - with the last third, then first third, then the middle third in the new order.
def last_first_middle(seq):
    first = math.ceil(len(seq)/3)
    middle = math.ceil(len(seq)/3)
    last = len(seq) - (first + middle)
    return seq[-last:] + seq[:first] + seq[first:(first+middle)]


if __name__ == "__main__":
    # run some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32) 

    #Check First Function
    assert swap_first_last(a_string) == "ghis is a strint"
    assert swap_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    print("Swap First and Last - PASSED!")

    #Check Second Function
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    print("Remove Every Other - PASSED!")

    #Check Third Function
    assert FirstFour_LastFour_EveryOther(a_string) == " sas"
    assert FirstFour_LastFour_EveryOther(a_tuple) == ()
    print("First 4, Last 4, and Every Other - PASSED!")

    #Check Fourth Function
    assert reverse_it(a_string) == "gnirts a si siht"
    assert reverse_it(a_tuple) == (32, 5, 12, 13, 54, 2)
    print("Reverse It - PASSED!")

    #Check Fifth Function
    assert last_first_middle(a_string) == "ringthis is a st"
    assert last_first_middle(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("Last, First and Middle - PASSED!")
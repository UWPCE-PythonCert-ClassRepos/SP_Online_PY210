#!/usr/bin/env python3
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
def exchange_first_last(seq):
    return(seq[-1:]+seq[1:-1]+seq[:1]) #with the first and last items exchanged.
def remove_every_other(seq): 
    return(seq[::2]) #with every other item removed.
def mix_quest(seq):
    return(seq[4:-4:2]) #with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def elements_reversed(seq):
    return(seq[::-1]) #with the elements reversed (just with slicing).
# I don't understand what is the "the middle third"
def last_first_third(seq):
    return(seq[-3:-2]+seq[2:3]) #with the last third, then first third, then the middle third in the new order

if __name__ == "__main__":    
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == 'ti sasrn'
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert mix_quest(a_string) == ' sas'
    assert mix_quest(a_tuple) == ()
    assert elements_reversed(a_string) == 'gnirts a si siht'
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert last_first_third(a_string) == 'ii'
    assert last_first_third(a_tuple) == (12, 13)
    
    print("tests passed")
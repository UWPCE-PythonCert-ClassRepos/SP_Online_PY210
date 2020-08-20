#!/usr/bin/env python3


def exchange_first_last(seq):
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]  
    return new_seq 


def every_other_removed(seq):
    #slice with every other item removed
    new_seq = seq[::2]
    return new_seq



if __name__ == "__main__":

    #initialize a couple diff sequences
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_second_tuple = (5, 72, 13, 26, 89, 3, 17, 63, 39, 45, 11, 9, 28)
    
    print()
    print("Will print tests of each function in order, for the following 3 sequences:\n")
    print("test sequence 1: ", a_string)
    print("test sequence 2: ", a_tuple)
    print("test sequence 3: ", a_second_tuple)
    print()
    
    print("switched first and last values:\n")
    print("sequence 1: ", exchange_first_last(a_string))
    print("sequence 2: ", exchange_first_last(a_tuple))
    print("sequence 3: ", exchange_first_last(a_second_tuple))
    print()


    #Now conduct some Assert tests for each function with the same 3 sequences.

    # tests for exchange_first_last(seq):
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_second_tuple) == (28, 72, 13, 26, 89, 3, 17, 63, 39, 45, 11, 9, 5)
    print("---tests for exchange_first_last(seq) passed!---")
    print()
    
    # tests for every_other_removed(seq):
    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_tuple) == (2, 13, 5)
    assert every_other_removed(a_second_tuple) == (5, 13, 89, 17, 39, 11, 28)
    print("---tests for every_other_removed(seq) passed!---")
    print()

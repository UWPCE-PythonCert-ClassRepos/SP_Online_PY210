#!/usr/bin/env python3


def exchange_first_last(seq):
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]  
    return new_seq 


def every_other_removed(seq):
    #slice with every other item removed
    new_seq = seq[::2]
    return new_seq


def every_other_short(seq):
    new_seq = seq[4:-4:2] #slice incl index 4 until excluding index 4 from end of seq, with every other item removed
    return new_seq


def reversed_slice(seq):
    new_seq = seq[::-1]  #copy of seq reversed
    return new_seq


def last_third_first(seq):
    i = len(seq)//3
    last = seq[i*2:]
    first = seq[:i]
    middle = seq[i:i*2]
    new_seq = last + first + middle
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
    
    print("every other element removed:\n")
    print("sequence 1: ", every_other_removed(a_string))
    print("sequence 2: ", every_other_removed(a_tuple))
    print("sequence 3: ", every_other_removed(a_second_tuple))
    print()

    print("every other element removed with first 4 and last 4 elements deleted:\n")
    print("sequence 1: ", every_other_short(a_string))
    print("sequence 2: ", every_other_short(a_tuple))
    print("sequence 3: ", every_other_short(a_second_tuple))
    print()
    
    print("reversed sequence:\n")
    print("sequence 1: ", reversed_slice(a_string))
    print("sequence 2: ", reversed_slice(a_tuple))
    print("sequence 3: ", reversed_slice(a_second_tuple))
    print()
    
    print("last 1/3, first 1/3, mid 1/3:\n")
    print("sequence 1: ", last_third_first(a_string))
    print("sequence 2: ", last_third_first(a_tuple))
    print("sequence 3: ", last_third_first(a_second_tuple))
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
    
    # tests for every_other_short(seq):
    assert every_other_short(a_string) == " sas"
    assert every_other_short(a_tuple) == ()
    assert every_other_short(a_second_tuple) == (89, 17, 39)
    print("---tests for every_other_short(seq) passed!---")
    print()
    
    # tests for reversed_slice(seq):
    assert reversed_slice(a_string) == "gnirts a si siht"
    assert reversed_slice(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reversed_slice(a_second_tuple) == (28, 9, 11, 45, 39, 63, 17, 3, 89, 26, 13, 72, 5)
    print("---tests for reversed_slice(seq) passed!---")
    print()

    # tests for last_third_first(seq):
    assert last_third_first(a_string) == "stringthis is a "
    assert last_third_first(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert last_third_first(a_second_tuple) == (39, 45, 11, 9, 28, 5, 72, 13, 26, 89, 3, 17, 63)
    print("---tests for last_third_first(seq) passed!---")
    print()
    
    print("ALL Assert Tests Passed!")

#!/usr/bin/env python3

def exchange_first_last(seq):
    """ 
        Function recieves a sequence and swaps
        the first and last element, returns the 
        swapped sequence
    
        :param: seq - sequence to swap first and last element
    """
    first_section_of_seq = seq[:1]
    mid_section_of_seq   = seq[1:-1]
    last_section_of_seq  = seq[-1:]
    
    new_sequence = last_section_of_seq + mid_section_of_seq + first_section_of_seq 

    return new_sequence

def remove_every_other(seq): 
    """ 
        function removes ever other item from the seq,
        by steps of 2
        
        :param: seq : sequence to remove items from. 
    """
    new_sequence = seq[::2]

    return new_sequence

def remove_first_last_four(seq): 
    """ 
        function removes first 4 sections and last 4 sections,
        proceeds to remove every other item,
        in the left over sequence, by steps of 2

        :param: seq: sequence to remove first, last,
        and return every other. 
    """
    first_four_last_four_removed = seq[4:-4]
    every_other = first_four_last_four_removed[::2] 
    return every_other

def reverse(seq): 
    """
        reverses the elements of a sequence
        :param: seq: sequence to reverse
    """
    new_sequence = seq[::-1]
    return new_sequence

def last_first_middle_third(seq): 
    """ 
        function returns the last third, 
        first third and middle third, in that 
        order

        :param: seq: sequence to extract, last third, 
        first third, and middle third. 
    """
    
    last_third  = seq[-3:]
    first_third = seq[:3]
    mid_seq   = seq[3:-3] 
    mid_third = mid_seq[:3]

    new_sequence = last_third + first_third + mid_third 
    return new_sequence


if __name__ == '__main__':

    a_string = "this is a string"
    a_tuple  = (2, 54, 13, 12, 5, 32)
    a_tuple2 = (2, 54, 13, 12, 5, 32, 20, 40, 70, 24, 16, 18)

    #String sequence test
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_first_last_four(a_string) == " sas"
    assert reverse(a_string) == "gnirts a si siht"
    assert last_first_middle_third(a_string) == "ingthis i"
    print("All string tests passed!")

    #Tuple Sequence test
    assert exchange_first_last(a_tuple)  == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_first_last_four(a_tuple2) == (5, 20)
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert last_first_middle_third(a_tuple2) == (24, 16, 18, 2, 54, 13, 12, 5, 32)
    print("All tuple tests passed!") 

    print("All tests passed!")

  

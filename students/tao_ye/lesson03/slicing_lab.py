#!/usr/bin/env python3

def exchange_first_last(sequence):
    """
    exchange the first and last items of a sequence

    :param sequence: a sequence
    :return: a new sequence
    
    """
    
    return (sequence[-1:] + sequence[1:-1] + sequence[:1])

def every_other_removed(sequence):
    """
    remove every other item of a sequence

    :param sequence: a sequence
    :return: a new sequence
    
    """
    return (sequence[::2])

def trim_every_other_removed(sequence):
    """
    remove the first 4 and the last 4 items, and keep
    every other item in the remaining sequence

    :param sequence: a sequence
    :return: a new sequence
    
    """
    
    return(sequence[4:-4:2])

def reverse(sequence):
    """
    reverse the order of elements in a sequence

    :param sequence: a sequence
    :return: a new sequence
    
    """
    return(sequence[::-1])

def three_thirds_reordered(sequence):
    """
    reorder the sequence: the last third, then first third, then
    the middle third in the new order

    :param sequence: a sequence
    :return: a new sequence
    
    """
    
    a_third = len(sequence)//3
    return(sequence[-a_third:] + sequence[:-a_third])


if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_tuple) == (2, 13, 5)
    assert trim_every_other_removed(a_string) == " sas"
    assert trim_every_other_removed(a_tuple) == ()
    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert three_thirds_reordered(a_string) == "tringthis is a s"
    assert three_thirds_reordered(a_tuple) == (5, 32, 2, 54, 13, 12)
    
    print('test passed')

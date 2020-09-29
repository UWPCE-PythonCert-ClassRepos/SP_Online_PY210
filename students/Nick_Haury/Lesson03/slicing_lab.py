'''
The intent of this lab is to create several functions which demonstrate
the functionality of modifying sequences (any sequence, not just strings)
in Python.  The functions will take a sequence as an argument, and then
return a copy of that sequence with some change made to the sequence.
'''


def exchange_first_last(sequence):
    '''
    Takes a sequence (string, etc.) as an argument, and then returns
    a copy of that sequence with the first and last elements reversed.
    '''

    return sequence[-1:] + sequence[1:-1] + sequence[:1]


def remove_every_other(sequence):
    '''
    Takes a sequence as an argument, and then returns a copy of that
    sequence with every other element (index 1, 3, 5, etc.) removed
    '''

    return sequence[::2]


def remove_first_last_four_then_every_other(sequence):
    '''
    Takes a sequence as an argument, and then returns a copy of that
    sequence with the first 4 and last 4 items removed, and then
    every other item in the remaining sequence.
    ex. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] -> [5, 7]
    '''

    return sequence[4:-4:2]


def reverse(sequence):
    '''
    Takes a sequence as an argument, and then returns a copy of that
    sequence in reverse order. ex. [1, 2, 3] -> [3, 2, 1]
    '''

    return sequence[::-1]


def swap_thirds(sequence):
    '''
    Takes a sequence as an argument, and then returns a copy of that
    sequence with the following change: take the sequence and break it
    into thirds.  Change the order to be the last third, the first
    third, and then the middle third.
    '''

    return sequence[len(sequence)//3:] + sequence[:len(sequence)//3]


if __name__ == "__main__":
    # create sequences to test
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_tuple = a_tuple + (6, 1, 4, 9, 8)
    a_list = [1, 2, 3, 4, 5, 6, 10]
    a_longer_list = a_list + [20, 50, 100, -6, "thing"]

    # testing functions
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_list) == [10, 2, 3, 4, 5, 6, 1]

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_every_other(a_list) == [1, 3, 5, 10]

    assert remove_first_last_four_then_every_other(a_string) == " sas"
    assert remove_first_last_four_then_every_other(a_longer_tuple) == (5, 6)
    assert remove_first_last_four_then_every_other(a_longer_list) == [5, 10]

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse(a_list) == [10, 6, 5, 4, 3, 2, 1]

    assert swap_thirds(a_string) == "is a stringthis "
    assert swap_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
    assert swap_thirds(a_list) == [3, 4, 5, 6, 10, 1, 2]

    print("tests passed")

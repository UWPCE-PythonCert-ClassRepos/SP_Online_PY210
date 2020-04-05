def exchange_first_last(seq):
    """
    Return sequence with first and last element flipped
    :param n: Requested sequence to be flipped
    """
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    """
    Return sequence with every other element removed.  Retains first element.
    :param n: Requested sequence to be sliced
    """
    return seq[::2]

def remove_four_leading_ending_every_other(seq):
    """
    Return sequence with first 4, last 4 and every other elements removed.
    :param n: Requested sequence to be sliced
    """
    return seq[4:-4:2]

def reverse_elements(seq):
    """
    Return sequence with elements reversed
    :param n: Requested sequence to be flipped
    """
    return seq[::-1]

def rotate_thirds(seq):
    """
    Return sequence with the the last third, then first third, then the middle third in the new order.
    :param n: Requested sequence to be rotated
    """
    length = len(seq)
    length_of_thirds = length // 3
    return seq[2*length_of_thirds:] + seq[:length_of_thirds] + seq[length_of_thirds:2*length_of_thirds]

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

a_longer_tuple = range(20)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_longer_tuple) == [19, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]

assert remove_every_other(a_longer_tuple) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
assert remove_every_other(a_string) ==  'ti sasrn'

assert remove_four_leading_ending_every_other(a_longer_tuple) == [4, 6, 8, 10, 12, 14]
assert remove_four_leading_ending_every_other(a_string) == ' sas'

assert reverse_elements(a_longer_tuple) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert reverse_elements(a_string) == 'gnirts a si siht'

assert rotate_thirds(a_longer_tuple) == [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert rotate_thirds(a_string) == 'stringthis is a '


print('all tests passed')
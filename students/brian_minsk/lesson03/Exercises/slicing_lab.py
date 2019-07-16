# Author: Brian Minsk

def exchange_first_last(seq):
    """ Exchange the first and last items in the sequence.

    Keyword arguments:
    seq -- the input sequence
    """
    return seq[-1:] + seq[1:len(seq) - 1] + seq[:1]

def remove_every_other_item(seq):
    """ Remove every  other item in the sequence. Assume the second item in the sequence is the first item removed.

    Keyword arguments:
    seq -- the input sequence
    """
    return seq[::2]

def crazy_splice(seq):
    """ Remove the first 4 and last 4 items. Remove every other item from the remaining.

    Keyword arguments:
    seq -- the input sequence
    """
    return seq[4:-4:2]

def reverse(seq):
    """ Reverse the sequence

    Keyword arguments:
    seq -- the input sequence
    """
    return seq[::-1]

def crazy_thirds(seq):
    """ Return the last third, then first third, then the middle third in the new order.
    If the imput sequence length cannot be evenly divided by three the last third will include the remaining items
    (i.e. the floor of the length divided by three plus the modulo of the length divided by three).
    (Note that the first third followed by the middle third is the same as the first two thirds)

    Keyword arguments:
    seq -- the input sequence
    """
    length_first = len(seq)//3 # the length of the middle part will be the same as the first
    length_last = length_first + len(seq)%3

    return seq[-1*length_last:] + seq[:2*length_first]
    
if __name__ == "__main__":
    # run some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other_item(a_string) == "ti sasrn"
    assert remove_every_other_item(a_tuple) == (2, 13, 5)

    assert crazy_splice(a_string) == " sas"
    assert crazy_splice(a_tuple) == ()
    assert crazy_splice(a_longer_tuple) ==(4, 6, 8, 10)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert crazy_thirds(a_string) == "stringthis is a "
    assert crazy_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert crazy_thirds(a_longer_tuple) == (10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

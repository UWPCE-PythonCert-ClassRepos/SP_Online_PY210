#!/usr/bin/env python3

def exchange_first_last(seq):
    """
    Exchange the first and last item in a sequence.
    :param seq: accepts any python sequence
    :type seq: tuple, list, string,etc.
    """
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq1):
    """
    Removes every other item in a sequence
    :param seq1: accepts any python sequence
    :type seq1: tuple, list, string, etc.
    """
    return seq1[0::2]
#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.

def remove_ends(seq2):
    """
    Removes the first 4 items and last 4 items of sequence.
    In addition, it removes every other item in the sequence
    that's left over.
    :param seq2: accepts any python sequence
    :type seq2: tuple, list, string, etc.
    """
    ends_removed = seq2[4:-4:2]
    return ends_removed

def reverse_it_up(seq3):
    """
    Reverses the order of all elements in the sequence
    :param seq3: accepts any python sequence
    :type seq3: tuple, list, string, etc.
    """
    return seq3[::-1]

def mixed_thirds(seq4):
    """
    Reverses a sequence with the order jumbled.
    The output will contain the sequence starting with the last third,
    then the first third, and then the middle third.
    :param seq4: accepts any python sequence
    :type seq4: tuple, list, string, etc.
    """
    #last third, then first third, then the middle third in the new order.
    one_third = int(len(seq4) / 3)
    if len(seq4) % 3 == 0:
        thirds_seq = seq4[-one_third:] + seq4[:one_third] + seq4[one_third:(2 * one_third)]
    
    elif len(seq4) % 3 == 1:
        thirds_seq = seq4[-one_third:] + seq4[:one_third] + seq4[one_third:(2 * one_third + 1)]
    else:
        thirds_seq = seq4[-(one_third + 1):] + seq4[:one_third + 1] + seq4[one_third + 1:(2 * one_third + 1)]

    return thirds_seq

if __name__=='__main__':
    a_string = "this is a strings"
    a_tuple = (2, 54, 13, 12, 5, 32, 34, 4, 23, 512, 3, 17)
    a_list = ["this", "is", "a", "test"]

    # Testing the output of exchanging the first and last item.
    assert exchange_first_last(a_string) == "shis is a stringt"
    assert exchange_first_last(a_tuple) == (17, 54, 13, 12, 5, 32, 34, 4, 23, 512, 3, 2)
    assert exchange_first_last(a_list) == ["test", "is", "a", "this"]

    # Testing the output of removing every other item in a sequence.
    assert remove_every_other(a_string) == "ti sasrns"
    assert remove_every_other(a_tuple) == (2, 13, 5, 34, 23, 3)
    assert remove_every_other(a_list) == ["this", "a"]

    # Testing the removal of ends and yielding every other element.
    assert remove_ends(a_tuple) == (5, 34)
    assert remove_ends(a_string) == " sasr"

    # Testing the output of reversing a sequence order.
    assert reverse_it_up(a_string) == "sgnirts a si siht"
    assert reverse_it_up(a_tuple) == (17, 3, 512, 23, 4, 34, 32, 5, 12, 13, 54, 2)
    assert reverse_it_up(a_list) == ["test", "a", "is", "this"]

    # Shuffling the last third, then first third, then the middle third in the new order.
    assert mixed_thirds(a_list) == ["test", "this", "is", "a"]
    assert mixed_thirds(a_tuple) == (23, 512, 3, 17, 2, 54, 13, 12, 5, 32, 34, 4)
    assert mixed_thirds(a_string) == "tringsthis is a s"

    print("All tests completed successfully!")
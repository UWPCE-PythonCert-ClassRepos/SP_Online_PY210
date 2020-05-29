# slicing_lab.py
# opcode6502: SP_Online_PY210


# REQ-01: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with the first and last items exchanged.
def exchange_first_last(seq):

    # DOCSTRING.
    """
    Returns a copy of a sequence with the first and last items exchanged

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of the sequence with the first and last items exchanged.
    """

    # Variables.
    first_element = seq[:1]
    last_element = seq[-1:]
    final_sequence = last_element + seq[1:-1] + first_element

    return final_sequence


# REQ-02: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with every other item removed.
def remove_alternate_items(seq):

    # DOCSTRING.
    """
    Returns a copy of a sequence with every other item removed

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of the sequence with every other item removed.
    """

    return seq[::2]


# REQ-03: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with the first 4 and the last 4 items removed,
# and then every other item in the remaining sequence.
def remove_four_print_alt(seq):

    # DOCSTRING.
    """
    Returns a copy of a sequence with the first 4 and the last 4 items removed,
    and then every other item in the remaining sequence.

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of the sequence with the first 4 and the last 4 items removed,
        and then every other item in the remaining sequence.
    """

    return seq[4:-4:2]


# REQ-04: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with the elements reversed (just with slicing).
def reverse_sequence(seq):

    # DOCSTRING.
    """
    Returns a copy of a sequence with the elements reversed (just with slicing).

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of a sequence with the elements reversed (just with slicing).
    """

    return seq[::-1]


# REQ-05: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with the last third, then first third,
# then the middle third in the new order.
def third_reorder(seq):

    # DOCSTRING.
    """
    Returns a copy of a sequence with the last third, then first third,
    then the middle third in the new order

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of a sequence with the last third, then first third,
        then the middle third in the new order
    """

    # First, we determine the length of the sequence divided by three.
    seq_third = int(len(seq) / 3)

    # Next, execute the correct code for the length of the string.
    if len(seq) % 3 == 0:
        new_seq = seq[-seq_third:] + seq[:seq_third] + seq[seq_third:(2 * seq_third)]
    elif len(seq) % 3 == 1:
        new_seq = seq[-seq_third:] + seq[:seq_third] + seq[seq_third:(2 * seq_third + 1)]
    else:
        new_seq = seq[-(seq_third + 1):] + seq[:seq_third + 1] + seq[seq_third + 1:(2 * seq_third + 1)]

    return new_seq


# REQ-06: Write a test or two for each of the above functions.
if __name__=='__main__':
    a_string = "The quick brown fox jumps over the lazy dogs"
    a_tuple = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233)

    assert exchange_first_last(a_string) == "she quick brown fox jumps over the lazy dogT"
    assert exchange_first_last(a_tuple) == (233, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 0)
    #
    assert remove_alternate_items(a_string) == "Teqikbonfxjmsoe h aydg"
    assert remove_alternate_items(a_tuple) == (0, 1, 3, 8, 21, 55, 144)
    #
    assert remove_four_print_alt(a_string) == "qikbonfxjmsoe h ay"
    assert remove_four_print_alt(a_tuple) == (3, 8, 21)
    #
    assert reverse_sequence(a_string) == "sgod yzal eht revo spmuj xof nworb kciuq ehT"
    assert reverse_sequence(a_tuple) == (233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0)
    #
    assert third_reorder(a_string) == "r the lazy dogsThe quick brown fox jumps ove"
    assert third_reorder(a_tuple) == (34, 55, 89, 144, 233, 0, 1, 1, 2, 3, 5, 8, 13, 21)

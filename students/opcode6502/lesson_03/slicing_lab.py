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

    # DEBUG statements for developer testing.
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: exchange_first_last(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq                : " + str(seq))
        print("[ DEBUG ]: type(seq)          : " + str(type(seq)))
        print("[ DEBUG ]: first_element      : " + str(first_element))
        print("[ DEBUG ]: last_element       : " + str(last_element))
        print("[ DEBUG ]: final_sequence     : " + str(final_sequence))
        print("")

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

    # DEBUG statements for developer testing.
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: remove_alternate_items(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq                : " + str(seq))
        print("[ DEBUG ]: type(seq)          : " + str(type(seq)))
        print("[ DEBUG ]: seq[0]             : " + str(seq[0]))
        print("[ DEBUG ]: seq[0:]            : " + str(seq[0:]))
        print("[ DEBUG ]: seq[:2]            : " + str(seq[:2]))
        print("[ DEBUG ]: seq[::2]           : " + str(seq[::2]))
        print("")

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

    # DEBUG statements for developer testing.
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: remove_four_print_alt(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq                : " + str(seq))
        print("[ DEBUG ]: type(seq)          : " + str(type(seq)))
        #
        # The first four items.
        print("[ DEBUG ]: seq[4]             : " + str(seq[4]))
        print("[ DEBUG ]: seq[4:]            : " + str(seq[4:]))
        #
        # The last four items.
        print("[ DEBUG ]: seq[-4]            : " + str(seq[-4]))
        print("[ DEBUG ]: seq[:-4]           : " + str(seq[:-4]))
        #
        # Every other item.
        print("[ DEBUG ]: seq[::2]           : " + str(seq[::2]))
        #
        # The final sliced sequence.
        print("[ DEBUG ]: seq[4:-4:2]        : " + str(seq[4:-4:2]))
        print("")

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

    # DEBUG statements for developer testing.
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: reverse_sequence(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq                : " + str(seq))
        print("[ DEBUG ]: type(seq)          : " + str(type(seq)))
        print("[ DEBUG ]: seq[1]             : " + str(seq[1]))
        print("[ DEBUG ]: seq[-1]            : " + str(seq[-1]))
        print("[ DEBUG ]: seq[:1]            : " + str(seq[:1]))
        print("[ DEBUG ]: seq[:-1]           : " + str(seq[:-1]))
        print("[ DEBUG ]: seq[::1]           : " + str(seq[::1]))
        print("[ DEBUG ]: seq[::-1]          : " + str(seq[::-1]))
        print("")

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

    # DEBUG statements for developer testing
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: third_reorder(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq                : " + str(seq))
        print("[ DEBUG ]: len(seq)           : " + str(len(seq)))
        print("[ DEBUG ]: len(seq) / 3       : " + str(len(seq) / 3))
        print("[ DEBUG ]: len(seq) % 3       : " + str(len(seq) % 3))
        print("[ DEBUG ]: seq[seq_third]     : " + str(seq[seq_third]))
        print("[ DEBUG ]: seq[-seq_third]    : " + str(seq[-seq_third]))
        print("[ DEBUG ]: seq[:seq_third]    : " + str(seq[:seq_third]))
        print("[ DEBUG ]: seq[seq_third:]    : " + str(seq[seq_third:]))
        print("[ DEBUG ]: seq[-seq_third:]   : " + str(seq[-seq_third:]))
        print("[ DEBUG ]: seq[::seq_third]   : " + str(seq[::seq_third]))
        print("[ DEBUG ]: seq[::-seq_third]  : " + str(seq[::-seq_third]))
        print("")

    # Next, execute the correct code for the length of the string.
    if len(seq) % 3 == 0:
        new_seq = seq[-seq_third:] + seq[:seq_third] + seq[seq_third:(2 * seq_third)]
    elif len(seq) % 3 == 1:
        new_seq = seq[-seq_third:] + seq[:seq_third] + seq[seq_third:(2 * seq_third + 1)]
    else:
        new_seq = seq[-(seq_third + 1):] + seq[:seq_third + 1] + seq[seq_third + 1:(2 * seq_third + 1)]

    return new_seq


# DEBUG: The debug_flag will turn on helpful testing statements.
# This creates a sort of 'black box' where you can read the exact steps
# that the code executed and debug where things went wrong (or right).
#
# NOTE: These debug messages are best viewed with a terminal width of at least
# 90 to 100 columns (depending on length of strings and tuples to be tested).
#
# Set to 1 = ENABLE debug messages.
# Set to 0 = DISABLE debug messages.
#
# DEBUG MESSAGES key:
# [ EXEC  ]: Informs which function is printing debug statements.
# [ DEBUG ]: A debug statement.
debug_flag = 0


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

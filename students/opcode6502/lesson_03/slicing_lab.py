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
        print("[ DEBUG ]: seq             : " + seq)
        print("[ DEBUG ]: first_element   : " + first_element)
        print("[ DEBUG ]: last_element    : " + last_element)
        print("[ DEBUG ]: final_sequence  : " + final_sequence)

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
        print("[ DEBUG ]: seq             : " + seq)
        print("[ DEBUG ]: seq[0]          : " + seq[0])
        print("[ DEBUG ]: seq[0:]         : " + seq[0:])
        print("[ DEBUG ]: seq[:2]         : " + seq[:2])
        print("[ DEBUG ]: seq[::2]        : " + seq[::2])

    return seq[::2]


# REQ-03: Write a function that takes a sequence as an argument, and
# returns a copy of that sequence with the first 4 and the last 4 items removed,
# and then every other item in the remaining sequence.
def remove_four_print_alternate_items(seq):

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
        print("[ EXEC  ]: seq_req_03(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq             : " + seq)
        #
        # The first four items.
        print("[ DEBUG ]: seq[4]          : " + seq[4])
        print("[ DEBUG ]: seq[4:]         : " + seq[4:])
        #
        # The last four items.
        print("[ DEBUG ]: seq[-4]         : " + seq[-4])
        print("[ DEBUG ]: seq[:-4]        : " + seq[:-4])
        #
        # Every other item.
        print("[ DEBUG ]: seq[::2]        : " + seq[::2])
        #
        # The final sliced sequence.
        print("[ DEBUG ]: seq[4:-4:2]     : " + seq[4:-4:2])

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
        print("[ DEBUG ]: seq             : " + seq)
        print("[ DEBUG ]: seq[1]          : " + seq[1])
        print("[ DEBUG ]: seq[-1]         : " + seq[-1])
        print("[ DEBUG ]: seq[:1]         : " + seq[:1])
        print("[ DEBUG ]: seq[:-1]        : " + seq[:-1])
        print("[ DEBUG ]: seq[::1]        : " + seq[::1])
        print("[ DEBUG ]: seq[::-1]       : " + seq[::-1])

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

    # DEBUG statements for developer testing.
    if debug_flag:
        print("--------------------------------------------------")
        print("[ EXEC  ]: third_reorder(seq): called!")
        print("--------------------------------------------------")
        print("[ DEBUG ]: seq             : " + seq)


# DEBUG: The debug_flag will turn on helpful testing statements.
# This creates a sort of 'black box' where you can read the exact steps
# that the code executed and debug where things went wrong.
#
# Set to 1 = ENABLE debug messages.
# Set to 0 = DISABLE debug messages.
#
# DEBUG MESSAGES key:
# [ EXEC  ]: Informs which function is printing debug statements.
# [ DEBUG ]: A debug statement.
debug_flag = 1


# The test data we will use for this source file.
a_string = "The quick brown fox jumps over the lazy dogs"


# Execute the code.
exchange_first_last(a_string)
remove_alternate_items(a_string)
remove_four_print_alternate_items(a_string)
reverse_sequence(a_string)
third_reorder(a_string)


# REQ-06: Write a test or two like that for each of the above functions.

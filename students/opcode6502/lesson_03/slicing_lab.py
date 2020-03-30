# slicing_lab.py
# opcode6502: SP_Online_PY210


# REQ-01: Write a function that take a sequence as an argument, and
# return a copy of that sequence with the first and last items exchanged.
def exchange_first_last(seq):

    # Python Docstring
    """
    Returns a copy of a sequence with the first and last items exchanged

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of the sequence with the first and last items exchanged.
    """

    #
    first_element = arg[:1]
    last_element = arg[-1:]
    final_sequence = last_element + arg[1:-1] + first_element

    # DEBUG statements for developer testing.
    if debug_flag:
        print("- - - - - - - - - -  - - - - - - - - - - - - - - -")
        print("[ EXEC  ]: exchange_first_last(seq): called!")
        print("[ DEBUG ]: arg: " + arg)
        print("[ DEBUG ]: first_element: " + first_element)
        print("[ DEBUG ]: last_element: " + last_element)
        print("[ DEBUG ]: final_sequence: " + final_sequence)

    return final_sequence


# REQ-02: Write a function that take a sequence as an argument, and
# return a copy of that sequence with every other item removed.
def remove_alternate_items(seq):

    # Python Docstring
    """
    Returns a copy of a sequence with every other item removed

    Args:
        param1: The sequence to be copied and changed.

    Returns:
        A copy of the sequence with every other item removed.
    """

    # DEBUG statements for developer testing.
    if debug_flag:
        print("- - - - - - - - - -  - - - - - - - - - - - - - - -")
        print("[ EXEC  ]: remove_alternate_items(seq): called!")
        print("[ DEBUG ]: arg: " + arg)
        print("[ DEBUG ]: arg[0] " + arg[0])
        print("[ DEBUG ]: arg[0:] " + arg[0:])
        print("[ DEBUG ]: arg[:2] " + arg[:2])
        print("[ DEBUG ]: arg[::2] " + arg[::2])

    return arg[::2]


# REQ-03: Write a function that take a sequence as an argument, and
# return a copy of that sequence with the first 4 and the last 4 items removed,
# and then every other item in the remaining sequence.
def seq_req_03(arg):
    print(arg)

# REQ-04: Write a function that take a sequence as an argument, and
# return a copy of that sequence with the elements reversed (just with slicing).
def seq_req_04(arg):
    print(arg)


# REQ-05: Write a function that take a sequence as an argument, and
# return a copy of that sequence with the last third, then first third,
# then the middle third in the new order.
def seq_req_05(arg):
    print(arg)


# DEBUG: The debug_flag will turn on helpful testing statements.
# This creates a sort of 'black box' where you can read the exact steps
# the code executed and debug where things went wrong.
#
# Set to 1 = ENABLE debug messages.
# Set to 0 = DISABLE debug messages.
#
# DEBUG MESSAGES key:
# [ EXEC  ]: Informs which function is printing debug statements.
# [ DEBUG ]: A debug statement.
debug_flag = 0


# The test data we will use for this source file.
a_string = "The quick brown fox jumps over the lazy dogs"


exchange_first_last(a_string)
seq_req_02(a_string)
seq_req_03(a_string)
seq_req_04(a_string)
seq_req_05(a_string)

# REQ-06: Write a test or two like that for each of the above functions.

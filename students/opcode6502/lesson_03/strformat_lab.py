# strformat_lab.py
# opcode6502: SP_Online_PY210


def main():

    # REQ-01: Write a format string that will take the following four element tuple: 
    # INPUT : ( 2, 123.4567, 10000, 12345.67) 
    # OUTPUT:  'file_002 :   123.46, 1.00e+04, 1.23e+04'

    # REQ-02: Using your results from Task One, repeat the exercise,
    # but this time using an alternate type of format string.

    # REQ-03: Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    # to take an arbitrary number of values.

    # REQ-04: Given a 5 element tuple:  ( 4, 30, 2017, 2, 27) 
    # Use string formating to print:  '02 27 2017 04 30'

    # REQ-05: Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    # Write an f-string that will display:
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    # Now see if you can change the f-string so that it
    # displays the names of the fruit in upper case,
    # and the weight 20% higher (that is 1.2 times higher).

    # REQ-06: Write some Python code to print a table of several rows,
    # each with a name, an age and a cost.
    #
    # Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
    #
    # And for an extra task,
    # given a tuple with 10 consecutive numbers,
    # can you work how to quickly print the tuple in
    # columns that are 5 charaters wide? It can be done on one short line!


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


if __name__=='__main__':
    main()
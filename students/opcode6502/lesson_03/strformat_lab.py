# strformat_lab.py
# opcode6502: SP_Online_PY210


def main():

    # REQ-01: Write a format string that will take the following four element tuple: 
    # INPUT : (2, 123.4567, 10000, 12345.67) 
    # OUTPUT:  'file_002 :   123.46, 1.00e+04, 1.23e+04'

    # DEBUG statements for developer testing.
    if debug_flag:

        # Create the test tuple
        test_tuple = (2, -2, 2.50, -2.50, 123.4567, 12345.67, "Hello", "Hi there", "The quick brown fox jumps over the lazy dogs")

        print("--------------------------------------------------")
        print("[ EXEC  ]: STRING FORMATTING DEBUG TESTING")
        print("--------------------------------------------------")
        for item in test_tuple:

            # Item
            print("[ DEBUG ]: item               : " + str(item))
            print("[ DEBUG ]: type               : " + str(type(item)))

            # Basic formatting usage
            # { } { } .format(value1, value2)

            # Intergers
            if isinstance(item, int):
                print("[ DEBUG ]: { :=}              : " + str('{:=}'.format(item)))
                print("[ DEBUG ]: { :+}              : " + str('{:+}'.format(item)))
                print("[ DEBUG ]: { :-}              : " + str('{:-}'.format(item)))
                print("[ DEBUG ]: { : }              : " + str('{: }'.format(item)))
                print("[ DEBUG ]: { :b}              : " + str('{:b}'.format(item)))
                print("[ DEBUG ]: { :d}              : " + str('{:d}'.format(item)))
                print("[ DEBUG ]: { :4d}             : " + str('{:4d}'.format(item)))
                print("[ DEBUG ]: { :e}              : " + str('{:e}'.format(item)))
                print("[ DEBUG ]: { :.4e}            : " + str('{:.4e}'.format(item)))
                print("[ DEBUG ]: { :f}              : " + str('{:f}'.format(item)))
                print("[ DEBUG ]: { :.4f}            : " + str('{:.4f}'.format(item)))
                print("[ DEBUG ]: { :g}              : " + str('{:g}'.format(item)))
                print("[ DEBUG ]: { :n}              : " + str('{:n}'.format(item)))
                print("[ DEBUG ]: { :o}              : " + str('{:o}'.format(item)))
                print("[ DEBUG ]: { :x}              : " + str('{:x}'.format(item)))

            # Floating Point
            if isinstance(item, float):
                print("[ DEBUG ]: { :=}              : " + str('{:=}'.format(item)))
                print("[ DEBUG ]: { :+}              : " + str('{:+}'.format(item)))
                print("[ DEBUG ]: { :-}              : " + str('{:-}'.format(item)))
                print("[ DEBUG ]: { : }              : " + str('{: }'.format(item)))
                print("[ DEBUG ]: { :e}              : " + str('{:e}'.format(item)))
                print("[ DEBUG ]: { :.4e}            : " + str('{:.4e}'.format(item)))
                print("[ DEBUG ]: { :f}              : " + str('{:f}'.format(item)))
                print("[ DEBUG ]: { :.4f}            : " + str('{:.4f}'.format(item)))
                print("[ DEBUG ]: { :g}              : " + str('{:g}'.format(item)))
                print("[ DEBUG ]: { :n}              : " + str('{:n}'.format(item)))

            # Strings
            if isinstance(item, str):

                # Alignment
                print("[ DEBUG ]: { :1}              : " + str('{:1}'.format(item)))
                print("[ DEBUG ]: { :>1}             : " + str('{:>1}'.format(item)))
                print("[ DEBUG ]: { :^1}             : " + str('{:^1}'.format(item)))
                print("[ DEBUG ]: { :50}             : " + str('{:50}'.format(item)))
                print("[ DEBUG ]: { :>50}            : " + str('{:>50}'.format(item)))
                print("[ DEBUG ]: { :^50}            : " + str('{:^50}'.format(item)))

                # Padding
                print("[ DEBUG ]: { :_<50}           : " + str('{:_<50}'.format(item)))
                print("[ DEBUG ]: { :_>50}           : " + str('{:_>50}'.format(item)))

                # Truncating
                print("[ DEBUG ]: { :.1}             : " + str('{:.1}'.format(item)))
                print("[ DEBUG ]: { :.5}             : " + str('{:.5}'.format(item)))
                print("[ DEBUG ]: { :.40}            : " + str('{:.40}'.format(item)))

            print("--------------------------------------------------")

    # Create tuple
    tuple_01 = (2, 123.4567, 10000, 12345.67)

    # Print tuple
    print("file_{0:0>3d}: {1:.2f}, {2:.2e}, {3:.2e}".format(*tuple_01))

    # REQ-02: Using your results from Task One, repeat the exercise,
    # but this time using an alternate type of format string.
    print(f"file_{tuple_01[0]:0>3d}: {tuple_01[1]:.2f}, {tuple_01[2]:.2e}, {tuple_01[3]:.2e}")

    # REQ-03: Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    # to take an arbitrary number of values.

    def formatter(in_tuple):
        l = len(in_tuple)
        output = ("The {} numbers are: " + ', '.join(['{:d}'] * l)).format(l, *in_tuple)
        return output
    tuple_02 = (1, 2)
    tuple_03 = (1, 1, 2, 3, 5, 8)
    tuple_04 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    print(formatter(tuple_02))
    print(formatter(tuple_03))
    print(formatter(tuple_04))

    # REQ-04: Given a 5 element tuple:  ( 4, 30, 2017, 2, 27) 
    # Use string formating to print:  '02 27 2017 04 30'

    tuple_05 = (4, 30, 2017, 2, 27)
    print("{3:0>2d} {4:0} {2:0} {0:0>2d} {1:0}".format(*tuple_05))

    # REQ-05: Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    # Write an f-string that will display:
    # The weight of an orange is 1.3 and the weight of a lemon is 1.1
    # Now see if you can change the f-string so that it
    # displays the names of the fruit in upper case,
    # and the weight 20% higher (that is 1.2 times higher).

    tuple_06 = ('orange', 1.3, 'lemon', 1.1)
    print(f"The weight of an {tuple_06[0]} is {tuple_06[1]} and the weight of a {tuple_06[2]} is {tuple_06[3]}")
    print(f"The weight of an {tuple_06[0].upper()} is {tuple_06[1]*1.2} and the weight of a {tuple_06[2].upper()} is {tuple_06[3]*1.2}")

    # REQ-06: Write some Python code to print a table of several rows,
    # each with a name, an age and a cost.
    #
    # Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

    # Create tuples
    tuple_name = ("John", "Joe", "Mike", "Tony")
    tuple_age = (20, 25, 32, 999)
    tuple_cost = (10.99, 15, 25.97654321, 2221)

    # Find length of the tuple (note: all tuples must be equal length or we receive an index error)
    l = len(tuple_cost)

    # Format the tuples with center alignment
    row_name = ('{:^15}'* l).format(*tuple_name)
    row_age = ('{:^15}'* l).format(*tuple_age)
    row_cost = ('{:^15.2f}'* l).format(*tuple_cost)

    # print tuples
    print(row_name)
    print(row_age)
    print(row_cost)

    # And for an extra task, given a tuple with 10 consecutive numbers,
    # can you work how to quickly print the tuple in
    # columns that are 5 charaters wide? It can be done on one short line!

    tuple_06 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(('{:5}' * (len(tuple_06))).format(*tuple_06))


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

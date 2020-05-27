# strformat_lab.py
# opcode6502: SP_Online_PY210


def main():

    # REQ-01: Write a format string that will take the following four element tuple: 
    # INPUT : (2, 123.4567, 10000, 12345.67) 
    # OUTPUT:  'file_002 :   123.46, 1.00e+04, 1.23e+04'

    # Create the tuple.
    tuple_01 = (2, 123.4567, 10000, 12345.67)

    # Print the tuple.
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
    tuple_06 = ('orange', 1.3, 'lemon', 1.1)
    print(f"The weight of an {tuple_06[0]} is {tuple_06[1]} and the weight of a {tuple_06[2]} is {tuple_06[3]}")

    # Now see if you can change the f-string so that it
    # displays the names of the fruit in upper case,
    # and the weight 20% higher (that is 1.2 times higher).
    print(f"The weight of an {tuple_06[0].upper()} is {tuple_06[1]*1.2} and the weight of a {tuple_06[2].upper()} is {tuple_06[3]*1.2}")

    # REQ-06: Write some Python code to print a table of several rows,
    # each with a name, an age and a cost.
    #
    # Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

    # Create the tuples
    tuple_name = ("John", "Joe", "Mike", "Tony")
    tuple_age = (20, 25, 32, 999)
    tuple_cost = (10.99, 15, 25.97654321, 2221)

    # Find the length of the tuples.
    # Note: all tuples must be equal length or we receive an index error.
    l = len(tuple_cost)

    # Format the tuples with center alignment.
    row_name = ('{:^15}'* l).format(*tuple_name)
    row_age = ('{:^15}'* l).format(*tuple_age)
    row_cost = ('{:^15.2f}'* l).format(*tuple_cost)

    # Print the tuples.
    print(row_name)
    print(row_age)
    print(row_cost)

    # And for an extra task, given a tuple with 10 consecutive numbers,
    # can you work how to quickly print the tuple in
    # columns that are 5 charaters wide? It can be done on one short line!

    tuple_06 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(('{:5}' * (len(tuple_06))).format(*tuple_06))


if __name__=='__main__':
    main()

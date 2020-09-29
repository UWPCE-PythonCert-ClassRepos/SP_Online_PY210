#!/usr/bin/env python3

"""Task One: Use a given tuple to produce a string using string formatting operators."""
a_tuple = (2, 123.4567, 10000, 12345.67)

file_name = a_tuple[0]
ele2 = a_tuple[1]
ele3 = a_tuple[2]
ele4 = a_tuple[3]

print(f"file_{file_name:03} :    {ele2:.2f}, {ele3:.2e}, {ele4:.3g}")

"""Task Two: Use the result from Task One to produce the same string using a different string format type (string.format() in this case)."""
print("file_{:03} :    {:.2f}, {:.2e}, {:.3g}".format(file_name, ele2, ele3, ele4))

"""Task Three: Produce a string that takes an arbitrary number of values."""
def formatter(in_tuple):
    tup_length = len(in_tuple)

    build_string = "the {} numbers are: {}" + (", {}" * (tup_length - 1))

    return build_string.format(tup_length, *in_tuple[:])

"""Task Four: Use a given tuple to produce a formatted string."""
tup_5 = (4, 30, 2017, 2, 27)

zero = tup_5[0]
one = tup_5[1]
two = tup_5[2]
three = tup_5[3]
four = tup_5[4]

print(f"{three:02} {four} {two} {zero:02} {one}")

"""Task Five: Use a given list to produce specific f-strings."""
list4 = ['oranges', 1.3, 'lemons', 1.1]

fruit = list4[0]
weight = list4[1]
fruit2 = list4[2]
weight2 = list4[3]

print(f"The weight of an {fruit[:-1]} is {weight} and the weight of a {fruit2[:-1]} is {weight2}")

# produce the same string as above with the weight values (indexes 1 and 3) 20% greater.
print(f"The weight of an {fruit[:-1].upper()} is {weight * 1.2} and the weight of a {fruit2[:-1].upper()} is {weight2 * 1.2}")

"""Task Six: Use string formatting to display data in columns.

Use alignment specifers to ensure the columns are properly aligned.
Extra task: display a tuple of 10 consecutive numbers in columns of 5 characters wide.
"""
row1 = ['Larry', 23, 190.00]
row2 = ['Sabine', 12, 4500.00]
row3 = ['Katy', 89, 42.50]
row4 = ['Ben', 6, 10500.23]

table = [row1, row2, row3, row4]

for row in table:
    print("{:20}{:>20}{:>20.2f}".format(*row[:]))

# task six: extra task
def consecutive_tup(n):
    print(("{:>5}" * len(n)).format(*n[:]))
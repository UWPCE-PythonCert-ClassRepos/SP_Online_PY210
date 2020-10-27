#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Lesson 03
# Description: Slicing Lab
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/16/2020, Created script
# Kate Golenkova, 10/18/2020, Changed script
# Kate Golenkova, 10/19/2020, Changed script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #

# Task One
print("Task One")
# Variables ------------------------------------------------------------------ #
a = (2, 123.4567, 10000, 12345.67)


# Functions ------------------------------------------------------------------ #
def format_string():
    """ Format each element in tuple as a string and print string """

    form = 'file_{:03d} :   {:.2f}, {:.2e}, {:.2e} '
    print(form.format(*a))

format_string()

# Task Two ------------------------------------------------------------------- #
print("\nTask Two")

# Variables ------------------------------------------------------------------ #

# Functions ------------------------------------------------------------------ #
def f_func():
    """ Format each element in tuple using keywords and f-string and print string """

    file, num1, num2, num3 = a
    print(f'file_{file:03d} :   {num1:.2f}, {num2:.2e}, {num3:.2e} ')

f_func()

# Task Three------------------------------------------------------------------- #
print("\nTask Three")

# Variables ------------------------------------------------------------------ #
tuple1 = (1, 3, 2, 5, 1, 6, 9)

# Functions ------------------------------------------------------------------ #
def formatter(tuple1):
    """ Dynamically build up the format string to accommodate the length of the tuple,
        Returns a string.
    """

    n = str(len(tuple1))
    form = ""
    for i in tuple1:
        form += '{:d}, '

    print(" The " + n + " numbers are: " + form.format(*tuple1))
    return form.format(*tuple1)

formatter(tuple1)
formatter(tuple1*2)

# Task Four ------------------------------------------------------------------ #
print("\nTask Four")

# Variables ------------------------------------------------------------------ #
tuple2 = ( 4, 30, 2017, 2, 27)

# Functions ------------------------------------------------------------------ #
def form_tuple(tuple2):
    """ Returns tuple with other order"""

    print(f'{tuple2[-2:] + tuple2[2:len(tuple2)-2] + tuple2[:2]}')

form_tuple(tuple2)


# Task Five ------------------------------------------------------------------ #
print("\nTask Five")

# Variables ------------------------------------------------------------------ #
fr = ['oranges', 1.3, 'lemons', 1.1]

# Functions ------------------------------------------------------------------ #
def f_str(fr):
    """ F-string displays list in certain order.
        Also, f-string format string with upper case letters and modified weight
    """

    fr[0] = 'orange'
    fr[2] = 'lemon'
    print(f'The weight of an {fr[0]} is {fr[1]} and the weight of a {fr[2]} is {fr[3]}')
    print(f'The weight of an {fr[0].upper()} is {fr[1]*1.2} and the weight of a {fr[2].upper()} is {fr[3]*1.2}')

f_str(fr)


# Task Six ------------------------------------------------------------------ #
print("\nTask Six")

# Variables ------------------------------------------------------------------ #
A = [
    [ 'The House', 30, 500000.00],
    [ 'The Boat', 8, 120000.00],
    [ 'The Car', 2, 50000.00]
    ]
aa = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Functions ------------------------------------------------------------------ #
def format_table(A):
    """ Returns rows in a table with all the items/ages/prices """

    for i in A:
        print('| Name: {0:10} | Age: {1:5} years | Price: {2:,} dollars |'.format(*i))

format_table(A)

# Print the tuple aa in columns that are 5 characters wide

print("The numbers are: ")
print("\n".join(len(aa)*["{:5}"]).format(*aa))


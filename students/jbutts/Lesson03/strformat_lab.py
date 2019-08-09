#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Module 3: strformat_lab

Task 1:

Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'

'''

print("\nTask 1:")

A_TUPLE = (2, 123.4567, 10000, 12345.67)
DESIRED_OUTPUT = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("\nPart 1:")
print("file_00{:d} :   {:.2f}, {:.2e}, {:.2e}".format(*A_TUPLE))
assert ("file_00{:d} :   {:.2f}, {:.2e}, {:.2e}".format(*A_TUPLE)) == DESIRED_OUTPUT


'''
Task 2

Using your results from Task One, repeat the exercise, but this time using an alternate type 
of format string (hint: think about alternative ways to use .format() (keywords anyone?), and 
also consider f-strings if you’ve not used them already).

'''


print("\nTask 2:")
print(f"file_00{A_TUPLE[0]:d} :   {A_TUPLE[1]:.2f}, {A_TUPLE[2]:.2e}, {A_TUPLE[3]:.2e}")
assert f"file_00{A_TUPLE[0]:d} :   {A_TUPLE[1]:.2f}, {A_TUPLE[2]:.2e}, {A_TUPLE[3]:.2e}"\
       == DESIRED_OUTPUT



'''
Task 3

Rewrite the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary # of values

'''
print("\nTask 3:")
A_TUPLE = (1, 2, 3, 4, 5, 6, 7)


def format_tuple(l, a_tuple):
    DISPLAY = ["{}"]*l
    print("The {} numbers are: ".format(l) + ", ".join(DISPLAY).format(*a_tuple))


format_tuple(len(A_TUPLE), A_TUPLE)

# assert format_tuple(len(a_tuple), a_tuple) == "The 7 numbers are: 1, 2, 3, 4, 5, 6, 7"

'''
Task 4

Given a 5 element tuple:

( 4, 30, 2017, 2, 27)

use string formating to print:

'02 27 2017 04 30'

Hint: use index numbers to specify positions.

'''

print("\nTask 4:")

t = ( 4, 30, 2017, 2, 27)
DESIRED_OUTPUT = '02 27 2017 04 30'
print(f"{t[3]:02} {t[4]} {t[2]} {t[0]:02} {t[1]}")
assert f"{t[3]:02} {t[4]} {t[2]} {t[0]:02} {t[1]}" == DESIRED_OUTPUT

'''
Task 5

Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

<<<<<<< HEAD
Now see if you can change the f-string so that it displays the names of the fruit in upper case, 
and the weight 20% higher (that is 1.2 times higher).
'''

print("\nTask 5:")

l = ['oranges', 1.3, 'lemons', 1.1]
DESIRED_OUTPUT = "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
OUTPUT = f"The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}"
print(OUTPUT)
assert OUTPUT == DESIRED_OUTPUT
OUTPUT = f"The weight of an {l[0][:-1].title()} is {(l[1]*1.2)} and the weight of a" \
         f" {l[2][:-1].title()} is {l[3]*1.2}"
print(OUTPUT)
assert OUTPUT == "The weight of an Orange is 1.56 and the weight of a Lemon is 1.32"



'''
Task 6

Write some Python code to print a table of several rows, each with a name, an age and a cost. 
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print 
the tuple in columns that are 5 characters wide? It can be done on one short line!

'''

print("\nTask 6:")
TABLE_DATA = list()
TABLE_DATA.append(["wine", 9, "$110.00"])
TABLE_DATA.append(["beer", 0.3, "$11.00"])
TABLE_DATA.append(["whisky", 18, "$11,000.00"])


print(f"\n\n{'drink':<10}{'age (y)':<8} {'price':<12}")
print("=" * 9 + " " + "=" * 8 + " " + "="*11)


for i in TABLE_DATA:
    print(f"{i[0]:<10}{i[1]:>8}{i[2]:>12}")

print(f"\n\n{'col1':<5}{'col2':<5}")
print("=" * 5 + " " + "=" * 5)

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# use the map() function to convert each int into a string so join() will work
print(''.join(map(str, t[0:5])) + " " + ''.join(map(str, t[-5:])))



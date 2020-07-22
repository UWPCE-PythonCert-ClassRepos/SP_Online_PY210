#! bin/user/env python3
"""
Task One:
Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
Task Two:
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string
(hint: think about alternative ways to use .format() (keywords anyone?),
and also consider f-strings if you’ve not used them already).
Task Three:
Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
Task Four:
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Task Five:
Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
Now see if you can change the f-string so that it displays the names of the fruit in upper case,
and the weight 20% higher (that is 1.2 times higher).
Task Six:
Write some Python code to print a table of several rows, each with a name, an age and a cost.
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers,
can you work how to quickly print the tuple in columns that are 5 charaters wide?
It can be done on one short line!
"""

my_tuple = (2, 123.4567,10000, 12345.67)
test = (6, 7, 8)
my_seq = (4, 30, 2017, 2, 27)
new_seq = ("oranges", 1.3, "lemons", 1.1)
inventory = (('Lex', 13, '$7800.99'),
             ('razer', 1, '$90.07899'),
             ('scooby', 3.5, '$800'),
             ('snoqualmie falls', 121, '$200,000,000'))

def formatter(seq):
    x = len(seq)
    form_str = ("The {} numbers are: " + ", ".join(["{}"] * x)).format(x, *seq)
    print(form_str)

def tabular_view(seq):
    print(seq[0])
    print(seq[1])
    print(seq[2])
    print(seq[3])

# Task one: take the four element tuple and produce
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("file_{:03d} : {:.2f}, {:.2e}, {:.2e}".format(my_tuple[0], my_tuple[1], my_tuple[2], my_tuple[3]))

# Task two: Use the same Tuple from task one but rewrite using a different format strings method
print(f"file_{my_tuple[0]:03d} : {my_tuple[1]:.2f}, {my_tuple[2]:.2e}, {my_tuple[3]:.2e}")

# Task three:
formatter(my_tuple)
formatter(test)

# Task four: rearranging given tuple using set positions
print(f"{my_seq[3]}, {my_seq[4]}, {my_seq[2]}, {my_seq[0]}, {my_seq[1]}")

# Task five:
print(f"The weight of an {new_seq[0]} is {new_seq[1]} and the weight of a {new_seq[2]} is {new_seq[3]}")
print(f"The weight of an {new_seq[0].upper()} is {new_seq[1] * 1.2} and the weight of a {new_seq[2].upper()} is {new_seq[3] * 1.2}")

# Task six:
tabular_view(inventory)
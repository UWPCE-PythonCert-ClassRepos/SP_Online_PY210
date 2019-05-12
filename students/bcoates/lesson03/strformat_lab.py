#!/usr/bin/env python3

# Task 1

# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'
output = "file_{0:03d} :   {1:.2f}, {2:.2e}, {3:.3g}"
print(output.format(2, 123.4567, 10000, 12345.67))

# Task 2

# Using your results from Task One, repeat the exercise, 
# but this time using an alternate type of format string
pad = 2
decimal = 123.4567
sci = 1000
significant = 12345.67
output = f"file_{pad:03d} :   {decimal:.2f}, {sci:.2e}, {significant:.3g}"
print(output)

# Task 3

# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.
def formatter(in_tuple):
    form_string = "the {} numbers are: ".format(str(len(in_tuple)))
    for i in in_tuple:
        if i < len(in_tuple):
            form_string += '{:d}, '
        else:
            form_string += '{:d}'
    return form_string.format(*in_tuple)

# Task 4

# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'
a_tuple = (4, 30, 2017, 2, 27)
output = '{3:02d} {4} {2} {0:02d} {1}'.format(*a_tuple)
print(output)

# Task 5

# Here’s a task for you: Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1
fruit_list = ['oranges', 1.3, 'lemons', 1.1]
output = f"The weight of an {fruit_list[0][:-1]} is {fruit_list[1]} and the weight of a {fruit_list[2][:-1]} is {fruit_list[3]}"
print(output)

# Now see if you can change the f-string so that it displays the 
# names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
output = f"The weight of an {fruit_list[0][:-1].upper()} is {fruit_list[1]*1.2} and the weight of a {fruit_list[2][:-1].upper()} is {fruit_list[3]*1.2}"
print(output)

# Task 6

# Write some Python code to print a table of several rows, each with a name,
# an age and a cost. Make sure some of the costs are in the hundreds and 
# thousands to test your alignment specifiers.
print("Name: {:<10}  Age: {:>3}  Cost:  {:>8}".format("Joe", 15, 22.22))
print("Name: {:<10}  Age: {:>3}  Cost:  {:>8}".format("Jill", 105, 24444.55))
print("Name: {:<10}  Age: {:>3}  Cost:  {:>8}".format("George", 28, 13.75))

# And for an extra task, given a tuple with 10 consecutive numbers, can you 
# work how to quickly print the tuple in columns that are 5 charaters wide? 
# It can be done on one short line!
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(str('{:>5}' * len(a_tuple)).format(*a_tuple))
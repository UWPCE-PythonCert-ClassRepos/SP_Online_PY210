# -*- coding: utf-8 -*-
"""
Grant Dowell
Excercise 3.3 - String Formatting
"""

# ---- Task 1 ----
a_tuple = (2, 123.4567, 10000, 12345.67)

a_str = "file_{:03d} :    {:.2f}, {:.2e}, {:3.2e}".format(
    a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3])
print(a_str)

# ---- Task 2 ----
b_str = (f"file_{a_tuple[0]:03d} :    {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, "
         "{a_tuple[3]:3.2e}")
print(b_str)

# ---- Task 3 ----
# Rewrite: "the 3 numbers are {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values

t = (1, 2, 3, 4)

def formatter(in_tuple):
    form_string = f"the {len(in_tuple)} numbers are: "
    for _ in in_tuple:
        form_string = form_string + " {:d},"
    form_string = form_string[:-1]  #Remove the trailing ','
    return form_string.format(*in_tuple)

c_str = formatter(t)
print(c_str)

# ---- Task 4 ----
# Given the tuple (4, 30, 2017, 2, 27)
# Print '02 27 2017 04 30'

b_tuple = (4, 30, 2017, 2, 27)
d_str = "{:02d} {:02d} {:d} {:02d} {:02d}".format(b_tuple[-2], b_tuple[-1],
         b_tuple[2], b_tuple[0], b_tuple[1])
print(d_str)

# ---- Task 5 ----
# Given: ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string to display "The weight of an orange is 1.3 and the weight
#    of a lemon is 1.1

in_list = ['oranges', 1.3, 'lemons', 1.1]
d_str = (f"The weight of an {in_list[0][:-1]} is {in_list[1]} and the weight "
         "of a {in_list[2][:-1]} is {in_list[3]}")
print(d_str)
e_str = (f"The weight of an {in_list[0][:-1].upper()} is {in_list[1]*1.2} and "
         "the weight of a {in_list[2][:-1].upper()} is {in_list[3]*1.2}")
print(e_str)

# ---- Task 6 ----
# Print a table of several rows, each with a name, age, and cost.
# For extra, given a tuple of 10 consecutive nubmers, work how to quickly print
#     the tuple in columns that are 5 characters wide. It can be done in one
#     short line

a_tup = ('Pizza', 5, 18.19)
b_tup = ('iphone', 2, 840)
c_tup = ('car', 15, 12480.56)
db = [a_tup, b_tup, c_tup]

print(f"Name       | Age |  Price")
print(f"---------------------------")
for item in db:
    print("{:<10} | {:3.0f} | {:8.2f}".format(*item))

d_tup = (10, 8432.93, 983, 983.398, 285, 8739, 1, 8462, 989.3, 10)
print(("{: 5.0f} "*10).format(*d_tup))

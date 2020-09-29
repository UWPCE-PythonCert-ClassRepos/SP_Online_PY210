#!/usr/bin/env python3
# --------------------------------
# 06/29/19 Jinee Han
# Python Programming Lesson 3
# StringFormat Lap
# ---------------------------------

# Task 1.
# Product 'file_002 :   123.46, 1.00e+04, 1.23e+04'
a_tuple = ( 2, 123.4567, 10000, 12345.67)
new_tuple = 'file_{:03d}: {:.2f}, {:.2e}, {:.2e}'.format(*a_tuple)
print ("Task 1\n")
print (new_tuple,'\n')

# Task 2.
# Use an alternate type of format string
file_number = 2
print ("Task 2\n")
print ("file_{:0>3d}".format(file_number))

number = 123.4567
precision = 2
print ("{:.{}f}".format(number,precision))

print (format(10000, "5.2e"))
print (format(12345.67, "5.2e"))
print ('\n')

# Task 3.

# Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
def formatter(in_tuple):
    l = len(in_tuple)
    form_string = ", ".join(["{}"] * l)
    return (("the {} numbers are: " + form_string) .format(l, *in_tuple))

a = [2,3,4]
print ("Task 3\n")
print (formatter(a),'\n')

# Task 4.

# Use string formating to print '02 27 2017 04 30'
a_tuple_2 = (4, 30, 2017, 2, 27)
form_string = " ".join(["{:02d}"] * 5)
new_list = form_string.format(a_tuple_2[3],a_tuple_2[4],a_tuple_2[2],a_tuple_2[0],a_tuple_2[1])

print("Task 4\n")
print(new_list,'\n')

# Task 5.

# Write an f-string to display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

fruit_list = ["orange", 1.3, "lemons", 1.1]
print ("Task 5\n")
print (fruit_list)
print (f"The weight of an {fruit_list[0]} is {fruit_list[1]} and the weight of a {fruit_list[2]} is {fruit_list[3]}.")
# displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
print (f"The weight of an {fruit_list[0].upper()} is {fruit_list[1]*1.2} and the weight of a {fruit_list[2].upper()} is {fruit_list[3]*1.2}.")
print ('\n')

#Task 6.

# Write some Python code to print a table of several rows,
# each with a name, an age and a cost.
# Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.


name = ("Abracatabra","Jo", "Dave")
age = (3, 28, 100)
cost = (29.95, 80, 1950345.678)
l = len(name)

format = ('{:^20}'* l).format(*name) # Align the name in the middle
format2 = ('{:^20}'* l).format(*age)  # Align the age in the middle
format3 = ('{:^20.2f}'* l).format(*cost) # Align the price in the middle
print ("Task 6\n")
print (format)
print (format2)
print (format3)

# Extra Task.

# given a tuple with 10 consecutive numbers,
# can you work how to quickly print the tuple in columns that are 5 characters wide? It can be done on one short line!


tuple_1 = (1,2,3,4,5,6,7,8,9,10)
print(('{:{width}}'*5).format(*tuple_1, width=5)) # I couldn't figure out...

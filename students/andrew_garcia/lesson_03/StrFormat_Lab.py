'''
Andrew Garcia
StrFormat Lab
6/19/19
'''


#!/usr/bin/env python3


# Task One
sequence = (2, 123.4567, 10000, 12345.67)
filename, two_decimals, scientific, scientific2 = sequence

print("'file_{:0>3d} :  {:.2f}, {:.2e}, {:.2e}'".format(filename, two_decimals, scientific, scientific2))


# Task Two
print(f"'file_{filename:0>3d} :  {two_decimals:.2f}, {scientific:.2e}, {scientific2:.2e}'")


# Task Three
def formatter(numbers):
    numbering = (('{:d}, ') * (len(numbers) - 1) + '{:d}').format(*numbers)
    formatted = ("The {} numbers are: {}".format(len(numbers), numbering))
    return formatted


# Task Four
tuple = ( 4, 30, 2017, 2, 27)

def new_tuple(tuple):
    one, two, three, four, five = tuple
    new_tuple = "{:0>2d} {} {} {:0>2d} {}".format(four, five, three, one, two)
    return new_tuple

print(new_tuple(tuple))


# Task Five
fruit_one = ['orange', 1.3]
fruit_two = ['lemon', 1.1]

print(f"The weight of an {fruit_one[0]} is {fruit_one[1]} and the weight of a {fruit_two[0]} is {fruit_two[1]}")
print(f"The weight of an {fruit_one[0].upper()} is {fruit_one[1] * 1.2} and the weight of a {fruit_two[0].upper()} is {fruit_two[1] * 1.2}")


# Task Six
information = [['Kevin', 32, 5.50], ['Michael', 42, 1500], ['Rachel', 29, 11], ['Joey', 25, 100000], ['Walter', 52, 500]]
print('{:12}{:10}{}'.format('Name', 'Age', 'Cost'))
for list in information:
    for item in list:
        print('{:12}{:<10}${:.2f}'.format(list[0], list[1], list[2]))
        break

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print((('{:<5}') * len(tuple)).format(*tuple))

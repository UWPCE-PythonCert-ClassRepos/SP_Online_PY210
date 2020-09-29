#!/usr/bin/env python3
import sys
##############################################################
# 20200615    djm list lab
# 20200623    djm list lab revised per comments from Natasha June 23, 2020
# 20200701    djm list lab revised per comments email Mon 6/29/2020 5:22 PM
#               No space after print; whitespace around assignment operators;
# added
#
#
# Duane McCollum Python self-paced winter 2020
#
# Exercise 3.1: List Lab (graded)
# https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/
#
#############################################################

# Series 1 revised
# instead of separate functions, actions are now single line
fruit = list(('Apples', 'Pears', 'Oranges', 'Peaches'))

# Ask the user for another fruit and add it to the end of the list.
# Display the list.
response = input("add a fruit > ")
print('your entered ' + response)
fruit.append(response)
print(fruit)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
response = input("get a fruit (by index)> ")
print('your entered ' + response)
print(fruit[int(response)])


# Add another fruit to the beginning of the list using “+” and display the list.
add_fruit = input("Add a fruit to the top of the list> ")
print('your entered ' + add_fruit )
fruit = [add_fruit] + fruit
print(fruit)

# Add another fruit to the beginning of the list using insert() and display the list.
add_fruit = input("Add a fruit to the top of the list> ")
print('your entered ' + add_fruit )
fruit.insert(0, add_fruit)
print(fruit)

# Display all the fruits that begin with “P”, using a for loop.
return_str = ''
for i, j in enumerate(fruit):
    if 'P' in j[0]:
        return_str += (j + '\n')
print(return_str)

# Series 2

#!/usr/bin/env python3
import sys
##############################################################
# 20200615    djm list lab
#
# Duane McCollum Python self-paced winter 2020
#
# Exercise 3.1: List Lab (graded)
# https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/
#
#############################################################

# Series 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
# Ask the user for another fruit and add it to the end of the list.
# Display the list.
# Ask the user for a number and display the number back to the user and the fruit
# corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
# Add another fruit to the beginning of the list using “+” and display the list.
# Add another fruit to the beginning of the list using insert() and display the list.
# Display all the fruits that begin with “P”, using a for loop
#
fruit = list(('Apples', 'Pears', 'Oranges' ,'Peaches'))

def add_a_fruit(response, seq):
    seq.append(response)
    return seq

def get_a_fruit(i, seq):
    if int(i) <= 0: i = '1'
    str_return = i + ' ' + seq[int(i)-1]
    return str_return

def add_a_fruit_to_top(item, seq):
    seq = [item] + seq
    return seq

def add_a_fruit_by_index(i, item, seq):
    if int(i) < 0: i = '0'
    else: i = int(i) - 1
    seq.insert(int(i),item )
    return seq

def disply_a_fruit (seq):
    return_str=''
    for i, j in enumerate(seq):
        if 'P' in j[0]:
            return_str += (j + ' at index: ' + i.__str__() +'\n')
    return  return_str

# Ask the user for another fruit and add it to the end of the list.
# Display the list.
response = input("add a fruit > ")
print ('your entered ' + response)
print (add_a_fruit(response, fruit))

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
response = input("get a fruit (by index)> ")
print ('your entered ' + response)
print (get_a_fruit(response, fruit))

# Add another fruit to the beginning of the list using “+” and display the list.
add_fruit = input("Add a fruit to the top of the list> ")
print ('your entered ' + add_fruit )
print (add_a_fruit_to_top(add_fruit, fruit))

# Add another fruit to the beginning of the list using insert() and display the list.
add_fruit = input("Add a fruit > ")
add_index = input("Where in the list? > ")
print ('your entered ' + add_fruit + ' to ' + add_index)
print (add_a_fruit_by_index(add_index, add_fruit, fruit))

# Display all the fruits that begin with “P”, using a for loop.
print (disply_a_fruit(fruit))
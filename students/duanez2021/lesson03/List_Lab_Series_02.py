#!/usr/bin/env python3
import sys

##############################################################
# 20200616    djm list lab series 2
# 20200701    djm   resub, updated file  for list lab series 02
#
# Duane McCollum Python self-paced winter 2020
#
# Exercise 3.2: List Lab (graded)
# https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/
# Series 2
#
# Using the list created in series 1 above:
#
#     Display the list.
#     Remove the last fruit from the list.
#     Display the list.
#     Ask the user for a fruit to delete, find it and delete it.
#     (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
#
#############################################################

# Series 2
fruit = list(('Apples', 'Pears', 'Oranges', 'Peaches'))


def find_a_fruit(x, seq):
    b = False
    x = x.lower()
    for i, j in enumerate(seq):
        if x in j.lower():
            b = True
    return b


# find a fruit by name, return the index


def find_a_fruit_index(x, seq):
    idx = False
    x = x.lower()
    for i, j in enumerate(seq):
        if x in j.lower():
            idx = i
    return idx


def remove_last_list_item(seq):
    x = seq[::-1]
    x = x[1:]
    x = x[::-1]
    return x


### user interaction ####
#     Display the list.
#     Remove the last fruit from the list.
#     Display the list.
#     Ask the user for a fruit to delete, find it and delete it.

def fruit_loops_delete(seq):
    x = seq[:]
    print(x)
    pop_item = input("Do you want to remove the last item from the list? (y/n) > ")
    if pop_item.lower() == 'y':
        x = remove_last_list_item(x)
    status = ''
    while status != 'n':
        print(x)
        remove_item = input("Remove a fruit (by name) > ")
        print('your entered ' + remove_item + ' to be removed.')
        if not find_a_fruit(remove_item, x):
            print(remove_item + ' was not found.')
        while find_a_fruit(remove_item, x):
            # print(remove_item + ' will be removed.')
            i = find_a_fruit_index(remove_item, x)
            sremove = x[i]
            x.remove(sremove)
            # print(seq)
        print(x)
        status = input("Continue? (y/n) > ")
        if status == 'n':
            exit()
        if not len(x):
            print("List is empty!")
            exit()


fruit = list(('Apples', 'Pears', 'Oranges', 'Peaches')) * 2

fruit_loops_delete(fruit)

find_a_fruit('Apples', fruit[1:4])

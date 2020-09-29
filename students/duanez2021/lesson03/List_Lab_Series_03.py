#!/usr/bin/env python3
import sys
##############################################################
# 20200617    djm list lab series 3
#
# Duane McCollum Python self-paced winter 2020
#
# Exercise 3.2: List Lab (graded)
# https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/
# Series 3
#
# Using the list created in series 1 above:
#     Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
#     For each “no”, delete that fruit from the list.
#     For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
#     Display the list.#
#
#############################################################

# List lab # 3
fruit = list(('Apples', 'Pears', 'Oranges' ,'Peaches'))
s = "I can't tell the difference between Whizzo butter and this dead crab."

# find a fruit by a name, return T/F
def find_a_fruit (x, seq):
    b = False
    x = x.lower()
    for i, j in enumerate(seq):
        if x in j.lower():
            b = True
    return  b

#find_a_fruit('dead crab', fruit)

# find a fruit by name, return the index
def find_a_fruit_index (x, seq):
    idx = False
    x = x.lower()
    for i, j in enumerate(seq):
        if x in j.lower():
            idx = i
    return idx

def input_validation (x, seq):
    b = False
    x = x.lower()
    for i, j in enumerate(seq):
        if x in j.lower():
            b = True
    return b
# input_validation('fasfdadfs', 'yn')

### user interaction ####
#     Display the list.
#     Remove the last fruit from the list.
#     Display the list.
#     Ask the user for a fruit to delete, find it and delete it.

def fruit_loops_preference(seq):
    print(seq)
    status = ''
    while status != 'n':
        for i, x in enumerate(seq):
            response = input('Do you like ' + x.lower() + '? (y/n) > ')
            if response.lower() == 'n':
                i = find_a_fruit_index(x.lower(), seq)
                sRemove = seq[i]
                seq.remove(sRemove)
                print(seq)
                status = input("Continue? (y/n) > ")
                while not (input_validation(status, 'yn')):
                    print('enter either Y or N')
                    status = input("Continue? (y/n) > ")
                if status == 'n': exit()
            else:
                status = input("Continue? (y/n) > ")
                print(seq)
        if status == 'n': exit()
        if not len(seq):
            print ("List is empty!")
            exit()

fruit = list(('Apples', 'Pears', 'Oranges' ,'Peaches'))*2


fruit_loops_preference(fruit)
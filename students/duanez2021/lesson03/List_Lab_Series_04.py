#!/usr/bin/env python3
import sys
##############################################################
# 20200617    djm list lab series 4
# 20200701    djm  resub, updated file  for list lab series 04
#
#
# Exercise 3.2: List Lab (graded)
# https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/
# Series 4
#
# Using the list created in series 1 above:
# Once more, using the list from series 1:
#
#     Make a new list with the contents of the original, but with all the letters in each item reversed.
#     Delete the last item of the original list. Display the original list and the copy.
# #
#############################################################

# List lab # 4
fruit = list(('Apples', 'Pears', 'Oranges' ,'Peaches'))
s = "I can't tell the difference between Whizzo butter and this dead crab."


def remove_last_list_item(seq):
    x = seq[::-1]
    x = x[1:]
    x = x[::-1]
    seq = x
    return seq


def reverse_list_items(seq):
    reverse_seq = []
    for i, j in enumerate(seq):
        reverse_seq.append(seq[i][::-1])
    return reverse_seq


def alter_lists(seq):
    print(seq)
    seq = remove_last_list_item(seq)
    seq = reverse_list_items(seq)
    return seq


print(fruit)


print(alter_lists(fruit))

#
# comment
#


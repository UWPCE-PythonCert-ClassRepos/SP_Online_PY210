#!/usr/bin/env python3
import sys

##############################################################
# 20200617      djm slice lab series
# 20200623      djm slice lab series redo lab 01
# 20200701    djm list lab revised per comments email Mon 6/29/2020 5:22 PM
#               No space after print; whitespace around assignment operators;
#
#
# slice lab
# Write some functions that take a sequence as an argument, and return a copy of that sequence:
#
#     with the first and last items exchanged.
#     with every other item removed.
#     with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
#     with the elements reversed (just with slicing).
#     with the last third, then first third, then the middle third in the new order.
#############################################################

# List lab # 3 redo w/o function using explicit indexes
fruit = list(('Apples', 'Pears', 'Oranges', 'Peaches'))
s = "I can't tell the difference between Whizzo butter and this dead crab."


#     with the first and last items exchanged.


def swap_first_and_last(seq):
    seq[0], seq[-1] = seq[-1], seq[0]
    return seq


# it's a list

print(fruit)

print(swap_first_and_last(fruit))


#     with every other item removed.
def every_other_item_removed(seq):
    return seq[::2]


# it's not a string
print(fruit)
print(every_other_item_removed(fruit))
print(fruit)

#     with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# use a bigger list
fruit2 = list(('Açaí', 'Ackee', 'Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant',
               'Black sapote', 'Blueberry', 'Boysenberry', 'Breadfruit', "Buddha's hand", 'Cactus pear',
               'Crab apple', 'Currant', 'Cherry', 'Cherimoya', 'Chico fruit', 'Cloudberry', 'Coconut', 'Cranberry',
               'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Goji berry', 'Gooseberry',
               'Grape', 'Raisin', 'Grapefruit', 'Guava'))


def remove_first_and_last_four(seq):
    return seq[4:-4]


print(remove_first_and_last_four(fruit2))


#     with the elements reversed (just with slicing).

def reverse_elements(seq):
    if type(seq) is not list:
        seq = seq[::-1]
    else:
        seq[:] = seq[::-1]
    return seq


print(s)
print(reverse_elements(s))
print(fruit)
print(reverse_elements(fruit))


# with the last third, then first third, then the middle third in the new order.

def elements_by_thirds(seq):
    if len(seq) <= 2:
        return seq[-1:] + seq[:1]
    else:
        thirds = round(len(seq) / 3)
        middleThird = thirds * 2
        if len(seq) % 3 > 0:
            middleThird = middleThird + 1
        return seq[-thirds:] + seq[:thirds] + seq[thirds:middleThird]


print(s)
print(elements_by_thirds(s))

print(fruit2)
print(elements_by_thirds(fruit2))

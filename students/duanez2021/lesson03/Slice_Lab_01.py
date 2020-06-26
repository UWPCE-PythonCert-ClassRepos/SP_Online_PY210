#!/usr/bin/env python3
import sys
##############################################################
# 20200617      djm list lab series 4
# 20200623      djm list lab series redo
# Duane McCollum Python self-paced winter 2020
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

# List lab # 3
fruit = list(('Apples', 'Pears', 'Oranges' ,'Peaches'))
s = "I can't tell the difference between Whizzo butter and this dead crab."
def swap_first_and_last(seq):
    if type(seq) is not list:
        #it's a string....
        x = list(seq)
        last_item = seq[len(seq) - 1]
        first_item = seq[0]
        x[0] = last_item
        x[len(x)-1] = first_item
        x = ''.join(x)
    else:
        #it's a not string....
        x = seq[:]
        last_item = seq[len(seq) - 1]
        first_item = seq[0]
        x[0] = last_item
        x[len(x) - 1] = first_item
    return (x)
# it's a string
print(s)
print(swap_first_and_last(s))
print(s)

# it's not a string
print(fruit)
print(swap_first_and_last(fruit))
print(fruit)

def swap_first_and_last2(seq):
    x = seq[:]
    return x[-1:] + x[1:-1] + x[0:1:1]

# it's a string
print(s)
print(swap_first_and_last2(s))
print(s)

# it's not a string
print(fruit)
print(swap_first_and_last2(fruit))
print(fruit)

def every_other_item_removed(seq):
    x=seq[:]
    x=x[::2]
    return (x)

# it's a string
print(s)
print(every_other_item_removed(s))
print(s)

# it's not a string
print(fruit)
print(every_other_item_removed(fruit))
print(fruit)


fruit2=list(('Açaí', 'Ackee', 'Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant',
             'Black sapote', 'Blueberry', 'Boysenberry', 'Breadfruit', "Buddha's hand", 'Cactus pear',
             'Crab apple', 'Currant', 'Cherry', 'Cherimoya', 'Chico fruit', 'Cloudberry', 'Coconut', 'Cranberry',
             'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Goji berry', 'Gooseberry',
             'Grape', 'Raisin', 'Grapefruit', 'Guava'))

def remove_first_and_last_four(seq):
    x = seq[:]
    return(x[4:len(x)-4])

print(remove_first_and_last_four(fruit2))
print(remove_first_and_last_four(s))


def reverse_elements(seq):
    x = seq[:]
    return(x[::-1])

print(s)
print(reverse_elements(s))
print(fruit)
print(reverse_elements(fruit))

# with the last third, then first third, then the middle third in the new order.
def thirds_a_list(seq):
    x=seq[:]
    list_length= len(x)
    if list_length % 3 == 0:
        thirds_size = list_length / 3
    else:
        thirds_size = round((list_length / 3)) + 1
    x=x[:][len(x):]
    return (thirds_size)

def elements_by_thirds(seq):
    x = seq[:]
    if len(x)<=2:
        return (x[-1:] + x[:1])
    else:
        thirds = round(len(x) / 3)
        middleThird = thirds * 2
        if len(x) % 3 > 0:
            middleThird= middleThird + 1
        return (x[-thirds:] + x[:thirds] + x[thirds:middleThird])

print(s)
print (elements_by_thirds(s))

print(fruit2)
print (elements_by_thirds(fruit2))



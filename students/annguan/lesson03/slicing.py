#Lesson 3 Slicing Lab Exercise
#some functions that take a sequence as an argument, and return a copy of that sequence

###Functions###

def exchange_first_last(seq):
    """take seq as an argument and return a copy of seq with the first and last items exchanged"""
    first = seq[0:1]
    middle = seq[1:-1]
    last = seq[-1:]
    seq_copy = last + middle + first
    return seq_copy

def remove_every_other_item(seq):
    """take seq as an argument and return a copy of every other item removed"""
    seq_copy = seq [0:len(seq):2]
    return seq_copy

def remove_4s_every_other_in_between(seq):
    """take seq as an argument and return a copy of with the first 4 and the last 4 items removed, and every other item in between"""
    seq_copy = seq [4:-4:2]
    return seq_copy

def reverse_elements(seq):
    """take seq as an argument and return a copy of with the elements reversed"""
    seq_copy = seq [::-1]
    return seq_copy

def replace_thirds(seq):
    """take seq as an argument and return a copy of with the middle third, then last third, then the first third in the new order"""
    third = int(len(seq)/3)
    middle_third = seq[third:-third]
    last_third = seq[-third:]
    first_third = seq[0:third]
    seq_copy = middle_third + last_third + first_third
    return seq_copy

###Tests###

# Test exchange_first_last(seq)
s = "this is a string"
t = (1,2,3,5,6,7)
assert exchange_first_last(s) == "ghis is a strint"
assert exchange_first_last(t) == (7,2,3,5,6,1)

# Test remove_every_other_item(seq)
s = "this is a string"
t = (1,4,6,7,8,9)
assert remove_every_other_item(s) == "ti sasrn"
assert remove_every_other_item(t) == "1,6,8"

#Test remove_4s_every_other_in_between(seq)
s = "this is a string"
t = (3,4,5,6,8,1,2,4,7) 
assert remove_4s_every_other_in_between(s) == " sas"
assert remove_4s_every_other_in_between(t) == (8,)

#Test reverse_elements(seq)
s = "this is a string"
t = (3,4,5,6,8,1,2,4,7) 
assert remove_4s_every_other_in_between(s) == "gnirts a si siht"
assert remove_4s_every_other_in_between(t) == (7, 4, 2, 1, 8, 6, 5, 4, 3)

#Test replace_thirds(seq)
t = (1,2,3,45,67,89,4,5,6)
assert replace_thirds(t) == (45, 67, 89, 4, 5, 6, 1, 2, 3)
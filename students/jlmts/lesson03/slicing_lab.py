"""
exercise 3.1: slicing lab
joli umetsu
py210

"""

"""
input: sequence
output: copy of sequence with:
     (1) first and last item exchanged 'exchange_first_last()'
     (2) every other item removed 'remove_every_other()'
     (3) first 4 and last 4 items removed, then every other remaining item 'four_removed_every_other()'
     (4) elements reversed (with slicing) 'reverse()'
     (5) last third, then first third, then middle third in the new order 'third_order()'
"""

# (1) first and last item exchanged
def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

# (2) every other item removed
def remove_every_other(seq):
    return seq[0::2]
    
# (3) first/last 4 items removed, remaining evey other item 
def four_removed_every_other(seq):
    return seq[4:len(seq)-4:2]

# (4) elements reversed
def reverse(seq):
    return seq[::-1]
    
# (5) last third, first third, middle third order
def third_order(seq):
    length = len(seq)
    third = length//3
    return seq[2*third:] + seq[:third] + seq[third:2*third]
    
"""
test section: check to see each function is working properly
"""
a_string = "this is a string"
a_tuple = (2,54,13,12,5,32)

# (1) ensure first and last items are swapped
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# (2) ensure every other item is removed, starting from index 1
assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

# (3) ensure first and last 4 items are removed, and every other item from the remaining string is there
assert four_removed_every_other(a_string) == " sas"
assert four_removed_every_other(a_tuple) == ()

# (4) ensure the elements are in reverse
assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32,5,12,13,54,2)

# (5) check that elements appear in blocks of thirds: last, first, middle
assert third_order(a_string) == "stringthis is a "
assert third_order(a_tuple) == (5,32,2,54,13,12)
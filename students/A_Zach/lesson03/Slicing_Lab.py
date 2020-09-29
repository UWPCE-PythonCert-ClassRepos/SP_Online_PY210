#Write a function that switches the first and last entry of a sequence.
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

#Write a function that removes every other entry in a sequence.
def every_other_removed(seq):
    return seq[0:len(seq)-1:2] 

#Write a function that removes the first 4 and last 4 digits in a sequence and then removes every other remaining entry.
def remove_first_last_4_every_other_removed(seq):
    return seq[4:len(seq)-5:2]

#Write a function that reverses the entries of a sequence    
def reversed(seq):
    return seq[::-1]

#Write a function that returns rearranges a sequence to the last third, first third, and middle third of the orginial sequence.    
def switch_thrids(seq):
    x = len(seq)//3
    return seq[-x:] + seq[:x] + seq[x:2*x]
    
#test sets. strings, lists are random. fishing wire? why?!
a_string = "fishing wire"
a_list = [1, 3, 2, 8, 3, 6]

#new learning: The assert command returns nothing if true, and returns an error if flase. Excellent for testing.
assert exchange_first_last(a_string) == "eishing wirf"
assert exchange_first_last(a_list) == [6, 3, 2, 8, 3, 1]
assert every_other_removed(a_string) == "fsigwr"
assert every_other_removed(a_list) == [1, 2, 3]
assert remove_first_last_4_every_other_removed(a_string) == "ig"
assert remove_first_last_4_every_other_removed(a_list) == []
assert reversed(a_string) == "eriw gnihsif"
assert reversed(a_list) == [6, 3, 8, 2, 3, 1]
assert switch_thrids(a_string) == "wirefishing "
assert switch_thrids(a_list) == [3, 6, 1, 3, 2, 8]

#Print a positive affirmation of successful functions
print("Tests Passed")
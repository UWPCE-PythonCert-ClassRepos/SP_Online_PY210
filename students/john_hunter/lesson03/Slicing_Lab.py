# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:49:33 2020

@author: johnh
"""
#slicing lab

def seq_first_last_ex(sequence):
    return sequence[-1:] + sequence[1:-1] + sequence[:1]
def seq_remove_odd_letters(sequence):
    #Slicing Only
    return sequence[::2]
def seq_firstfour_lastfour(sequence):
    sequence=sequence[4:-4]
    return seq_remove_odd_letters(sequence)
def seq_elements_reversed(sequence):
    #Slicing only
    return sequence[::-1]
def seq_last_first_middle(sequence):
    sequence1=list()
    third=int(round(len(sequence)/3))
    for item in sequence[-third:]:
        sequence1.append(item)
    for item1 in sequence[:-third]:
        sequence1.append(item1)
    return sequence1
#Tests
test1=['ad', 22, 1, 'e', 7, 'seq', 'other', 'crab', 2, 3, 'can']
test2="calivinists love the leviathan and that is funny to me"
test3="careful cathy causes a conundrum"
test4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

total=[test1,test2,test3,test4]

for item in total:
    print(seq_first_last_ex(item))
    print(seq_remove_odd_letters(item))
    print(seq_firstfour_lastfour(item))
    print(seq_elements_reversed(item))
    print(seq_last_first_middle(item))



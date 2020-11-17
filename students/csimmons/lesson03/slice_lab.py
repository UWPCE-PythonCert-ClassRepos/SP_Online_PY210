#!/usr/bin/env python3
# Craig Simmons
# Python 210
# slicing_lab.py: Slice Lab Exercises
# Created 11/16/2020 - csimmons

def exchange_first_last(seq):
    if type(seq) == str:
        first = seq[0]
        last = seq[-1]
        mid = seq[1:-1]
        newstr= last + mid + first
        return(newstr)
    else:
        seq[0],seq[-1] = seq[-1],seq[0]
        return(seq)
        
def remove_every_other(seq):
    return seq[0::2]

'''
def remove_four_begin_end(seq):
    middle = seq[4:-4:2]
    return middle

def reverse(seq):
    return seq[::-1]

def rearrage_thirds(seq):
    third = len(seq)/3
    front = seq[:int(third)]
    middle = seq[int(third):(int(third)*2)]
    end = seq[(int(third)*2):]
    return (end + front + middle)
'''
#write tests

a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
a_string = 'April is the cruellest month, breeding Lilacs out of the dead land'
b_string = 'GaiusJuliusCeasar'



if __name__ == "__main__":
    assert remove_every_other(a_string) == 'Arli h rels ot,bedn iasoto h edln'
    assert remove_every_other(b_string) == 'Gisuisesr'
    assert remove_every_other(a_list) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert remove_every_other(b_list) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    print('remove_every_other() tests all passed')

    assert exchange_first_last(a_list) == [20,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1]
    assert exchange_first_last(b_list) == [24,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,1]
    assert exchange_first_last(a_string) == 'dpril is the cruellest month, breeding Lilacs out of the dead lanA'
    assert exchange_first_last(b_string) == 'raiusJuliusCeasaG'
    print('exchange_first_last has Passed')


#!/usr/bin/env python3
# Craig Simmons
# Python 210
# slicing_lab.py: Slice Lab Exercises
# Created 11/16/2020 - csimmons

def exchange_first_last(seq):
    seq[0],seq[-1] = seq[-1],seq[0]
    return(seq)

def remove_every_other(seq):
    del seq[1::2]
    return seq

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

#write tests

a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
a_string = 'April is the cruellest month, breeding Lilacs out of the dead land'
b_string = 'GaiusJuliusCeasar'

print(rearrage_thirds(a_list))
print(rearrage_thirds(a_string))
print(rearrage_thirds(b_string))
print(rearrage_thirds(b_list))

if __name__ == "__main__":
    # run some tests
    assert rearrage_thirds(a_list) == 0
    assert rearrage_thirds(b_list) == 0
    assert rearrage_thirds(a_string) == 0
    assert rearrage_thirds(b_string) == 0

    print("All tests passed")
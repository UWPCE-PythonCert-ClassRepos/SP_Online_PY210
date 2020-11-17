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

def remove_four_begin_end(seq):
   return seq[4:-4:2]

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



if __name__ == "__main__":
    assert rearrage_thirds(a_string) == 's out of the dead landApril is the cruellest month, breeding Lilac'
    assert rearrage_thirds(b_string) == 'sCeasarGaiusJuliu'
    assert rearrage_thirds(a_list) == [13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert rearrage_thirds(b_list) == [17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    assert reverse(a_string) == 'dnal daed eht fo tuo scaliL gnideerb ,htnom tselleurc eht si lirpA'
    assert reverse(b_string) == 'rasaeCsuiluJsuiaG'
    assert reverse(a_list) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse(b_list) == [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    assert remove_every_other(a_string) == 'Arli h rels ot,bedn iasoto h edln'
    assert remove_every_other(b_string) == 'Gisuisesr'
    assert remove_every_other(a_list) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert remove_every_other(b_list) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

    assert exchange_first_last(a_list) == [20,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1]
    assert exchange_first_last(b_list) == [24,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,1]
    assert exchange_first_last(a_string) == 'dpril is the cruellest month, breeding Lilacs out of the dead lanA'
    assert exchange_first_last(b_string) == 'raiusJuliusCeasaG'

    assert remove_four_begin_end(a_string) == 'li h rels ot,bedn iasoto h ed'
    assert remove_four_begin_end(b_string) == 'suise'
    assert remove_four_begin_end(a_list) == [5, 7, 9, 11, 13, 15]
    assert remove_four_begin_end(b_list) == [5, 7, 9, 11, 13, 15, 17, 19]
    print('All tests passed...')

   


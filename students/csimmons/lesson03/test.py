#!usr/bin/env/python3
a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
a_string = 'April is the cruellest month, breeding Lilacs out of the dead land'
b_string = 'GaiusJuliusCeasar'


def remove_every_other(seq):
    if type(seq) == str:
        print('This is a string')
    else:
        del seq[1::2]
        return seq

print('list1')
print(remove_every_other(a_list))
print('list2')
print(remove_every_other(b_list))
print ('string1')
print(remove_every_other(a_string))
print ('string2')
print(remove_every_other(b_string))

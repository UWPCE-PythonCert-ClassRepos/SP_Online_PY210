#!usr/bin/env/python3
a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
c_list = ['ant', 'bear', 'cat', 'dog', 'eagle', 'fox','gnat', 'hawk', 'iguana', 'jackal', 'kangaroo']
a_string = 'April is the cruellest month, breeding Lilacs out of the dead land'
b_string = 'GaiusJuliusCeasar'


def remove_every_other(seq):
    return seq[0::2]

def remove_four_begin_end(seq):
   return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]


print('list3')
print(remove_every_other(c_list))
print ('list3')
print(remove_four_begin_end(c_list))
print ('list3')
print(reverse(c_list))



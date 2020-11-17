#!usr/bin/env/python3
a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
c_list = ['ant', 'bear', 'cat', 'dog', 'eagle', 'fox','gnat', 'hawk', 'iguana', 'jackal', 'kangaroo']
a_string = 'April is the cruellest month, breeding Lilacs out of the dead land'
b_string = 'GaiusJuliusCeasar'

def rearrage_thirds(seq):
    third = len(seq)/3
    front = seq[:int(third)]
    middle = seq[int(third):(int(third)*2)]
    end = seq[(int(third)*2):]
    return (end + front + middle)

print('list3')
print(rearrage_thirds(c_list))
print('list2')
print(rearrage_thirds(b_list))
print ('string1')
print(rearrage_thirds(a_string))
print ('string2')
print(rearrage_thirds(b_string))



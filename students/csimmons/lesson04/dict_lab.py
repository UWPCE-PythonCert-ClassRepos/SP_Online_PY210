#!/usr/bin/env python3
# Craig Simmons
# Python 210
# dict_lab.py 
# Created 12/4/2020 - csimmons
'''
# Part 1
main_dict = {
            'name' : 'Chris',
            'city' : 'Seattle',
            'cake' : 'Chocolate',
            }

print(main_dict)

del main_dict['cake']
print(main_dict)

main_dict['fruit'] = 'Mango'
print(main_dict)
print(main_dict.keys()) 
print(main_dict.values())
print('cake' in main_dict)
print('Mango' in main_dict.values())

# Part 2
main_dict2 = {
            'name' : 'Chris',
            'city' : 'Seattle',
            'cake' : 'Chocolate',
            }
def count_letters(main_dict2):
    for v in main_dict2:
        main_dict2[v] = main_dict2[v].lower().count('t')
    print(main_dict2)

count_letters(main_dict2)

donorlist[i][1].append(f_gift)

# Part3
# Sets 1
def set_modulus():
    s1 = set()
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(1,21):
        s1.update([i])
        mod2 = (i % 2)
        mod3 = (i % 3)
        mod4 = (i % 4)
        if mod2 == 0:
            s2.add(i)
        if mod3 == 0:
            s3.add(i)
        if mod4 == 0:
            s4.add(i)
    print('\nNumbers from 1-20: ', s1)
    print('\nNumbers from 1-20 divisible by 2: ', s2)
    print('\nNumbers from 1-20 divisible by 3: ', s3)
    print('\nNumbers from 1-20 divisible by 4: ', s4)
    print('\nIs s3 a subset of s2? ', s3.issubset(s2))
    print('\nIs s4 a subset of s2? ', s4.issubset(s2))

# read python.org doc 4.6.6. Ranges()
#learned about 3rd arg 'step' redo above as- 

set_modulus()

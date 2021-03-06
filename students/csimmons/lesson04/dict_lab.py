#!/usr/bin/env python3
# Craig Simmons
# Python 210
# dict_lab.py 
# Created 12/4/2020 - csimmons

# Dictionary 1
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
print('Is "cake" in main_dict? ','cake' in main_dict)
print('Is "Mango" in main_dict? ','Mango' in main_dict.values())

# Dictionary 2
main_dict2 = {
            'name' : 'Chris',
            'city' : 'Seattle',
            'cake' : 'Chocolate'
            }
def count_letters(main_dict2):
    for v in main_dict2:
        main_dict2[v] = main_dict2[v].lower().count('t')
    print('\n', main_dict2)

count_letters(main_dict2)
# Sets 1

def set_modulus():
    s1 = set()
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(1,21):
        s1.update([i])
        if (i % 2) == 0:
            s2.add(i)
        if (i % 3) == 0:
            s3.add(i)
        if (i % 4) == 0:
            s4.add(i)
    print('\ns1: ', s1)
    print('s2: ', s2)
    print('s3: ', s3)
    print('s4: ', s4)
    print('Is s3 a subset of s2? ', s3.issubset(s2))
    print('Is s4 a subset of s2? ', s4.issubset(s2))

set_modulus()

# Sets 2

s1 = set(['P','y','t','h','o','n'])
s2 = frozenset(('m','a','r','a','t','h','o','n',))

print('\nSet s1: ',s1)
print('Frozen Set s2: ',s2)
s1.add('i')
print('s1 with "i" added', s1)
print('Union between the 2 sets: ',s1.union(s2))
print('Intersection between the 2 sets: ',s1.intersection(s2))


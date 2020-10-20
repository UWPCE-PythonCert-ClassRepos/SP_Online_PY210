#!/usr/bin/env python3

'''Dict Lab Exercise'''

print('Dictionaries 1')
#create dictionary
dict1 = {'city': 'Seattle', 'cake': 'chocolate', 'name': 'Chris'}
print(dict1)
#Delete 'cake'
dict1.pop('cake')
print(dict1)
#Add entry fruit
dict1['fruit'] = 'Mango'
print(dict1)
#print keys
print('keys: {}'.format(dict1.keys()))
#print values
print('values: {}'.format(dict1.values()))
#is cake in dictionary?
print('Is cake a key in dict? {}'.format('cake' in dict1))
#is Mango in dictionary?
print('Is mango a value in dict? {}'.format('Mango' in dict1.values()))

print('\n\nDictionary 2')
dict2 = {}
for k, v in dict1.items():
    dict2[k] = v.lower().count('t')
print(dict2)

print('\n\nSets Exercise 1')
s2 = set()
s3 = set()
s4 = set()
for i in range(0, 21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2, s3, s4)

#is s3 subset of s2
print('Is s3 a subset of s2? {}'.format(s3.issubset(s2)))
#is s4 subset of s2
print('Is s4 a subset of s2? {}'.format(s4.issubset(s2)))

print('\n\nSets Exercise 2')

set1 = set(list('Python'))
print('set1 ',set1)
set1.add('i')
print('set1' , set1)

set2 = frozenset(list('marathon'))
print('set2 ', set2)

print('Union of set1 and set2: {}'.format(set1.union(set2)))
print('Intersection of set1 and set2: {}'.format(set1.intersection(set2)))

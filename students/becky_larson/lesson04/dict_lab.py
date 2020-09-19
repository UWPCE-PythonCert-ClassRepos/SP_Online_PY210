#!/usr/bin/env python3

#  Dictionaries 1
print('********************* dict1 ')
dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict)
dict.pop('cake')
print(dict)
dict.update({'fruit': 'Mango'})
print(dict)
print(dict.values())
print('cake' in dict.keys())
print('Mango' in dict.values())

#  Dictionaries 2
print('********************* dict2 ')

dict2 = dict.copy()

for k, v in dict2.items():
    dict2.update({k: v.lower().count('t')})
print(dict2)

#  Sets
print('********************* sets ')
numbers = range(21)

s2 = set()
s3 = set()
s4 = set()

for number in numbers:
    if (number % 2 == 0):
        s2.add(number)
    if (number % 3 == 0):
        s3.add(number)
    if (number % 4 == 0):
        s4.add(number)

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))


print('********************* sets 2 ')
a_set = set('python')
print(a_set)
a_set.add('i')
print(a_set)

f_set = frozenset('marathon')
print(f_set)

print(a_set.union(f_set))
print(a_set.intersection(f_set))

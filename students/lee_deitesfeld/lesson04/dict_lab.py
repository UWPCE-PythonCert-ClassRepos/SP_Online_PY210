#!/usr/bin/env python3

#DICTIONARIES 1
dictionary = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dictionary)

#deletes key 'cake' from dict
del dictionary['cake']
print(dictionary)

#adds 'fruit' to dict
dictionary['fruit'] = 'Mango'
print(dictionary)

#prints the keys in dict
for key,value in dictionary.items():
    print(key)

#prints the values in dict
for key,value in dictionary.items():
    print(value)

#tests if 'cake' in dictionary
if 'cake' in dictionary:
    print('True')
else:
    print('False')

#tests if 'Mango' in dictionary
if 'Mango' in dictionary.values():
    print('True')
else:
    print('False')

#DICTIONARIES 2
#Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
dictionary2 = {'name':10, 'citty':10, 'cake':10}
for x in dictionary2:
    t_count = x.count('t')
    dictionary2[x] = t_count
print(dictionary2)

#SETS1
s2 = {2,4,6,8,10,12,14,16,18,20}
s3 = {3,6,9,12,15,18}
s4 = {4,8,12,16,20}
print(s2)
print(s3)
print(s4)

#Display if s3 is a subset of s2
if s3.issubset(s2):
    print('True')
else:
    print('False')

#Display if 4 is a subset of s2
if s4.issubset(s2):
    print('True')
else:
    print('False')

#Create a set with the letters in ‘Python’ and add ‘i’ to the set
set_python = {'P', 'y', 't', 'h', 'o', 'n'}
set_python.update('i')
print(set_python)

#Create a frozenset with the letters in ‘marathon’
frozen = {'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'}
fSet = frozenset(frozen)
print(fSet)

#display the union and intersection of the two sets
print(set_python.union(fSet))

print(set_python.intersection(fSet))

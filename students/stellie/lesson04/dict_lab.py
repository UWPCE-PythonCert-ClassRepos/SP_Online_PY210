#!/usr/bin/env python3

# Dictionaries 1
# Creates dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle" who likes “Chocolate”
dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

# Prints the dictionary items
print('\nDictionary:', dict)

# Deletes entry for "cake" and displays the dictionary
dict.pop('cake')
print('\nEntry for cake deleted:', dict)

# Adds an entry for "fruit" with "Mango" and displays the dictionary
dict['fruit'] = 'Mango'
print('\nEntry for fruit added:', dict)

print('\nDictionary keys:', dict.keys())  # displays the dictionary keys
print('\nDictionary values:', dict.values())  # displays the dictionary values
print('\nDoes cake appear in the dictionary: {}'.format('cake' in dict.keys()))  # displays whether or not "cake" is a key in the dictionary (False)
print('\nDoes Mango appear in the dictionary: {}'.format('Mango' in dict.values()))  # displays whether or not "Mango" is a value in the dictionary (True)

# Dictionaries 2
# Displays dictionary from item 1 with number of 't's as values
dict_2 = {'name': 'Chris'.lower().count('t'), 'city': 'Seattle'.lower().count('t'), 'cake': 'Chocolate'.lower().count('t')}
print('\nDictionary with counts of ts:', dict_2)

# Sets
s2 = set()
s3 = set()
s4 = set()
for i in range(0, 20):
    if i % 2 == 0:
        s2.update([i])  # creates set containing numbers from zero through twenty divisible by 2
for i in range(0, 20):
    if i % 3 == 0:
        s3.update([i])  # creates set containing numbers from zero through twenty divisible by 3
for i in range(0, 20):
    if i % 4 == 0:
        s4.update([i])  # creates set containing numbers from zero through twenty divisible by 4

print('\nSets:', s2, s3, s4)  # displays all sets
print('\nIs s3 a subset of s2: {}'.format(s3.issubset(s2)))  # displays if s3 is subset of s2 (False)
print('\nIs s4 a subset of s2: {}'.format(s4.issubset(s2)))  # displays if s4 is subset of s2 (True)

# Sets 2
s = set(['P', 'y', 't', 'h', 'o', 'n'])  # creates set with letters in 'Python'
s.add('i')  # adds 'i' to the set
fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))  # creates frozenset with letters in 'marathon'
print('\nUnion of set and frozenset', s.union(fs))  # displays union of two sets
print('\nIntersection of set and frozenset', s.intersection(fs))  # displays intersection of two sets
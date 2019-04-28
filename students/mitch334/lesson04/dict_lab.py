"""Lesson 04 | Dictionary and Set Lab"""
# Goal: Learn the basic ins and outs of Python dictionaries and sets.
#
# When the script is run, it should accomplish the following four series of actions:

#!/usr/bin/env python3

# Dictionaries 1
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
# Display the dictionary.
d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)

# Delete the entry for “cake”.
# Display the dictionary.
d.pop('cake')
print(d)

# Add an entry for “fruit” with “Mango” and display the dictionary.
d['fruit'] = 'Mango'
print(d)

# Display the dictionary keys.
# for key in d:
#     print(key)
print(d.keys())

# Display the dictionary values.
# for value in d.values():
#     print(value)
print(d.values())

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in d)

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
# print(d.get('Mango'))
print('Mango' in d.values())


# Dictionaries 2
# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
print('d: ',d)

d2 = {}
for k, v in d.items():
    d2[k] = v.lower().count('t')

print(d2)

# Sets
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
# Display the sets.
s2 = set(range(0, 21, 2))
print(s2)
s3 = set(range(0, 21, 3))
print(s3)
s4 = set(range(0, 21, 4))
print(s4)

# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).
print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s5 = set('Python')
print(s5)

s5.update('i')
print(s5)

# Create a frozenset with the letters in ‘marathon’.
sf5 = frozenset('marathon')
print(sf5)

# display the union and intersection of the two sets.
print(s5.union(sf5))
print(s5.intersection(sf5))

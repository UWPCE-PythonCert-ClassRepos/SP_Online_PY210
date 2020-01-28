#!/usr/bin/env python3
# dict_lab.py
# Lisa Ferrier, Python 210, Lesson 04 exercise


# Dictionaries 1
# Create a dictionary named dict1
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)

# Remove key 'cake' and its value 'Chocolate' from dict1
dict1.pop('cake')
print(dict1)

# Add a key 'fruit' with a value 'Mango' to dict1
dict1.update({'fruit': 'Mango'})
print(dict1)

# Check if 'cake' is key in dict1
'cake' in dict1.keys()

# Check if 'Mango' is a value in dict1
'Mango' in dict1.values()

# Dictionaries 2
# Count frequency of occurrence of the letter 't' in each value pair.
# Create a new dictionary (dict2) with the key and replaces value with the count.
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
dict2 = {}

for k, v in dict1.items():
    v = v.lower().count('t')
    dict2[k] = v
print(dict2)

# Sets 1
# Create sets s2, s3, s4 that contain nums from 0 - 20
s = range(21)
s2 = set()
s3 = set()
s4 = set()

# If divisible by 2, 3, or 4 add number to respective set
for i in s:
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

# Check if s3 and s4 are a subset of s2
s3.issubset(s2)  # false
s4.issubset(s2)  # true

# Sets 2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s = set('Python')
s.add('i')

# Create a frozenset with the letters in ‘marathon’.
s2 = frozenset('Marathon')

# Display the union and intersection of the two sets.
print(s.union(s,s2))
print(s.intersection(s, s2))
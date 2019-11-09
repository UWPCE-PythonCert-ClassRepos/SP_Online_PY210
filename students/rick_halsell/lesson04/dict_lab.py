#!/usr/bin/env python3

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes
dict = {'name': 'Chris', 'city': 'Seattle', 'cake' : 'chocolate'}

# Display the dictionary.
print('\nDisplaying Dictionary:')
print(dict)

# Delete the entry for “cake”
dict.pop('cake')

# Display the dictionary.
print('\nDisplaying Dictionary After Removal:')
print(dict)

# Add an entry for “fruit” with “Mango” and display the dictionary
dict['fruit'] = 'Mango'

# Display the dictionary keys.
print('\nDisplaying Dictionary Keys:')
for key in dict.keys():
    print(key)

# Display the dictionary values.
print('\nDisplaying Dictionary Values:')
for value in dict.values():
    print(value)

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('\nChecking if cake is in dictionary:')
print('cake' in dict.keys())

# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('\nChecking if Mango is in dictionary:')
print('Mango' in dict.values())

# Part 2
print('\nCreating Second Dictionary:')
dict2 = {}

print('\nAdding Key To Dictionary and Values Based on Number of "t\'s" in Value:')
for key, value in dict.items():
    counter = value.count('t')
    dict2[key] = counter
print(dict2)

# Create Set2
s2 = set()
s3 = set()
s4 = set()
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4
s2 = set(filter(lambda x: (x % 2 == 0), range(0,21)))

s3 = set(filter(lambda x: (x % 3 == 0), range(0,21)))

s4 = set(filter(lambda x: (x % 4 == 0), range(0,21)))

# Printing Sest for verification
print('\nSet s2:')
print(s2)

print('\nSet s3:')
print(s3)
# checking is subset request
print('\nIs s3 a subset of s2?:')
print(s3.issubset(s2))

print('\nSet s4:')
print(s4)
# checking is subset request
print('\nIs s4 a subset of s2?:')
print(s4.issubset(s2))

# Set Part 2
print()
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
pythonset = set('Python')
# viewing set
#print(pythonset)
# updating set
pythonset.update('i')
# viewing updated set
#print(pythonset)

# Create a frozenset with the letters in ‘marathon’.
#newword = 'marathon'
frozennewword = frozenset('marathon')
#print(frozennewword)

# Display the union and intersection of the two sets.
# Union of the two sets
print("Pythoni Union marathon : ", pythonset.union(frozennewword))

print("Pythoni Intersection marathon : ", pythonset.intersection(frozennewword))

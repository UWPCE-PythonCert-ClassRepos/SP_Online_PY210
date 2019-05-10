#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


'''
DICTIONARIES 1
'''

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle”
# who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
chris_dict = {
    "Name": "Chris",
    "City": "Seattle",
    "Cake": "Chocolate"
}

# Display the Dict
print(chris_dict)

# Delete the entry for cake
chris_dict.pop("Cake")

# Display the Dict
print(chris_dict)

# Add an entry for “fruit” with “Mango” and display the dictionary.
chris_dict.update({"Fruit": "Mango"})

# Display the Dict
print(chris_dict)

# Display the dict keys
print(chris_dict.keys())

# Display the dict values
print(chris_dict.values())

# Display whether "Cake" is in the dict keys
print(chris_dict.get("Cake"))

# Display whether "Mango" is in the dict values
print("Mango" in chris_dict.values())


'''
DICTIONARIES 2

Using the dictionary from item 1: Make a dictionary using the same 
keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).

'''

chris_dict = {
    "Name": "Chris",
    "City": "Seattle",
    "Cake": "Chocolate"
}

for k, v in chris_dict.items():
    i = 0
    for l in v:
        if l in ("t", "T"):
            i += 1
    chris_dict[k] = i

print(chris_dict)

'''
SETS 1


Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).

'''
s2 = set()
s3 = set()
s4 = set()

for i in range(0, 20):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

assert s3.issubset(s2) == False
assert s4.issubset(s2) == True

'''
SETS 2

Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.

'''

python_i = set()
marathon_set = set()

for l in "python":
    python_i.add(l)
python_i.add("i")

for l in "marathon":
    marathon_set.add(l)

marathon = frozenset(marathon_set)

assert marathon.union(python_i) == {'y', 'o', 'a', 'm', 'n', 'h', 't', 'r', 'p', 'i'}
assert marathon.intersection(python_i) == {'n', 'o', 'h', 't'}

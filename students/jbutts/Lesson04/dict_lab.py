#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
DICTIONARIES 1
'''

# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle”
# who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
CHRIS_DICT = {
    "Name": "Chris",
    "City": "Seattle",
    "Cake": "Chocolate"
}


# Display the Dict
print(CHRIS_DICT)

# Delete the entry for cake
CHRIS_DICT.pop("Cake")

# Display the Dict
print(CHRIS_DICT)

# Add an entry for “fruit” with “Mango” and display the dictionary.
CHRIS_DICT.update({"Fruit": "Mango"})

# Display the Dict
print(CHRIS_DICT)

# Display the dict keys
print(CHRIS_DICT.keys())

# Display the dict values
print(CHRIS_DICT.values())

# Display whether "Cake" is in the dict keys
print(CHRIS_DICT.get("Cake"))

# Display whether "Mango" is in the dict values
print("Mango" in CHRIS_DICT.values())


'''
DICTIONARIES 2

Using the dictionary from item 1: Make a dictionary using the same 
keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
'''

CHRIS_DICT = {
    "Name": "Chris",
    "City": "Seattle",
    "Cake": "Chocolate"
}

for k, v in CHRIS_DICT.items():
    i = 0
    for l in v:
        if l in ("t", "T"):
            i += 1
    CHRIS_DICT[k] = i

print(CHRIS_DICT)

'''
SETS 1

Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
'''

S2 = set()
S3 = set()
S4 = set()

for i in range(0, 20):
    if i % 2 == 0:
        S2.add(i)
    if i % 3 == 0:
        S3.add(i)
    if i % 4 == 0:
        S4.add(i)

assert not S3.issubset(S2)
assert S4.issubset(S2)

'''
SETS 2

Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.

'''

PYTHON_I = set()
MARATHON_SET = set()

for l in "python":
    PYTHON_I.add(l)
PYTHON_I.add("i")

for l in "marathon":
    MARATHON_SET.add(l)

MARATHON = frozenset(MARATHON_SET)

assert MARATHON.union(PYTHON_I) == {'y', 'o', 'a', 'm', 'n', 'h', 't', 'r', 'p', 'i'}
assert MARATHON.intersection(PYTHON_I) == {'n', 'o', 'h', 't'}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 4, Lab

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html

Dictionaries 1
    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).

Dictionaries 2
    Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
    The result should look something like:
    {"name": 0
    "city": 2
    "cake": 2
    }

Sets 1
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
Sets 2
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’.
    Display the union and intersection of the two sets.

"""


# Dictionaries 1
print("* Dictionaries 1 *")
first_dict = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(first_dict)
first_dict.pop("cake")
print(first_dict)
first_dict['fruit'] = "Mango"
print(first_dict)
print(first_dict.keys())
print(first_dict.values())
print("cake" in first_dict.keys())
print("Mango" in first_dict.values())

# Dictionaries 2
print("\n* Dictionaries 2 *")
second_dict = first_dict.copy()
for key in second_dict.keys():
    second_dict[key] = second_dict[key].lower().count('t')
print(second_dict)

# Set 1
print("\n* Set 1 *")
s2 = set(range(0,21,2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Set 2
print("\n* Set 2 *")
s5 = set("Python")
s5.update("i")
s6 = frozenset("marathon")
print(s5)
print(s6)

print(s6.union(s5))
print(s6.intersection(s5))
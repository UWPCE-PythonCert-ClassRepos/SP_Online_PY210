#!/usr/bin/env python3

# Dictionary and Set Lab
# Dev: Roslyn Melookaran
# Date: 9/17/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/9/20, created script
# ---------------------------------------------------------------------------------#


def set_s2(set2):
    """ Compute numbers from 0-20 that are divisible by 2. Add these to set.
                :param: set2 (set)
                :return: set2 (set)
                """
    for i in range(21):
        if i % 2 == 0:
            set2.update([i])
    return set2


def set_s3(set3):
    """ Compute numbers from 0-20 that are divisible by 3. Add these to set.
                :param: set3 (set)
                :return: set3 (set)
                """
    for i in range(21):
        if i % 3 == 0:
            set3.update([i])
    return set3


def set_s4(set4):
    """ Compute numbers from 0-20 that are divisible by 3. Add these to set.
                :param: set4 (set)
                :return: set4 (set)
                """
    for i in range(21):
        if i % 4 == 0:
            set4.update([i])
    return set4

# ----------DICTIONARIES 1 ------------#
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
dict_info = {"Name": "Chris", "City": "Seattle", "Cake": "Chocolate"}
# Display the dictionary.
print(dict_info)
# Delete the entry for “cake”.
# dict_info.popitem() #<--- This one removes an arbitrary value
dict_info.pop("Cake")  # <-- This one you can specify
# Display the dictionary.
print(dict_info)
# Add an entry for “fruit” with “Mango” and display the dictionary.
dict_info.update({"Fruit": "Mango"})
# Display the dictionary keys.
print(dict_info.keys())
# Display the dictionary values.
print(dict_info.values())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("Cake" in dict_info)
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in dict_info.values())

# ----------DICTIONARIES 2 ------------#
for item in dict_info:
    value = dict_info.get(item)
    count = 0
    count = value.lower().count("t")
    dict_info.__setitem__(item, count)
print(dict_info)

# ----------Set 1 ------------#
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).

s2 = set()
s3 = set()
s4 = set()

s2 = set_s2(s2)
print(s2)

s3 = set_s3(s3)
print(s3)

s4 = set_s4(s4)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# ----------Set 2 ------------#

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
set_python = set(["p", "y", "t", "h", "o", "n"])
set_python.add("i")
print(set_python)
# Create a frozenset with the letters in ‘marathon’.
set_marathon = frozenset(["m", "a", "r", "a", "t", "h", "o", "n"])
print(set_marathon)
# Display the union and intersection of the two sets.
set_intersect = set_python.intersection(set_marathon)
print(set_intersect)
set_union = set_python.union(set_marathon)
print(set_union)


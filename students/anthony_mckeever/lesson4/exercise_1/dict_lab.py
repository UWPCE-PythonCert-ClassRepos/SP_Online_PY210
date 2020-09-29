#!/usr/bin/env python3

"""
Programming In Python - Lesson 4 Exercise 1: Dictionary (and Set) Lab
Code Poet: Anthony McKeever
Start Date: 08/05/2019
End Date: 08/05/2019
"""

# Task 1 - Dictionaries 1
print("Task 1 - Dictionaries:")
fun_dictionary = {"name": "Sophia",
                    "city": "Seattle",
                    "cake": "Marble"
                   }

print(fun_dictionary)
fun_dictionary.pop("cake")
print(fun_dictionary)
fun_dictionary.update({"fruit": "Mango"})

print(fun_dictionary.keys())
print(fun_dictionary.values())

has_cake = "cake" in fun_dictionary.keys()
has_mango = "Mango" in fun_dictionary.values()

print("Has Cake:", has_cake)
print("Has Mango:", has_mango)


# Task 2 - Dictionaries 2
print("\n\nTask 2 - Dictionaries 2:")
fun_dictionary2 = {}
for k, v in fun_dictionary.items():
    fun_dictionary2.update({k : v.lower().count('t')})
print(fun_dictionary2)


# Task 3 - Sets 1
print("\n\nTask 3 - Sets:")
s2_list = []
s3_list = []
s4_list = []

for i in range(21):
    if i % 2 == 0:
        s2_list.append(i)
    if i % 3 == 0:
        s3_list.append(i)
    if i % 4 == 0:
        s4_list.append(i)

s2 = set(s2_list)
s3 = set(s3_list)
s4 = set(s4_list)

print(s2)
print(s3)
print(s4)

print("s3 is subset of s2:", s3.issubset(s2))
print("s4 is subset of s2:", s4.issubset(s2))

# Task 4 - Sets 2
print("\n\nTask 4 - Sets 2:")
python_set = set(['p', 'y', 't', 'h', 'o', 'n'])
python_set.update('i')

marathon_set = set(["m", "a", "r", "a", "t", "h", "o", "n"])

union_set = python_set.union(marathon_set)
intersect_set = python_set.intersection(marathon_set)
print("Union Set:", union_set)
print("Intersection Set:", intersect_set)

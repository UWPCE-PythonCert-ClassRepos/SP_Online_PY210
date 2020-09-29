#!/usr/bin/env python3
import sys

##############################################################
# 20200706    djm   Dictionary and Set Lab
#
#
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html
# #
# # Dictionaries 1
# #
# #     Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle”
# # who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
# #     Display the dictionary.
# #     Delete the entry for “cake”.
# #     Display the dictionary.
# #     Add an entry for “fruit” with “Mango” and display the dictionary.
# #         Display the dictionary keys.
# #         Display the dictionary values.
# #         Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
# #         Display whether or not “Mango” is a value in the dictionary (i.e. True).
# #
# #
#
################################################################

# #     Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle”
# # who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
cakes = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

# #     Display the dictionary.
print(cakes)

# #     Delete the entry for “cake”.
cakes.pop('cake')

# #     Display the dictionary.
print(cakes)

# #     Add an entry for “fruit” with “Mango” and display the dictionary.
cakes.update({'fruit': 'Mango'})

# #         Display the dictionary keys.
cakes.keys()

# #         Display the dictionary values.
cakes.values()

# #         Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in cakes.keys())
# or
if 'cake' not in cakes.keys():
    print(1 == 2)
else:
    print(1 == 1)

# #         Display whether or not “Mango” is a value in the dictionary (i.e. True).

print('Mango' in cakes.values())

################################################################################################
# Dictionaries 2
# #
# #     Using the dictionary from item 1: Make a dictionary using the same keys but with the number
#   of ‘t’s in each value as the value (consider upper and lower case?).
# #
# #     The result should look something like:
# #
# #     {"name": 0
# #      "city": 2
# #      "cake": 2
# #     }
# #

cakes = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

cakes_with_t = cakes.copy()

# one way
for i in cakes_with_t:
    cakes_with_t[i] = cakes[i].lower().count('t')
# another
print (cakes_with_t)

################################################################################################
# Sets
#
#     Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#     divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
#     Display the sets.
#     Display if s3 is a subset of s2 (False)
#     and if s4 is a subset of s2 (True).
#

# Sets 1

# get a range of numbers
x = range(0, 20)

s2 = set()
for n in x:
  if n % 2 == 0:
    s2.add(n)

s3 = set()
for n in x:
    if n % 3 == 0:
        s3.add(n)

s4 = set()
for n in x:
    if n % 4 == 0:
        s4.add(n)

print(s2)
print(s3)
print(s4)

#     Display if s3 is a subset of s2 (False)
print(s3.issubset(s2))
#     and if s4 is a subset of s2 (True).
print(s4.issubset(s2))


################################################################################################
# Sets 2
#
#     Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#     Create a frozenset with the letters in ‘marathon’.
#     Display the union and intersection of the two sets.
#
#

s5 = set()
for i, j in enumerate('Python'):
    s5.add(j)
s5.add('i')

frz = set()
for i, j in enumerate('marathon'):
    frz.add(j)
type(frz)
frz = frozenset(frz)
type(frz)

print(s5)
print(frz)

print(s5.union(frz))
print(s5.intersection(frz))




x = tuple(range(1,11))
print("{:d}\n{:d}\n{:d}\n{:d}\n{:d}\n{:d}\n{:d}\n{:d}\n{:d}\n{:d}".format(*x))

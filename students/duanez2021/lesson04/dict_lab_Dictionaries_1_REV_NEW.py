#!/usr/bin/env python3
import sys

##############################################################
# 20200706    djm   Dictionary and Set Lab
#
#
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






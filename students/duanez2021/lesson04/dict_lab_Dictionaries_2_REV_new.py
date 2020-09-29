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
#
################################################################

cakes = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

cakes_with_t = cakes.copy()

# one way
for i in cakes_with_t:
    cakes_with_t[i] = cakes[i].lower().count('t')
# another
print (cakes_with_t)

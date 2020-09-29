# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:02:41 2019

@author: Philip Behrend
"""

#!/usr/bin/env python3

# make executable: chmod +x dict_lab.py

person_dict = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
print(person_dict)
del person_dict["cake"]
print(person_dict)
person_dict["fruit"] = "Mango"
print(person_dict.keys(), '\n', person_dict.values(), '\n',
      "cake" in person_dict.keys(), '\n', "Mango" in person_dict.values())

# Dictionaries 2
t_dict = {}
for i in person_dict.keys():
    t_dict[i] = person_dict[i].count('t')
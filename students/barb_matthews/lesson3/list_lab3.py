#!/usr/bin/env python3

## Lesson 3.3 List Lab, delete user input disliked fruits
## By: B. Matthews
## 9/17/2020

import string
import copy

fruitslist = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits = copy.deepcopy(fruitslist)

def askFruits():
    """From a list of fruits, remove the ones the user doesn't like"""
    ask = "yes"

    for item in fruitslist:
        ask = input("Do you like %s?\nPlease enter (Yes) (No) or (Quit) >>" % item)
        if (ask.lower() == "no"):
            fruits.remove(item)
        elif (ask.lower() == "quit"):
            break
    print(fruits)

# test the function
askFruits()
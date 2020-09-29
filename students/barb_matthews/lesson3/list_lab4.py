#!/usr/bin/env python3

## Lesson 3.4 List Lab
## Make a new list with the contents of the original, but with all the letters in each item reversed.
## Delete the last item of the original list. Display the original list and the copy.
## By: B. Matthews
## 9/17/2020

import string
import copy

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
backwardsfruits = copy.deepcopy(fruits)

reversedString=[]

for i,item in enumerate(backwardsfruits):
    index = len(item)
    revitem = ""
    while index > 0:
        revitem += item[ index -1 ]
        index -= 1
    backwardsfruits[i] = revitem
    #print(backwardsfruits)

print("\nOriginal: ", fruits)
fruits.pop()
print("Original without last item: ", fruits)
print("\nCopy: ", backwardsfruits)


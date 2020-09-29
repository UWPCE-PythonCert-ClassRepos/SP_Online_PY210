#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:35:32 2020

@author: miriam
"""

# Series 1
L = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(L)
F = input("Please type in a fruit: ")
L.append(F)
print(L)

for num in L:
    num = int(input("\nPlease enter in a fruit number (1-5): "))
    print(num, L[num-1])
    break
else:
    print('')
L = ["Grapes"] + L
print(L)
L.insert(0, "Bananas")
print(L)

for fruits in L:
    if fruits.startswith('P'):
        print(fruits)

# Series 2
print(L)
L2 = L
del L2[-1]
print(L2)

D = input('Which fruit should be deleted: ')
if D in L2:
    L2.remove(D)
else:
    print(D, "not in list")
print(L2)

# Series 3
def series3(L):
    L3 = L[:]
    for i in L3:
        Q = input("Do you like {}: ".format(i.lower()))
        while Q.lower() != "yes" and Q.lower() != "no":
            Q = input("Do you like {}: ".format(i.lower()))
        if Q.lower() == "no":
            L.remove(i)
        else:
            continue
    print(L, "\n")

# series 4
def series4(L):
    L4 = []
    for i in L:
        L4.append(i[::-1])
    L.pop()
    print (L4)
    print (L)

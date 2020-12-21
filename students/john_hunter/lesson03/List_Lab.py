#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:48:59 2020

@author: johnh
"""

#list lab

def series1(fruit):
    print(fruit)
    extraFruit = input('Enter another fruit: ')
    fruit.append(extraFruit)
    print(fruit)
    indexOfFruit = int(input('Enter an integer: '))
    print(fruit[indexOfFruit-1])
    fruit = [input("Enter another fruit: "),] + fruit
    fruit.insert(0, input("Enter another fruit: "))
    print(fruit)
    for item in fruit:
        if item[0]=='p' or item[0]=='P':
            print(item)
    return fruit    
def series2(fruit):
    print(fruit)
    lastIndex = len(fruit)
    fruit.pop(lastIndex-1)
    print(fruit)
    missingFruit = input('Choose a fruit from the list to be deleted: ')
    x = fruit.index(missingFruit)
    fruit.pop(x)
    print(fruit)
    return None
def series3(fruit):
    print(fruit)
    fruitNew = list()
    for item in fruit:
        itemEach = item.lower()
        while True:
            yesOrNo = input('Do you like {}, yes/no: '.format(itemEach))
            if yesOrNo == 'no':
                x = fruit.index(item)
                fruit.pop(x)
                break
            elif yesOrNo == 'yes':
                fruitNew.append(item)
                break
            else:
                print('Please enter \'yes\' or \'no\': ')
                continue
            
    print(fruitNew)
    return None     

def series4(fruit):
    fruitNew = list()
    for item in fruit:
        itemNew = str()
        x=len(item)
        for i in range(x):
            itemNew+=item[-(i+1)]
        fruitNew.append(str(itemNew))
    print(fruitNew)
    del fruit[-1]
    print(fruit)
moreFruit=str()
fruit= ["Apples", "Pears", "Oranges", "Peaches"]
moreFruit = series1(fruit)
moreFruit2 = moreFruit
series2(moreFruit)
series3(moreFruit2)
series4(fruit)
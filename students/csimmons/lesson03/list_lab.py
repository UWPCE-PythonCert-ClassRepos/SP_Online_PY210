#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/16/2020 - csimmons

fruit = ['Apples', 'Pears', 'Oranges', 'Blueberries']

def series_one():
    print('We have the following fruits available: ' + str(fruit))
    add_fruit = input('What kind of fruit do you want to add?  ')
    fruit.append(add_fruit)
    print('The following fruits are now available: ' + str(fruit))
    print('\nSelect one of the above fruits by its position in the list')
    fruit_idx = input('Please enter a number: ')
    print(fruit[(int(fruit_idx)-1)] + ' are in position ' + str(fruit_idx))
    fruit = ['Pineapple'] + fruit
    fruit.insert(0, 'Banana')
    print(fruit)
    for i in fruit:
        if i.startswith("P"):
            print(i)
    return fruit

def series_one():


series_one()
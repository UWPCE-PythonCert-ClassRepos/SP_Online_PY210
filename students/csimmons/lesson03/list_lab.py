#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/16/2020 - csimmons

def series_one():
    fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('We have the following fruits available: ' + str(fruit))
    add_fruit = input('What kind of fruit do you want to add?  ')
    fruit.append(add_fruit)
    print('The following fruits are now available: ' + str(fruit))
    print('\nSelect one of the above fruits by its position in the list')
    fruit_idx = input('Please enter a number:')
    print(fruit[(int(fruit_idx)-1)] + ' are in position ' + str(fruit_idx))
    anotherfruit = ['Grapes']
    finalfruit = ['Pineapple']
    fruit = fruit + anotherfruit
    print(fruit)
    #add_fruit2 = input('Add another fruit:  ')
    #add_fruit3 = input('Add one last fruit:  ')
    #another = add_fruit2 + fruit
    #lastone = add_fruit3 + fruit
    #print('Added another fruit by concatenation: ' + str(another))
    #print('Added one last to list with insert(): ' + str(lastone))




series_one()
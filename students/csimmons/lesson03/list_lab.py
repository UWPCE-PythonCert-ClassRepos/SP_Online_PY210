#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/16/2020 - csimmons

fruits = ['Apples', 'Pears', 'Oranges', 'Blueberries']

def series_one(fruits):
    #fruit = ['Apples', 'Pears', 'Oranges', 'Blueberries']
    print('We have the following fruits available: ' + str(fruits))
    add_fruit = input('What kind of fruit do you want to add?  ')
    fruits.append(add_fruit)
    print('The following fruits are now available: ' + str(fruits))
    print('\nSelect one of the above fruits by its position in the list')
    fruit_idx = input('Please enter a number: ')
    print(fruits[(int(fruit_idx)-1)] + ' are in position ' + str(fruit_idx))
    fruits = ['Pineapples'] + fruits
    print(str(fruits) + ' Pineapples added to list using concatenation')
    fruits.insert(0, 'Bananas')
    print(str(fruits) + ' Bananas added to list using insert()')
    for fruit in fruits:
        if fruit.startswith("P"):
            print(fruit)
    return fruits

series_one(fruits)

def series_two():
    fruits = ['Banana', 'Pineapple', 'Apples', 'Pears', 'Oranges', 'Blueberries', 'khl']
    print(fruits)
    fruits.pop(-1)
    print(fruit)
    delete_fruit = input('Please select a fruit to delete from the list:  ')
    fruit.remove(delete_fruit)
    print(fruit)
    double_fruit = fruit*2
    print(double_fruit)



    print(fruit)

series_two(fruits)
'''
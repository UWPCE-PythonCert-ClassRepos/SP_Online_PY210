#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/16/2020 - csimmons

fruits = ['Apples', 'Pears', 'Oranges', 'Blueberries']



def series_one(fruits):
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


def series_two(fruits):
    #fruits = ['Banana', 'Pineapple', 'Apples', 'Pears', 'Oranges', 'Blueberries', 'khl']
    print(fruits)
    fruits.pop(-1)
    print(fruits)
    user_remove = input("Please select a fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in fruits:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    else:
        fruits.remove(user_remove)
    print(fruits)
    print("Fin")
    
    # Bonus Section
    double_fruit = fruits * 2 
    print(double_fruit)
    user_remove = input("Please select another fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in double_fruit:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    for fruit in double_fruit:
        while user_remove in double_fruit:
            double_fruit.remove(user_remove)
    print(double_fruit)
    print(fruits)
    return(double_fruit)


series_one(fruits)
series_two(fruits)
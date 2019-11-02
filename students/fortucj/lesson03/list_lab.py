#!/usr/bin/env python

def Series1():
    """
    This is Series 1.

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
    """

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches'] #1st and second bullets
    print(fruits)

    new_fruit1 = input("Please provide another fruit.") #3rd & 4th bullets
    fruits.append(new_fruit1)
    print(fruits)

    length = len(fruits) #5th bullet
    "Please provide a number between 1 and {}.".format(length)
    fruit_number = int(input("Please provide a number between 1 and {}.".format(length)))
    print(fruit_number, fruits[fruit_number - 1])

    new_fruit2 = [input("Please provide another fruit.")] #6th bullet
    fruits = new_fruit2 + fruits
    print(fruits)

    new_fruit3 = input("Please provide another fruit.") #7th bullet
    fruits.insert(0,new_fruit3)
    print(fruits)

    P_list = [] #last bullet
    for item in fruits:
        if item[0] == 'P':
            P_list += [item]
    print(P_list)






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
    length_P = len(P_list)
    print(("Items beginning with 'P' are " + ", ".join(["{}"] * length_P)).format(*P_list))

    return fruits #additional return command for following series



def Series2():
    """
    This is Series2

    Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    """

    ask = input("Do you want the default list? ('yes' or 'no')") #option to take default list or execute Series1
    if ask == 'yes':
        fruits2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    elif ask == 'no':
        fruits2 = Series1()

    print(fruits2) #first bullet

    fruits2.pop() #second bullet
    print(fruits2)

    fruits2 = 2 * fruits2 #third bullet
    print('here is the double list: {}'.format(fruits2))


    del_fruit = '' #4th & 5th bullet
    while del_fruit not in fruits2:
        del_fruit = input("Please provide a fruit to delete")
    while del_fruit in fruits2:
        fruits2.remove(del_fruit)

    print(fruits2) #display results




#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Module 3: list_lab

Series 1

Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
<<<<<<< HEAD
Ask the user for a number and display the number back to the user and the fruit corresponding
to that number (on a 1-is-first basis).
=======
Ask the user for a number and display the number back to the user and the fruit corresponding to that number
(on a 1-is-first basis).
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.

'''


def show_list(prompt, items):
<<<<<<< HEAD
    '''
    Print a comma-separated list of the items in a list
    '''

=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    display = prompt + ": " + ", ".join(len(items) * ["{}"]).format(*items)
    print(display)


def enumerate_list(items):
<<<<<<< HEAD
    '''
    Print a numbered list
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    for i, items in enumerate(items):
        print("{:<4}{:<10}".format(i + 1, items))


def remove_list_item_by_name(item, items):
<<<<<<< HEAD
    '''
    Remove an item from a list if it matches user input
    '''
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    while item in items:
        items.remove(item)
        if item not in items:
            break
<<<<<<< HEAD
=======
    else:
        remove_item = int(input("\nplease choose the number of the fruit you'd like to delete (1 - " + str(len(items)) + ") >>> "))
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    return items


print("\n\nSERIES 1\n\n")
<<<<<<< HEAD
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']
FRUITS_ORIG = list(FRUITS) # so we a copy instead of a pointer!!!
show_list("Initial list", FRUITS)
ADD_FRUIT = str(input("Please input another fruit to add to the list >>  "))
FRUITS.append(ADD_FRUIT)
show_list("Added item to end", FRUITS)
SHOW_NUMBER = int(input("Please input the number of the fruit you'd like to display"
                        " (1-" + str(len(FRUITS)) + ")>>  "))
SHOW_NUMBER -= 1 # Add number so our numbering starts at 1
print("Selection: " + FRUITS[SHOW_NUMBER])
# add to beginning using +
FRUITS = ['Banana'] + FRUITS
show_list("Added Banana to front of list using +", FRUITS)
# add to beginning using append
FRUITS.insert(0, 'Pineapple')
show_list("Added Pineapple to front using insert", FRUITS)
=======
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_orig = list(fruits) # so we a copy instead of a pointer!!!
show_list("Initial list", fruits)
add_fruit = str(input("Please input another fruit to add to the list >>  "))
fruits.append(add_fruit)
show_list("Added item to end", fruits)
show_number = int(input("Please input the number of the fruit you'd like to display (1-" + str(len(fruits)) + ")>>  "))
show_number -= 1 # Add number so our numbering starts at 1
print("Selection: " + fruits[show_number])
# add to beginning using +
fruits = ['Banana'] + fruits
show_list("Added Banana to front of list using +", fruits)
# add to beginning using append
fruits.insert(0, 'Pineapple')
show_list("Added Pineapple to front using insert", fruits)
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7


'''

Series 2

Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
<<<<<<< HEAD
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, 
delete all occurrences.)
=======
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
'''

print("\n\nSERIES 2\n\n")

<<<<<<< HEAD
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']

#  Show the list created in Series 1
show_list("List created in Series 1", FRUITS)

#  Remove last fruit from list
FRUITS.pop(len(FRUITS) - 1)
show_list("Removed last item", FRUITS)

#  List available items for deletion:
print("\n\nLet's delete one of these fruits:\n")
enumerate_list(FRUITS)

REMOVE_ITEM = int(input("\nplease choose the number of the fruit you'd like to delete"
                        " (1 - " + str(len(FRUITS)) + ") >>> "))
FRUITS.pop(REMOVE_ITEM)

FRUITS = FRUITS * 2

print("\n\nBONUS!: Let's delete all of one type of these fruits:\n")
enumerate_list(FRUITS)

REMOVE_ITEM = int(input("\nplease choose the number of the fruit you'd like to delete"
                        " (1 - " + str(len(FRUITS)) + ") >>> "))
REMOVE_FRUIT = FRUITS[REMOVE_ITEM - 1] #  Handle the off-by-1

FRUITS = remove_list_item_by_name(REMOVE_FRUIT, FRUITS)
print("\n\nUpdated list after deletion: \n")
enumerate_list(FRUITS)
=======
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

#  Show the list created in Series 1
show_list("List created in Series 1", fruits)

#  Remove last fruit from list
fruits.pop(len(fruits)-1)
show_list("Removed last item", fruits)

#  List available items for deletion:
print("\n\nLet's delete one of these fruits:\n")
enumerate_list(fruits)

remove_item = int(input("\nplease choose the number of the fruit you'd like to delete (1 - " + str(len(fruits)) + ") >>> "))
fruits.pop(remove_item)

fruits = fruits * 2

print("\n\nBONUS!: Let's delete all of one type of these fruits:\n")
enumerate_list(fruits)

remove_item = int(input("\nplease choose the number of the fruit you'd like to delete (1 - " + str(len(fruits)) + ") >>> "))
remove_fruit = fruits[remove_item - 1] #  Handle the off-by-1

fruits = remove_list_item_by_name(remove_fruit, fruits)
print("\n\nUpdated list after deletion: \n")
enumerate_list(fruits)
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7






'''
Series 3

Again, using the list from series 1:

<<<<<<< HEAD
* Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list 
(making the fruit all lowercase).
* For each “no”, delete that fruit from the list.
* For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values 
(a while loop is good here) Display the list.
=======
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.

>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
'''

print("\n\nSERIES 3\n\n")

<<<<<<< HEAD
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']

print("\n\nLet's remove items from the list that you don't like...\n\n")
enumerate_list(FRUITS)
remove_fruits = []

for fruit in FRUITS:
=======
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print("\n\nLet's remove items from the list that you don't like...\n\n")
enumerate_list(fruits)
remove_fruits = []

for fruit in fruits:
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    response = '' #  declare or reset answer from previous
    while response.lower() not in ["yes", "no"]:
        response = str(input("Do you like {}?".format(fruit) + " (yes/no) >>> ")).lower()
        if response == 'no':
<<<<<<< HEAD
            remove_fruits.append(fruit) #  Actually removing the fruit from the list here causes an
            #  off-by-one. Create a list and do it after this loop.
=======
            remove_fruits.append(fruit) #  Actually removing the fruit from the list here causes an off-by-one. Create a list and do it after this loop.
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
            print("OK, removing {}!".format(fruit))

#  Now remove the fruits the user answered "no" to...
for fruit in remove_fruits:
<<<<<<< HEAD
    FRUITS = remove_list_item_by_name(fruit, FRUITS)


print("\n\nHere are the fruits you like: \n")
enumerate_list(FRUITS)
=======
    fruits = remove_list_item_by_name(fruit, fruits)


print("\n\nHere are the fruits you like: \n")
enumerate_list(fruits)
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7


'''
Series 4

Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
<<<<<<< HEAD
=======

>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
'''

print("\n\nSERIES 4\n\n")

<<<<<<< HEAD
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']
FRUITS_ORIG = FRUITS[:]
FRUITS_COPY = FRUITS[:]

print("\n\nA:\n\n")
STIURF = []  # fruits spelled backwards!

for fruit in FRUITS:
    STIURF.append(fruit[::-1].lower().title())

show_list("Here's the fruits before", FRUITS)
FRUITS = STIURF
show_list("Here's the same fruits spelled backwards", FRUITS)

print("\n\nB:\n\n")
FRUITS_ORIG.pop(len(FRUITS_ORIG) - 1)

show_list("here's the original list with the last item removed", FRUITS_ORIG)
show_list("here's a copy the original list", FRUITS_COPY)
=======
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_orig = fruits[:]
fruits_copy = fruits[:]

print("\n\nA:\n\n")
stiurf = []  # fruits spelled backwards!

for fruit in fruits:
    stiurf.append(fruit[::-1].lower().title())

show_list("Here's the fruits before", fruits)
fruits = stiurf
show_list("Here's the same fruits spelled backwards", fruits)

print("\n\nB:\n\n")
fruits_orig.pop(len(fruits_orig)-1)

show_list("here's the original list with the last item removed", fruits_orig)
show_list("here's a copy the original list", fruits_copy)

>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7

#!/usr/bin/env python3
import contextlib
# Series 1

def fruitselectionfunc():
    global FruitSelection
    FruitSelection = input('2. Select an item from the list of fruit based on number > ')
    return FruitSelection

print('Series 1:')
# fruit list follows:
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
# prints out the current list of fruit
print(f'Current list of fruit: {fruit}.')
# user input prompt
FruitResponse = input('1. Please enter the name of a fruit to add to the list > ')
# adds user input to the end of the list
fruit.append(FruitResponse)
# prints out the updated list of fruit
print(f'The list now contains : {fruit}.')
# prompts user to make a selection from the list of fruit
# calls funtion to input numerical selection
fruitselectionfunc()

# while loop to prompt user for digit entry and handle non-valid entries
while True:
    if FruitSelection.isdigit():
        FruitSelection = int(FruitSelection)
        break
    else:
        with contextlib.suppress(ValueError): # attempt to use contextlib to ignore exceptions
            print('Please enter an interger:')
            fruitselectionfunc()

# normalize the selection for humans by subtracting 1 from FruitSelection input
FruitSelection = (FruitSelection - 1)
# print out selection for user
print(fruit[FruitSelection])
# Prompts user to add another fruit to the list, but at the beginning of the list
FruitResponseBegin = input('3. Please enter the name of a fruit to add to the beginning of the list > ')
# adding fruit to the beginning of list using +
fruit = [FruitResponseBegin] + fruit
# printing list contents after addition
print(fruit)
# Prompts user to add another fruit to the beginning of the list
FruitResponseBeginTwo = input('4. Please enter the another name of a fruit to add to the beginning of the list > ')
# # adding an additional item to the beginning of the list using insert()
fruit.insert(0, FruitResponseBeginTwo)
# printing list contents after second addition
print(fruit)
# first sort the list and make uppercase
fruit.sort(key=str.upper)
# Display all the fruits that begin with “P”, using a for loop
print('All items that begin With the letter P')
for item in fruit:
    item = item.capitalize() # capitalized the first letter of each item
    if item.startswith('P'): # searched for all items that start with 'P'
        print(item) # printed the item
# Series 2
# Display the list
print(fruit)
#Remove the last fruit from the list.
del fruit[-1]
# Display the list after last item removed
print(fruit)
# Ask the user for a fruit to delete, find it and delete it.
fruit = fruit * 2
print(f'The list has been doubled: \n {fruit}')
while True:
    FruitResponseDeletion = input('5. Please enter the name of a fruit to delete from the list > ')
    if FruitResponseDeletion in fruit:
        for item in fruit:
            with contextlib.suppress(ValueError): # handle error when loop removes all occurrences
                fruit.remove(FruitResponseDeletion)
            continue
        print(fruit)
        break
    else:
        print('Fruit Not Found.')
# Tells users which fruit was removed
print(f'{FruitResponseDeletion} removed from the list.')
# prints list again
print(fruit)
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

# Series 3
# Ask the user for input displaying a line like “Do you like apples?”
#for each fruit in the list (making the fruit all lowercase).
for item in fruit:
    item.lower() # lowers the case
    answer = input(f'Y or N - Do you like {item}? ') # prompts the user
    i = 0 # sets a value for the while loop
    while i < len(fruit): # sets the conditions of the loop
        if answer.lower() == 'y':
            i += 1 # increments the value
            continue
        elif answer.lower() == 'n':
            with contextlib.suppress(ValueError): # handle error when loop removes all occurrences
                fruit.remove(item) # removes the value from the list
                print(fruit) # prints the list after each iteration
            i += 1 # increments the value
            continue
        else:
            print('Please enter Y or N.')
            continue
print(fruit) # prints the final list

# Series 4
# Make a new list with the contents of the original, but with all the letters in each item reversed.
fruit_new = ['Apples', 'Pears', 'Oranges', 'Peaches'] # copy of original list
fruit_copy = [] # empty list for copy
for item in fruit_new: # for loop to populate the new list
    fruit_copy.append(item[::-1]) # add the item in reveresed
# Delete the last item of the original list. Display the original list and the copy.
del fruit_copy[-1] # delete the last time of the copy of the list
print(fruit_copy) # print out copy of original
print(fruit_new) # print out new list with reversed items

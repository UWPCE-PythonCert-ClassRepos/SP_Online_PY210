#!/usr/bin/env python3

"""PY210_SP - exercise 3.2 - list_lab
author: Nick Miller"""

# Begin series 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.

fruits = ["Oranges", "Peaches", "Apples", "Pineapples"]

# Display the list (plain old print() is fine…).

print(fruits)
print()

# Ask the user for another fruit and add it to the end of the list.

user_add = input("Enter a fruit to add to the end of the list: ")

user_add = user_add.capitalize()

fruits.append(user_add)

# Display the list.

print(fruits)
print()

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
# (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.

pick = str(len(fruits))
ask = "Pick a number between 1 and " + pick + ": "

while True:
    try:
        user_pick = int(input(ask))
        if user_pick in range(len(fruits)+1):
            break
    except:
        pass
    print('\nIncorrect input, try again')

user_pick = user_pick - 1
user_pick_str = "The fruit at position " + str((user_pick + 1)) + " is " + fruits[user_pick]
print(user_pick_str)
print()

# Add another fruit to the beginning of the list using “+” and display the list.

user_add = input("Enter a fruit to the front of the list: ")

user_add = [user_add.capitalize()]

fruits = user_add + fruits

print(fruits)
print()

# Add another fruit to the beginning of the list using insert() and display the list.

user_add = input("Enter another fruit to add at the beginning: ")

user_add = user_add.capitalize()

fruits.insert(0, user_add)

print(fruits)
print()

# Display all the fruits that begin with “P”, using a for loop.

pfruits = []

for i in range(len(fruits)):
    if fruits[i][0] == "P":

        pfruit = fruits[i]
        pfruits.insert(0, pfruit)

print("Here are all the fruit in the list that start with 'P'.")
print(pfruits)
print()

print("That was the end of series 1.")
print()

# End series 1

# Begin series 2

# Display the list.

print("Begin series 2:")
print()

print("This is the current list:")
print(fruits)
print()

# Remove the last fruit from the list.

del fruits[-1]

# Display the list.
print("Same list, last item removed: ")
print(fruits)
print()

# Ask the user for a fruit to delete, find it and delete it.
usr_choose = input("Enter a fruit to remove from the list: ")

usr_choose = usr_choose.strip()
usr_choose = usr_choose.capitalize()

while usr_choose not in fruits:
    usr_choose= input("Sorry, that fruit is not in the list, enter a fruit to remove from the list: ")
    usr_choose = usr_choose.strip()
    usr_choose = usr_choose.capitalize()

while usr_choose in fruits:
    fruits.remove(usr_choose)

print(fruits)
print()

# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

print("Bonus - the list has been multiplied, it looks like this: ")
fruits = fruits * 2
print(fruits)
print()

usr_choose = input("Enter a fruit to remove from the list: ")

usr_choose = usr_choose.strip()
usr_choose = usr_choose.capitalize()

while usr_choose not in fruits:
    usr_choose = input("Sorry, that fruit is not in the list, enter a fruit to remove from the list(s): ")
    usr_choose = usr_choose.strip()
    usr_choose = usr_choose.capitalize()

while usr_choose in fruits:
    fruits.remove(usr_choose)

print("The doubled list, sans the item you entered:")
print(fruits)
print()

print("That was the end of series 2.")
print()

print("Begin series 3:")
print()

delfruits = []
for fruit in fruits:
    question = "Do you like " + fruit + "? (y/n): "
    yesorno = input(question)
    drop = fruits.index(fruit)
    while yesorno != "y" and yesorno != "n":
        yesorno = input("Please enter y or n: ").lower()
    if yesorno == "n":
        delfruits.append(drop)
for i in delfruits:
    fruits.pop(i)

print("Here is a list of just the fruits you like:")
print(fruits)

print("That was the end of series 3.")
print()

print("Begin series 4:")
print()

backwardsfruits = []
for i in fruits:
    i = i[::-1]
    backwardsfruits.append(i)

print("Here are all the fruits in the list, with their letters reversed:")
print(backwardsfruits)
print()

del fruits[-1]
print("Here is the original list with the last item deleted:")
print(fruits)

# End list_lab
